# acquisition/canon.py
# Controle du Canon EOS R7
#
# Sur Linux  : gphoto2 CLI (capture directe sans carte SD)
# Sur Windows : EDSDK via ctypes (DirItemCreated fonctionne sur Windows)
#
# Le choix est automatique selon le systeme d'exploitation detecte.

import os
import sys
import time
import subprocess
import threading

# Detecter le systeme d'exploitation
WINDOWS = sys.platform == "win32"
LINUX   = sys.platform.startswith("linux")

# ── Chemins bibliotheques ─────────────────────────────────────────────────────
CHEMIN_LIB_LINUX   = os.path.expanduser(
    "~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so"
)
CHEMIN_LIB_WINDOWS = r"C:\EDSDK\Library\EDSDK.dll"

# ── Constantes EDSDK (Windows uniquement) ─────────────────────────────────────
EDS_ERR_OK                             = 0x00000000
kEdsCameraCommand_TakePicture          = 0x00000000
kEdsFileCreateDisposition_CreateAlways = 0x00000002
kEdsAccess_ReadWrite                   = 0x00000001
kEdsObjectEvent_DirItemCreated         = 0x00000203
kEdsPropID_SaveTo                      = 0x00000390
kEdsSaveTo_Host                        = 0x00000002

# ── Variables globales EDSDK (Windows) ───────────────────────────────────────
_edsdk            = None
_camera           = None
_sdk_initialise   = False
_callback_ref     = None
_thread_events    = None
_continuer_events = False
_chemin_destination = None


# ==============================================================================
# PARTIE COMMUNE : detection et connexion
# ==============================================================================

def _gvfs_libre():
    """
    Tue les processus gvfs sur Linux.
    gvfs prend automatiquement le controle du Canon des qu'il est branche.
    Sans cette etape, ni gphoto2 ni l'EDSDK ne peuvent y acceder.
    """
    if LINUX:
        subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"],  capture_output=True)
        subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
        time.sleep(1.5)


def connecter_canon():
    """
    Detecte le Canon et etablit la connexion.

    Linux   : verifie via gphoto2 --auto-detect, retourne True/False
    Windows : charge l'EDSDK, ouvre une session, retourne le handle ou None

    Retour :
      Linux   -> True si detecte, False sinon
      Windows -> handle camera (ctypes.c_void_p) si connecte, None sinon
    """
    _gvfs_libre()

    if LINUX:
        return _connecter_linux()
    else:
        return _connecter_windows()


def prendre_photo_canon(chemin_fichier):
    """
    Declenche le Canon et sauvegarde la photo dans chemin_fichier.

    Linux   : utilise gphoto2 --capture-image-and-download
    Windows : utilise l'EDSDK avec le callback DirItemCreated

    Retourne chemin_fichier si succes, None sinon.
    """
    if LINUX:
        return _prendre_photo_linux(chemin_fichier)
    else:
        return _prendre_photo_windows(chemin_fichier)


def deconnecter_canon():
    """Ferme proprement la connexion."""
    if WINDOWS:
        _deconnecter_windows()


# ==============================================================================
# LINUX : gphoto2 CLI
# ==============================================================================

def _connecter_linux():
    """
    Verifie que le Canon est detecte par gphoto2.
    gphoto2 est un outil en ligne de commande qui supporte des centaines
    d'appareils photo via le protocole PTP/USB.
    """
    try:
        r = subprocess.run(
            ["gphoto2", "--auto-detect"],
            capture_output=True, text=True, timeout=10
        )
        if "usb:" in r.stdout:
            print("[Canon Linux] Canon detecte via gphoto2.")
            return True
        else:
            print("[Canon Linux] Aucun appareil detecte.")
            print("[Canon Linux] Verifiez : Canon allume + cable USB.")
            return False
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 non installe.")
        print("[Canon Linux] Installez-le : sudo apt install gphoto2")
        return False
    except subprocess.TimeoutExpired:
        print("[Canon Linux] Timeout detection.")
        return False


def _prendre_photo_linux(chemin_fichier):
    """
    Declenche et recupere la photo via gphoto2.

    gphoto2 --capture-image-and-download :
      1. Declenche l'obturateur
      2. Recupere la photo depuis l'appareil (sans carte SD necessaire)
      3. La sauvegarde dans chemin_fichier
      4. Supprime le fichier temporaire sur l'appareil
    """
    _gvfs_libre()

    dossier = os.path.dirname(chemin_fichier)
    if dossier:
        os.makedirs(dossier, exist_ok=True)

    print(f"[Canon Linux] gphoto2 -> {chemin_fichier}")

    try:
        r = subprocess.run(
            [
                "gphoto2",
                "--capture-image-and-download",
                "--filename", chemin_fichier,
                "--force-overwrite"
            ],
            capture_output=True, text=True, timeout=30
        )

        if r.returncode == 0 and os.path.exists(chemin_fichier):
            taille_ko = os.path.getsize(chemin_fichier) / 1024
            print(f"[Canon Linux] Photo sauvegardee ({taille_ko:.0f} Ko)")
            return chemin_fichier
        else:
            print(f"[Canon Linux] ECHEC gphoto2 (code {r.returncode})")
            if r.stderr:
                print(f"[Canon Linux] {r.stderr.strip()}")
            if "Could not claim" in r.stderr or "Busy" in r.stderr:
                print("[Canon Linux] gvfs a repris le controle. Relancez la detection.")
            if "focus" in r.stderr.lower():
                print("[Canon Linux] Probleme autofocus. Passez l'objectif en MF.")
            return None

    except subprocess.TimeoutExpired:
        print("[Canon Linux] TIMEOUT 30s.")
        return None
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 non installe. sudo apt install gphoto2")
        return None


# ==============================================================================
# WINDOWS : EDSDK via ctypes
# ==============================================================================

def _boucle_events_windows():
    """
    Pompe la file d'evenements EDSDK toutes les 50ms.
    Sur Windows, DirItemCreated se declenche correctement.
    Ce thread doit tourner pendant toute la duree de la session.
    """
    while _continuer_events:
        if _edsdk:
            _edsdk.EdsGetEvent()
        time.sleep(0.05)


def _charger_edsdk_windows():
    """Charge EDSDK.dll sur Windows."""
    global _edsdk
    import ctypes

    chemin = CHEMIN_LIB_WINDOWS
    if not os.path.exists(chemin):
        print(f"[Canon Windows] EDSDK.dll introuvable : {chemin}")
        print("[Canon Windows] Installez l'EDSDK et verifiez le chemin dans canon.py")
        return False
    try:
        # WinDLL pour les DLL Windows (convention d'appel stdcall)
        _edsdk = ctypes.WinDLL(chemin)
        print(f"[Canon Windows] EDSDK.dll charge : {chemin}")
        return True
    except OSError as e:
        print(f"[Canon Windows] ERREUR chargement DLL : {e}")
        return False


def _connecter_windows():
    """
    Charge l'EDSDK, initialise le SDK et ouvre une session Canon.
    Demarre le thread d'evenements.
    Retourne le handle camera ou None.
    """
    import ctypes
    global _camera, _sdk_initialise, _thread_events, _continuer_events

    if _camera is not None:
        return _camera

    if _edsdk is None:
        if not _charger_edsdk_windows():
            return None

    if not _sdk_initialise:
        err = _edsdk.EdsInitializeSDK()
        if err != EDS_ERR_OK:
            print(f"[Canon Windows] ERREUR EdsInitializeSDK : {hex(err)}")
            return None
        _sdk_initialise = True

    # Demarrer le thread d'evenements
    _continuer_events = True
    _thread_events = threading.Thread(target=_boucle_events_windows, daemon=True)
    _thread_events.start()

    camera_list = ctypes.c_void_p()
    err = _edsdk.EdsGetCameraList(ctypes.byref(camera_list))
    if err != EDS_ERR_OK:
        print(f"[Canon Windows] ERREUR EdsGetCameraList : {hex(err)}")
        return None

    count = ctypes.c_int()
    _edsdk.EdsGetChildCount(camera_list, ctypes.byref(count))

    if count.value == 0:
        print("[Canon Windows] Aucune camera detectee.")
        _edsdk.EdsRelease(camera_list)
        return None

    camera = ctypes.c_void_p()
    _edsdk.EdsGetChildAtIndex(camera_list, 0, ctypes.byref(camera))
    _edsdk.EdsRelease(camera_list)

    err = _edsdk.EdsOpenSession(camera)
    if err != EDS_ERR_OK:
        print(f"[Canon Windows] ERREUR EdsOpenSession : {hex(err)}")
        _edsdk.EdsRelease(camera)
        return None

    _camera = camera
    print(f"[Canon Windows] Canon EOS R7 connecte via EDSDK.")
    return camera


def _prendre_photo_windows(chemin_fichier):
    """
    Declenche et recupere la photo via EDSDK sur Windows.
    Utilise le callback DirItemCreated qui fonctionne sur Windows.
    """
    import ctypes
    global _chemin_destination, _callback_ref

    if _camera is None:
        print("[Canon Windows] Pas de session ouverte.")
        return None

    os.makedirs(
        os.path.dirname(chemin_fichier) if os.path.dirname(chemin_fichier) else ".",
        exist_ok=True
    )
    _chemin_destination = chemin_fichier

    photo_recue = [False]
    resultat    = [None]

    CALLBACK_TYPE = ctypes.CFUNCTYPE(
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_void_p,
        ctypes.c_void_p
    )

    def on_object_event(event, obj, context):
        if event == kEdsObjectEvent_DirItemCreated:
            chemin = _chemin_destination
            stream = ctypes.c_void_p()
            err_s = _edsdk.EdsCreateFileStream(
                chemin.encode("utf-8"),
                kEdsFileCreateDisposition_CreateAlways,
                kEdsAccess_ReadWrite,
                ctypes.byref(stream)
            )
            if err_s == EDS_ERR_OK:
                _edsdk.EdsDownload(obj, ctypes.c_ulonglong(0), stream)
                _edsdk.EdsDownloadComplete(obj)
                _edsdk.EdsRelease(stream)
                print(f"[Canon Windows] Photo sauvegardee -> {chemin}")
                resultat[0] = chemin
            else:
                print(f"[Canon Windows] ERREUR EdsCreateFileStream : {hex(err_s)}")
                _edsdk.EdsDownloadCancel(obj)
            _edsdk.EdsRelease(obj)
            photo_recue[0] = True
        return EDS_ERR_OK

    _callback_ref = CALLBACK_TYPE(on_object_event)

    _edsdk.EdsSetObjectEventHandler(
        _camera, kEdsObjectEvent_DirItemCreated, _callback_ref, None
    )

    # SaveTo = Host sur Windows
    import ctypes as ct
    save_to = ct.c_uint(kEdsSaveTo_Host)
    _edsdk.EdsSetPropertyData(
        _camera, kEdsPropID_SaveTo, 0, ct.sizeof(save_to), ct.byref(save_to)
    )

    err = _edsdk.EdsSendCommand(_camera, kEdsCameraCommand_TakePicture, 0)
    if err != EDS_ERR_OK:
        print(f"[Canon Windows] ERREUR declenchement : {hex(err)}")
        return None

    print("[Canon Windows] Attente de la photo (max 20s)...")
    debut = time.time()
    while not photo_recue[0]:
        time.sleep(0.1)
        if time.time() - debut > 20:
            print("[Canon Windows] TIMEOUT.")
            return None

    return resultat[0]


def _deconnecter_windows():
    """Ferme la session EDSDK sur Windows."""
    global _camera, _sdk_initialise, _continuer_events
    _continuer_events = False
    if _camera is not None:
        _edsdk.EdsCloseSession(_camera)
        _edsdk.EdsRelease(_camera)
        _camera = None
    if _edsdk is not None and _sdk_initialise:
        _edsdk.EdsTerminateSDK()
        _sdk_initialise = False
    print("[Canon Windows] Deconnecte.")


# ==============================================================================
# TEST DIRECT
# ==============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print(f"TEST CANON — systeme : {'Windows' if WINDOWS else 'Linux'}")
    print("=" * 50)

    print("\n[1/2] Detection...")
    ok = connecter_canon()
    if not ok:
        print("ECHEC : Canon non detecte.")
        exit(1)
    print("Canon detecte.")

    print("\n[2/2] Prise de photo...")
    os.makedirs("images/test", exist_ok=True)
    res = prendre_photo_canon("images/test/canon_test.jpg")

    if res and os.path.exists(res):
        print(f"\nSUCCES : {res} ({os.path.getsize(res) / 1024:.0f} Ko)")
    else:
        print("\nECHEC.")

    deconnecter_canon()
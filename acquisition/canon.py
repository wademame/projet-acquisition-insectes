# acquisition/canon.py
# Controle du Canon EOS R7 via EDSDK (USB) avec ctypes
#
# Le fichier libEDSDK.so doit etre dans :
#   ~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so
#
# gvfs est tue automatiquement depuis interface.py avant chaque connexion.
# Plus besoin de lancer pkill manuellement.
#
# Mode SaveTo = Host : la photo est transferee directement vers le PC.
# La carte SD n'est pas necessaire.

import ctypes
import os
import time
import threading

CHEMIN_LIB = os.path.expanduser(
    "~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so"
)

# ── Constantes EDSDK ──────────────────────────────────────────────────────────
EDS_ERR_OK                             = 0x00000000
kEdsCameraCommand_TakePicture          = 0x00000000
kEdsFileCreateDisposition_CreateAlways = 0x00000002
kEdsAccess_ReadWrite                   = 0x00000001
kEdsObjectEvent_DirItemCreated         = 0x00000203
kEdsPropID_SaveTo                      = 0x00000390
kEdsSaveTo_Host                        = 0x00000002   # transfert direct vers le PC

# ── Variables globales ────────────────────────────────────────────────────────
_edsdk        = None
_camera       = None
_callback_ref = None   # reference gardee pour eviter le garbage collector

# Thread qui pompe en continu les evenements EDSDK
_thread_events    = None
_continuer_events = False

# Chemin du fichier de destination pour le callback
_chemin_destination = None


def _boucle_events():
    """
    Pompe en continu la file d'evenements EDSDK.
    Cette fonction tourne dans un thread separe pendant toute la duree
    de la session. Sans ce thread, les callbacks EDSDK ne sont jamais
    declenches et la photo n'est jamais recue.
    """
    global _continuer_events
    while _continuer_events:
        if _edsdk:
            _edsdk.EdsGetEvent()
        time.sleep(0.05)


def charger_edsdk():
    global _edsdk
    chemin = os.path.expanduser(CHEMIN_LIB)
    if not os.path.exists(chemin):
        emplacements = [
            os.path.expanduser("~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so"),
            "/usr/local/lib/libEDSDK.so",
            "./libEDSDK.so",
        ]
        for e in emplacements:
            if os.path.exists(e):
                chemin = e
                break
        else:
            print("EDSDK non trouve. Verifiez le chemin dans canon.py.")
            return False
    try:
        _edsdk = ctypes.CDLL(chemin)
        print(f"EDSDK charge depuis : {chemin}")
        return True
    except OSError as e:
        print(f"Erreur chargement EDSDK : {e}")
        return False


def initialiser_edsdk():
    if _edsdk is None:
        if not charger_edsdk():
            return False
    err = _edsdk.EdsInitializeSDK()
    if err != EDS_ERR_OK:
        print(f"Erreur initialisation EDSDK : {hex(err)}")
        return False
    print("EDSDK initialise.")
    return True


def connecter_canon():
    """
    Detecte le Canon EOS R7, ouvre une session et demarre le thread
    qui pompe les evenements EDSDK en arriere-plan.
    Retourne le handle camera si succes, None sinon.
    """
    global _camera, _thread_events, _continuer_events

    if _edsdk is None:
        if not initialiser_edsdk():
            return None

    camera_list = ctypes.c_void_p()
    err = _edsdk.EdsGetCameraList(ctypes.byref(camera_list))
    if err != EDS_ERR_OK:
        print(f"Erreur liste cameras : {hex(err)}")
        return None

    count = ctypes.c_int()
    _edsdk.EdsGetChildCount(camera_list, ctypes.byref(count))

    if count.value == 0:
        print("Aucune camera Canon detectee.")
        _edsdk.EdsRelease(camera_list)
        return None

    print(f"{count.value} camera Canon detectee.")

    camera = ctypes.c_void_p()
    _edsdk.EdsGetChildAtIndex(camera_list, 0, ctypes.byref(camera))
    _edsdk.EdsRelease(camera_list)

    err = _edsdk.EdsOpenSession(camera)
    if err != EDS_ERR_OK:
        print(f"Erreur ouverture session : {hex(err)}")
        _edsdk.EdsRelease(camera)
        return None

    _camera = camera
    print("Canon EOS R7 connecte via EDSDK.")

    # Demarrer le thread qui pompe les evenements EDSDK
    _continuer_events = True
    _thread_events = threading.Thread(target=_boucle_events, daemon=True)
    _thread_events.start()

    return camera


def prendre_photo_canon(chemin_fichier):
    """
    Declenche le Canon et recupere la photo directement sur le PC
    sans utiliser la carte SD (mode SaveTo = Host).

    Fonctionnement :
    1. On configure SaveTo = Host : le Canon envoie la photo via USB
       au lieu de l'ecrire sur la carte SD.
    2. On enregistre un callback sur l'evenement DirItemCreated.
       Ce callback est appele automatiquement par le thread _boucle_events
       des qu'une nouvelle photo est disponible.
    3. On declenche (TakePicture).
    4. On attend jusqu'a 20 secondes que le callback soit appele et
       que la photo soit sauvegardee dans chemin_fichier.

    Sans la carte SD, l'appareil photo peut quand meme fonctionner car
    SaveTo = Host indique au Canon de tout envoyer vers l'ordinateur.
    """
    global _chemin_destination, _callback_ref

    if _camera is None:
        print("Canon non connecte.")
        return None

    os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)
    _chemin_destination = chemin_fichier

    # Indicateurs de progression
    photo_recue = [False]
    resultat    = [None]

    # Type du callback EDSDK (signature C)
    CALLBACK_TYPE = ctypes.CFUNCTYPE(
        ctypes.c_uint,    # retour : EdsError
        ctypes.c_uint,    # event
        ctypes.c_void_p,  # object (handle du fichier)
        ctypes.c_void_p   # context
    )

    def on_object_event(event, obj, context):
        """
        Appele par EDSDK quand une nouvelle photo est disponible.
        On telecharge le fichier vers chemin_fichier.
        """
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
                print(f"Canon : photo sauvegardee -> {chemin}")
                resultat[0] = chemin
            else:
                print(f"Canon : erreur creation stream : {hex(err_s)}")
                _edsdk.EdsDownloadCancel(obj)
            _edsdk.EdsRelease(obj)
            photo_recue[0] = True
        return EDS_ERR_OK

    # Garder la reference (empeche Python de supprimer le callback)
    _callback_ref = CALLBACK_TYPE(on_object_event)

    # Enregistrer le callback
    _edsdk.EdsSetObjectEventHandler(
        _camera,
        kEdsObjectEvent_DirItemCreated,
        _callback_ref,
        None
    )

    # Mode SaveTo = Host : transfert direct vers le PC, sans carte SD
    save_to = ctypes.c_uint(kEdsSaveTo_Host)
    _edsdk.EdsSetPropertyData(
        _camera,
        kEdsPropID_SaveTo,
        0,
        ctypes.sizeof(save_to),
        ctypes.byref(save_to)
    )

    # Declencher
    err = _edsdk.EdsSendCommand(_camera, kEdsCameraCommand_TakePicture, 0)
    if err != EDS_ERR_OK:
        print(f"Erreur declenchement : {hex(err)}")
        return None

    # Attendre le callback (max 20 secondes)
    # Le thread _boucle_events pompe EdsGetEvent() en continu,
    # ce qui permet au callback d'etre appele sans bloquer ce thread.
    debut = time.time()
    while not photo_recue[0]:
        time.sleep(0.1)
        if time.time() - debut > 20:
            print("Canon : timeout — aucune photo recue apres 20 secondes.")
            return None

    return resultat[0]


def deconnecter_canon():
    """Arrete le thread evenements et ferme la session."""
    global _camera, _continuer_events
    _continuer_events = False
    if _camera is not None:
        _edsdk.EdsCloseSession(_camera)
        _edsdk.EdsRelease(_camera)
        _camera = None
    if _edsdk is not None:
        _edsdk.EdsTerminateSDK()
    print("Canon deconnecte.")


# Test direct
if __name__ == "__main__":
    import subprocess
    subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"], capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
    time.sleep(2)
    cam = connecter_canon()
    if cam:
        os.makedirs("images/test", exist_ok=True)
        res = prendre_photo_canon("images/test/canon_test.jpg")
        print(f"Resultat : {res}")
        deconnecter_canon()
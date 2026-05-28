# acquisition/canon.py
# Controle du Canon EOS R7 via EDSDK (USB) avec ctypes
#
# METHODE : SaveTo = Camera (enregistrement sur carte SD)
# Le Canon prend la photo et l'ecrit sur sa carte SD.
# On navigue ensuite dans l'arborescence de la carte pour
# recuperer le dernier fichier cree et le copier sur le PC.
#
# Pourquoi cette methode plutot que SaveTo = Host ?
# Sur Linux, l'evenement DirItemCreated de l'EDSDK ne se declenche
# pas de facon fiable en mode SaveTo Host. C'est un probleme connu
# sur Linux (fonctionne bien sur Windows et Mac).
# La methode par navigation d'arborescence est celle utilisee par
# le programme exemple officiel Canon (MultiCamCui) et elle fonctionne.

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
kEdsSaveTo_Camera                      = 0x00000001   # enregistre sur la carte SD
kEdsPropID_SaveTo                      = 0x00000390

# ── Variables globales ────────────────────────────────────────────────────────
_edsdk            = None
_camera           = None
_sdk_initialise   = False
_thread_events    = None
_continuer_events = False


def _boucle_events():
    """Pompe la file d'evenements EDSDK toutes les 50ms."""
    while _continuer_events:
        if _edsdk:
            _edsdk.EdsGetEvent()
        time.sleep(0.05)


def charger_edsdk():
    global _edsdk
    chemin = os.path.expanduser(CHEMIN_LIB)
    if not os.path.exists(chemin):
        for e in [
            os.path.expanduser("~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so"),
            "/usr/local/lib/libEDSDK.so",
            "./libEDSDK.so",
        ]:
            if os.path.exists(e):
                chemin = e
                break
        else:
            print("[EDSDK] ERREUR : libEDSDK.so introuvable.")
            return False
    try:
        _edsdk = ctypes.CDLL(chemin)
        print(f"[EDSDK] Charge depuis : {chemin}")
        return True
    except OSError as e:
        print(f"[EDSDK] ERREUR chargement : {e}")
        return False


def initialiser_edsdk():
    global _sdk_initialise
    if _sdk_initialise:
        return True
    if _edsdk is None:
        if not charger_edsdk():
            return False
    err = _edsdk.EdsInitializeSDK()
    if err != EDS_ERR_OK:
        print(f"[EDSDK] ERREUR initialisation : {hex(err)}")
        return False
    _sdk_initialise = True
    print("[EDSDK] SDK initialise.")
    return True


def connecter_canon():
    """
    Connecte le Canon EOS R7 et ouvre une session.
    Demarre le thread d'evenements en arriere-plan.
    Retourne le handle camera, ou None si echec.
    """
    global _camera, _thread_events, _continuer_events

    if _camera is not None:
        return _camera

    if not initialiser_edsdk():
        return None

    # Demarrer le thread d'evenements
    _continuer_events = True
    _thread_events = threading.Thread(target=_boucle_events, daemon=True)
    _thread_events.start()

    camera_list = ctypes.c_void_p()
    err = _edsdk.EdsGetCameraList(ctypes.byref(camera_list))
    if err != EDS_ERR_OK:
        print(f"[EDSDK] ERREUR EdsGetCameraList : {hex(err)}")
        return None

    count = ctypes.c_int()
    _edsdk.EdsGetChildCount(camera_list, ctypes.byref(count))
    print(f"[EDSDK] {count.value} camera(s) detectee(s).")

    if count.value == 0:
        print("[EDSDK] Aucune camera. Canon allume + cable USB + gvfs tue ?")
        _edsdk.EdsRelease(camera_list)
        return None

    camera = ctypes.c_void_p()
    _edsdk.EdsGetChildAtIndex(camera_list, 0, ctypes.byref(camera))
    _edsdk.EdsRelease(camera_list)

    err = _edsdk.EdsOpenSession(camera)
    if err != EDS_ERR_OK:
        print(f"[EDSDK] ERREUR EdsOpenSession : {hex(err)}")
        _edsdk.EdsRelease(camera)
        return None

    _camera = camera
    print("[EDSDK] Canon EOS R7 connecte. Session ouverte.")
    return camera


def _compter_fichiers_carte(camera):
    """
    Compte le nombre total de fichiers sur la carte SD du Canon.
    Utilise pour detecter quand une nouvelle photo a ete prise.
    Navigue : Camera -> Volume -> Dossier -> Fichiers
    """
    total = 0
    try:
        # Niveau 1 : volumes (cartes memoire)
        nb_volumes = ctypes.c_int()
        _edsdk.EdsGetChildCount(camera, ctypes.byref(nb_volumes))

        for v in range(nb_volumes.value):
            volume = ctypes.c_void_p()
            if _edsdk.EdsGetChildAtIndex(camera, v, ctypes.byref(volume)) != EDS_ERR_OK:
                continue

            # Niveau 2 : dossiers dans le volume
            nb_dossiers = ctypes.c_int()
            _edsdk.EdsGetChildCount(volume, ctypes.byref(nb_dossiers))

            for d in range(nb_dossiers.value):
                dossier = ctypes.c_void_p()
                if _edsdk.EdsGetChildAtIndex(volume, d, ctypes.byref(dossier)) != EDS_ERR_OK:
                    continue

                # Niveau 3 : fichiers dans le dossier
                nb_fichiers = ctypes.c_int()
                _edsdk.EdsGetChildCount(dossier, ctypes.byref(nb_fichiers))
                total += nb_fichiers.value
                _edsdk.EdsRelease(dossier)

            _edsdk.EdsRelease(volume)
    except Exception:
        pass
    return total


def _telecharger_dernier_fichier(camera, chemin_destination):
    """
    Navigue dans l'arborescence de la carte SD du Canon et
    telecharge le DERNIER fichier de chaque dossier.
    
    Structure de la carte Canon :
    Camera
    └── Volume (carte SD)
        └── DCIM/
            └── 100CANON/ (ou numerote autrement)
                ├── IMG_0001.JPG
                ├── IMG_0002.JPG
                └── IMG_XXXX.JPG  <- on veut celui-la (le dernier)
    """
    try:
        nb_volumes = ctypes.c_int()
        _edsdk.EdsGetChildCount(camera, ctypes.byref(nb_volumes))

        if nb_volumes.value == 0:
            print("[Canon] Aucun volume (carte SD) trouve.")
            return False

        # Prendre le premier volume (premiere carte SD)
        volume = ctypes.c_void_p()
        if _edsdk.EdsGetChildAtIndex(camera, 0, ctypes.byref(volume)) != EDS_ERR_OK:
            print("[Canon] Impossible d'acceder au volume.")
            return False

        nb_dossiers = ctypes.c_int()
        _edsdk.EdsGetChildCount(volume, ctypes.byref(nb_dossiers))
        print(f"[Canon] {nb_dossiers.value} dossier(s) sur la carte.")

        # Parcourir tous les dossiers et trouver le dernier fichier
        dernier_fichier = None

        for d in range(nb_dossiers.value):
            dossier = ctypes.c_void_p()
            if _edsdk.EdsGetChildAtIndex(volume, d, ctypes.byref(dossier)) != EDS_ERR_OK:
                continue

            nb_fichiers = ctypes.c_int()
            _edsdk.EdsGetChildCount(dossier, ctypes.byref(nb_fichiers))

            if nb_fichiers.value > 0:
                # Prendre le dernier fichier du dossier
                fichier = ctypes.c_void_p()
                idx_dernier = nb_fichiers.value - 1
                if _edsdk.EdsGetChildAtIndex(dossier, idx_dernier, ctypes.byref(fichier)) == EDS_ERR_OK:
                    if dernier_fichier is not None:
                        _edsdk.EdsRelease(dernier_fichier)
                    dernier_fichier = fichier

            _edsdk.EdsRelease(dossier)

        _edsdk.EdsRelease(volume)

        if dernier_fichier is None:
            print("[Canon] Aucun fichier trouve sur la carte.")
            return False

        # Telecharger le fichier vers le PC
        print(f"[Canon] Telechargement vers {chemin_destination}...")
        os.makedirs(
            os.path.dirname(chemin_destination) if os.path.dirname(chemin_destination) else ".",
            exist_ok=True
        )

        stream = ctypes.c_void_p()
        err = _edsdk.EdsCreateFileStream(
            chemin_destination.encode("utf-8"),
            kEdsFileCreateDisposition_CreateAlways,
            kEdsAccess_ReadWrite,
            ctypes.byref(stream)
        )

        if err != EDS_ERR_OK:
            print(f"[Canon] ERREUR EdsCreateFileStream : {hex(err)}")
            _edsdk.EdsRelease(dernier_fichier)
            return False

        # Taille 0 = telecharger le fichier entier
        _edsdk.EdsDownload(dernier_fichier, ctypes.c_ulonglong(0), stream)
        _edsdk.EdsDownloadComplete(dernier_fichier)
        _edsdk.EdsRelease(stream)
        _edsdk.EdsRelease(dernier_fichier)

        # Verifier que le fichier a bien ete cree et qu'il n'est pas vide
        if os.path.exists(chemin_destination) and os.path.getsize(chemin_destination) > 0:
            taille_ko = os.path.getsize(chemin_destination) / 1024
            print(f"[Canon] Fichier sauvegarde ({taille_ko:.0f} Ko) -> {chemin_destination}")
            return True
        else:
            print("[Canon] ERREUR : fichier vide ou non cree.")
            return False

    except Exception as e:
        print(f"[Canon] ERREUR navigation carte : {e}")
        return False


def prendre_photo_canon(chemin_fichier):
    """
    Declenche le Canon et recupere la photo depuis la carte SD.

    Etapes :
    1. Compter les fichiers existants sur la carte (avant)
    2. Configurer SaveTo = Camera (enregistrement sur carte SD)
    3. Declencher TakePicture
    4. Attendre que le nombre de fichiers augmente (max 15s)
    5. Telecharger le dernier fichier vers chemin_fichier

    Necessite une carte SD dans le Canon.

    Retourne chemin_fichier si succes, None sinon.
    """
    if _camera is None:
        print("[Canon] Pas de session ouverte. Appeler connecter_canon() d'abord.")
        return None

    # Compter les fichiers AVANT le declenchement
    nb_avant = _compter_fichiers_carte(_camera)
    print(f"[Canon] Fichiers sur la carte avant : {nb_avant}")

    # Configurer SaveTo = Camera (enregistrement sur carte SD)
    save_to = ctypes.c_uint(kEdsSaveTo_Camera)
    _edsdk.EdsSetPropertyData(
        _camera, kEdsPropID_SaveTo, 0,
        ctypes.sizeof(save_to), ctypes.byref(save_to)
    )

    # Declencher
    print("[Canon] Declenchement...")
    err = _edsdk.EdsSendCommand(_camera, kEdsCameraCommand_TakePicture, 0)
    if err != EDS_ERR_OK:
        print(f"[Canon] ERREUR declenchement : {hex(err)}")
        if err == 0x8D:
            print("[Canon] Erreur autofocus. Passez l'objectif en mode MF.")
        elif err == 0x61:
            print("[Canon] Handle invalide. Reconnectez le Canon.")
        return None

    print("[Canon] Commande envoyee. Attente de l'ecriture sur la carte...")

    # Attendre que le nombre de fichiers augmente (max 15 secondes)
    for tentative in range(150):   # 150 x 100ms = 15 secondes
        time.sleep(0.1)
        nb_apres = _compter_fichiers_carte(_camera)
        if nb_apres > nb_avant:
            print(f"[Canon] Nouvelle photo detectee sur la carte ({nb_apres} fichiers).")
            break
    else:
        print("[Canon] TIMEOUT : aucune nouvelle photo sur la carte apres 15s.")
        print("[Canon] Verifiez que le Canon est en mode prise de vue (M, Av, Tv, P).")
        return None

    # Attendre 0.5s supplementaires pour que l'ecriture soit complete
    time.sleep(0.5)

    # Telecharger le dernier fichier
    if _telecharger_dernier_fichier(_camera, chemin_fichier):
        return chemin_fichier
    return None


def deconnecter_canon():
    """Ferme la session et libere les ressources."""
    global _camera, _sdk_initialise, _continuer_events
    _continuer_events = False
    if _camera is not None:
        _edsdk.EdsCloseSession(_camera)
        _edsdk.EdsRelease(_camera)
        _camera = None
        print("[Canon] Session fermee.")
    if _edsdk is not None and _sdk_initialise:
        _edsdk.EdsTerminateSDK()
        _sdk_initialise = False


# ── Test direct ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import subprocess

    print("=" * 50)
    print("TEST CANON EOS R7 — methode carte SD")
    print("=" * 50)
    print("IMPORTANT : la carte SD doit etre dans le Canon.")
    print()

    subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"], capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
    time.sleep(2)

    cam = connecter_canon()
    if not cam:
        print("ECHEC connexion.")
        exit(1)

    os.makedirs("images/test", exist_ok=True)
    res = prendre_photo_canon("images/test/canon_test.jpg")

    if res and os.path.exists(res):
        print(f"\nSUCCES : {res} ({os.path.getsize(res) / 1024:.0f} Ko)")
    else:
        print("\nECHEC : photo non recuperee.")

    deconnecter_canon()
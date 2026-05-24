# acquisition/canon.py
# Controle du Canon EOS R7 via EDSDK (USB) avec ctypes
#
# Le fichier libEDSDK.so doit etre dans :
#   ~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so
#
# gvfs est tue automatiquement depuis interface.py avant chaque connexion.
# Plus besoin de lancer pkill manuellement.

import ctypes
import os
import time

CHEMIN_LIB = os.path.expanduser(
    "~/EDSDKv132010L/Linux/EDSDK/Library/x86_64/libEDSDK.so"
)

# ── Constantes EDSDK (EDSDK_API_Reference.pdf) ────────────────────────────────
EDS_ERR_OK                             = 0x00000000
kEdsCameraCommand_TakePicture          = 0x00000000
kEdsFileCreateDisposition_CreateAlways = 0x00000002
kEdsAccess_ReadWrite                   = 0x00000001
kEdsObjectEvent_DirItemCreated         = 0x00000203
kEdsPropID_SaveTo                      = 0x00000390
kEdsSaveTo_Host                        = 0x00000002

# ── Variables globales ────────────────────────────────────────────────────────
_edsdk   = None
_camera  = None

# Chemin de destination fourni par l'interface (mis a jour avant chaque capture)
_chemin_destination = None

# Callback de l'evenement "nouveau fichier cree" — stocke en global pour
# empecher le garbage collector Python de le supprimer pendant l'execution
_callback_ref = None


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
    Detecte le Canon EOS R7 et ouvre une session.
    Retourne le handle camera si succes, None sinon.

    Cette fonction est appelee depuis interface.py, qui a deja tue gvfs
    avant de l'invoquer. Ne pas rappeler pkill ici.
    """
    global _camera

    if _edsdk is None:
        if not initialiser_edsdk():
            return None

    # Obtenir la liste des cameras
    camera_list = ctypes.c_void_p()
    err = _edsdk.EdsGetCameraList(ctypes.byref(camera_list))
    if err != EDS_ERR_OK:
        print(f"Erreur liste cameras EDSDK : {hex(err)}")
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
    return camera


def prendre_photo_canon(chemin_fichier):
    """
    Declenche le Canon et recupere la photo sur l'ordinateur.

    Fonctionnement :
    1. On configure le Canon pour sauvegarder sur l'ordinateur (SaveTo = Host).
    2. On enregistre un callback sur l'evenement DirItemCreated : ce callback
       est appele par EDSDK des qu'une nouvelle photo est disponible.
    3. On declenche (TakePicture).
    4. On attend jusqu'a 15 secondes que le callback soit appele.
    5. Le callback telecharge le fichier directement dans chemin_fichier.

    L'erreur 0x22 (EDS_ERR_FILE_NOT_FOUND) dans l'ancienne version venait
    d'une navigation manuelle incorrecte dans l'arborescence de la carte
    memoire. En utilisant le callback DirItemCreated, on recoit directement
    le handle du fichier sans avoir a naviguer manuellement.
    """
    global _chemin_destination, _callback_ref

    if _camera is None:
        print("Canon non connecte.")
        return None

    os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)
    _chemin_destination = chemin_fichier

    # Indicateur de completion (liste mutable pour etre modifiable dans le callback)
    photo_recue = [False]
    resultat    = [None]

    # Type du callback EDSDK : EdsObjectEventHandler
    # Signature : EdsError callback(EdsObjectEvent event, EdsBaseRef object, EdsVoid* context)
    CALLBACK_TYPE = ctypes.CFUNCTYPE(
        ctypes.c_uint,       # type de retour : EdsError
        ctypes.c_uint,       # event
        ctypes.c_void_p,     # object (le dir_item de la photo)
        ctypes.c_void_p      # context
    )

    def on_object_event(event, obj, context):
        """
        Appele par EDSDK quand un evenement objet se produit.
        On ne reagit qu'a DirItemCreated (nouvelle photo disponible).
        """
        if event == kEdsObjectEvent_DirItemCreated:
            chemin = _chemin_destination
            stream = ctypes.c_void_p()
            chemin_bytes = chemin.encode('utf-8')

            err_stream = _edsdk.EdsCreateFileStream(
                chemin_bytes,
                kEdsFileCreateDisposition_CreateAlways,
                kEdsAccess_ReadWrite,
                ctypes.byref(stream)
            )

            if err_stream == EDS_ERR_OK:
                _edsdk.EdsDownload(obj, ctypes.c_ulonglong(0), stream)
                _edsdk.EdsDownloadComplete(obj)
                _edsdk.EdsRelease(stream)
                print(f"Canon : photo sauvegardee -> {chemin}")
                resultat[0] = chemin
            else:
                print(f"Canon : erreur creation stream : {hex(err_stream)}")
                _edsdk.EdsDownloadCancel(obj)

            _edsdk.EdsRelease(obj)
            photo_recue[0] = True

        return EDS_ERR_OK

    # Garder une reference au callback (empeche Python de le supprimer)
    _callback_ref = CALLBACK_TYPE(on_object_event)

    # Enregistrer le callback aupres de l'EDSDK
    _edsdk.EdsSetObjectEventHandler(
        _camera,
        kEdsObjectEvent_DirItemCreated,
        _callback_ref,
        None
    )

    # Configurer le Canon pour transferer directement vers l'ordinateur
    save_to = ctypes.c_uint(kEdsSaveTo_Host)
    _edsdk.EdsSetPropertyData(
        _camera,
        kEdsPropID_SaveTo,
        0,
        ctypes.sizeof(save_to),
        ctypes.byref(save_to)
    )

    # Declencher la photo
    err = _edsdk.EdsSendCommand(_camera, kEdsCameraCommand_TakePicture, 0)
    if err != EDS_ERR_OK:
        print(f"Erreur declenchement : {hex(err)}")
        return None

    # Attendre que le callback soit appele (max 15 secondes)
    debut = time.time()
    while not photo_recue[0]:
        # Pomper les evenements EDSDK (equivalent d'une boucle d'evenements)
        _edsdk.EdsGetEvent()
        time.sleep(0.1)
        if time.time() - debut > 15:
            print("Canon : timeout — photo non recue apres 15 secondes.")
            return None

    return resultat[0]


def deconnecter_canon():
    """Ferme la session et libere les ressources EDSDK."""
    global _camera
    if _camera is not None:
        _edsdk.EdsCloseSession(_camera)
        _edsdk.EdsRelease(_camera)
        _camera = None
    if _edsdk is not None:
        _edsdk.EdsTerminateSDK()
    print("Canon deconnecte.")


# Test direct (python3 acquisition/canon.py)
if __name__ == "__main__":
    import subprocess
    subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"], capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
    time.sleep(2)

    cam = connecter_canon()
    if cam:
        os.makedirs("images/test", exist_ok=True)
        resultat = prendre_photo_canon("images/test/canon_test.jpg")
        if resultat:
            print(f"Test reussi : {resultat}")
        else:
            print("Test echoue.")
        deconnecter_canon()
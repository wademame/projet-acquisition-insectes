# acquisition/canon.py
# Controle du Canon EOS R7
#
# Linux   : gphoto2 CLI (sudo apt install gphoto2)
# Windows : digiCamControl CLI (https://digicamcontrol.com/download)
#
# Pourquoi pas l'EDSDK ?
# L'EDSDK Canon presente deux problemes bloquants non resolus :
#   - Sur Linux : l'evenement DirItemCreated ne se declenche jamais,
#     bug connu de Canon non corrige.
#   - Sur Windows : la boucle d'evenements COM doit tourner dans le thread
#     principal, incompatible avec le threading de Tkinter.
# gphoto2 (Linux) et digiCamControl (Windows) contournent ces problemes.

import os
import sys
import time
import subprocess
import shutil

WINDOWS = sys.platform == "win32"
LINUX   = sys.platform.startswith("linux")

# Chemin vers digiCamControl sur Windows
DIGICAM_CMD = r"C:\Program Files (x86)\digiCamControl\CameraControlCmd.exe"


# ==============================================================================
# INTERFACE COMMUNE
# ==============================================================================

def connecter_canon():
    """
    Verifie que le Canon est detecte et accessible.
    Linux   -> True/False via gphoto2 --auto-detect
    Windows -> True/False via digiCamControl /capture test
    """
    if LINUX:
        return _connecter_linux()
    return _connecter_windows()


def prendre_photo_canon(chemin_fichier):
    """
    Declenche le Canon et sauvegarde la photo dans chemin_fichier.
    Linux   -> gphoto2 --capture-image-and-download
    Windows -> digiCamControl /capture /filename
    Retourne chemin_fichier si succes, None sinon.
    """
    if LINUX:
        return _prendre_photo_linux(chemin_fichier)
    return _prendre_photo_windows(chemin_fichier)


def deconnecter_canon():
    """Pas de session persistante a fermer sur ces deux methodes."""
    pass


# ==============================================================================
# LINUX — gphoto2
# ==============================================================================

def _gvfs_libre():
    """
    Tue gvfs-gphoto2 avant d'utiliser gphoto2.
    gvfs est un daemon Ubuntu qui prend automatiquement le controle
    du Canon des qu'il est branche, empechant gphoto2 d'y acceder.
    """
    subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"],  capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
    time.sleep(1.5)


def _connecter_linux():
    _gvfs_libre()
    try:
        r = subprocess.run(
            ["gphoto2", "--auto-detect"],
            capture_output=True, text=True, timeout=10
        )
        if "usb:" in r.stdout:
            print("[Canon Linux] Canon detecte via gphoto2.")
            return True
        print("[Canon Linux] Non detecte. Canon allume + cable USB ?")
        return False
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 absent : sudo apt install gphoto2")
        return False
    except subprocess.TimeoutExpired:
        print("[Canon Linux] Timeout detection.")
        return False


def _prendre_photo_linux(chemin_fichier):
    """
    Capture avec gphoto2 --capture-image-and-download.
    La photo est transferee directement sans carte SD.
    """
    _gvfs_libre()
    if os.path.dirname(chemin_fichier):
        os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

    print(f"[Canon Linux] Declenchement -> {chemin_fichier}")
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
            taille = os.path.getsize(chemin_fichier) // 1024
            print(f"[Canon Linux] OK ({taille} Ko) -> {chemin_fichier}")
            return chemin_fichier
        print(f"[Canon Linux] ECHEC (code {r.returncode}) : {r.stderr.strip()}")
        return None
    except subprocess.TimeoutExpired:
        print("[Canon Linux] TIMEOUT 30s.")
        return None
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 absent : sudo apt install gphoto2")
        return None


# ==============================================================================
# WINDOWS — digiCamControl
# ==============================================================================

def _connecter_windows():
    """
    Verifie que digiCamControl est installe et detecte le Canon.
    digiCamControl est un logiciel Windows gratuit qui supporte
    le controle a distance des appareils photo Canon via USB.
    Site : https://digicamcontrol.com/download
    """
    if not os.path.exists(DIGICAM_CMD):
        print(f"[Canon Windows] digiCamControl introuvable : {DIGICAM_CMD}")
        print("[Canon Windows] Installez-le depuis : https://digicamcontrol.com/download")
        return False

    try:
        # /list liste les cameras connectees sans declencher
        r = subprocess.run(
            [DIGICAM_CMD, "/list"],
            capture_output=True, text=True, timeout=10
        )
        sortie = r.stdout + r.stderr
        # digiCamControl affiche "Canon EOS" ou "New Camera is connected"
        if "Canon" in sortie or "Camera" in sortie:
            print("[Canon Windows] Canon detecte via digiCamControl.")
            return True
        # Si /list ne fonctionne pas (certaines versions), on essaie autrement
        print("[Canon Windows] Canon detecte (digiCamControl present).")
        return True
    except subprocess.TimeoutExpired:
        print("[Canon Windows] Timeout detection.")
        return False
    except Exception as e:
        print(f"[Canon Windows] Erreur detection : {e}")
        return False


def _prendre_photo_windows(chemin_fichier):
    """
    Capture avec digiCamControl /capture /filename.

    digiCamControl declenche le Canon, recupere la photo et la copie
    dans le fichier indique. La carte SD n'est pas necessaire.

    Fonctionnement de /filename :
    digiCamControl sauvegarde directement dans le chemin fourni.
    On cree le dossier si necessaire avant d'appeler la commande.
    """
    if not os.path.exists(DIGICAM_CMD):
        print(f"[Canon Windows] digiCamControl introuvable : {DIGICAM_CMD}")
        return None

    dossier = os.path.dirname(chemin_fichier)
    if dossier:
        os.makedirs(dossier, exist_ok=True)

    # Chemin absolu obligatoire pour digiCamControl
    chemin_absolu = os.path.abspath(chemin_fichier)

    print(f"[Canon Windows] Declenchement -> {chemin_absolu}")

    try:
        r = subprocess.run(
            [
                DIGICAM_CMD,
                "/capture",
                "/filename", chemin_absolu
            ],
            capture_output=True, text=True, timeout=30
        )

        sortie = r.stdout + r.stderr

        # Verifier si la photo a ete transferee
        if os.path.exists(chemin_absolu) and os.path.getsize(chemin_absolu) > 0:
            taille = os.path.getsize(chemin_absolu) // 1024
            print(f"[Canon Windows] OK ({taille} Ko) -> {chemin_absolu}")
            return chemin_absolu

        # digiCamControl peut sauvegarder dans son dossier par defaut
        # Si le fichier n'est pas au bon endroit, chercher la derniere photo transferee
        if "Transfer done" in sortie:
            # Extraire le chemin depuis la sortie de digiCamControl
            # Format : "Transfer done :C:\chemin\vers\photo.JPG"
            for ligne in sortie.splitlines():
                if "Transfer done" in ligne and ":" in ligne:
                    # Extraire le chemin apres "Transfer done :"
                    parties = ligne.split("Transfer done :")
                    if len(parties) > 1:
                        chemin_source = parties[1].strip()
                        if os.path.exists(chemin_source):
                            # Copier vers le bon emplacement
                            shutil.copy2(chemin_source, chemin_absolu)
                            taille = os.path.getsize(chemin_absolu) // 1024
                            print(f"[Canon Windows] OK ({taille} Ko) -> {chemin_absolu}")
                            return chemin_absolu

        print(f"[Canon Windows] ECHEC.")
        if sortie:
            print(f"[Canon Windows] Sortie : {sortie[:300]}")
        return None

    except subprocess.TimeoutExpired:
        print("[Canon Windows] TIMEOUT 30s.")
        return None
    except Exception as e:
        print(f"[Canon Windows] Erreur : {e}")
        return None


# ==============================================================================
# TEST DIRECT
# ==============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print(f"TEST CANON — {'Windows' if WINDOWS else 'Linux'}")
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
        print(f"\nSUCCES : {res} ({os.path.getsize(res)//1024} Ko)")
    else:
        print("\nECHEC : photo non recuperee.")

    deconnecter_canon()
# acquisition/canon.py
# Contrôle du Canon EOS R7
# Linux   : gphoto2 CLI
# Windows : digiCamControl CLI
#
# Problème "Could not claim USB device" avec téléphone branché :
# ADB (Android Debug Bridge) lance un daemon qui scanne tous les appareils USB,
# y compris le Canon. gvfs fait pareil. Les deux bloquent gphoto2.
#
# Solution appliquée dans ce fichier :
# Avant chaque capture Canon, on tue le daemon ADB et gvfs.
# Après la capture, on redémarre ADB pour que l'Android reste disponible.
#
# Règle udev permanente à lancer UNE SEULE FOIS sur le PC (Linux Mint / Ubuntu) :
#
#   sudo tee /etc/udev/rules.d/99-canon-r7.rules << 'EOF'
#   ATTRS{idVendor}=="04a9", ATTRS{idProduct}=="32f7", ENV{ID_MEDIA_PLAYER}="1"
#   ATTRS{idVendor}=="04a9", ATTRS{idProduct}=="32f7", ENV{MTP_NO_PROBE}="1"
#   EOF
#   sudo udevadm control --reload-rules
#   sudo udevadm trigger
#
# Après ça, gvfs ignore le Canon. ADB est toujours tué avant chaque capture
# mais redémarre automatiquement pour l'Android.

import os
import sys
import time
import subprocess
import shutil

WINDOWS = sys.platform == "win32"
LINUX   = sys.platform.startswith("linux")

DIGICAM_CMD = r"C:\Program Files (x86)\digiCamControl\CameraControlCmd.exe"


def connecter_canon():
    if LINUX:
        return _connecter_linux()
    return _connecter_windows()


def prendre_photo_canon(chemin_fichier):
    if LINUX:
        return _prendre_photo_linux(chemin_fichier)
    return _prendre_photo_windows(chemin_fichier)


def deconnecter_canon():
    pass


def _liberer_usb_canon():
    """
    Libère le port USB du Canon en tuant tous les processus qui pourraient
    le bloquer : gvfs-gphoto2 et le daemon ADB.

    ADB est redémarré après la capture par l'interface si l'Android est branché.
    sleep 2 laisse le temps au système de libérer l'interface USB.
    Note : écrire "sleep 2" avec un espace — "sleep2" est une erreur courante.
    """
    subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"],  capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
    subprocess.run(["adb", "kill-server"], capture_output=True)
    time.sleep(2)


def _connecter_linux():
    _liberer_usb_canon()
    try:
        r = subprocess.run(
            ["gphoto2", "--auto-detect"],
            capture_output=True, text=True, timeout=10
        )
        if "Canon" in r.stdout or "usb:" in r.stdout:
            print("[Canon Linux] Détecté via gphoto2.")
            return True
        print("[Canon Linux] Non détecté. Canon allumé + câble USB ?")
        return False
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 absent : sudo apt install gphoto2")
        return False


def _prendre_photo_linux(chemin_fichier):
    _liberer_usb_canon()
    dossier = os.path.dirname(chemin_fichier)
    if dossier:
        os.makedirs(dossier, exist_ok=True)
    base_sans_ext = os.path.splitext(chemin_fichier)[0]
    print(f"[Canon Linux] gphoto2 -> {chemin_fichier}")
    try:
        r = subprocess.run(
            ["gphoto2", "--capture-image-and-download",
             "--filename", chemin_fichier, "--force-overwrite"],
            capture_output=True, text=True, timeout=30
        )
        if r.returncode == 0:
            fichier = _trouver_fichier_cree(dossier, base_sans_ext, chemin_fichier)
            if fichier:
                print(f"[Canon Linux] OK ({os.path.getsize(fichier)//1024} Ko) -> {fichier}")
                return fichier
        print(f"[Canon Linux] Échec (code {r.returncode}) : {r.stderr.strip()[:200]}")
        if "Could not claim" in r.stderr:
            print("[Canon Linux] Un processus bloque encore le Canon.")
            print("[Canon Linux] Essayez de débrancher puis rebrancher le Canon.")
        return None
    except subprocess.TimeoutExpired:
        print("[Canon Linux] TIMEOUT 30s.")
        return None
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 absent : sudo apt install gphoto2")
        return None


def _trouver_fichier_cree(dossier, base_sans_ext, chemin_demande):
    """
    Cherche le fichier créé par gphoto2 quelle que soit son extension.
    L'appareil peut produire .cr3 même si on demande .jpg (format RAW).
    """
    if os.path.exists(chemin_demande) and os.path.getsize(chemin_demande) > 0:
        return chemin_demande
    nom_base = os.path.basename(base_sans_ext).lower()
    if os.path.exists(dossier):
        for f in os.listdir(dossier):
            if os.path.splitext(f)[0].lower() == nom_base:
                chemin = os.path.join(dossier, f)
                if os.path.getsize(chemin) > 0:
                    return chemin
    return None


def _connecter_windows():
    if not os.path.exists(DIGICAM_CMD):
        print(f"[Canon Windows] digiCamControl introuvable : {DIGICAM_CMD}")
        print("[Canon Windows] Installez-le : https://digicamcontrol.com/download")
        return False
    print("[Canon Windows] digiCamControl présent.")
    return True


def _prendre_photo_windows(chemin_fichier):
    if not os.path.exists(DIGICAM_CMD):
        return None
    dossier = os.path.dirname(chemin_fichier)
    if dossier:
        os.makedirs(dossier, exist_ok=True)
    chemin_absolu = os.path.abspath(chemin_fichier)
    base_sans_ext = os.path.splitext(chemin_absolu)[0]
    print(f"[Canon Windows] digiCamControl -> {chemin_absolu}")
    try:
        r = subprocess.run(
            [DIGICAM_CMD, "/capture", "/filename", chemin_absolu],
            capture_output=True, text=True, timeout=30
        )
        sortie = r.stdout + r.stderr
        if os.path.exists(chemin_absolu) and os.path.getsize(chemin_absolu) > 0:
            print(f"[Canon Windows] OK ({os.path.getsize(chemin_absolu)//1024} Ko)")
            return chemin_absolu
        if "Transfer done" in sortie:
            for ligne in sortie.splitlines():
                if "Transfer done" in ligne:
                    parties = ligne.split("Transfer done :")
                    if len(parties) > 1:
                        source = parties[1].strip()
                        if os.path.exists(source):
                            ext_source = os.path.splitext(source)[1]
                            cible = base_sans_ext + ext_source
                            shutil.copy2(source, cible)
                            print(f"[Canon Windows] OK ({os.path.getsize(cible)//1024} Ko) -> {cible}")
                            return cible
        print("[Canon Windows] Échec.")
        return None
    except subprocess.TimeoutExpired:
        print("[Canon Windows] TIMEOUT.")
        return None
    except Exception as e:
        print(f"[Canon Windows] Erreur : {e}")
        return None


if __name__ == "__main__":
    print(f"TEST CANON — {'Windows' if WINDOWS else 'Linux'}")
    ok = connecter_canon()
    if not ok:
        exit(1)
    os.makedirs("images/test", exist_ok=True)
    res = prendre_photo_canon("images/test/canon_test.jpg")
    print(f"Résultat : {res if res else 'Échec'}")
    deconnecter_canon()
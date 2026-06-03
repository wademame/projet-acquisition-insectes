# acquisition/canon.py
# Contrôle du Canon EOS R7 via gphoto2 (Linux) ou digiCamControl (Windows).


import os
import sys
import time
import subprocess
import shutil

WINDOWS = sys.platform == "win32"
LINUX   = sys.platform.startswith("linux")

DIGICAM_CMD = r"C:\Program Files (x86)\digiCamControl\CameraControlCmd.exe"

# Port USB du Canon, mis à jour à chaque détection
_port_canon = None


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


def _liberer_gvfs():
    """
    Tue gvfs-gphoto2 et gvfsd-mtp qui bloquent l'accès au Canon.
    ADB n'est pas tué ici pour ne pas couper la connexion Android.
    sleep 2 laisse le temps au système de libérer le port USB.
    """
    subprocess.run(["pkill", "-9", "-f", "gvfs-gphoto2"],  capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-gphoto2"], capture_output=True)
    subprocess.run(["pkill", "-9", "-f", "gvfsd-mtp"],     capture_output=True)
    time.sleep(2)


def _detecter_port_canon():
    """
    Cherche le port USB du Canon dans la liste gphoto2 --auto-detect.
    Retourne le port sous forme "usb:004,030" ou None si non trouvé. Car
    Quand le téléphone et le Canon sont branchés, gphoto2 liste deux appareils.
    Sans --port, gphoto2 prend le premier, souvent le téléphone.
    On cherche explicitement la ligne qui contient "Canon" pour avoir son port.

    Exemple de sortie de gphoto2 --auto-detect :
        Oppo Find 7 (ID 1)    usb:004,032
        Canon EOS R7          usb:004,034
    On récupère "usb:004,034".
    """
    try:
        r = subprocess.run(
            ["gphoto2", "--auto-detect"],
            capture_output=True, text=True, timeout=10
        )
        for ligne in r.stdout.splitlines():
            if "Canon" in ligne or "canon" in ligne.lower():
                # La ligne est du type par exemple "Canon EOS R7     usb:004,034"
                # Le port est le dernier mot de la ligne
                parties = ligne.split()
                for p in reversed(parties):
                    if p.startswith("usb:"):
                        return p
    except Exception:
        pass
    return None


def _connecter_linux():
    global _port_canon
    _liberer_gvfs()
    try:
        port = _detecter_port_canon()
        if port:
            _port_canon = port
            print(f"[Canon Linux] Détecté sur le port {port}.")
            return True
        # Vérifier s'il y a au moins un appareil avec gphoto2
        r = subprocess.run(
            ["gphoto2", "--auto-detect"],
            capture_output=True, text=True, timeout=10
        )
        if "usb:" in r.stdout:
            print("[Canon Linux] Appareil détecté mais pas identifié comme Canon.")
            print(f"[Canon Linux] Liste : {r.stdout.strip()}")
        else:
            print("[Canon Linux] Aucun appareil. Canon allumé + câble USB ?")
        return False
    except FileNotFoundError:
        print("[Canon Linux] gphoto2 absent : sudo apt install gphoto2")
        return False


def _prendre_photo_linux(chemin_fichier):
    """
    Capture avec gphoto2 en spécifiant explicitement le port du Canon.
    Si le port n'est pas connu, on le détecte d'abord.

    L'option --port usb:XXX,YYY force gphoto2 à utiliser le Canon et non
    le téléphone Android même s'ils sont tous les deux branchés.
    """
    global _port_canon

    _liberer_gvfs()

    # Détecter le port si pas encore fait
    if not _port_canon:
        _port_canon = _detecter_port_canon()

    if not _port_canon:
        print("[Canon Linux] Port Canon non trouvé. Canon branché et allumé ?")
        return None

    dossier = os.path.dirname(chemin_fichier)
    if dossier:
        os.makedirs(dossier, exist_ok=True)

    base_sans_ext = os.path.splitext(chemin_fichier)[0]
    print(f"[Canon Linux] gphoto2 --port {_port_canon} -> {chemin_fichier}")

    try:
        r = subprocess.run(
            [
                "gphoto2",
                "--port", _port_canon,
                "--capture-image-and-download",
                "--filename", chemin_fichier,
                "--force-overwrite"
            ],
            capture_output=True, text=True, timeout=30
        )

        if r.returncode == 0:
            fichier = _trouver_fichier_cree(dossier, base_sans_ext, chemin_fichier)
            if fichier:
                print(f"[Canon Linux] OK ({os.path.getsize(fichier)//1024} Ko) -> {fichier}")
                return fichier

        print(f"[Canon Linux] Échec (code {r.returncode}) : {r.stderr.strip()[:300]}")

        if "PTP Device Busy" in r.stderr or "0x2019" in r.stderr:
            print("[Canon Linux] L'objectif est en mode AF (autofocus).")
            print("[Canon Linux] Passez l'objectif en MF (mise au point manuelle).")
            print("[Canon Linux] Interrupteur AF/MF sur l'objectif.")
        elif "Could not claim" in r.stderr:
            print("[Canon Linux] Port USB bloqué. Débranchez et rebranchez le Canon.")
        elif "Unsupported operation" in r.stderr or "generic capture" in r.stderr:
            # gphoto2 a pris le mauvais appareil il va du coup réinitialiser le port
            _port_canon = None
            print("[Canon Linux] Mauvais appareil ciblé. Port réinitialisé.")
            print("[Canon Linux] Relancez la détection.")

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
    L'appareil peut produire .cr3 (RAW) même si on demande .jpg.
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
    print(f"TEST CANON : {'Windows' if WINDOWS else 'Linux'}")
    print("Détection du port Canon...")
    ok = connecter_canon()
    if not ok:
        print("Canon non détecté.")
        exit(1)
    print(f"Canon détecté sur le port : {_port_canon}")
    os.makedirs("images/test", exist_ok=True)
    res = prendre_photo_canon("images/test/canon_test.jpg")
    print(f"Résultat : {res if res else 'Échec'}")
    deconnecter_canon()
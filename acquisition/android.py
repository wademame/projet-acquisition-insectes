# acquisition/android.py
# Controle Android via ADB
# INSTALLATION : sudo apt install adb
# Sur le telephone : Options developpeur > Debogage USB > Activer

import subprocess
import os
import time
from acquisition.nommage import (
    generer_nom_fichier,
    generer_chemin_dossier,
    prochain_numero_photo
)


def connecter_android():
    """
    Verifie la connexion ADB et retourne l'ID du telephone.
    Retourne None si aucun telephone n'est detecte.
    """
    try:
        r = subprocess.run(['adb', 'devices'], capture_output=True, text=True, timeout=5)
        appareils = [
            l.split('\t')[0]
            for l in r.stdout.strip().split('\n')[1:]
            if '\tdevice' in l
        ]
        if appareils:
            print(f"Android connecte : {appareils[0]}")
            return appareils[0]
        print("Aucun Android detecte.")
        return None
    except FileNotFoundError:
        print("ADB non installe. Lance : sudo apt install adb")
        return None


def prendre_photo_android(id_appareil, chemin_destination):
    """
    Prend UNE photo avec l'Android et la copie sur l'ordi.

    Methode :
    1. On note combien de photos existent dans DCIM/Camera AVANT
    2. On declenche la camera
    3. On attend que le nombre de photos augmente
    4. On recupere UNIQUEMENT la nouvelle photo
    5. On la copie avec le bon nom dans le bon dossier
    """
    os.makedirs(os.path.dirname(chemin_destination), exist_ok=True)

    dossier_android = '/sdcard/DCIM/Camera/'

    # Etape 1 : compter les photos existantes avant le declenchement
    def lister_photos():
        r = subprocess.run(
            ['adb', '-s', id_appareil, 'shell', 'ls', '-t', dossier_android],
            capture_output=True, text=True
        )
        return [
            f.strip() for f in r.stdout.strip().split('\n')
            if f.strip().lower().endswith(('.jpg', '.jpeg'))
        ]

    photos_avant = lister_photos()
    print(f"Photos existantes avant : {len(photos_avant)}")

    # Etape 2 : ouvrir la camera et declencher
    # D'abord fermer toute instance ouverte de la camera
    subprocess.run(
        ['adb', '-s', id_appareil, 'shell', 'am', 'force-stop', 'com.android.camera2'],
        capture_output=True
    )
    subprocess.run(
        ['adb', '-s', id_appareil, 'shell', 'am', 'force-stop', 'com.google.android.GoogleCamera'],
        capture_output=True
    )
    time.sleep(0.5)

    # Lancer la camera en mode capture immediate
    subprocess.run([
        'adb', '-s', id_appareil, 'shell',
        'am', 'start', '-a', 'android.media.action.STILL_IMAGE_CAMERA'
    ], capture_output=True)
    time.sleep(2)

    # Declencher (keyevent CAMERA = 27, ou VOLUME_DOWN = 25 selon le telephone)
    subprocess.run(
        ['adb', '-s', id_appareil, 'shell', 'input', 'keyevent', '27'],
        capture_output=True
    )
    time.sleep(0.5)
    # Deuxieme essai avec volume down au cas ou
    subprocess.run(
        ['adb', '-s', id_appareil, 'shell', 'input', 'keyevent', '25'],
        capture_output=True
    )

    # Etape 3 : attendre l'apparition de la nouvelle photo (max 10 secondes)
    nouvelle_photo = None
    for tentative in range(20):
        time.sleep(0.5)
        photos_apres = lister_photos()

        # Trouver les nouvelles photos (celles qui n'etaient pas la avant)
        nouvelles = [p for p in photos_apres if p not in photos_avant]

        if nouvelles:
            nouvelle_photo = dossier_android + nouvelles[0]
            print(f"Nouvelle photo detectee : {nouvelle_photo}")
            break

    if nouvelle_photo is None:
        print("Android : aucune nouvelle photo detectee apres 10 secondes.")
        print("Essaie de declencher manuellement depuis le telephone.")
        return None

    # Etape 4 : attendre que le fichier soit completement ecrit
    time.sleep(1)

    # Etape 5 : copier la photo sur l'ordi avec le bon nom
    r_pull = subprocess.run(
        ['adb', '-s', id_appareil, 'pull', nouvelle_photo, chemin_destination],
        capture_output=True, text=True
    )

    if r_pull.returncode == 0:
        print(f"Android : photo sauvegardee -> {chemin_destination}")
        return chemin_destination
    else:
        print(f"Android : erreur copie : {r_pull.stderr}")
        return None


if __name__ == "__main__":
    print("=== Test Android via ADB ===")
    id_tel = connecter_android()
    if id_tel:
        os.makedirs("images/test", exist_ok=True)
        res = prendre_photo_android(id_tel, "images/test/android_test.jpg")
        if res:
            print(f"Test reussi : {res}")
        else:
            print("Test echoue.")
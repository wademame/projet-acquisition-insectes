# traitement/stacking.py
# Focus stacking : combine plusieurs photos prises a des focales differentes
# pour produire une seule image entierement nette.
#
# Principe :
#   A fort grossissement, la profondeur de champ est tres faible.
#   On prend plusieurs photos du meme insecte en changeant la mise au point
#   a chaque prise (focus different). Chaque photo est nette sur une zone
#   differente. L'algorithme detecte les zones nettes de chaque image et
#   les assemble en une seule image ou tout est net.
#
# Methode : AlignMTB + Mertens (OpenCV)
#   AlignMTB : aligne les images pour corriger les micro-decalages
#              dus a la manipulation manuelle du focus.
#   Mertens  : fusionne les images en selectionnant les zones nettes
#              de chacune (algorithme de fusion par exposition multiple).
#
# Installation dans le venv :
#   pip install opencv-python
#
# Le fichier .tiff est un format d'image sans compression, comme le PNG
# mais utilise en standard dans les domaines scientifiques et medicaux.
# Il preserves toutes les informations sans perte de qualite.
# Il s'ouvre directement dans le gestionnaire de fichiers Ubuntu.

import cv2
import os
import numpy as np


def charger_images(liste_chemins):
    """
    Charge une liste de fichiers image.
    Retourne une liste de tableaux numpy (format OpenCV).
    Ignore les fichiers qui ne peuvent pas etre lus en affichant un avertissement.
    """
    images = []
    for chemin in liste_chemins:
        # os.path.abspath convertit le chemin relatif en chemin absolu
        # pour eviter les erreurs de chemin selon d'ou on lance le script
        chemin_abs = os.path.abspath(chemin)
        img = cv2.imread(chemin_abs)
        if img is None:
            print(f"Attention : impossible de charger {chemin_abs}")
            print("  Verifiez que le fichier existe et que le chemin est correct.")
        else:
            images.append(img)
    print(f"{len(images)} image(s) chargee(s) sur {len(liste_chemins)} fournie(s).")
    return images


def aligner_images(images):
    """
    Aligne les images entre elles pour corriger les micro-decalages.

    Entre deux prises de vue, meme sur trepied, il peut y avoir de legeres
    vibrations ou des deplacements dus a la manipulation du focus.
    AlignMTB (Median Threshold Bitmap) corrige ces decalages rapidement
    en comparant les niveaux de luminosite des images.
    """
    if len(images) < 2:
        return images
    aligneur = cv2.createAlignMTB()
    aligneur.process(images, images)
    print("Alignement termine.")
    return images


def fusionner_focus(images):
    """
    Fusionne les images en selectionnant les zones nettes de chacune.

    L'algorithme de Mertens calcule pour chaque pixel un score de qualite
    base sur le contraste local (les zones nettes ont un contraste eleve,
    les zones floues un contraste faible). Il construit ensuite l'image
    finale en ponderant chaque pixel selon ce score.

    Retourne une image numpy uint8 (valeurs entre 0 et 255).
    """
    fusionneur = cv2.createMergeMertens()
    resultat_float = fusionneur.process(images)
    # L'algorithme retourne des valeurs float32 entre 0 et 1.
    # On les convertit en entiers 0-255 pour sauvegarder en image standard.
    resultat_uint8 = np.clip(resultat_float * 255, 0, 255).astype("uint8")
    print("Fusion terminee.")
    return resultat_uint8


def sauvegarder_resultat(image, chemin_sortie):
    """
    Sauvegarde l'image stackee dans le fichier indique.
    Cree les dossiers intermediaires si necessaire.
    """
    dossier = os.path.dirname(chemin_sortie)
    if dossier:
        os.makedirs(dossier, exist_ok=True)
    succes = cv2.imwrite(chemin_sortie, image)
    if succes:
        print(f"Image stackee sauvegardee -> {chemin_sortie}")
    else:
        print(f"Erreur : impossible de sauvegarder dans {chemin_sortie}")
    return succes


def focus_stacking(liste_chemins, chemin_sortie):
    """
    Fonction principale appelee depuis l'interface.

    Parametres :
        liste_chemins : liste de chemins vers les photos brutes
        chemin_sortie : chemin du fichier de sortie (.tiff recommande)

    Retourne le chemin de sortie si succes, None sinon.

    Exemple d'appel :
        focus_stacking(
            ["images/Canon/scolyte1/individu_01/photo01.jpg",
             "images/Canon/scolyte1/individu_01/photo02.jpg",
             "images/Canon/scolyte1/individu_01/photo03.jpg"],
            "images/Canon/scolyte1/individu_01/scolyte1_ind01_camCanon_mag10x_angleDorsal_STACKEE.tiff"
        )
    """
    if len(liste_chemins) < 2:
        print("Il faut au moins 2 images pour le focus stacking.")
        return None

    print(f"\nFocus stacking de {len(liste_chemins)} images...")
    print("Etape 1/3 : chargement des images")
    images = charger_images(liste_chemins)

    if len(images) < 2:
        print("Pas assez d'images valides (minimum 2).")
        return None

    print("Etape 2/3 : alignement")
    images = aligner_images(images)

    print("Etape 3/3 : fusion focus stacking")
    resultat = fusionner_focus(images)

    if sauvegarder_resultat(resultat, chemin_sortie):
        print(f"Succes : {chemin_sortie}\n")
        return chemin_sortie

    return None


# ── Test depuis le terminal ───────────────────────────────────────────────────
# Usage : python3 traitement/stacking.py photo1.jpg photo2.jpg photo3.jpg sortie.tiff
#
# Exemple concret avec vos photos :
#   python3 traitement/stacking.py \
#     images/Android/scolyte1/individu_01/scolyte1_ind01_camAndroid_mag10x_angleDorsal_photo01.jpg \
#     images/Android/scolyte1/individu_01/scolyte1_ind01_camAndroid_mag10x_angleDorsal_photo02.jpg \
#     images/Android/scolyte1/individu_01/scolyte1_ind01_camAndroid_mag10x_angleDorsal_photo03.jpg \
#     images/Android/scolyte1/individu_01/scolyte1_STACKEE.tiff
#
# Pour voir les vrais noms de vos fichiers :
#   ls images/Android/scolyte1/individu_01/

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage : python3 traitement/stacking.py photo1 photo2 [photo3...] sortie.tiff")
        print("")
        print("Pour voir les fichiers disponibles :")
        print("  ls images/Android/scolyte1/individu_01/")
        sys.exit(0)

    entrees = sys.argv[1:-1]
    sortie  = sys.argv[-1]
    res = focus_stacking(entrees, sortie)
    if res:
        print(f"Stacking reussi : {res}")
    else:
        print("Stacking echoue.")

#La Jeulin se comporte comme une webcam standard. 
# Python lui assigne un numéro (0, 1, 2...). 
# Ce script trouve le bon numéro et capture une image.
# fichier : acquisition/jeulin.py
     # bibliothèque caméra
# acquisition/jeulin.py
# Controle de la camera Jeulin e-mago via USB (protocole webcam)

import cv2
import os
import time
from acquisition.nommage import generer_nom_fichier, generer_chemin_dossier


def trouver_index_jeulin():
    """
    Liste toutes les cameras disponibles et affiche leurs index.
    Utilise ce script une fois pour trouver l'index de la Jeulin.
    """
    print("Recherche des cameras disponibles...")
    cameras_trouvees = []

    for i in range(6):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            largeur = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            hauteur = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            print(f"  Index {i} : camera detectee ({largeur}x{hauteur})")
            cameras_trouvees.append(i)
            cap.release()
        else:
            cap.release()

    if not cameras_trouvees:
        print("Aucune camera detectee. Verifie le branchement USB.")
    return cameras_trouvees


def prendre_photo_jeulin(index_camera, chemin_fichier):
    """
    Capture une image depuis la Jeulin et la sauvegarde.
    index_camera : le numero trouve avec trouver_index_jeulin()
    chemin_fichier : chemin complet avec nom du fichier
    """
    cap = cv2.VideoCapture(index_camera)

    if not cap.isOpened():
        print(f"Erreur : impossible d'ouvrir la camera a l'index {index_camera}.")
        return None

    # Regler la resolution maximale de la Jeulin (2592 x 1944)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)

    # Attendre que le capteur se stabilise (important pour la qualite)
    time.sleep(0.5)

    ok, image = cap.read()
    cap.release()

    if ok:
        os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)
        cv2.imwrite(chemin_fichier, image)
        print(f"Jeulin : photo sauvegardee -> {chemin_fichier}")
        return chemin_fichier
    else:
        print(f"Erreur : capture echouee depuis la Jeulin (index {index_camera}).")
        return None


def serie_focus_stacking_jeulin(index_camera, espece, num_individu, grossissement, angle,
                                 dossier_base="images", nb_photos=10):
    """
    Prend une serie de photos depuis la Jeulin.
    Note : le focus de la Jeulin se change manuellement sur la loupe.
    """
    photos = []
    dossier = generer_chemin_dossier(dossier_base, espece, num_individu, "Jeulin")

    for i in range(1, nb_photos + 1):
        input(f"  Jeulin - photo {i}/{nb_photos} : ajuste le focus puis appuie sur ENTREE")

        nom_fichier = generer_nom_fichier(
            espece, num_individu, "Jeulin", grossissement, angle, i, "png"
        )
        chemin = os.path.join(dossier, nom_fichier)

        resultat = prendre_photo_jeulin(index_camera, chemin)
        if resultat:
            photos.append(resultat)

    print(f"Jeulin : serie terminee, {len(photos)} photos prises.")
    return photos
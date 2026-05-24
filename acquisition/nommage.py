# acquisition/nommage.py
# Gestion du nommage des fichiers et creation des dossiers
# Les parametres viennent directement du formulaire de l'interface

import os


def generer_nom_fichier(espece, num_individu, appareil, grossissement, angle,
                         num_photo, extension):
    """
    Genere un nom de fichier structure avec toutes les metadonnees.

    Exemple de resultat :
        scolyte1_ind01_camCanon_mag10x_angleTop_photo03.jpg

    Les parametres viennent du formulaire de l'interface :
        espece        : champ "Espece"         ex: "scolyte1"
        num_individu  : champ "N individu"     ex: 1
        appareil      : "Canon", "Jeulin" ou "Android"
        grossissement : champ "Grossissement"  ex: "10x"
        angle         : champ "Angle"          ex: "Top"
        num_photo     : numero auto-incremente ex: 1, 2, 3...
        extension     : "jpg", "png", "CR3"
    """
    nom = (
        f"{espece}"
        f"_ind{num_individu:02d}"
        f"_cam{appareil}"
        f"_mag{grossissement}"
        f"_angle{angle}"
        f"_photo{num_photo:02d}"
        f".{extension}"
    )
    return nom


def generer_chemin_dossier(dossier_base, appareil, espece, num_individu):
    """
    Genere le chemin du dossier de stockage.

    Structure : images/Canon/scolyte1/individu_01/
                images/Jeulin/scolyte1/individu_01/
                images/Android/scolyte1/individu_01/

    Cree automatiquement les dossiers s'ils n'existent pas.
    """
    chemin = os.path.join(
        dossier_base,
        appareil,
        espece,
        f"individu_{num_individu:02d}"
    )
    os.makedirs(chemin, exist_ok=True)
    return chemin


def prochain_numero_photo(dossier, espece, num_individu, appareil, grossissement,
                           angle, extension):
    """
    Trouve le prochain numero de photo disponible dans le dossier.
    Evite d'ecraser un fichier existant.

    Si photo01.jpg existe deja -> retourne 2
    Si photo01.jpg et photo02.jpg existent -> retourne 3
    """
    numero = 1
    while True:
        nom = generer_nom_fichier(
            espece, num_individu, appareil, grossissement, angle, numero, extension
        )
        chemin_complet = os.path.join(dossier, nom)
        if not os.path.exists(chemin_complet):
            return numero
        numero += 1


# Test rapide
if __name__ == "__main__":
    nom = generer_nom_fichier("scolyte1", 1, "Canon", "10x", "Top", 3, "jpg")
    print(nom)
    # -> scolyte1_ind01_camCanon_mag10x_angleTop_photo03.jpg

    chemin = generer_chemin_dossier("images", "Canon", "scolyte1", 1)
    print(chemin)
    # -> images/Canon/scolyte1/individu_01
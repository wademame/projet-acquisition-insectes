# acquisition/nommage.py
# Nommage structuré des fichiers et création automatique des dossiers.
#
# Convention : espece_indXX_camAppareil_angleAngle_photoXX.ext
# Exemple    : scolyte1_ind01_camCanon_angleDorsal_photo03.jpg
#
# Le grossissement a été retiré car les images sont toutes prises
# à la même distance avec la loupe binoculaire — l'information est
# redondante avec le contexte expérimental.
#
# L'extension n'est pas forcée — elle vient du fichier réel produit par l'appareil.

import os


def generer_nom_fichier(espece, num_individu, appareil, angle, num_photo, extension):
    """
    Génère le nom de fichier avec toutes les métadonnées encodées dedans.
    Le modèle IA peut lire l'espèce, l'angle, etc. directement depuis le nom.

    Retourne par exemple : scolyte1_ind01_camCanon_angleDorsal_photo03.jpg
    """
    return (
        f"{espece}"
        f"_ind{num_individu:02d}"
        f"_cam{appareil}"
        f"_angle{angle}"
        f"_photo{num_photo:02d}"
        f".{extension.lstrip('.')}"
    )


def generer_chemin_dossier(dossier_base, appareil, espece, num_individu):
    """
    Génère le chemin du dossier et le crée automatiquement.
    Structure : images/Canon/scolyte1/individu_01/

    os.makedirs avec exist_ok=True crée tous les sous-dossiers en une commande
    et ne plante pas si le dossier existe déjà.
    """
    chemin = os.path.join(
        dossier_base,
        appareil,
        espece,
        f"individu_{num_individu:02d}"
    )
    os.makedirs(chemin, exist_ok=True)
    return chemin


def prochain_numero_photo(dossier, espece, num_individu, appareil, angle, extension):
    """
    Trouve le premier numéro de photo disponible dans le dossier.
    Algorithme : boucle while, teste si le fichier existe, incrémente sinon.
    Garantit qu'aucune photo n'est jamais écrasée.
    """
    numero = 1
    while True:
        nom = generer_nom_fichier(espece, num_individu, appareil, angle, numero, extension)
        if not os.path.exists(os.path.join(dossier, nom)):
            return numero
        numero += 1


if __name__ == "__main__":
    print(generer_nom_fichier("scolyte1", 1, "Canon", "Dorsal", 3, "jpg"))
    print(generer_nom_fichier("scolyte1", 1, "Canon", "Dorsal", 3, "cr3"))
    print(generer_chemin_dossier("images", "Canon", "scolyte1", 1))
#Helicon Focus peut être lancé en ligne de commande depuis Python pour traiter 
# automatiquement des dossiers entiers.
# fichier : traitement/stacking.py

import subprocess
import os

# Chemin vers Helicon Focus (à adapter selon ton installation)
HELICON_PATH = r"C:\Program Files\Helicon Software\Helicon Focus 8\HeliconFocus.exe"

def focus_stack_dossier(dossier_entree, fichier_sortie):
    """
    Prend toutes les photos d'un dossier
    et crée 1 image stackée
    
    dossier_entree : dossier avec les 10 photos brutes
    fichier_sortie : chemin de l'image finale
    """
    commande = [
        HELICON_PATH,
        "-silent",           # pas d'interface graphique
        "-mp:1",             # méthode A (rapide)
        "-rp:4",             # rayon de fusion
        f"-source:{dossier_entree}",
        f"-result:{fichier_sortie}"
    ]
    
    print(f"Stack en cours : {dossier_entree}")
    resultat = subprocess.run(commande, capture_output=True)
    
    if resultat.returncode == 0:
        print(f"✓ Stack terminé : {fichier_sortie}")
    else:
        print("ERREUR stacking :", resultat.stderr.decode())

# Traiter tous les insectes automatiquement
def traiter_toutes_les_series():
    dossier_images = "images"
    
    for espece in os.listdir(dossier_images):
        for individu in os.listdir(f"{dossier_images}/{espece}"):
            for serie in os.listdir(f"{dossier_images}/{espece}/{individu}"):
                dossier_brutes = f"{dossier_images}/{espece}/{individu}/{serie}/canon"
                fichier_stack = f"{dossier_images}/{espece}/{individu}/{serie}/canon_stackee.tiff"
                
                focus_stack_dossier(dossier_brutes, fichier_stack)

traiter_toutes_les_series()
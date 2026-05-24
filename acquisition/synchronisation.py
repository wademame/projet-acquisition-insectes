# fichier : acquisition/synchronisation.py

import threading   # pour lancer plusieurs choses en parallèle
import time
import os
from datetime import datetime

# On importe les fonctions des autres scripts
from acquisition.canon  import prendre_photo_canon
from acquisition.jeulin import prendre_photo_jeulin
from acquisition.android import declencher_iphone
from acquisition.nommage import generer_chemin_dossier

def creer_dossier(espece, numero_individu, numero_serie):
    """Crée le dossier de destination pour cette prise"""
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    dossier = f"images/{espece}/individu_{numero_individu:03d}/serie_{numero_serie:02d}_{horodatage}"
    os.makedirs(dossier + "/canon",  exist_ok=True)
    os.makedirs(dossier + "/jeulin", exist_ok=True)
    os.makedirs(dossier + "/iphone", exist_ok=True)
    return dossier

def capture_synchronisee(espece, num_individu, num_serie, num_photo):
    """
    Déclenche les 3 appareils en même temps.
    C'est la fonction principale de tout le projet !
    """
    dossier = creer_dossier(espece, num_individu, num_serie)
    resultats = {}  # stocke les résultats de chaque appareil
    
    # Préparer les 3 "tâches" à lancer en parallèle
    def tache_canon():
        chemin = f"{dossier}/canon/photo_{num_photo:02d}.CR3"
        resultats['canon'] = prendre_photo_canon(chemin)
    
    def tache_jeulin():
        chemin = f"{dossier}/jeulin/photo_{num_photo:02d}.png"
        resultats['jeulin'] = prendre_photo_jeulin(1, chemin)
    
    def tache_iphone():
        chemin = f"{dossier}/iphone/photo_{num_photo:02d}.jpg"
        resultats['iphone'] = declencher_iphone(chemin)
    
    # Créer les 3 threads
    t1 = threading.Thread(target=tache_canon)
    t2 = threading.Thread(target=tache_jeulin)
    t3 = threading.Thread(target=tache_iphone)
    
    # Lancer les 3 EN MÊME TEMPS
    print(f"Déclenchement synchronisé — photo {num_photo}...")
    t1.start()
    t2.start()
    t3.start()
    
    # Attendre que les 3 aient fini
    t1.join()
    t2.join()
    t3.join()
    
    print(f"Photo {num_photo} capturée par les 3 appareils !")
    return resultats

# ============================================
# EXEMPLE COMPLET : 40 insectes, 5 espèces
# 10 photos par insecte (pour le focus stacking)
# ============================================

especes = ["scolyte_sp1", "scolyte_sp2", "scolyte_sp3", "scolyte_sp4", "scolyte_sp5"]
individus_par_espece = 8  # 8 insectes × 5 espèces = 40 individus

for espece in especes:
    for num_ind in range(1, individus_par_espece + 1):
        print(f"\n=== {espece} — Individu {num_ind} ===")
        input("Appuie sur ENTRÉE quand l'insecte est en place...")
        
        # 10 photos avec focus progressif
        for num_photo in range(1, 11):
            capture_synchronisee(espece, num_ind, 1, num_photo)
            time.sleep(0.3)  # petit délai entre les photos

print("\nAcquisition terminée !")
# fichier : main.py — le script principal à lancer

from acquisition.synchronisation import capture_synchronisee
from traitement.stacking import focus_stack_dossier
from base_de_donnees.bdd import ajouter_photo, ajouter_individu
import time

def workflow_insecte(espece_id, nom_espece, num_individu):
    """
    Workflow complet pour UN insecte :
    1. Capture 10 photos avec 3 appareils
    2. Focus stacking → 1 photo par appareil
    3. Enregistrement en base de données
    """
    print(f"\n{'='*50}")
    print(f"  {nom_espece} — Individu {num_individu}")
    print(f"{'='*50}")
    
    # === ÉTAPE 1 : ACQUISITION ===
    print("\n[1/3] Acquisition des photos...")
    input("Place l'insecte et appuie sur ENTRÉE")
    
    photos_brutes = []
    for num_photo in range(1, 11):  # 10 photos
        resultats = capture_synchronisee(nom_espece, num_individu, 1, num_photo)
        photos_brutes.append(resultats)
        
        # Avancer le focus entre chaque photo
        # (ajuster selon les paramètres du Canon)
        time.sleep(0.5)
    
    print(f"10 photos × 3 appareils = 30 images capturées")
    
    # === ÉTAPE 2 : FOCUS STACKING ===
    print("\n[2/3] Focus stacking en cours...")
    
    for appareil in ["canon", "jeulin", "iphone"]:
        dossier_brut = f"images/{nom_espece}/individu_{num_individu:03d}/serie_01/{appareil}"
        fichier_stack = f"images/{nom_espece}/individu_{num_individu:03d}/stackee_{appareil}.tiff"
        
        focus_stack_dossier(dossier_brut, fichier_stack)
    
    print("3 images stackées créées")
    
    # === ÉTAPE 3 : BASE DE DONNÉES ===
    print("\n[3/3] Enregistrement en base de données...")
    
    individu_id = ajouter_individu(espece_id, num_individu)
    
    for appareil in ["canon", "jeulin", "iphone"]:
        fichier = f"images/{nom_espece}/individu_{num_individu:03d}/stackee_{appareil}.tiff"
        ajouter_photo(individu_id, appareil, "stackee", fichier, "2592x1944")
    
    print("✓ Tout enregistré en base de données !")
    print(f"\nIndividu {num_individu} terminé !\n")

# ============ LANCEMENT PRINCIPAL ============
if __name__ == "__main__":
    print("=== Système d'acquisition d'insectes ===\n")
    
    especes = [
        (1, "Scolytus_scolytus"),
        (2, "Ips_typographus"),
        (3, "Dendroctonus_micans"),
        (4, "Tomicus_piniperda"),
        (5, "Pityogenes_chalcographus")
    ]
    
    for espece_id, nom_espece in especes:
        for num_ind in range(1, 9):  # 8 individus par espèce
            workflow_insecte(espece_id, nom_espece, num_ind)
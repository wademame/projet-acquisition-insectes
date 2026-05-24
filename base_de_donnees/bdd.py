#SQLite est une base de données qui tient dans un seul fichier .db. 
# Pas besoin de serveur. Python l'intègre nativement.
# fichier : base_de_donnees/bdd.py

import sqlite3   # intégré à Python, pas besoin d'installer !
import datetime

def creer_base_de_donnees():
    """Crée la structure de la base de données"""
    
    # Connexion (crée le fichier si il n'existe pas)
    conn = sqlite3.connect("dataset_insectes.db")
    curseur = conn.cursor()
    
    # Table des espèces
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS especes (
            id          INTEGER PRIMARY KEY,
            nom_latin   TEXT NOT NULL,
            nom_commun  TEXT,
            famille     TEXT,
            description TEXT
        )
    """)
    
    # Table des individus
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS individus (
            id          INTEGER PRIMARY KEY,
            espece_id   INTEGER REFERENCES especes(id),
            numero      INTEGER,
            date_capture TEXT,
            lieu        TEXT,
            notes       TEXT
        )
    """)
    
    # Table des photos
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS photos (
            id            INTEGER PRIMARY KEY,
            individu_id   INTEGER REFERENCES individus(id),
            appareil      TEXT,    -- 'canon', 'jeulin' ou 'iphone'
            type_photo    TEXT,    -- 'brute' ou 'stackee'
            chemin_fichier TEXT,
            resolution    TEXT,
            date_prise    TEXT,
            num_serie     INTEGER,
            num_dans_serie INTEGER,
            focus_position INTEGER
        )
    """)
    
    conn.commit()
    conn.close()
    print("Base de données créée : dataset_insectes.db")

def ajouter_photo(individu_id, appareil, type_photo, chemin, resolution, focus_pos=None):
    """Enregistre une photo dans la base"""
    conn = sqlite3.connect("dataset_insectes.db")
    curseur = conn.cursor()
    
    curseur.execute("""
        INSERT INTO photos 
        (individu_id, appareil, type_photo, chemin_fichier, resolution, date_prise, focus_position)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (individu_id, appareil, type_photo, chemin, resolution,
          datetime.datetime.now().isoformat(), focus_pos))
    
    conn.commit()
    conn.close()
    print(f"Photo enregistrée en BDD : {chemin}")

# Créer la base au premier lancement
creer_base_de_donnees()


#Les métadonnées EXIF sont des informations cachées dans le fichier image (date,
#  appareil, paramètres...). ExifTool permet de les lire et modifier.
# Installer ExifTool (logiciel externe) + la bibliothèque Python
#pip install pyexiftool

import exiftool

def lire_metadata(chemin_image):
    """Lit toutes les métadonnées d'une image"""
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(chemin_image)[0]
        
        print("Appareil :", metadata.get("EXIF:Model", "inconnu"))
        print("Date :", metadata.get("EXIF:DateTimeOriginal", "inconnue"))
        print("ISO :", metadata.get("EXIF:ISO", "inconnu"))
        print("Focale :", metadata.get("EXIF:FocalLength", "inconnue"))
        return metadata

def ajouter_metadata_insecte(chemin_image, espece, individu_id):
    """Ajoute des métadonnées personnalisées à l'image"""
    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            chemin_image,
            tags={
                "XMP:Subject": espece,
                "XMP:Description": f"Individu {individu_id}",
                "XMP:Source": "Stage dataset insectes"
            }
        )
    print(f"Métadonnées ajoutées à {chemin_image}")
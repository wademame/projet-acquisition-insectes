# text.py
# Tous les textes de l'interface en français et en anglais.

TEXTES = {
    "FR": {
        "titre":                    "Système d'acquisition d'images d'insectes",
        "guide_btn":                "Guide d'utilisation",
        "langue_btn":               "English",
        "params_titre":             "Paramètres de la photo",
        "params_note":              "* À remplir avant de déclencher une photo.",
        "espece":                   "Espèce :",
        "individu":                 "N° individu :",
        "grossissement":            "Grossissement :",
        "angle":                    "Angle :",
        "connexion_titre":          "Connexion des appareils",
        "actualiser":               "Actualiser la détection",
        "canon_lbl":                "Appareil photo Canon",
        "jeulin_lbl":               "Caméra Jeulin e-Mago",
        "android_lbl":              "Smartphone Android",
        "declencher_titre":         "Déclenchement",
        "declencher_note":          "Cliquez sur l'appareil souhaité pour prendre une photo.",
        "btn_canon":                "Canon EOS R7",
        "btn_jeulin":               "Jeulin e-Mago",
        "btn_android":              "Android",
        "champs_manquants":         "Veuillez remplir les champs : ",
        "journal_titre":            "Journal d'événements",
        "effacer":                  "Effacer le journal",
        "photo_titre":              "Photo prise",
        "cliquer_agrandir":         "(cliquez sur la photo pour agrandir)",
        "supprimer":                "Supprimer cette photo",
        "session_titre":            "Photos de cette session :",
        "session_note":             "Ctrl+clic pour sélectionner plusieurs photos, puis lancer le stacking.",
        "btn_stack":                "Lancer le focus stacking",
        "stack_sel_insuffisante":   "Sélectionnez au moins 2 photos pour le stacking.",
        "stack_chemins_introuvables":"Chemins des photos introuvables.",
        "stack_debut":              "Focus stacking de",
        "stack_images":             "images...",
        "stack_en_cours":           "Stacking en cours, veuillez patienter...",
        "stack_ok":                 "Image stackée sauvegardée",
        "stack_ok_court":           "Stacking terminé.",
        "stack_echec":              "Échec du focus stacking.",
        "confirmer_titre":          "Confirmer la suppression",
        "confirmer_msg":            "Supprimer cette photo ?",
        "demarrage":                "Système démarré. Vérification des appareils en cours...",
        "verification":             "Vérification des appareils...",
        "detectes":                 "Appareils détectés",
        "aucun":                    "Aucun appareil détecté.",
        "canon_ok_linux":           "Canon EOS R7 : connecté via gphoto2.",
        "canon_ok_windows":         "Canon EOS R7 : connecté via digiCamControl.",
        "canon_non":                "Canon : non détecté. Vérifiez le câble USB et que l'appareil est allumé.",
        "canon_err":                "Canon erreur",
        "canon_statut_linux":       "Connecté (gphoto2)",
        "canon_statut_windows":     "Connecté (digiCamControl)",
        "jeulin_ok":                "Jeulin détectée à l'index",
        "jeulin_non":               "Jeulin : non détectée (vérifiez le branchement).",
        "jeulin_err":               "Jeulin erreur",
        "android_ok":               "Android connecté",
        "android_adb_ver":          "Android : version ADB incorrecte. Voir Guide section Android.",
        "android_non":              "Android : non détecté. Activez le débogage USB dans les options développeur.",
        "android_adb_abs":          "Android : ADB non installé. Commande : sudo apt install adb",
        "declench_log":             "Déclenchement",
        "photo_ok":                 "Photo sauvegardée",
        "photo_echec":              "Échec capture",
        "canon_decon":              "Canon non connecté. Actualisez la détection ou vérifiez le câble.",
        "jeulin_decon":             "Jeulin non détectée. Branchez la caméra et actualisez.",
        "android_decon":            "Android non connecté. Vérifiez le câble et le débogage USB.",
        "suppr_log":                "Photo supprimée",
        "suppr_err":                "Impossible de supprimer",
        "guide_titre":              "Guide d'utilisation",
        "fermer":                   "Fermer",
        "non_detecte":              "Non détecté",
        "non_branche":              "Non branché",
        "connecte_android":         "Connecté",
        "adb_ver_pb":               "Problème version ADB",
        "adb_absent":               "ADB non installé",
        "verif_en_cours":           "Vérification...",
        "err_canon":                "Erreur connexion",
    },
    "EN": {
        "titre":                    "Insect image acquisition system",
        "guide_btn":                "User guide",
        "langue_btn":               "Français",
        "params_titre":             "Photo parameters",
        "params_note":              "* Must be filled in before triggering a photo.",
        "espece":                   "Species :",
        "individu":                 "Individual No. :",
        "grossissement":            "Magnification :",
        "angle":                    "Angle :",
        "connexion_titre":          "Device connection",
        "actualiser":               "Refresh detection",
        "canon_lbl":                "Canon camera",
        "jeulin_lbl":               "Jeulin e-Mago camera",
        "android_lbl":              "Android smartphone",
        "declencher_titre":         "Trigger",
        "declencher_note":          "Click on the desired device to take a photo.",
        "btn_canon":                "Canon EOS R7",
        "btn_jeulin":               "Jeulin e-Mago",
        "btn_android":              "Android",
        "champs_manquants":         "Please fill in the fields: ",
        "journal_titre":            "Event log",
        "effacer":                  "Clear log",
        "photo_titre":              "Last photo",
        "cliquer_agrandir":         "(click on the photo to enlarge)",
        "supprimer":                "Delete this photo",
        "session_titre":            "Photos this session :",
        "session_note":             "Ctrl+click to select multiple photos, then launch stacking.",
        "btn_stack":                "Launch focus stacking",
        "stack_sel_insuffisante":   "Select at least 2 photos for stacking.",
        "stack_chemins_introuvables":"Photo paths not found.",
        "stack_debut":              "Focus stacking of",
        "stack_images":             "images...",
        "stack_en_cours":           "Stacking in progress, please wait...",
        "stack_ok":                 "Stacked image saved",
        "stack_ok_court":           "Stacking complete.",
        "stack_echec":              "Focus stacking failed.",
        "confirmer_titre":          "Confirm deletion",
        "confirmer_msg":            "Delete this photo?",
        "demarrage":                "System started. Checking devices...",
        "verification":             "Checking devices...",
        "detectes":                 "Detected devices",
        "aucun":                    "No device detected.",
        "canon_ok_linux":           "Canon EOS R7: connected via gphoto2.",
        "canon_ok_windows":         "Canon EOS R7: connected via digiCamControl.",
        "canon_non":                "Canon: not detected. Check USB cable and that the camera is on.",
        "canon_err":                "Canon error",
        "canon_statut_linux":       "Connected (gphoto2)",
        "canon_statut_windows":     "Connected (digiCamControl)",
        "jeulin_ok":                "Jeulin detected at index",
        "jeulin_non":               "Jeulin: not detected (check USB connection).",
        "jeulin_err":               "Jeulin error",
        "android_ok":               "Android connected",
        "android_adb_ver":          "Android: wrong ADB version. See Guide - Android section.",
        "android_non":              "Android: not detected. Enable USB debugging in developer options.",
        "android_adb_abs":          "Android: ADB not installed. Command: sudo apt install adb",
        "declench_log":             "Triggering",
        "photo_ok":                 "Photo saved",
        "photo_echec":              "Capture failed",
        "canon_decon":              "Canon not connected. Refresh detection or check cable.",
        "jeulin_decon":             "Jeulin not detected. Plug in the camera and refresh.",
        "android_decon":            "Android not connected. Check cable and USB debugging.",
        "suppr_log":                "Photo deleted",
        "suppr_err":                "Cannot delete",
        "guide_titre":              "User guide",
        "fermer":                   "Close",
        "non_detecte":              "Not detected",
        "non_branche":              "Not connected",
        "connecte_android":         "Connected",
        "adb_ver_pb":               "ADB version mismatch",
        "adb_absent":               "ADB not installed",
        "verif_en_cours":           "Checking...",
        "err_canon":                "Connection error",
    }
}

GUIDE_FR = """GUIDE D'UTILISATION
Système d'acquisition d'images d'insectes
==========================================

Sommaire
--------
1. Présentation du système
2. Comment ouvrir le logiciel
3. Étapes à suivre avant chaque prise de vue
4. Focus stacking : obtenir une image entièrement nette
5. Où sont stockées les photos
6. Que faire si un appareil n'est pas détecté
7. Questions fréquentes


1. PRÉSENTATION DU SYSTÈME
---------------------------
Ce logiciel permet de piloter trois appareils de capture d'images depuis un
seul écran : un appareil photo Canon EOS R7, une caméra de microscopie Jeulin
e-Mago et un smartphone Android. Chaque appareil peut être déclenché
indépendamment. Les photos sont enregistrées automatiquement dans des dossiers
organisés selon l'espèce, le numéro de l'individu et l'appareil utilisé.


2. COMMENT OUVRIR LE LOGICIEL
------------------------------
Sur Linux :
Double-cliquez sur le fichier "lancer_acquisition.sh" situé sur le bureau,
ou ouvrez un terminal et tapez :
    cd ~/projet_insectes
    python3 interface.py

Sur Windows :
Double-cliquez sur le fichier "lancer.bat" situé dans le dossier du projet,
ou créez un raccourci sur le bureau pointant vers ce fichier.


3. ÉTAPES À SUIVRE AVANT CHAQUE PRISE DE VUE
---------------------------------------------
a) Branchez les appareils via leurs câbles USB respectifs.

b) Au démarrage, le logiciel vérifie automatiquement quels appareils sont
   détectés. Le statut de chaque appareil s'affiche dans la section
   "Connexion des appareils" :
     - Texte vert  : l'appareil est prêt à être utilisé.
     - Texte rouge : l'appareil n'est pas détecté (voir section 6).
     - Texte orange : l'appareil est en attente ou pose un problème mineur.

c) Remplissez les quatre champs dans la section "Paramètres de la photo" :
     - Espèce        : nom de l'espèce étudiée, par exemple "scolyte1"
     - N° individu   : numéro du spécimen, par exemple 3 pour le troisième
     - Grossissement : le zoom utilisé sur la loupe binoculaire (10x, 20x...)
     - Angle         : la position de l'insecte sous la loupe.
                       Dorsal = vue de dessus, Side = vue de côté,
                       Front = vue de face, Back = vue de derrière.

   Ces quatre champs sont obligatoires. Si l'un d'eux est vide, le logiciel
   vous le signalera et n'effectuera pas la capture.

d) Cliquez sur le bouton de l'appareil souhaité pour prendre une photo.
   Le bouton se grise le temps de la capture, puis redevient actif.

e) La photo apparaît dans l'aperçu à droite. Cliquez dessus pour l'agrandir.
   Si elle ne convient pas, cliquez "Supprimer cette photo" et recommencez.


4. FOCUS STACKING : OBTENIR UNE IMAGE ENTIÈREMENT NETTE
---------------------------------------------------------
À fort grossissement, il est impossible d'avoir tout l'insecte net sur une
seule photo. Le focus stacking résout ce problème en combinant plusieurs
photos prises à des mises au point différentes.

Étapes :
a) Prenez entre 5 et 10 photos du même insecte sans le bouger, en changeant
   la mise au point manuellement entre chaque prise.
b) Dans la liste "Photos de cette session", sélectionnez toutes ces photos
   avec Ctrl+clic.
c) Cliquez sur le bouton vert "Lancer le focus stacking".
d) Le logiciel produit automatiquement une image entièrement nette, sauvegardée
   dans le même dossier que les photos brutes, avec le suffixe _STACKEE.tiff.


5. OÙ SONT STOCKÉES LES PHOTOS
--------------------------------
    images/
    +-- Canon/
    |   +-- scolyte1/
    |       +-- individu_01/
    |           +-- scolyte1_ind01_camCanon_mag10x_angleDorsal_photo01.jpg
    |           +-- scolyte1_ind01_camCanon_mag10x_angleDorsal_STACKEE.tiff
    +-- Jeulin/
    +-- Android/

Les photos ne sont jamais écrasées. Si vous prenez plusieurs photos avec les
mêmes paramètres, le numéro en fin de nom de fichier s'incrémente
automatiquement (photo01, photo02, photo03...).


6. QUE FAIRE SI UN APPAREIL N'EST PAS DÉTECTÉ
-----------------------------------------------
Canon EOS R7 :
  - Vérifiez que l'appareil est allumé et le câble USB branché.
  - Cliquez "Actualiser la détection".
  - Sur Linux, le logiciel libère automatiquement le pilote système (gvfs)
    qui peut bloquer la connexion. Aucune action manuelle requise.
  - Sur Windows, assurez-vous que digiCamControl est installé.

Caméra Jeulin e-Mago :
  - Branchez la caméra en USB, puis cliquez "Actualiser la détection".

Smartphone Android :
  - Vérifiez que le câble USB est branché.
  - Sur le téléphone : Paramètres > À propos du téléphone > tapez 7 fois sur
    "Numéro de build" pour activer les options développeur.
    Puis Paramètres > Options développeur > Débogage USB > Activez.
  - Acceptez la fenêtre d'autorisation qui apparaît sur le téléphone.
  - Si le journal affiche "version ADB incorrecte", contactez la stagiaire.


7. QUESTIONS FRÉQUENTES
------------------------
Q : Le bouton ne répond plus après avoir cliqué.
R : Le bouton est désactivé le temps de la capture. Il se réactive
    automatiquement. Attendez quelques secondes.

Q : J'ai pris deux photos avec les mêmes paramètres. L'ancienne est-elle perdue ?
R : Non. Le logiciel numérote les photos automatiquement. La nouvelle photo
    portera le numéro suivant (photo02, photo03...).

Q : Combien de photos faut-il pour le focus stacking ?
R : Entre 5 et 10 photos donnent de bons résultats.
"""

GUIDE_EN = """USER GUIDE
Insect Image Acquisition System
================================

Table of contents
-----------------
1. System overview
2. How to open the software
3. Steps before each capture
4. Focus stacking: getting a fully sharp image
5. Where photos are stored
6. Troubleshooting device detection
7. Frequently asked questions


1. SYSTEM OVERVIEW
-------------------
This software allows you to control three image capture devices from a single
screen: a Canon EOS R7 camera, a Jeulin e-Mago microscopy camera, and an
Android smartphone. Each device can be triggered independently. Photos are
automatically saved in folders organised by species, individual number, and
device used.


2. HOW TO OPEN THE SOFTWARE
-----------------------------
On Linux:
Double-click "lancer_acquisition.sh" on the desktop, or open a terminal and type:
    cd ~/projet_insectes
    python3 interface.py

On Windows:
Double-click "lancer.bat" in the project folder, or create a shortcut on the
desktop pointing to this file.


3. STEPS BEFORE EACH CAPTURE
------------------------------
a) Connect the devices via their USB cables.

b) At startup, the software automatically checks which devices are detected:
     - Green text  : the device is ready.
     - Red text    : not detected (see section 6).
     - Orange text : pending or minor issue.

c) Fill in the four fields in "Photo parameters":
     - Species      : name of the species, e.g. "scolyte1"
     - Individual No.: specimen number
     - Magnification : zoom level on the loupe (10x, 20x...)
     - Angle         : Dorsal = top view, Side = side view,
                       Front = front view, Back = rear view.

d) Click the button for the device you want to use.

e) The photo appears in the preview. Click to enlarge. If unsatisfactory,
   click "Delete this photo" and try again.


4. FOCUS STACKING: GETTING A FULLY SHARP IMAGE
------------------------------------------------
At high magnification, it is impossible to have the whole insect sharp in a
single photo. Focus stacking solves this by combining several photos taken
at different focus positions.

Steps:
a) Take 5 to 10 photos of the same insect without moving it, adjusting the
   focus manually between each shot.
b) In the "Photos this session" list, select all these photos using Ctrl+click.
c) Click the green "Launch focus stacking" button.
d) The software produces a fully sharp image saved in the same folder as the
   source photos, with the suffix _STACKEE.tiff.


5. WHERE PHOTOS ARE STORED
----------------------------
    images/
    +-- Canon/
    |   +-- scolyte1/
    |       +-- individu_01/
    |           +-- scolyte1_ind01_camCanon_mag10x_angleDorsal_photo01.jpg
    |           +-- scolyte1_ind01_camCanon_mag10x_angleDorsal_STACKEE.tiff
    +-- Jeulin/
    +-- Android/

Photos are never overwritten. If you take several photos with the same
parameters, the number at the end of the filename increments automatically.


6. TROUBLESHOOTING DEVICE DETECTION
-------------------------------------
Canon EOS R7:
  - Check it is switched on and the USB cable is connected.
  - Click "Refresh detection".
  - On Linux, the software automatically releases the system driver (gvfs)
    that can block the connection. No manual action required.
  - On Windows, make sure digiCamControl is installed.

Jeulin e-Mago camera:
  - Plug in via USB, then click "Refresh detection".

Android smartphone:
  - Check the USB cable is connected.
  - On the phone: Settings > About phone > tap "Build number" 7 times to
    enable developer options. Then Settings > Developer options >
    USB debugging > enable it. Accept the authorisation pop-up.
  - If the log shows "ADB version mismatch", contact the intern.


7. FREQUENTLY ASKED QUESTIONS
-------------------------------
Q: The button stopped responding after I clicked it.
A: The button is disabled during the capture and reactivates automatically.

Q: I took two photos with the same parameters. Was the old one overwritten?
A: No. Photos are numbered automatically (photo02, photo03...).

Q: How many photos are needed for focus stacking?
A: Between 5 and 10 photos give good results.
"""
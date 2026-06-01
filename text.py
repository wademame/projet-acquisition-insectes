# text.py
# Tous les textes de l'interface en français et en anglais.
# Importé par interface.py via : from text import TEXTES, GUIDE_FR, GUIDE_EN
#
# Note sur le guide : la zone d'affichage dans l'interface est un widget
# tk.Text avec la police Courier. Les balises de mise en forme (gras, taille)
# sont appliquées via des tags Tkinter dans interface.py, pas ici.
# Les marqueurs ##TITRE## et ##SOUS## sont interprétés par interface.py
# pour appliquer la mise en forme correspondante.

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
        "stack_chemins_introuvables": "Chemins des photos introuvables.",
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
        "stack_chemins_introuvables": "Photo paths not found.",
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

# ==============================================================================
# GUIDES D'UTILISATION
#
# Format spécial pour la mise en forme dans interface.py :
#   §TITRE§    → texte centré en gras, grande police, couleur bordeaux
#   §H1§       → titre de section en gras
#   §CODE§     → ligne en police Courier sur fond sombre
#   §LIEN§url§label§ → lien cliquable
#   §ANCRE§id§ → ancre pour le sommaire
#   §SAUT§     → saut de ligne visible
# Les paragraphes normaux sont en texte justifié.
# ==============================================================================

GUIDE_SECTIONS_FR = [
    "1. Comment ouvrir le logiciel",
    "2. Étapes avant chaque prise de vue",
    "3. Focus stacking",
    "4. Où sont stockées les photos",
    "5. Dépannage",
    "6. Questions fréquentes",
]

GUIDE_FR = """\
§TITRE§GUIDE D'UTILISATION§
§SOUS§Système d'acquisition d'images d'insectes§

Ce logiciel permet de piloter trois appareils de capture d'images depuis un seul écran : un appareil photo Canon EOS R7, une caméra de microscopie Jeulin e-Mago et un smartphone Android. Chaque appareil peut être déclenché indépendamment. Les photos sont enregistrées automatiquement dans des dossiers organisés selon l'espèce, le numéro de l'individu et l'appareil utilisé.

§H1§SOMMAIRE§
§LIEN§sec1§1. Comment ouvrir le logiciel§
§LIEN§sec2§2. Étapes à suivre avant chaque prise de vue§
§LIEN§sec3§3. Focus stacking : obtenir une image entièrement nette§
§LIEN§sec4§4. Où sont stockées les photos§
§LIEN§sec5§5. Que faire si un appareil n'est pas détecté§

§ANCRE§sec1§
§H1§1. Comment ouvrir le logiciel ?§

§SOUS§Sur Linux§
Double-cliquez sur le fichier lancer_acquisition.sh situé sur le bureau, puis choisissez « Exécuter dans un terminal ».

Ou bien, ouvrez un terminal et tapez :
§CODE§cd ~/projet-acquisition-insectes
§CODE§source venv/bin/activate
§CODE§python3 interface.py

§SOUS§Sur Windows§
Double-cliquez sur le fichier lancer.bat situé dans le dossier du projet. Une fenêtre noire s'ouvre brièvement, puis l'interface apparaît.

Pour créer un raccourci sur le bureau : clic droit sur le bureau → Nouveau → Raccourci → entrez le chemin vers lancer.bat → nommez-le « Acquisition insectes » → Terminer.

§ANCRE§sec2§
§H1§2. Étapes à suivre avant chaque prise de vue§

a)  Branchez les appareils via leurs câbles USB respectifs. Lorsqu'une fenêtre apparaît sur le téléphone, choisissez « Transfert de fichiers » et non « Charge seulement ».

b)  Au démarrage, le logiciel vérifie automatiquement quels appareils sont détectés. Le statut de chaque appareil s'affiche dans la section « Connexion des appareils » :

      Texte vert    →  l'appareil est prêt à être utilisé.
      Texte rouge   →  non détecté (voir section 5).
      Texte orange  →  en attente ou problème mineur.

c)  Remplissez les quatre champs dans la section « Paramètres de la photo » :

      Espèce         :  nom de l'espèce étudiée (ex : scolyte1)
      N° individu    :  numéro du spécimen (ex : 3 pour le troisième)
      Grossissement  :  zoom de la loupe binoculaire (10x, 20x, 40x...)
      Angle          :  Dorsal = vue de dessus
                        Side   = vue de côté
                        Front  = vue de face
                        Back   = vue de derrière

    Ces quatre champs sont obligatoires. Si l'un est vide, le logiciel vous le signalera et n'effectuera pas la capture.

d)  Cliquez sur le bouton de l'appareil souhaité pour prendre une photo. Le bouton se grise le temps de la capture, puis redevient actif automatiquement.

e)  La photo apparaît dans l'aperçu à droite de l'écran. Cliquez dessus pour l'agrandir et vérifier sa qualité. Si elle ne convient pas, cliquez « Supprimer cette photo » et recommencez.

§ANCRE§sec3§
§H1§3. Focus stacking : obtenir une image entièrement nette§

À fort grossissement sous une loupe binoculaire, la profondeur de champ est très faible. Cela signifie qu'une seule photo ne peut pas avoir tout l'insecte net en même temps : si la tête est nette, le thorax sera flou. Le focus stacking résout ce problème en combinant plusieurs photos prises à des mises au point différentes pour produire une image où tout est net.

§SOUS§Étapes§
a)  Prenez entre 5 et 10 photos du même insecte sans le bouger, en changeant la mise au point d'un cran entre chaque prise (tournez la molette de focus de la loupe).

b)  Dans la liste « Photos de cette session » à droite de l'écran, maintenez la touche Ctrl enfoncée et cliquez sur chacune des photos de la série pour les sélectionner.

c)  Cliquez sur le bouton vert « Lancer le focus stacking ».

d)  Le logiciel traite les images en arrière-plan. L'image résultat s'affiche dans l'aperçu et est sauvegardée automatiquement dans le même dossier que les photos brutes, avec le suffixe _STACKEE.tiff.

§ANCRE§sec4§
§H1§4. Où sont stockées les photos ?§

Toutes les photos sont enregistrées automatiquement dans le dossier projet-acquisition-insectes, puis dans images. Ce dossier est organisé en trois niveaux : d'abord par appareil (Canon, Jeulin ou Android), ensuite par espèce, puis par numéro d'individu. Par exemple, la première photo d'un scolyte (individu 1) prise avec le Canon à 10x en vue dorsale se trouvera dans :
§CODE§images/Canon/scolyte1/individu_01/§
§CODE§  scolyte1_ind01_camCanon_mag10x_angleDorsal_photo01.jpg§

Les photos ne sont jamais écrasées. Si vous prenez plusieurs photos avec les mêmes paramètres, le numéro en fin de nom s'incrémente automatiquement (photo01, photo02, photo03...). Pour accéder à vos photos, ouvrez le gestionnaire de fichiers et naviguez jusqu'au dossier images.

§ANCRE§sec5§
§H1§5. Que faire si un appareil n'est pas détecté ?§

§SOUS§Canon EOS R7§
Si le statut est rouge, vérifiez que l'appareil est allumé (interrupteur sur ON) et que le câble USB est bien branché des deux côtés, puis cliquez sur « Actualiser la détection ».

Sur Linux, le logiciel libère automatiquement le pilote système (gvfs) qui peut bloquer la connexion. Aucune action manuelle n'est requise. Sur Windows, assurez-vous que le logiciel digiCamControl est bien installé (téléchargement : digicamcontrol.com).

§SOUS§Caméra Jeulin e-Mago§
Branchez la caméra en USB si ce n'est pas fait, puis cliquez sur « Actualiser la détection ».

§SOUS§Smartphone Android§
Vérifiez que le câble USB est branché. Lorsqu'une fenêtre apparaît sur le téléphone, choisissez « Transfert de fichiers » (et non « Charge seulement »).

Pour activer le débogage USB : allez dans Paramètres → À propos du téléphone, puis tapez 7 fois sur « Numéro de build » pour débloquer les options développeur. Ensuite : Paramètres → Options développeur → Débogage USB → Activez. Acceptez la fenêtre d'autorisation qui apparaît sur le téléphone.

Si vous ne trouvez pas ces options selon votre modèle d'Android, consultez la documentation officielle :
§LIEN§https://developer.android.com/studio/debug/dev-options?hl=fr§developer.android.com — Activer les options développeur§

"""

GUIDE_SECTIONS_EN = [
    "1. How to open the software",
    "2. Steps before each capture",
    "3. Focus stacking",
    "4. Where photos are stored",
    "5. Troubleshooting",
    "6. Frequently asked questions",
]

GUIDE_EN = """\
§TITRE§USER GUIDE§
§SOUS§Insect Image Acquisition System§

This software allows you to control three image capture devices from a single screen: a Canon EOS R7 camera, a Jeulin e-Mago microscopy camera, and an Android smartphone. Each device can be triggered independently. Photos are automatically saved in folders organised by species, individual number, and device used.

§H1§TABLE OF CONTENTS§
§LIEN§sec1§1. How to open the software§
§LIEN§sec2§2. Steps before each capture§
§LIEN§sec3§3. Focus stacking: getting a fully sharp image§
§LIEN§sec4§4. Where photos are stored§
§LIEN§sec5§5. Troubleshooting§

§ANCRE§sec1§
§H1§1. How to open the software§

§SOUS§On Linux§
Double-click the file lancer_acquisition.sh on the desktop, then choose "Run in terminal".

Or open a terminal and type:
§CODE§cd ~/projet-acquisition-insectes
§CODE§source venv/bin/activate
§CODE§python3 interface.py

§SOUS§On Windows§
Double-click the file lancer.bat in the project folder. A black window briefly appears, then the interface opens.

To create a desktop shortcut: right-click desktop → New → Shortcut → enter the path to lancer.bat → name it "Insect Acquisition" → Finish.

§ANCRE§sec2§
§H1§2. Steps before each capture§

a)  Connect the devices via their USB cables. If a window appears on the phone, choose "File transfer" (not "Charge only").

b)  At startup, the software automatically checks which devices are detected. The status appears in "Device connection":

      Green text   →  device ready.
      Red text     →  not detected (see section 5).
      Orange text  →  pending or minor issue.

c)  Fill in the four fields in "Photo parameters":

      Species       :  species name (e.g. scolyte1)
      Individual No.:  specimen number (e.g. 3)
      Magnification :  loupe zoom (10x, 20x, 40x...)
      Angle         :  Dorsal = top view
                       Side   = side view
                       Front  = front view
                       Back   = rear view

    All four fields are mandatory. If any is empty, the software will warn you and will not perform the capture.

d)  Click the button for the device you want to use. The button greys out during the capture, then reactivates automatically.

e)  The photo appears in the preview on the right. Click to enlarge and check quality. If unsatisfactory, click "Delete this photo" and try again.

§ANCRE§sec3§
§H1§3. Focus stacking: getting a fully sharp image§

At high magnification under a binocular loupe, the depth of field is very shallow. A single photo cannot have the whole insect sharp: if the head is sharp, the thorax will be blurred. Focus stacking solves this by combining several photos taken at different focus positions to produce a fully sharp image.

§SOUS§Steps§
a)  Take 5 to 10 photos of the same insect without moving it, adjusting the focus one notch between each shot.

b)  In the "Photos this session" list on the right, hold Ctrl and click each photo in the series.

c)  Click the green "Launch focus stacking" button.

d)  The software processes the images in the background. The result appears in the preview and is saved in the same folder as the source photos, with the suffix _STACKEE.tiff.

§ANCRE§sec4§
§H1§4. Where photos are stored§

All photos are saved in the projet-acquisition-insectes folder, then in images. This folder is organised in three levels: first by device (Canon, Jeulin or Android), then by species, then by individual number. For example:
§CODE§images/Canon/scolyte1/individu_01/§
§CODE§  scolyte1_ind01_camCanon_mag10x_angleDorsal_photo01.jpg§

Photos are never overwritten. If you take several photos with the same parameters, the number increments automatically. To access your photos, open the file manager and navigate to the images folder.

§ANCRE§sec5§
§H1§5. Troubleshooting§

§SOUS§Canon EOS R7§
Check the camera is switched on (power switch to ON) and the USB cable is firmly connected, then click "Refresh detection".

On Linux, the software automatically releases the gvfs driver that can block the connection. No manual action required. On Windows, make sure digiCamControl is installed (download: digicamcontrol.com).

§SOUS§Jeulin e-Mago camera§
Plug in the camera via USB, then click "Refresh detection".

§SOUS§Android smartphone§
Check the USB cable is connected. When a window appears on the phone, choose "File transfer" (not "Charge only").

To enable USB debugging: go to Settings → About phone, tap "Build number" 7 times to unlock developer options. Then: Settings → Developer options → USB debugging → Enable. Accept the authorisation pop-up on the phone.

If you cannot find these options for your model:
§LIEN§https://developer.android.com/studio/debug/dev-options§developer.android.com — Enable developer options§




"""
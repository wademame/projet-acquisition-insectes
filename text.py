# text.py
# Tous les textes de l'interface en français et en anglais.
# Importé par interface.py via : from text import TEXTES, GUIDE_FR, GUIDE_EN
#
# Marqueurs de mise en forme interprétés par interface.py :
#   §TITRE§texte§    → centré, gras, grande police, couleur bordeaux
#   §SOUS§texte§     → sous-titre en gras
#   §H1§texte§       → titre de section en gras
#   §CODE§texte      → ligne en police Courier sur fond sombre
#   §LIEN§url§label§ → lien cliquable (externe = navigateur, interne = ancre)
#   §ANCRE§id§       → position cible pour le sommaire cliquable

TEXTES = {
    "FR": {
        "titre":                    "Système d'acquisition d'images d'insectes",
        "guide_btn":                "Guide d'utilisation",
        "langue_btn":               "English",
        "params_titre":             "Paramètres de la photo",
        "params_note":              "* À remplir avant de déclencher une photo.",
        "espece":                   "Espèce :",
        "individu":                 "N° individu :",
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

GUIDE_SECTIONS_FR = [
    "1. Comment ouvrir le logiciel",
    "2. Préparer les appareils",
    "3. Étapes avant chaque prise de vue",
    "4. Focus stacking",
    "5. Où sont stockées les photos",
    "6. Dépannage",
]

GUIDE_FR = """\
§TITRE§GUIDE D'UTILISATION§
§SOUS§Système d'acquisition d'images d'insectes§

Ce logiciel permet de piloter trois appareils de capture d'images depuis un seul écran : un appareil photo Canon EOS R7, une caméra de microscopie Jeulin e-Mago et un smartphone Android. Chaque appareil peut être déclenché indépendamment. Les photos sont enregistrées automatiquement dans des dossiers organisés selon l'espèce, le numéro de l'individu et l'appareil utilisé.


§H1§SOMMAIRE§
§LIEN§sec1§1. Comment ouvrir le logiciel§
§LIEN§sec2§2. Préparer les appareils avant la première utilisation§
§LIEN§sec3§3. Étapes à suivre avant chaque prise de vue§
§LIEN§sec4§4. Focus stacking : obtenir une image entièrement nette§
§LIEN§sec5§5. Où sont stockées les photos§
§LIEN§sec6§6. Que faire si un appareil n'est pas détecté§

§ANCRE§sec1§
§H1§1. Comment ouvrir le logiciel ?§

§SOUS§Sur Linux§
Double-cliquez sur l'icône "Acquisition insectes" sur le bureau.

§SOUS§Sur Windows§
Double-cliquez sur le fichier lancer.bat dans le dossier du projet. Une fenêtre noire s'ouvre brièvement, puis l'interface apparaît.

Pour créer un raccourci sur le bureau : faites un clic droit sur lancer.bat, puis choisissez « Envoyer vers » > « Bureau (créer un raccourci) ».

§ANCRE§sec2§
§H1§2. Préparer les appareils avant la première utilisation§

Cette section explique comment configurer chaque appareil pour qu'il soit reconnu par le logiciel. Ces étapes ne sont à faire qu'une seule fois.

§SOUS§Canon EOS R7§
L'objectif doit être en mode MF (mise au point manuelle) si le téléphone est branché en même temps et que vous utilisez linux. L'interrupteur AF/MF se trouve sur l'objectif. Si l'objectif est en AF (autofocus), le logiciel ne pourra pas déclencher la prise de vue lorsque le téléphone est branché en même temps.

L'appareil doit être en mode photo (et non vidéo) et ne pas être en veille au moment de la capture.

§SOUS§Smartphone Android : activer le débogage USB§
Le débogage USB est une option développeur qui permet à l'ordinateur de contrôler le téléphone. Elle doit être activée une seule fois.

a)  Allez dans Paramètres : À propos du téléphone.
b)  Tapez 7 fois sur « Numéro de build » jusqu'au message « Vous êtes développeur ! ».
c)  Retournez dans Paramètres : Options développeur.
d)  Activez « Débogage USB ».
e)  Branchez le téléphone en USB. Une fenêtre apparaît sur l'écran : choisissez « Transfert de fichiers » et acceptez l'autorisation de débogage.

Si vous ne trouvez pas ces options sur votre modèle d'Android, vous trouverez comment faire selon votre version du modèle d'android en cliquant sur ce lien :
§LIEN§https://developer.android.com/studio/debug/dev-options?hl=fr§developer.android.com : Activer les options développeur§

§ANCRE§sec3§
§H1§3. Étapes à suivre avant chaque prise de vue§

a)  Branchez les appareils via leurs câbles USB respectifs.

b)  Au démarrage, le logiciel vérifie automatiquement quels appareils sont détectés. Le statut de chaque appareil s'affiche dans la section « Connexion des appareils » :

      Texte vert    :  l'appareil est prêt à être utilisé.
      Texte rouge   :  non détecté (voir section 6).
      Texte orange  :  en attente ou problème mineur.

c)  Remplissez les champs dans la section « Paramètres de la photo » :

      Espèce         :  nom de l'espèce étudiée (ex : scolyte1)
      N° individu    :  numéro du spécimen (ex : 3 pour le troisième)
      Angle          :  Dorsal = vue de dessus
                        Side   = vue de côté
                        Front  = vue de face
                        Back   = vue de derrière

    Ces trois champs sont obligatoires. Si l'un est vide, le logiciel vous le signalera et n'effectuera pas la capture.

d)  Cliquez sur le bouton de l'appareil souhaité. Le bouton se grise pendant la capture, puis redevient actif automatiquement.

e)  La photo apparaît dans l'aperçu à droite. Cliquez dessus pour l'agrandir. Si elle ne convient pas, supprimez-la et recommencez.

§SOUS§Régler la luminosité et le gamma de la caméra Jeulin§
Sous la prévisualisation Jeulin, deux curseurs permettent d'ajuster l'image en direct avant de déclencher :
 
      Luminosité  :  de -64 à 64. La valeur 0 correspond au réglage d'usine.
                     Augmenter éclaircit toute l'image uniformément.
                     Diminuer assombrit l'ensemble.
 
      Gamma       :  de 72 à 500. La valeur recommandée est 200.
                     Le gamma agit différemment de la luminosité : il éclaircit
                     surtout les zones sombres (détails cachés dans les parties
                     foncées de l'insecte) sans "cramer" les zones déjà claires.
                     C'est le réglage le plus utile pour voir les détails fins
                     d'un insecte sous la loupe.
 
Le bouton ↺ défaut remet chaque curseur à sa valeur d'origine.
Ces réglages sont appliqués en temps réel directement au pilote de la caméra.
Ils n'affectent que la prévisualisation et les photos prises avec la Jeulin,
pas les autres appareils.
 
Si vous débranchez puis rebranchez un appareil, cliquez sur « Actualiser la détection », la prévisualisation redémarrera automatiquement pour la jeulin sinon, fermer le logiciel et le rouvrir.

§ANCRE§sec4§
§H1§4. Focus stacking : obtenir une image entièrement nette§

À fort grossissement sous une loupe binoculaire, une seule photo ne peut pas avoir tout l'insecte net : si la tête est nette, le thorax sera flou. Le focus stacking combine plusieurs photos prises à des mises au point différentes pour produire une image entièrement nette.

§SOUS§Étapes§
a)  Prenez plusieurs photos (2 à 10 ou plus) du même insecte sans le bouger, en changeant la mise au point d'un cran entre chaque prise.

b)  Dans la liste « Photos de cette session », maintenez Ctrl enfoncée et cliquez sur chaque photo de la série.

c)  Cliquez sur le bouton vert « Lancer le focus stacking ».

d)  L'image résultat s'affiche dans l'aperçu et est sauvegardée dans le même dossier avec le suffixe _STACKEE.tiff.

§ANCRE§sec5§
§H1§5. Où sont stockées les photos ?§

Les photos sont enregistrées dans le dossier projet-acquisition-insectes > images, organisé en trois niveaux : appareil (Canon, Jeulin ou Android), puis espèce, puis numéro d'individu.

Par exemple, la première photo d'un scolyte (individu 1) prise avec le Canon en vue dorsale se trouve dans : images > Canon > scolyte1 > individu_01 et est nommée "scolyte1_ind01_camCanon_angleDorsal_photo01.jpg"

Pour accéder à vos photos : ouvrez le gestionnaire de fichiers et naviguez vers : Dossier personnel ou home > projet-acquisition-insectes > images

Les photos ne sont jamais écrasées. Le numéro en fin de nom s'incrémente automatiquement (photo01, photo02, photo03...).

§ANCRE§sec6§
§H1§6. Que faire si un appareil n'est pas détecté ?§

§SOUS§Canon EOS R7§
Vérifiez que l'appareil est allumé (interrupteur sur ON), qu'il est en mode photo (pas vidéo), que l'objectif est en mode MF, et que le câble USB est bien branché. Cliquez ensuite sur « Actualiser la détection ».

Sur Linux, si le Canon et le téléphone sont branchés simultanément, un conflit USB peut empêcher la capture. Si l'objectif est en mode AF et que le téléphone est branché, le logiciel affichera un message vous demandant de passer en MF.

§SOUS§Caméra Jeulin e-Mago§
Branchez la caméra en USB, puis cliquez sur « Actualiser la détection ». Si la caméra apparaît en orange ou disparaît lors d'une actualisation, attendez quelques secondes et réactualisez : c'est un comportement normal lié au driver USB.

§SOUS§Smartphone Android§
Vérifiez que le câble USB est branché et que vous avez choisi « Transfert de fichiers » sur le téléphone (et non « Charge seulement »). Si le débogage USB n'est pas encore activé, suivez les étapes de la section 2.
"""

GUIDE_SECTIONS_EN = [
    "1. How to open the software",
    "2. Preparing the devices",
    "3. Steps before each capture",
    "4. Focus stacking",
    "5. Where photos are stored",
    "6. Troubleshooting",
]

GUIDE_EN = """\
§TITRE§USER GUIDE§
§SOUS§Insect Image Acquisition System§

This software allows you to control three image capture devices from a single screen: a Canon EOS R7 camera, a Jeulin e-Mago microscopy camera, and an Android smartphone. Each device can be triggered independently. Photos are automatically saved in folders organised by species, individual number, and device used.

§H1§TABLE OF CONTENTS§
§LIEN§sec1§1. How to open the software§
§LIEN§sec2§2. Preparing the devices for first use§
§LIEN§sec3§3. Steps before each capture§
§LIEN§sec4§4. Focus stacking: getting a fully sharp image§
§LIEN§sec5§5. Where photos are stored§
§LIEN§sec6§6. Troubleshooting§

§ANCRE§sec1§
§H1§1. How to open the software§

§SOUS§On Linux§
Double-click the "Acquisition insectes" icon on the desktop.

§SOUS§On Windows§
Double-click lancer.bat in the project folder. A black window briefly appears, then the interface opens.

To create a desktop shortcut: right-click lancer.bat > "Send to" > "Desktop (create shortcut)".

§ANCRE§sec2§
§H1§2. Preparing the devices for first use§

§SOUS§Canon EOS R7§
The lens must be in MF (manual focus) mode. The AF/MF switch is on the lens. If the lens is in AF (autofocus) mode, the software maybe will not be able to trigger the capture while using the phone at the same time.

The camera must be in photo mode (not video) and must not be in sleep mode at the time of capture.

§SOUS§Android smartphone : enabling USB debugging§
USB debugging allows the computer to control the phone. It only needs to be enabled once.

a)  Go to Settings > About phone.
b)  Tap "Build number" 7 times until you see "You are now a developer!".
c)  Go back to Settings > Developer options.
d)  Enable "USB debugging".
e)  Plug in the phone via USB. A pop-up will appear: choose "File transfer" and accept the debugging authorisation.

If you cannot find these options on your Android model, you will find instructions for your Android version by clicking on this link:
§LIEN§https://developer.android.com/studio/debug/dev-options§developer.android.com : Enable developer options§

§ANCRE§sec3§
§H1§3. Steps before each capture§

a)  Connect the devices via their USB cables.

b)  At startup, the software automatically checks which devices are detected. The status appears in "Device connection":

      Green text   :  device ready.
      Red text     :  not detected (see section 6).
      Orange text  :  pending or minor issue.

c)  Fill in the fields in "Photo parameters":

      Species       :  species name (e.g. scolyte1)
      Individual No.:  specimen number (e.g. 3)
      Angle         :  Dorsal = top view
                       Side   = side view
                       Front  = front view
                       Back   = rear view

    All three fields are mandatory. If any is empty, the software will warn you and will not perform the capture.

d)  Click the button for the device you want to use. The button greys out during the capture, then reactivates automatically.

e)  The photo appears in the preview on the right. Click to enlarge. If unsatisfactory, delete it and try again.

§SOUS§Adjusting brightness and gamma on the Jeulin camera§
Below the Jeulin preview, two sliders let you adjust the image in real time before triggering:
 
      Brightness  :  from -64 to 64. The value 0 is the factory default.
                     Increasing brightens the whole image uniformly.
                     Decreasing darkens the whole image.
 
      Gamma       :  from 72 to 500. The recommended value is 200.
                     Gamma works differently from brightness: it brightens
                     mainly the dark areas (hidden details in the darker parts
                     of the insect) without overexposing the already bright areas.
                     This is the most useful setting for revealing fine details
                     of an insect under the loupe.
 
The ↺ default button resets each slider to its factory value.
These settings are applied in real time directly to the camera driver.
They only affect the Jeulin preview and photos, not the other devices.


If you unplug and then plug back in a device, click on "Refresh detection", the preview will automatically restart for the game, otherwise, close the software and reopen it.

§ANCRE§sec4§
§H1§4. Focus stacking: getting a fully sharp image§

At high magnification under a binocular loupe, a single photo cannot have the whole insect sharp. Focus stacking combines several photos taken at different focus positions to produce a fully sharp image.

§SOUS§Steps§
a)  Take several photos (2 to 10 or more) of the same insect without moving it, adjusting the focus one notch between each shot.

b)  In the "Photos this session" list, hold Ctrl and click each photo in the series.

c)  Click the green "Launch focus stacking" button.

d)  The result appears in the preview and is saved in the same folder with the suffix _STACKEE.tiff.

§ANCRE§sec5§
§H1§5. Where photos are stored§

Photos are saved in projet-acquisition-insectes > images, organised in three levels: device (Canon, Jeulin or Android), then species, then individual number.

For example, the first photo of a scolyte (individual 1) taken with the Canon in dorsal view: images > Canon > scolyte1 > individu_01 and is named "scolyte1_ind01_camCanon_angleDorsal_photo01.jpg" 

To access your photos: open the file manager and navigate to:
Home folder > projet-acquisition-insectes > images

Photos are never overwritten. The number at the end of the filename increments automatically.

§ANCRE§sec6§
§H1§6. Troubleshooting§

§SOUS§Canon EOS R7§
Check that the camera is switched on (power switch to ON), that it is in photo mode (not video), that the lens is in MF mode, and that the USB cable is firmly connected. Then click "Refresh detection".

On Linux, if the Canon and the phone are connected at the same time, a USB conflict may prevent the capture. If the lens is in AF mode and the phone is connected, the software will display a message asking you to switch to MF.

§SOUS§Jeulin e-Mago camera§
Plug in the camera via USB, then click "Refresh detection". If the camera appears as orange or disappears during a refresh, wait a few seconds and try again : this is normal behaviour related to the USB driver.

§SOUS§Android smartphone§
Check the USB cable is connected and that you selected "File transfer" on the phone (not "Charge only"). If USB debugging is not yet enabled, follow the steps in section 2.
"""
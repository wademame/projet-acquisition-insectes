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

GUIDE_FR = """GUIDE D'UTILISATION <-- (en gars et au centre)

Ce logiciel permet de piloter trois appareils de capture d'images depuis un
seul écran : un appareil photo Canon EOS R7, une caméra de microscopie Jeulin
e-Mago et un smartphone Android. <br> 
Chaque appareil peut être déclenché indépendamment. Les photos sont enregistrées automatiquement dans des dossiers
organisés selon l'espèce, le numéro de l'individu et l'appareil utilisé.

-->  (Justifier le texte dans les paragraphes)

... ici faire un somaire cliquable

1) COMMENT OUVRIR LE LOGICIEL ? <-- (en gras)

Sur Linux :
Double-cliquez sur le fichier "lancer_acquisition.sh" situé sur le bureau,
ou ouvrez un terminal et tapez :

    cd ~/projet-acquisition-insectes

    source venv/bin/activate

    python3 interface.py

    (fromater les commande en une police couleur etc style code)

Sur Windows :
Double-cliquez sur le fichier "lancer.bat" situé dans le dossier du projet,
ou créez un raccourci sur le bureau pointant vers ce fichier : (clique droit sur le bureau > creer un raccourci > mettre ...)


2) ÉTAPES À SUIVRE AVANT CHAQUE PRISE DE VUE <-- (en gras)

a) Branchez les appareils via leurs câbles USB respectifs.

b) Au démarrage, le logiciel vérifie automatiquement quels appareils sont
   détectés. 
   Le statut de chaque appareil s'affiche dans la section "Connexion des appareils" :

     - Texte vert  : l'appareil est prêt à être utilisé.
     - Texte rouge : l'appareil n'est pas détecté (voir section 5).
     - Texte orange : l'appareil est en attente ou pose un problème mineur.

c) Remplissez les quatre champs dans la section "Paramètres de la photo" :

     - Espèce        : nom de l'espèce étudiée
     - N° individu   : numéro du spécimen (par exemple 3 pour le troisième)
     - Grossissement : le zoom utilisé sur la loupe (10x, 20x...)
     - Angle         : la position de l'insecte sous la loupe.
                       Dorsal = vue de dessus, Side = vue de côté,
                       Front = vue de face, Back = vue de derrière.

   Ces quatre champs sont obligatoires. Si l'un d'eux est vide, le logiciel
   vous le signalera et n'effectuera pas la capture.

d) Cliquez sur le bouton de l'appareil souhaité pour prendre une photo.
   Le bouton se grise le temps de la capture, puis redevient actif.

e) La photo apparaît dans l'aperçu à droite. Cliquez dessus pour l'agrandir.
   Si elle ne convient pas, cliquez "Supprimer cette photo" et recommencez.


3) FOCUS STACKING : OBTENIR UNE IMAGE ENTIÈREMENT NETTE

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


4) OÙ SONT STOCKÉES LES PHOTOS

Les photos se trouvent dans le dossier projet-acquisition-insectes puis dans images.
Vous verrez un dossier pour chaque appareil et dans chaque appareil .... (expliquer avec des mots)

Les photos ne sont jamais écrasées. Si vous prenez plusieurs photos avec les
mêmes paramètres, le numéro en fin de nom de fichier s'incrémente
automatiquement (photo01, photo02, photo03...).


5) QUE FAIRE SI UN APPAREIL N'EST PAS DÉTECTÉ

Canon EOS R7 :

  - Vérifiez que l'appareil est allumé et le câble USB branché.
  - Cliquez "Actualiser la détection".
  - Sur Linux, le logiciel libère automatiquement le pilote système (gvfs)
    qui peut bloquer la connexion. Aucune action manuelle requise.
  - Sur Windows, assurez-vous que digiCamControl est installé.
  (mettre en gras Linux et Windows)

Caméra Jeulin e-Mago :

  - Branchez la caméra en USB, puis cliquez "Actualiser la détection".

Smartphone Android :

  - Vérifiez que le câble USB est branché et cliquer sur transfert fichiers/android auto etc (ne pas prendre charge seulement en tot cas).

  - Sur le téléphone : Paramètres > À propos du téléphone > tapez 7 fois sur
    "Numéro de build" pour activer les options développeur.
    Puis Paramètres > Options développeur > Débogage USB > Activez.
  - Acceptez la fenêtre d'autorisation qui apparaît sur le téléphone.
  -   si vous n'arrivez pas à trouver ses options, vérifiez votre version d'android dans à propos etc dans les parametre du systeme et 
  suivez cette documentation https://developer.android.com/studio/debug/dev-options?hl=fr ou https://www.embarcadero.com/starthere/xe5/mobdevsetup/android/fr/enabling_usb_debugging_on_an_android_device.html 
  qui vous guidera selon votre version et modèle d'android.

"""

GUIDE_EN = """

reécrire en anglais
"""
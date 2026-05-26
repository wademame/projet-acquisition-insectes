# text.py
# Tous les textes de l'interface en francais et en anglais.
# Importe par interface.py.

TEXTES = {
    "FR": {
        "titre":                    "Systeme d'acquisition d'images d'insectes",
        "guide_btn":                "Guide d'utilisation",
        "langue_btn":               "English",
        "params_titre":             "Parametres de la photo",
        "params_note":              "* A remplir avant de declencher une photo.",
        "espece":                   "Espece :",
        "individu":                 "N° individu :",
        "grossissement":            "Grossissement :",
        "angle":                    "Angle :",
        "connexion_titre":          "Connexion des appareils",
        "actualiser":               "Actualiser la detection",
        "canon_lbl":                "Appareil photo Canon",
        "jeulin_lbl":               "Camera Jeulin e-Mago",
        "android_lbl":              "Smartphone Android",
        "declencher_titre":         "Declenchement",
        "declencher_note":          "Cliquez sur l'appareil souhaite pour prendre une photo.",
        "btn_canon":                "Canon EOS R7",
        "btn_jeulin":               "Jeulin e-Mago",
        "btn_android":              "Android",
        "champs_manquants":         "Veuillez remplir les champs : ",
        "journal_titre":            "Journal d'evenements",
        "effacer":                  "Effacer le journal",
        "photo_titre":              "Photo prise",
        "cliquer_agrandir":         "(cliquez sur la photo pour agrandir)",
        "supprimer":                "Supprimer cette photo",
        "session_titre":            "Photos de cette session :",
        "session_note":             "Ctrl+clic pour selectionner plusieurs photos, puis lancer le stacking.",
        "btn_stack":                "Lancer le focus stacking",
        "stack_sel_insuffisante":   "Selectionnez au moins 2 photos pour le stacking.",
        "stack_chemins_introuvables":"Chemins des photos introuvables.",
        "stack_debut":              "Focus stacking de",
        "stack_images":             "images...",
        "stack_en_cours":           "Stacking en cours, veuillez patienter...",
        "stack_ok":                 "Image stackee sauvegardee",
        "stack_ok_court":           "Stacking termine.",
        "stack_echec":              "Echec du focus stacking.",
        "confirmer_titre":          "Confirmer la suppression",
        "confirmer_msg":            "Supprimer cette photo ?",
        "demarrage":                "Systeme demarre. Verification des appareils en cours...",
        "verification":             "Verification des appareils...",
        "detectes":                 "Appareils detectes",
        "aucun":                    "Aucun appareil detecte.",
        "canon_ok":                 "Canon EOS R7 : connecte via EDSDK.",
        "canon_non":                "Canon : non detecte. Verifiez le cable USB et que l'appareil est allume.",
        "canon_err":                "Canon erreur",
        "jeulin_ok":                "Jeulin detectee a l'index",
        "jeulin_non":               "Jeulin : non detectee (verifiez le branchement).",
        "jeulin_err":               "Jeulin erreur",
        "android_ok":               "Android connecte",
        "android_adb_ver":          "Android : version ADB incorrecte. Voir Guide section Android.",
        "android_non":              "Android : non detecte. Activez le debogage USB dans les options developpeur.",
        "android_adb_abs":          "Android : ADB non installe. Commande : sudo apt install adb",
        "declench_log":             "Declenchement",
        "photo_ok":                 "Photo sauvegardee",
        "photo_echec":              "Echec capture",
        "canon_decon":              "Canon non connecte. Actualisez la detection ou verifiez le cable.",
        "jeulin_decon":             "Jeulin non detectee. Branchez la camera et actualisez.",
        "android_decon":            "Android non connecte. Verifiez le cable et le debogage USB.",
        "suppr_log":                "Photo supprimee",
        "suppr_err":                "Impossible de supprimer",
        "guide_titre":              "Guide d'utilisation",
        "fermer":                   "Fermer",
        "connecte_edsdk":           "Connecte (EDSDK USB)",
        "non_detecte":              "Non detecte",
        "err_edsdk":                "Erreur EDSDK",
        "non_branche":              "Non branche",
        "connecte_android":         "Connecte",
        "adb_ver_pb":               "Probleme version ADB",
        "adb_absent":               "ADB non installe",
        "verif_en_cours":           "Verification...",
    },
    "EN": {
        "titre":                    "Insect image acquisition system",
        "guide_btn":                "User guide",
        "langue_btn":               "Francais",
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
        "canon_ok":                 "Canon EOS R7: connected via EDSDK.",
        "canon_non":                "Canon: not detected. Check USB cable and that the camera is on.",
        "canon_err":                "Canon error",
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
        "connecte_edsdk":           "Connected (EDSDK USB)",
        "non_detecte":              "Not detected",
        "err_edsdk":                "EDSDK error",
        "non_branche":              "Not connected",
        "connecte_android":         "Connected",
        "adb_ver_pb":               "ADB version mismatch",
        "adb_absent":               "ADB not installed",
        "verif_en_cours":           "Checking...",
    }
}

GUIDE_FR = """GUIDE D'UTILISATION
Systeme d'acquisition d'images d'insectes
==========================================

Sommaire
--------
1. Presentation du systeme
2. Comment ouvrir le logiciel
3. Etapes a suivre avant chaque prise de vue
4. Focus stacking : obtenir une image entierement nette
5. Ou sont stockees les photos
6. Que faire si un appareil n'est pas detecte
7. Questions frequentes


1. PRESENTATION DU SYSTEME
---------------------------
Ce logiciel permet de piloter trois appareils de capture d'images depuis un
seul ecran : un appareil photo Canon EOS R7, une camera de microscopie Jeulin
e-Mago et un smartphone Android. Chaque appareil peut etre declenche
independamment. Les photos sont enregistrees automatiquement dans des dossiers
organises selon l'espece, le numero de l'individu et l'appareil utilise.


2. COMMENT OUVRIR LE LOGICIEL
------------------------------
Double-cliquez sur le fichier "Lancer l'acquisition.desktop" situe sur le
bureau de l'ordinateur. Le logiciel s'ouvre automatiquement.

Si le raccourci n'est pas sur le bureau, demandez a la stagiaire de le
recreer, ou ouvrez un terminal et tapez :
    cd ~/projet_insectes
    python3 interface.py


3. ETAPES A SUIVRE AVANT CHAQUE PRISE DE VUE
---------------------------------------------
a) Branchez les appareils que vous souhaitez utiliser via leurs cables USB.

b) Au demarrage, le logiciel verifie automatiquement quels appareils sont
   detectes. Le statut de chaque appareil s'affiche dans la section
   "Connexion des appareils" :
     - Texte vert  : l'appareil est pret a etre utilise.
     - Texte rouge : l'appareil n'est pas detecte (voir section 6).
     - Texte orange : l'appareil est en attente ou pose un probleme mineur.

c) Remplissez les quatre champs dans la section "Parametres de la photo" :
     - Espece        : nom de l'espece etudiee, par exemple "scolyte1"
     - N° individu   : numero du specimen, par exemple 3 pour le troisieme
     - Grossissement : le zoom utilise sur la loupe binoculaire (10x, 20x...)
     - Angle         : la position de l'insecte sous la loupe.
                       Dorsal = vue de dessus, Side = vue de cote,
                       Front = vue de face, Back = vue de derriere.

   Ces quatre champs sont obligatoires. Si l'un d'eux est vide, le logiciel
   vous le signalera et n'effectuera pas la capture.

d) Cliquez sur le bouton de l'appareil souhaite pour prendre une photo.
   Le bouton se grise le temps de la capture, puis redevient actif.

e) La photo apparait dans l'apercu a droite. Cliquez dessus pour l'agrandir.
   Si elle ne convient pas, cliquez "Supprimer cette photo" et recommencez.


4. FOCUS STACKING : OBTENIR UNE IMAGE ENTIEREMENT NETTE
---------------------------------------------------------
A fort grossissement, il est impossible d'avoir tout l'insecte net sur une
seule photo. Le focus stacking resout ce probleme en combinant plusieurs
photos prises a des mises au point differentes.

Etapes :
a) Prenez entre 5 et 10 photos du meme insecte sans le bouger, en changeant
   la mise au point manuellement entre chaque prise (tournez la molette de
   focus de la loupe d'un cran entre chaque photo).
b) Dans la liste "Photos de cette session", selectionnez toutes ces photos
   avec Ctrl+clic (maintenez la touche Ctrl et cliquez sur chaque photo).
c) Cliquez sur le bouton vert "Lancer le focus stacking".
d) Le logiciel produit automatiquement une image entierement nette, sauvegardee
   dans le meme dossier que les photos brutes, avec le suffixe _STACKEE.tiff.
   Cette image apparait dans l'apercu quand le traitement est termine.


5. OU SONT STOCKEES LES PHOTOS
--------------------------------
    images/
    +-- Canon/
    |   +-- scolyte1/
    |       +-- individu_01/
    |           +-- scolyte1_ind01_camCanon_mag10x_angleDorsal_photo01.jpg
    |           +-- scolyte1_ind01_camCanon_mag10x_angleDorsal_STACKEE.tiff
    +-- Jeulin/
    +-- Android/

Les photos ne sont jamais ecrasees. Si vous prenez plusieurs photos avec les
memes parametres, le numero en fin de nom s'incremente automatiquement.


6. QUE FAIRE SI UN APPAREIL N'EST PAS DETECTE
-----------------------------------------------
Canon EOS R7 :
  - Verifiez que l'appareil est allume et le cable USB branche.
  - Cliquez "Actualiser la detection". Le logiciel libere automatiquement
    le pilote systeme qui peut bloquer la connexion.

Camera Jeulin e-Mago :
  - Branchez la camera en USB, puis cliquez "Actualiser la detection".

Smartphone Android :
  - Verifiez que le cable USB est branche.
  - Sur le telephone : Parametres > A propos du telephone > tapez 7 fois sur
    "Numero de build" pour activer les options developpeur.
    Puis Parametres > Options developpeur > Debogage USB > Activez.
  - Acceptez la fenetre d'autorisation qui apparait sur le telephone.
  - Si le journal affiche "version ADB incorrecte", contactez la stagiaire.


7. QUESTIONS FREQUENTES
------------------------
Q : Le bouton ne repond plus apres avoir clique.
R : Le bouton est desactive le temps de la capture. Il se reactive
    automatiquement. Attendez quelques secondes.

Q : J'ai pris deux photos avec les memes parametres. L'ancienne est-elle perdue ?
R : Non. Le logiciel numerote les photos automatiquement. La nouvelle photo
    portera le numero suivant (photo02, photo03...).

Q : Combien de photos faut-il pour le focus stacking ?
R : Entre 5 et 10 photos donnent de bons resultats. Moins de 3 photos
    produira un resultat mediocre.
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
Double-click the "Launch acquisition.desktop" file on the computer desktop.

If the shortcut is not on the desktop, ask the intern to recreate it, or open
a terminal and type:
    cd ~/projet_insectes
    python3 interface.py


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
   focus manually between each shot (turn the loupe focus wheel one notch).
b) In the "Photos this session" list, select all these photos using Ctrl+click.
c) Click the green "Launch focus stacking" button.
d) The software produces a fully sharp image saved in the same folder as the
   source photos, with the suffix _STACKEE.tiff. It appears in the preview
   when processing is complete.


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
  - Click "Refresh detection". The software automatically releases the
    system driver that can block the connection.

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
A: Between 5 and 10 photos give good results. Fewer than 3 will give
   a poor result.
"""
# ── Textes bilingues ────────────────────────────────────────────────────────── j'ai mis dans ~/projet_insectes/text.py

TEXTES = {
    "FR": {
        "titre":            "Systeme d'acquisition d'images d'insectes",
        "guide_btn":        "Guide d'utilisation",
        "langue_btn":       "English",
        "params_titre":     "Parametres de la photo",
        "params_note":      "* A remplir avant de declencher une photo.",
        "espece":           "Espece :",
        "individu":         "N° individu :",
        "grossissement":    "Grossissement :",
        "angle":            "Angle :",
        "connexion_titre":  "Connexion des appareils",
        "actualiser":       "Actualiser la detection",
        "canon_lbl":        "Appareil photo Canon",
        "jeulin_lbl":       "Camera Jeulin e-Mago",
        "android_lbl":      "Smartphone Android",
        "declencher_titre": "Declenchement",
        "declencher_note":  "Cliquez sur l'appareil souhaite pour prendre une photo.",
        "btn_canon":        "Canon EOS R7",
        "btn_jeulin":       "Jeulin e-Mago",
        "btn_android":      "Android",
        "champs_manquants": "Veuillez remplir les champs : ",
        "journal_titre":    "Journal d'evenements",
        "effacer":          "Effacer le journal",
        "photo_titre":      "Photo prise",
        "cliquer_agrandir": "(cliquez sur la photo pour agrandir)",
        "supprimer":        "Supprimer cette photo",
        "session_titre":    "Photos de cette session :",
        "confirmer_titre":  "Confirmer la suppression",
        "confirmer_msg":    "Supprimer cette photo ?",
        "demarrage":        "Systeme demarre. Verification des appareils en cours...",
        "verification":     "Verification des appareils...",
        "detectes":         "Appareils detectes",
        "aucun":            "Aucun appareil detecte.",
        "canon_ok":         "Canon EOS R7 : connecte via EDSDK.",
        "canon_non":        "Canon : non detecte. Verifiez le cable USB et que l'appareil est allume.",
        "canon_err":        "Canon erreur",
        "jeulin_ok":        "Jeulin detectee a l'index",
        "jeulin_non":       "Jeulin : non detectee (verifiez le branchement).",
        "jeulin_err":       "Jeulin erreur",
        "android_ok":       "Android connecte",
        "android_adb_ver":  "Android : version ADB incorrecte. Voir Guide section Android.",
        "android_non":      "Android : non detecte. Activez le debogage USB dans les options developpeur.",
        "android_adb_abs":  "Android : ADB non installe. Commande : sudo apt install adb",
        "declench_log":     "Declenchement",
        "photo_ok":         "Photo sauvegardee",
        "photo_echec":      "Echec capture",
        "canon_decon":      "Canon non connecte. Actualisez la detection ou verifiez le cable.",
        "jeulin_decon":     "Jeulin non detectee. Branchez la camera et actualisez.",
        "android_decon":    "Android non connecte. Verifiez le cable et le debogage USB.",
        "suppr_log":        "Photo supprimee",
        "suppr_err":        "Impossible de supprimer",
        "guide_titre":      "Guide d'utilisation",
        "fermer":           "Fermer",
        "connecte_edsdk":   "Connecte (EDSDK USB)",
        "non_detecte":      "Non detecte",
        "err_edsdk":        "Erreur EDSDK",
        "non_branche":      "Non branche",
        "connecte_android": "Connecte",
        "adb_ver_pb":       "Probleme version ADB",
        "adb_absent":       "ADB non installe",
        "verif_en_cours":   "Verification...",
    },
    "EN": {
        "titre":            "Insect image acquisition system",
        "guide_btn":        "User guide",
        "langue_btn":       "Francais",
        "params_titre":     "Photo parameters",
        "params_note":      "* Must be filled in before triggering a photo.",
        "espece":           "Species :",
        "individu":         "Individual No. :",
        "grossissement":    "Magnification :",
        "angle":            "Angle :",
        "connexion_titre":  "Device connection",
        "actualiser":       "Refresh detection",
        "canon_lbl":        "Canon camera",
        "jeulin_lbl":       "Jeulin e-Mago camera",
        "android_lbl":      "Android smartphone",
        "declencher_titre": "Trigger",
        "declencher_note":  "Click on the desired device to take a photo.",
        "btn_canon":        "Canon EOS R7",
        "btn_jeulin":       "Jeulin e-Mago",
        "btn_android":      "Android",
        "champs_manquants": "Please fill in the fields: ",
        "journal_titre":    "Event log",
        "effacer":          "Clear log",
        "photo_titre":      "Last photo",
        "cliquer_agrandir": "(click on the photo to enlarge)",
        "supprimer":        "Delete this photo",
        "session_titre":    "Photos this session :",
        "confirmer_titre":  "Confirm deletion",
        "confirmer_msg":    "Delete this photo?",
        "demarrage":        "System started. Checking devices...",
        "verification":     "Checking devices...",
        "detectes":         "Detected devices",
        "aucun":            "No device detected.",
        "canon_ok":         "Canon EOS R7: connected via EDSDK.",
        "canon_non":        "Canon: not detected. Check USB cable and that the camera is on.",
        "canon_err":        "Canon error",
        "jeulin_ok":        "Jeulin detected at index",
        "jeulin_non":       "Jeulin: not detected (check USB connection).",
        "jeulin_err":       "Jeulin error",
        "android_ok":       "Android connected",
        "android_adb_ver":  "Android: wrong ADB version. See Guide - Android section.",
        "android_non":      "Android: not detected. Enable USB debugging in developer options.",
        "android_adb_abs":  "Android: ADB not installed. Command: sudo apt install adb",
        "declench_log":     "Triggering",
        "photo_ok":         "Photo saved",
        "photo_echec":      "Capture failed",
        "canon_decon":      "Canon not connected. Refresh detection or check cable.",
        "jeulin_decon":     "Jeulin not detected. Plug in the camera and refresh.",
        "android_decon":    "Android not connected. Check cable and USB debugging.",
        "suppr_log":        "Photo deleted",
        "suppr_err":        "Cannot delete",
        "guide_titre":      "User guide",
        "fermer":           "Close",
        "connecte_edsdk":   "Connected (EDSDK USB)",
        "non_detecte":      "Not detected",
        "err_edsdk":        "EDSDK error",
        "non_branche":      "Not connected",
        "connecte_android": "Connected",
        "adb_ver_pb":       "ADB version mismatch",
        "adb_absent":       "ADB not installed",
        "verif_en_cours":   "Checking...",
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
4. Ou sont stockees les photos
5. Que faire si un appareil n'est pas detecte
6. Questions frequentes


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
a) Branchez les appareils que vous souhaitez utiliser via leurs cables USB
   respectifs. Le Canon et l'Android se branchent avec un cable USB-C ou
   USB-A selon le modele. La Jeulin se branche avec son cable USB fourni.

b) Au demarrage, le logiciel verifie automatiquement quels appareils sont
   detectes. Le statut de chaque appareil s'affiche dans la section
   "Connexion des appareils" :
     - Texte vert  : l'appareil est pret a etre utilise.
     - Texte rouge : l'appareil n'est pas detecte (voir section 5).
     - Texte orange : l'appareil est en attente ou pose un probleme mineur.

c) Remplissez les quatre champs dans la section "Parametres de la photo" :
     - Espece        : nom de l'espece etudiee, par exemple "scolyte1"
     - N° individu   : numero du specimen, par exemple 3 pour le troisieme
     - Grossissement : le zoom utilise sur la loupe binoculaire (10x, 20x...)
     - Angle         : la position de l'insecte sous la loupe. "Top" signifie
                       vu de dessus, "Side" de cote, "Front" de face,
                       "Back" de derriere.

   Ces quatre champs sont obligatoires. Si l'un d'eux est vide, le logiciel
   vous le signalera et n'effectuera pas la capture.

d) Cliquez sur le bouton correspondant a l'appareil avec lequel vous souhaitez
   prendre une photo. Les trois boutons sont visibles dans la section
   "Declenchement". Le bouton se grise le temps de la capture, puis redevient
   actif automatiquement.

e) La photo apparait dans la zone d'apercu a droite de l'ecran. Cliquez
   dessus pour l'agrandir et verifier sa qualite. Si elle ne convient pas,
   cliquez sur "Supprimer cette photo" et recommencez.


4. OU SONT STOCKEES LES PHOTOS
--------------------------------
Toutes les photos sont enregistrees automatiquement dans le dossier "images"
situe dans le dossier du projet, avec la structure suivante :

    images/
    +-- Canon/
    |   +-- scolyte1/
    |       +-- individu_01/
    |           +-- scolyte1_ind01_camCanon_mag10x_angleTop_photo01.jpg
    |           +-- scolyte1_ind01_camCanon_mag10x_angleTop_photo02.jpg
    +-- Jeulin/
    |   +-- scolyte1/
    |       +-- individu_01/
    +-- Android/
        +-- scolyte1/
            +-- individu_01/

Si vous prenez plusieurs photos avec les memes parametres, le numero en fin
de nom de fichier s'incremente automatiquement (photo01, photo02, photo03...).
Aucune photo ne sera jamais ecrasee.

Pour acceder aux photos, ouvrez le gestionnaire de fichiers, naviguez jusqu'au
dossier "projet_insectes", puis "images".


5. QUE FAIRE SI UN APPAREIL N'EST PAS DETECTE
-----------------------------------------------
Canon EOS R7 :
  - Verifiez que l'appareil photo est allume (interrupteur sur ON).
  - Verifiez que le cable USB est bien branche des deux cotes.
  - Cliquez sur "Actualiser la detection". Le logiciel libere automatiquement
    le pilote systeme qui peut parfois bloquer la connexion.
  - Si le probleme persiste, eteignez et rallumez le Canon, puis actualisez.

Camera Jeulin e-Mago :
  - Branchez la camera en USB si ce n'est pas fait.
  - Cliquez sur "Actualiser la detection".

Smartphone Android :
  - Verifiez que le cable USB est branche.
  - Sur le telephone : allez dans Parametres, puis "A propos du telephone",
    puis tapez sept fois sur "Numero de build" pour activer les options
    developpeur. Allez ensuite dans Parametres, "Options developpeur", puis
    activez "Debogage USB".
  - Une fenetre peut apparaitre sur le telephone pour autoriser la connexion :
    acceptez-la.
  - Si le journal affiche "version ADB incorrecte", contactez la stagiaire
    pour une mise a jour logicielle (operation a faire une seule fois).


6. QUESTIONS FREQUENTES
------------------------
Q : J'ai pris une photo avec les memes parametres qu'une precedente.
    Est-ce que l'ancienne a ete effacee ?
R : Non. Le logiciel numerote les photos automatiquement. La nouvelle photo
    portera le numero suivant (photo02, photo03, etc.).

Q : Le bouton ne repond plus apres avoir clique.
R : Le bouton est desactive le temps de la capture. Il se reactive seul des
    que la photo est sauvegardee. Attendez quelques secondes.

Q : La liste "Photos de cette session" n'affiche pas une photo que j'ai prise
    lors d'une session precedente.
R : La liste n'affiche que les photos prises depuis l'ouverture actuelle du
    logiciel. Les photos des sessions precedentes sont bien enregistrees dans
    le dossier "images" et peuvent etre consultees via le gestionnaire de
    fichiers.

Q : Peut-on utiliser plusieurs appareils en meme temps ?
R : Oui, mais en cliquant sur chaque bouton separement. Les captures ne sont
    pas simultanees dans cette version, mais les parametres de nommage sont
    identiques si vous ne changez pas les champs entre deux captures.
"""

GUIDE_EN = """USER GUIDE
Insect Image Acquisition System
================================

Table of contents
-----------------
1. System overview
2. How to open the software
3. Steps before each capture
4. Where photos are stored
5. Troubleshooting device detection
6. Frequently asked questions


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
The software opens automatically.

If the shortcut is not on the desktop, ask the intern to recreate it, or open
a terminal and type:
    cd ~/projet_insectes
    python3 interface.py


3. STEPS BEFORE EACH CAPTURE
------------------------------
a) Connect the devices you wish to use via their USB cables. The Canon and
   Android connect with a USB-C or USB-A cable depending on the model. The
   Jeulin connects with its supplied USB cable.

b) At startup, the software automatically checks which devices are detected.
   The status of each device is shown in the "Device connection" section:
     - Green text  : the device is ready to use.
     - Red text    : the device is not detected (see section 5).
     - Orange text : the device is pending or has a minor issue.

c) Fill in the four fields in the "Photo parameters" section:
     - Species      : name of the species studied, for example "scolyte1"
     - Individual No.: number of the specimen, e.g. 3 for the third one
     - Magnification : zoom level used on the binocular loupe (10x, 20x...)
     - Angle         : position of the insect under the loupe. "Top" means
                       seen from above, "Side" from the side, "Front" from
                       the front, "Back" from behind.

   All four fields are mandatory. If any is empty, the software will warn you
   and will not perform the capture.

d) Click the button corresponding to the device you want to use. The three
   buttons are visible in the "Trigger" section. The button greys out during
   the capture, then becomes active again automatically.

e) The photo appears in the preview area on the right of the screen. Click
   on it to enlarge it and check its quality. If it is not satisfactory, click
   "Delete this photo" and try again.


4. WHERE PHOTOS ARE STORED
----------------------------
All photos are automatically saved in the "images" folder located in the
project folder, with the following structure:

    images/
    +-- Canon/
    |   +-- scolyte1/
    |       +-- individu_01/
    |           +-- scolyte1_ind01_camCanon_mag10x_angleTop_photo01.jpg
    |           +-- scolyte1_ind01_camCanon_mag10x_angleTop_photo02.jpg
    +-- Jeulin/
    |   +-- scolyte1/
    |       +-- individu_01/
    +-- Android/
        +-- scolyte1/
            +-- individu_01/

If you take several photos with the same parameters, the number at the end of
the file name increments automatically (photo01, photo02, photo03...).
No photo will ever be overwritten.

To access your photos, open the file manager, navigate to the "projet_insectes"
folder, then "images".


5. TROUBLESHOOTING DEVICE DETECTION
-------------------------------------
Canon EOS R7:
  - Check that the camera is switched on (power switch to ON).
  - Check that the USB cable is firmly connected at both ends.
  - Click "Refresh detection". The software automatically releases the system
    driver that can sometimes block the connection.
  - If the problem persists, switch the Canon off and on again, then refresh.

Jeulin e-Mago camera:
  - Plug in the camera via USB if not already done.
  - Click "Refresh detection".

Android smartphone:
  - Check that the USB cable is connected.
  - On the phone: go to Settings, then "About phone", then tap "Build number"
    seven times to enable developer options. Then go to Settings, "Developer
    options", and enable "USB debugging".
  - A pop-up may appear on the phone asking to authorise the connection:
    accept it.
  - If the log displays "ADB version mismatch", contact the intern for a
    one-time software update.


6. FREQUENTLY ASKED QUESTIONS
-------------------------------
Q: I took a photo with the same parameters as a previous one. Was the old one
   overwritten?
A: No. The software numbers photos automatically. The new photo will be given
   the next number (photo02, photo03, etc.).

Q: The button stopped responding after I clicked it.
A: The button is disabled during the capture. It reactivates automatically
   once the photo is saved. Wait a few seconds.

Q: The "Photos this session" list does not show a photo I took in a previous
   session.
A: The list only shows photos taken since the software was last opened. Photos
   from previous sessions are saved in the "images" folder and can be viewed
   through the file manager.

Q: Can I use several devices at the same time?
A: Yes, but by clicking each button separately. Captures are not simultaneous
   in this version, but the naming parameters are identical if you do not
   change the fields between captures.
"""
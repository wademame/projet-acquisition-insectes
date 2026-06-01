# Système d'acquisition d'images d'insectes

Plateforme de prise de vue multi-caméras développée pour le laboratoire Chrono-Environnement de Montbéliard. Le but est de constituer un dataset d'images d'insectes de haute qualité pour entraîner un modèle d'IA capable de reconnaître automatiquement différentes espèces.

Trois appareils sont pilotés depuis une seule interface : un Canon EOS R7, une caméra de microscopie Jeulin e-Mago, et un smartphone Android. Les photos sont nommées et rangées automatiquement. Un focus stacking intégré permet de produire des images entièrement nettes depuis plusieurs prises à focales différentes.

> Stage BUT3 — Mame Diarra Wade — Chrono-Environnement, Montbéliard, 2026

---

## Interface

![Interface principale](docs/screenshots/interface_principale.png)
*Insérez ici une capture de l'interface avec les trois boutons de déclenchement*

![Focus stacking](docs/screenshots/focus_stacking.png)
*Insérez ici une capture du résultat d'un focus stacking*

---

## Ce que ça fait concrètement

- On branche les appareils en USB, l'interface détecte tout automatiquement
- On renseigne l'espèce, le numéro d'individu, le grossissement et l'angle
- On clique sur le bouton de l'appareil voulu, la photo s'affiche dans l'aperçu
- Pour le focus stacking : on prend 5 à 10 photos en changeant la mise au point, on les sélectionne dans la liste, et on clique sur le bouton vert
- Les fichiers sont rangés automatiquement dans `images/Canon/espece/individu_01/`

---

## Installation rapide

### Linux (Ubuntu 20.04 / Linux Mint)

```bash
git clone https://github.com/TON_COMPTE/projet-acquisition-insectes.git
cd projet-acquisition-insectes
sudo apt install python3 python3-tk python3-venv git gphoto2 enfuse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Pour le raccourci bureau :
```bash
cp lancer_acquisition.desktop ~/Bureau/
chmod +x ~/Bureau/lancer_acquisition.desktop
```

### Windows 10/11

```
1. Installer Python 3.11 depuis python.org (cocher "Add Python to PATH")
2. Copier le projet ou : git clone https://github.com/TON_COMPTE/projet-acquisition-insectes.git
3. Double-cliquer sur lancer.bat
```

Installer aussi [digiCamControl](https://digicamcontrol.com/download) pour le Canon.

---

## Nommage des fichiers

Les métadonnées sont encodées directement dans le nom :

```
scolyte1_ind01_camCanon_mag10x_angleDorsal_photo03.jpg
```

| Partie | Signification |
|---|---|
| `scolyte1` | espèce |
| `ind01` | numéro d'individu |
| `camCanon` | appareil utilisé |
| `mag10x` | grossissement (magnification) |
| `angleDorsal` | position de l'insecte |
| `photo03` | numéro dans la série |

Image stackée finale : `scolyte1_ind01_camCanon_mag10x_angleDorsal_STACKEE.tiff`

---

## Structure du projet

```
projet-acquisition-insectes/
├── interface.py          ← lancer avec : python3 interface.py
├── text.py               ← textes FR/EN de l'interface
├── lancer_acquisition.sh ou lancer_acquisition .desktop ← raccourci bureau Linux
├── lancer.bat            ← raccourci bureau Windows
├── requirements.txt
├── .gitignore
├── acquisition/
│   ├── canon.py          ← Canon (gphoto2 sur Linux, digiCamControl sur Windows)
│   ├── jeulin.py         ← Jeulin e-Mago (OpenCV)
│   ├── android.py        ← Android (ADB)
│   └── nommage.py        ← nommage et création automatique des dossiers
├── traitement/
│   └── stacking.py       ← focus stacking (enfuse + fallback Mertens OpenCV)
└── docs/
    ├── GUIDE_UTILISATION.pdf
    ├── GUIDE_INSTALLATION.pdf
    ├── DOCUMENTATION_TECHNIQUE.pdf
    └── WEBOGRAPHIE.pdf
```

---

## Dépendances Python

```
opencv-python    # capture Jeulin + algorithme de focus stacking (fallback)
pillow           # affichage des photos dans l'interface
```

Tout le reste (`tkinter`, `subprocess`, `threading`, `os`, `sys`, `time`, `datetime`) est inclus dans Python.

---

## Outils externes

| Outil | OS | Usage |
|---|---|---|
| gphoto2 | Linux | Contrôle Canon EOS R7 |
| digiCamControl | Windows | Contrôle Canon EOS R7 |
| ADB platform-tools | Linux · Windows | Contrôle Android |
| enfuse | Linux | Focus stacking (sudo apt install enfuse) |

---

## Documentation

- [Guide d'utilisation](docs/GUIDE_UTILISATION.pdf)
- [Guide d'installation](docs/GUIDE_INSTALLATION.pdf)
- [Documentation technique](docs/DOCUMENTATION_TECHNIQUE.pdf)
- [Webographie](docs/WEBOGRAPHIE.pdf)

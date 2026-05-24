# Systeme d'acquisition multi-capteurs d'images d'insectes

Projet de stage — Constitution d'un dataset d'images d'insectes pour l'IA

## Description

Systeme permettant d'acquerir, traiter et stocker des images d'insectes
a l'aide de 3 appareils differents, afin de constituer un dataset
pour l'entrainement d'un modele de reconnaissance d'especes.

## Appareils utilises

- Appareil photo Canon EOS R7 (controle via EDSDK USB)
- Camera Jeulin e-mago (controle via OpenCV / UVC)
- Smartphone Android (controle via ADB)

## Fonctionnalites

- Interface graphique Tkinter avec 3 boutons de declenchement independants
- Nommage automatique des photos avec metadonnees integrees
- Structure de dossiers automatique : images/Appareil/espece/individu_XX/
- Apercu de la derniere photo dans l'interface
- Journal d'evenements horodate

## Convention de nommage
espece_indXX_camAppareil_magXx_angleXxx_photoXX.jpg
Exemple : scolyte1_ind01_camCanon_mag10x_angleDorsal_photo01.jpg

## Installation

```bash
git clone https://github.com/ton-pseudo/projet-acquisition-insectes.git
cd projet-acquisition-insectes
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 interface.py
```

## Technologies

Python 3.8 | Tkinter | OpenCV | ADB | Canon EDSDK | Ubuntu 20.04

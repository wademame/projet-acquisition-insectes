# traitement/stacking.py
# Focus stacking : combine plusieurs photos prises à des mises au point
# différentes pour produire une seule image entièrement nette.
#
# ── Algorithmes utilisés ─────────────────────────────────────────────────────
#
# Méthode principale : enfuse (open source, gratuit, disponible sur Linux)
#   Fait partie du projet Hugin (https://hugin.sourceforge.io).
#   Utilise une fusion multi-bandes par pondération de l'exposition,
#   du contraste et de la saturation — même principe que Mertens mais
#   plus robuste sur les textures fines. Produit des résultats proches
#   des logiciels professionnels.
#   Installation : sudo apt install enfuse
#
# Fallback (si enfuse non installé) : AlignMTB + Mertens (OpenCV)
#
#   AlignMTB (Median Threshold Bitmap) :
#     Algorithme d'alignement qui compare les niveaux de luminosité de
#     chaque image et calcule un décalage en x et y pour les superposer.
#     Corrige les micro-décalages dus à la manipulation manuelle du focus.
#     Complexité O(n * pixels) — rapide car travaille sur des images
#     binarisées (seuil médian) plutôt que sur les valeurs brutes.
#
#   Mertens (fusion multi-échelle) :
#     Pour chaque pixel, calcule trois scores : contraste local (variance
#     du Laplacien dans un voisinage), saturation et exposition.
#     Combine ces scores avec des pyramides laplaciennes pour une fusion
#     progressive sans artefacts de couture.
#     Peut produire de légers halos sur des textures très fines.
#
# ── Automatisation du nommage et de la sauvegarde ───────────────────────────
#
# Le pipeline complet est :
#   1. L'utilisateur sélectionne des photos dans l'interface (Ctrl+clic)
#   2. focus_stacking() est appelé avec la liste des chemins
#   3. Le nom de sortie est construit automatiquement depuis le nom
#      de la première photo brute en remplaçant "_photoXX" par "_STACKEE"
#   4. Le fichier est sauvegardé en .tiff sans compression (sans perte)
#   5. L'aperçu dans l'interface se met à jour automatiquement

import cv2
import os
import sys
import subprocess
import shutil
import tempfile
import numpy as np


def focus_stacking(liste_chemins, chemin_sortie):
    """
    Fonction principale appelée depuis interface.py.

    Essaie enfuse en priorité (meilleure qualité, gratuit).
    Si non installé, utilise AlignMTB + Mertens d'OpenCV.

    Paramètres :
        liste_chemins : liste de chemins vers les photos brutes
        chemin_sortie : chemin du fichier de sortie (.tiff recommandé)
    Retourne chemin_sortie si succès, None sinon.
    """
    if len(liste_chemins) < 2:
        print("[Stacking] Il faut au moins 2 images.")
        return None

    print(f"[Stacking] {len(liste_chemins)} images en entrée.")

    if shutil.which("enfuse") is not None:
        print("[Stacking] Méthode : enfuse (open source)")
        resultat = _stacking_enfuse(liste_chemins, chemin_sortie)
        if resultat:
            return resultat
        print("[Stacking] enfuse a échoué. Fallback : Mertens OpenCV.")
    else:
        print("[Stacking] enfuse non installé. Fallback : Mertens OpenCV.")
        print("[Stacking] Pour installer enfuse : sudo apt install enfuse")

    return _stacking_mertens(liste_chemins, chemin_sortie)


# ==============================================================================
# MÉTHODE 1 : enfuse (gratuit, open source)
# ==============================================================================

def _stacking_enfuse(liste_chemins, chemin_sortie):
    """
    Focus stacking avec enfuse.

    enfuse prend des images en entrée et produit une image fusionnée
    en pondérant chaque pixel selon son contraste local, sa saturation
    et son exposition. C'est conçu pour le HDR mais fonctionne très bien
    pour le focus stacking.

    On utilise align_image_stack (inclus avec enfuse/hugin) pour aligner
    les images avant la fusion si disponible, sinon on passe directement
    à enfuse.

    Installation : sudo apt install enfuse
    (inclut align_image_stack sur la plupart des distributions)
    """
    dossier_sortie = os.path.dirname(os.path.abspath(chemin_sortie))
    if dossier_sortie:
        os.makedirs(dossier_sortie, exist_ok=True)

    chemins_abs = [os.path.abspath(c) for c in liste_chemins]

    with tempfile.TemporaryDirectory() as tmp:
        # Étape 1 : aligner les images si align_image_stack est disponible
        images_a_fusionner = chemins_abs
        if shutil.which("align_image_stack"):
            print("[enfuse] Alignement avec align_image_stack...")
            pattern_aligne = os.path.join(tmp, "aligned_%04d.tif")
            r_align = subprocess.run(
                ["align_image_stack", "-m", "-a", pattern_aligne] + chemins_abs,
                capture_output=True, text=True, timeout=120
            )
            # Récupérer les fichiers alignés produits
            alignes = sorted([
                os.path.join(tmp, f)
                for f in os.listdir(tmp)
                if f.startswith("aligned_") and f.endswith(".tif")
            ])
            if alignes:
                images_a_fusionner = alignes
                print(f"[enfuse] {len(alignes)} images alignées.")

        # Étape 2 : fusionner avec enfuse
        sortie_abs = os.path.abspath(chemin_sortie)
        print(f"[enfuse] Fusion -> {sortie_abs}")
        r = subprocess.run(
            ["enfuse",
             "--exposure-weight=0",   # pas de pondération exposition (focus stack)
             "--saturation-weight=0", # pas de pondération saturation
             "--contrast-weight=1",   # pondération uniquement sur le contraste (netteté)
             "--contrast-window-size=5",
             f"--output={sortie_abs}"] + images_a_fusionner,
            capture_output=True, text=True, timeout=120
        )

        if os.path.exists(sortie_abs) and os.path.getsize(sortie_abs) > 0:
            taille = os.path.getsize(sortie_abs) // 1024
            print(f"[enfuse] Succès ({taille} Ko) -> {sortie_abs}")
            return sortie_abs

        print(f"[enfuse] Échec (code {r.returncode}).")
        if r.stderr:
            print(f"[enfuse] {r.stderr[:300]}")
        return None


# ==============================================================================
# MÉTHODE 2 : AlignMTB + Mertens (OpenCV) — fallback universel
# ==============================================================================

def _charger_images(liste_chemins):
    images = []
    for chemin in liste_chemins:
        img = cv2.imread(os.path.abspath(chemin))
        if img is None:
            print(f"[Stacking] Impossible de charger : {chemin}")
        else:
            images.append(img)
    print(f"[Stacking] {len(images)} image(s) chargée(s).")
    return images


def _aligner_images(images):
    """
    AlignMTB : aligne par seuillage médian de luminosité.
    Corrige les décalages x/y entre images.
    """
    if len(images) < 2:
        return images
    aligneur = cv2.createAlignMTB()
    aligneur.process(images, images)
    print("[Stacking] Alignement AlignMTB terminé.")
    return images


def _fusionner_mertens(images):
    """
    Mertens : fusion par pondération multi-échelle.
    Score par pixel = contraste local × saturation × exposition.
    Résultat en float32 (0-1) converti en uint8 (0-255).
    """
    fusionneur = cv2.createMergeMertens()
    resultat_float = fusionneur.process(images)
    resultat_uint8 = np.clip(resultat_float * 255, 0, 255).astype("uint8")
    print("[Stacking] Fusion Mertens terminée.")
    return resultat_uint8


def _stacking_mertens(liste_chemins, chemin_sortie):
    dossier = os.path.dirname(chemin_sortie)
    if dossier:
        os.makedirs(dossier, exist_ok=True)

    images = _charger_images(liste_chemins)
    if len(images) < 2:
        return None

    images = _aligner_images(images)
    resultat = _fusionner_mertens(images)

    if cv2.imwrite(chemin_sortie, resultat) and os.path.exists(chemin_sortie):
        print(f"[Stacking] Sauvegardé ({os.path.getsize(chemin_sortie)//1024} Ko) -> {chemin_sortie}")
        return chemin_sortie

    print(f"[Stacking] Erreur sauvegarde.")
    return None


# ==============================================================================
# TEST DIRECT
# ==============================================================================

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage : python3 traitement/stacking.py photo1 photo2 [photo3...] sortie.tiff")
        sys.exit(0)
    entrees = sys.argv[1:-1]
    sortie  = sys.argv[-1]
    res = focus_stacking(entrees, sortie)
    print(f"\nRésultat : {'Succès — ' + res if res else 'Échec'}")
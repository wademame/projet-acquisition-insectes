# interface.py
# Lancement : python3 interface.py

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import sys
import os
import time
import datetime
import subprocess
from PIL import Image, ImageTk
from text import TEXTES, GUIDE_FR, GUIDE_EN

WINDOWS = sys.platform == "win32"
LINUX   = sys.platform.startswith("linux")

C_BG         = "#FFFFFF"
C_BARRE      = "#5C1A3B"
C_CANON      = "#A06080"
C_JEULIN_BG  = "#FFFFFF"
C_JEULIN_FG  = "#5C1A3B"
C_ANDROID    = "#A06080"
C_STACK_BG   = "#3A7D44"
C_ROUGE      = "#C0394B"
C_VERT       = "#5C9E6E"
C_ORANGE     = "#D4860A"
C_GRIS_TEXTE = "#5A4060"
C_FRAME_BG   = "#FFFFFF"
C_LOG_BG     = "#2D1F3A"
C_LOG_FG     = "#F0D8EC"
C_GUIDE_BTN  = "#FDF4F4"


class InterfaceAcquisition:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Acquisition d'insectes")
        self.fenetre.geometry("1280x980")
        self.fenetre.configure(bg=C_BG)

        self.langue             = "FR"
        self.canon_disponible   = False
        self.android_disponible = False
        self.android_id         = None
        self.index_jeulin       = None
        self.chemin_video_jeulin = None  # ex : /dev/video2
        self.derniere_photo     = None
        self.photo_tk           = None
        self.chemins_session    = []

        self._preview_active   = False
        self._preview_cap      = None
        self._photo_preview_tk = None
        self._preview_job      = None
        self._jeulin_echecs    = 0

        self._construire_interface()
        threading.Thread(target=self._verifier_tous, daemon=True).start()
        self.fenetre.mainloop()

    def t(self, cle):
        return TEXTES[self.langue][cle]

    # Construction

    def _construire_interface(self):
        self._barre_titre()
        corps = tk.Frame(self.fenetre, bg=C_BG)
        corps.pack(fill="both", expand=True, padx=10, pady=8)
        col_g = tk.Frame(corps, bg=C_BG)
        col_g.pack(side="left", fill="both", expand=True)
        col_d = tk.Frame(corps, bg=C_BG, width=320)
        col_d.pack(side="right", fill="y", padx=(10, 0))
        col_d.pack_propagate(False)
        self._construire_gauche(col_g)
        self._construire_droite(col_d)

    def _barre_titre(self):
        barre = tk.Frame(self.fenetre, bg=C_BARRE, height=50)
        barre.pack(fill="x")
        barre.pack_propagate(False)
        self.lbl_titre = tk.Label(barre, text=self.t("titre"),
            font=("Arial", 13, "bold"), fg="white", bg=C_BARRE)
        self.lbl_titre.pack(side="left", padx=16, pady=12)
        self.btn_langue = tk.Button(barre, text=self.t("langue_btn"),
            font=("Arial", 9), bg=C_GUIDE_BTN, fg="black",
            activebackground="#E7E4E4", relief="flat", padx=8,
            command=self._changer_langue)
        self.btn_langue.pack(side="right", padx=6, pady=12)
        self.btn_guide = tk.Button(barre, text=self.t("guide_btn"),
            font=("Arial", 10, "bold"), bg=C_GUIDE_BTN, fg="black",
            activebackground="#E7E4E4", relief="flat", padx=10,
            command=self._ouvrir_guide)
        self.btn_guide.pack(side="right", padx=6, pady=12)

    def _construire_gauche(self, parent):
        self._section_metadonnees(parent)
        self._section_connexion(parent)
        self._section_preview_jeulin(parent)
        self._section_declenchement(parent)
        self._section_journal(parent)

    def _section_metadonnees(self, parent):
        self.frame_params = tk.LabelFrame(parent,
            text=self.t("params_titre"),
            font=("Arial", 11, "bold"), fg="#000000",
            bg=C_FRAME_BG, padx=10, pady=8)
        self.frame_params.pack(fill="x", pady=(0, 8))
        self.lbl_params_note = tk.Label(self.frame_params,
            text=self.t("params_note"),
            bg=C_FRAME_BG, fg=C_ROUGE, font=("Arial", 9, "italic"))
        self.lbl_params_note.pack(anchor="w", pady=(0, 6))
        champs = [
            ("espece",   "champ_espece",   "Entry",    "", None),
            ("individu", "champ_individu", "Combobox", "", [str(i) for i in range(1, 21)]),
            ("angle",    "champ_angle",    "Combobox", "", ["Dorsal","Side","Front","Back"]),
        ]
        self.labels_champs = {}
        for cle_trad, attr, type_w, defaut, options in champs:
            ligne = tk.Frame(self.frame_params, bg=C_FRAME_BG)
            ligne.pack(fill="x", pady=3)
            lbl = tk.Label(ligne, text=self.t(cle_trad),
                bg=C_FRAME_BG, fg=C_GRIS_TEXTE,
                width=16, anchor="w", font=("Arial", 10))
            lbl.pack(side="left")
            self.labels_champs[cle_trad] = lbl
            if type_w == "Entry":
                w = tk.Entry(ligne, width=22, font=("Arial", 10),
                    bg="white", fg=C_GRIS_TEXTE, relief="solid", bd=1)
                w.insert(0, defaut)
            else:
                w = ttk.Combobox(ligne, values=options, width=12, font=("Arial", 10))
                w.set(defaut)
            w.pack(side="left", padx=4)
            setattr(self, attr, w)

    def _section_connexion(self, parent):
        self.frame_conn = tk.LabelFrame(parent,
            text=self.t("connexion_titre"),
            font=("Arial", 11), fg=C_GRIS_TEXTE,
            bg=C_FRAME_BG, padx=10, pady=6)
        self.frame_conn.pack(fill="x", pady=(0, 8))
        self.btn_actualiser = tk.Button(self.frame_conn,
            text=self.t("actualiser"),
            font=("Arial", 10), bg="#DDDADA", fg="black",
            activebackground="#CECECE", relief="flat", padx=8,
            command=self._lancer_verification)
        self.btn_actualiser.pack(anchor="w", pady=(0, 6))
        self.statuts = {}
        self.labels_appareils = {}
        for cle, cle_trad in [("Canon","canon_lbl"),("Jeulin","jeulin_lbl"),("Android","android_lbl")]:
            ligne = tk.Frame(self.frame_conn, bg=C_FRAME_BG)
            ligne.pack(fill="x", pady=2)
            lbl_nom = tk.Label(ligne, text=self.t(cle_trad),
                bg=C_FRAME_BG, fg=C_GRIS_TEXTE,
                width=26, anchor="w", font=("Arial", 10))
            lbl_nom.pack(side="left")
            self.labels_appareils[cle] = lbl_nom
            lbl_statut = tk.Label(ligne, text=self.t("verif_en_cours"),
                fg=C_ORANGE, bg=C_FRAME_BG, font=("Arial", 10, "italic"))
            lbl_statut.pack(side="left")
            self.statuts[cle] = lbl_statut

    def _section_preview_jeulin(self, parent):
        """
        Prévisualisation Jeulin avec curseurs Luminosité et Gamma.

        OpenCV traduit sa propre plage 0-255 vers la plage du driver, mais
        la correspondance n'est pas exacte. La caméra expose brightness de
        -64 à 64 et gamma de 72 à 500, des plages différentes de celle
        d'OpenCV. v4l2-ctl envoie directement la valeur native au driver,
        sans aucune conversion, ce qui garantit que le réglage prend effet.

        Le Gamma agit sur les tons moyens et zones sombres, il révèle les
        détails cachés dans les parties sombres de l'insecte sans "cramer"
        les zones déjà claires. Le contraste est déjà bien réglé à 32 par
        défaut. Le gain amplifie aussi le bruit, donc on le laisse à 0.
        Valeur gamma recommandée : 200 (défaut naturel du capteur).
        """
        self.frame_preview = tk.LabelFrame(parent,
            text="Prévisualtion Caméra Jeulin",
            font=("Arial", 10, "bold"), fg=C_JEULIN_FG,
            bg=C_FRAME_BG, padx=2, pady=2)
        self.frame_preview.pack(fill="x", pady=(0, 4))

        self.frame_preview_inner = tk.Frame(
            self.frame_preview, bg="#1A1A1A", width=620, height=290)
        self.frame_preview_inner.pack(fill="x", padx=2, pady=2)
        self.frame_preview_inner.pack_propagate(False)

        self.label_preview = tk.Label(
            self.frame_preview_inner,
            text="Jeulin non détectée.\nBranchez la caméra et actualisez.",
            bg="#1A1A1A", fg="#888888", font=("Arial", 10, "italic"))
        self.label_preview.place(relx=0.5, rely=0.5, anchor="center")

        # Curseurs luminosité et gamma
        frame_ctrl = tk.Frame(self.frame_preview, bg=C_FRAME_BG)
        frame_ctrl.pack(fill="x", padx=4, pady=(2, 4))

        # Plages natives V4L2 de cette caméra
        # brightness : -64 à 64, défaut 0
        # gamma      :  72 à 500, défaut 200 (recommandé pour insectes)
        self._val_brightness = tk.IntVar(value=0)
        self._val_gamma      = tk.IntVar(value=200)
        self._val_exposure   = tk.IntVar(value=200)

        curseurs = [
            ("Luminosité", self._val_brightness, -64, 64,   0,   "brightness"),
            ("Gamma",      self._val_gamma,        72, 500, 200,  "gamma"),
        ]

        for i, (label, var, vmin, vmax, neutre, ctrl_name) in enumerate(curseurs):
            col = tk.Frame(frame_ctrl, bg=C_FRAME_BG)
            col.grid(row=0, column=i, padx=12, sticky="ew")
            frame_ctrl.columnconfigure(i, weight=1)

            tk.Label(col, text=label, bg=C_FRAME_BG, fg=C_GRIS_TEXTE,
                font=("Arial", 9, "bold")).pack(anchor="w")

            # Affichage de la valeur courante
            lbl_val = tk.Label(col, textvariable=var,
                bg=C_FRAME_BG, fg=C_BARRE, font=("Arial", 9))
            lbl_val.pack(anchor="e")

            curseur = tk.Scale(col,
                from_=vmin, to=vmax,
                variable=var,
                orient="horizontal",
                bg=C_FRAME_BG, fg=C_GRIS_TEXTE,
                activebackground=C_BARRE,
                troughcolor="#E0D0E8",
                highlightthickness=0,
                sliderlength=18,
                showvalue=0,
                command=lambda v, cn=ctrl_name, vr=var: self._appliquer_v4l2(cn, vr.get()))
            curseur.pack(fill="x")

            # Bouton reset
            tk.Button(col, text="↺  défaut",
                font=("Arial", 8), bg="#DDDADA", fg="black",
                relief="flat", padx=4, pady=1,
                command=lambda vr=var, n=neutre, cn=ctrl_name: (
                    vr.set(n), self._appliquer_v4l2(cn, n))
            ).pack(anchor="w", pady=(2, 0))

    def _appliquer_v4l2(self, ctrl_name, valeur):
        """
        Applique un réglage directement au driver V4L2 via v4l2-ctl.
        Contourne le problème de plage OpenCV : v4l2-ctl envoie la valeur
        native au driver sans aucune conversion intermédiaire.

        chemin_video_jeulin est le chemin /dev/videoX détecté lors
        de la vérification de la Jeulin.
        """
        if not LINUX or not self.chemin_video_jeulin:
            return
        subprocess.run(
            ["v4l2-ctl", "-d", self.chemin_video_jeulin,
             f"--set-ctrl={ctrl_name}={int(valeur)}"],
            capture_output=True
        )

    def _section_declenchement(self, parent):
        self.frame_declench = tk.LabelFrame(parent,
            text=self.t("declencher_titre"),
            font=("Arial", 11, "bold"), fg=C_GRIS_TEXTE,
            bg=C_FRAME_BG, padx=10, pady=10)
        self.frame_declench.pack(fill="x", pady=(0, 8))
        self.lbl_declench_note = tk.Label(self.frame_declench,
            text=self.t("declencher_note"),
            bg=C_FRAME_BG, fg="#888", font=("Arial", 9, "italic"))
        self.lbl_declench_note.pack(anchor="w", pady=(0, 8))
        ligne_btns = tk.Frame(self.frame_declench, bg=C_FRAME_BG)
        ligne_btns.pack(fill="x")
        ligne_btns.columnconfigure(0, weight=1)
        ligne_btns.columnconfigure(1, weight=1)
        ligne_btns.columnconfigure(2, weight=1)
        self.btn_canon = tk.Button(ligne_btns, text=self.t("btn_canon"),
            bg=C_CANON, fg="white", activebackground=C_BARRE,
            font=("Arial", 11, "bold"), relief="flat", height=2, cursor="hand2",
            command=lambda: self._declencher_un("Canon"))
        self.btn_canon.grid(row=0, column=0, padx=6, sticky="ew")
        self.btn_jeulin = tk.Button(ligne_btns, text=self.t("btn_jeulin"),
            bg=C_JEULIN_BG, fg=C_JEULIN_FG, activebackground="#F0E0EC",
            highlightbackground=C_BARRE, highlightthickness=2,
            font=("Arial", 11, "bold"), relief="solid", bd=2, height=2, cursor="hand2",
            command=lambda: self._declencher_un("Jeulin"))
        self.btn_jeulin.grid(row=0, column=1, padx=6, sticky="ew")
        self.btn_android = tk.Button(ligne_btns, text=self.t("btn_android"),
            bg=C_ANDROID, fg="white", activebackground=C_BARRE,
            font=("Arial", 11, "bold"), relief="flat", height=2, cursor="hand2",
            command=lambda: self._declencher_un("Android"))
        self.btn_android.grid(row=0, column=2, padx=6, sticky="ew")
        self.lbl_erreur_champs = tk.Label(self.frame_declench,
            text="", fg=C_ROUGE, bg=C_FRAME_BG, font=("Arial", 9, "italic"))
        self.lbl_erreur_champs.pack(anchor="w", pady=(6, 0))

    def _section_journal(self, parent):
        self.frame_journal = tk.LabelFrame(parent,
            text=self.t("journal_titre"),
            font=("Arial", 11), fg=C_GRIS_TEXTE,
            bg=C_FRAME_BG, padx=5, pady=5)
        self.frame_journal.pack(fill="both", expand=True)
        self.zone_log = tk.Text(self.frame_journal,
            height=6, font=("Courier", 10), state="disabled",
            bg=C_LOG_BG, fg=C_LOG_FG, insertbackground="white", relief="flat")
        sc = tk.Scrollbar(self.frame_journal, command=self.zone_log.yview)
        self.zone_log.configure(yscrollcommand=sc.set)
        self.zone_log.pack(side="left", fill="both", expand=True)
        sc.pack(side="right", fill="y")
        self.btn_effacer = tk.Button(parent, text=self.t("effacer"),
            font=("Arial", 9), bg="#E7D4D6", fg="black",
            relief="flat", padx=6, command=self._effacer_journal)
        self.btn_effacer.pack(anchor="e", pady=(4, 0))
        self.log(self.t("demarrage"))

    def _construire_droite(self, parent):
        self.lbl_photo_titre = tk.Label(parent, text=self.t("photo_titre"),
            font=("Arial", 11, "bold"), fg=C_GRIS_TEXTE, bg=C_BG)
        self.lbl_photo_titre.pack(pady=(0, 4))
        self.frame_apercu = tk.Frame(parent,
            bg="#E4E4E4", width=310, height=225, relief="groove", bd=2)
        self.frame_apercu.pack(fill="x")
        self.frame_apercu.pack_propagate(False)
        self.label_apercu = tk.Label(self.frame_apercu,
            text="Aucune photo\nprise pour l'instant",
            bg="#E4E4E4", fg="#7A5070",
            font=("Arial", 10, "italic"), cursor="hand2")
        self.label_apercu.pack(expand=True)
        self.label_apercu.bind("<Button-1>", self._agrandir_photo)
        self.lbl_indication = tk.Label(parent, text=self.t("cliquer_agrandir"),
            bg=C_BG, fg="#999", font=("Arial", 8, "italic"))
        self.lbl_indication.pack(pady=(2, 0))
        self.label_nom_photo = tk.Label(parent, text="",
            bg=C_BG, fg=C_GRIS_TEXTE,
            font=("Courier", 8), wraplength=310, justify="left")
        self.label_nom_photo.pack(pady=4, anchor="w")
        self.btn_supprimer = tk.Button(parent, text=self.t("supprimer"),
            font=("Arial", 10), bg="#E7D4D6", fg="black",
            relief="flat", state="disabled",
            command=self._supprimer_photo_apercu)
        self.btn_supprimer.pack(fill="x", pady=2)
        tk.Frame(parent, bg="#CCCCCC", height=1).pack(fill="x", pady=(12, 6))
        self.lbl_session = tk.Label(parent, text=self.t("session_titre"),
            font=("Arial", 10, "bold"), fg=C_GRIS_TEXTE, bg=C_BG)
        self.lbl_session.pack(anchor="w")
        self.lbl_session_note = tk.Label(parent, text=self.t("session_note"),
            bg=C_BG, fg="#666666",
            font=("Arial", 9), wraplength=300, justify="left")
        self.lbl_session_note.pack(anchor="w", pady=(2, 6))
        frame_liste = tk.Frame(parent, bg=C_BG)
        frame_liste.pack(fill="both", expand=True)
        self.liste_photos = tk.Listbox(frame_liste,
            font=("Courier", 8), height=8,
            bg="white", fg=C_GRIS_TEXTE,
            selectbackground="#D4A0B8", selectforeground="white",
            relief="solid", bd=1, selectmode="extended")
        sc_liste = tk.Scrollbar(frame_liste, command=self.liste_photos.yview)
        self.liste_photos.configure(yscrollcommand=sc_liste.set)
        self.liste_photos.pack(side="left", fill="both", expand=True)
        sc_liste.pack(side="right", fill="y")
        self.liste_photos.bind("<<ListboxSelect>>", self._afficher_photo_selectionnee)
        self.btn_supprimer_selection = tk.Button(parent,
            text="Supprimer la sélection",
            font=("Arial", 9), bg="#E7D4D6", fg="black",
            relief="flat", command=self._supprimer_photos_selectionnees)
        self.btn_supprimer_selection.pack(fill="x", pady=(2, 4))
        self.btn_stack = tk.Button(parent, text=self.t("btn_stack"),
            font=("Arial", 10, "bold"), bg=C_STACK_BG, fg="white",
            relief="flat", cursor="hand2", pady=6,
            command=self._lancer_stacking)
        self.btn_stack.pack(fill="x", pady=(4, 0))
        self.lbl_stack_statut = tk.Label(parent,
            text="", bg=C_BG, fg=C_GRIS_TEXTE,
            font=("Arial", 9, "italic"), wraplength=300)
        self.lbl_stack_statut.pack(anchor="w", pady=(3, 0))

    # Langue

    def _changer_langue(self):
        self.langue = "EN" if self.langue == "FR" else "FR"
        self.btn_langue.configure(text=self.t("langue_btn"))
        self._mettre_a_jour_textes()

    def _mettre_a_jour_textes(self):
        self.fenetre.title(self.t("titre"))
        self.lbl_titre.configure(text=self.t("titre"))
        self.btn_guide.configure(text=self.t("guide_btn"))
        self.frame_params.configure(text=self.t("params_titre"))
        self.lbl_params_note.configure(text=self.t("params_note"))
        for cle in ["espece", "individu", "angle"]:
            self.labels_champs[cle].configure(text=self.t(cle))
        self.frame_conn.configure(text=self.t("connexion_titre"))
        self.btn_actualiser.configure(text=self.t("actualiser"))
        for cle, cle_trad in [("Canon","canon_lbl"),("Jeulin","jeulin_lbl"),("Android","android_lbl")]:
            self.labels_appareils[cle].configure(text=self.t(cle_trad))
        self.frame_declench.configure(text=self.t("declencher_titre"))
        self.lbl_declench_note.configure(text=self.t("declencher_note"))
        self.btn_canon.configure(text=self.t("btn_canon"))
        self.btn_jeulin.configure(text=self.t("btn_jeulin"))
        self.btn_android.configure(text=self.t("btn_android"))
        self.frame_journal.configure(text=self.t("journal_titre"))
        self.btn_effacer.configure(text=self.t("effacer"))
        self.lbl_photo_titre.configure(text=self.t("photo_titre"))
        self.lbl_indication.configure(text=self.t("cliquer_agrandir"))
        self.btn_supprimer.configure(text=self.t("supprimer"))
        self.lbl_session.configure(text=self.t("session_titre"))
        self.lbl_session_note.configure(text=self.t("session_note"))
        self.btn_stack.configure(text=self.t("btn_stack"))

    # Journal

    def log(self, message):
        heure = datetime.datetime.now().strftime("%H:%M:%S")
        self.zone_log.configure(state="normal")
        self.zone_log.insert("end", f"[{heure}] {message}\n")
        self.zone_log.see("end")
        self.zone_log.configure(state="disabled")

    def _effacer_journal(self):
        self.zone_log.configure(state="normal")
        self.zone_log.delete("1.0", "end")
        self.zone_log.configure(state="disabled")

    # Vérification

    def _lancer_verification(self):
        threading.Thread(target=self._verifier_tous, daemon=True).start()

    def _verifier_tous(self):
        self.fenetre.after(0, lambda: self.log(self.t("verification")))
        self._verifier_canon()
        self._verifier_jeulin()
        self._verifier_android()
        ok = []
        if self.canon_disponible:          ok.append("Canon")
        if self.index_jeulin is not None:  ok.append("Jeulin")
        if self.android_disponible:        ok.append("Android")
        msg = f"{self.t('detectes')} : {', '.join(ok)}" if ok else self.t("aucun")
        self.fenetre.after(0, lambda: self.log(msg))

    def _verifier_canon(self):
        try:
            from acquisition.canon import connecter_canon
            ok = connecter_canon()
            if ok:
                self.canon_disponible = True
                statut  = self.t("canon_statut_linux") if LINUX else self.t("canon_statut_windows")
                msg_log = self.t("canon_ok_linux")     if LINUX else self.t("canon_ok_windows")
                self.fenetre.after(0, lambda s=statut: self.statuts["Canon"].configure(text=s, fg=C_VERT))
                self.fenetre.after(0, lambda m=msg_log: self.log(m))
            else:
                self.canon_disponible = False
                self.fenetre.after(0, lambda: self.statuts["Canon"].configure(
                    text=self.t("non_detecte"), fg=C_ROUGE))
                self.fenetre.after(0, lambda: self.log(self.t("canon_non")))
        except Exception as e:
            self.canon_disponible = False
            self.fenetre.after(0, lambda: self.statuts["Canon"].configure(
                text=self.t("err_canon"), fg=C_ROUGE))
            self.fenetre.after(0, lambda err=e: self.log(f"{self.t('canon_err')} : {err}"))

    def _verifier_jeulin(self):
        """
        Détecte la Jeulin et mémorise le chemin /dev/videoX.
        Ce chemin est utilisé par v4l2-ctl pour les réglages luminosité/gamma.

        Bug reconnexion corrigé :
        Quand on débranhe/rebranche la Jeulin, le chemin /dev/videoX peut
        changer. On arrête la preview avant de réouvrir la caméra pour
        libérer le handle OpenCV, puis on redémarre proprement.
        """
        try:
            import cv2
            index_trouve = None
            chemin_trouve = None

            try:
                r = subprocess.run(["v4l2-ctl", "--list-devices"],
                    capture_output=True, text=True, timeout=5)
                lignes = r.stdout.split("\n")
                nom_courant = ""
                for ligne in lignes:
                    if ligne and not ligne.startswith("\t"):
                        nom_courant = ligne.lower()
                    elif ligne.startswith("\t") and (
                            "jeulin" in nom_courant or "e-mago" in nom_courant
                            or "hd usb camera" in nom_courant):
                        chemin = ligne.strip()
                        if "video" in chemin:
                            try:
                                idx = int(chemin.replace("/dev/video", "").strip())
                                index_trouve = idx
                                chemin_trouve = chemin
                                break
                            except ValueError:
                                pass
            except Exception:
                pass

            if index_trouve is None:
                debut = 1 if LINUX else 0
                for i in range(debut, 8):
                    cap = cv2.VideoCapture(i)
                    if cap.isOpened():
                        ok_read, _ = cap.read()
                        cap.release()
                        if ok_read:
                            index_trouve = i
                            chemin_trouve = f"/dev/video{i}"
                            break
                    else:
                        cap.release()

            if index_trouve is not None:
                self._jeulin_echecs = 0

                # Si la caméra a changé de chemin (débranché/rebranché),
                # arrêter la preview avant de mettre à jour l'index
                if (self.chemin_video_jeulin != chemin_trouve
                        and self._preview_active):
                    self.fenetre.after(0, self._arreter_preview)
                    time.sleep(0.5)

                self.index_jeulin        = index_trouve
                self.chemin_video_jeulin = chemin_trouve

                self.fenetre.after(0, lambda idx=index_trouve: self.statuts["Jeulin"].configure(
                    text=f"Connectée (index {idx})", fg=C_VERT))
                self.fenetre.after(0, lambda idx=index_trouve: self.log(
                    f"{self.t('jeulin_ok')} {idx}."))

                # Appliquer les réglages gamma/brightness immédiatement
                self._appliquer_v4l2("brightness", self._val_brightness.get())
                self._appliquer_v4l2("gamma",      self._val_gamma.get())

                # Redémarrer la preview si elle n'est pas déjà active
                if not self._preview_active:
                    self.fenetre.after(700, self._demarrer_preview)

            else:
                self._jeulin_echecs += 1
                if self._jeulin_echecs >= 3:
                    self.index_jeulin        = None
                    self.chemin_video_jeulin = None
                    self.fenetre.after(0, lambda: self.statuts["Jeulin"].configure(
                        text=self.t("non_branche"), fg=C_ORANGE))
                    self.fenetre.after(0, lambda: self.log(self.t("jeulin_non")))
                    # Si la caméra a disparu, arrêter la preview
                    if self._preview_active:
                        self.fenetre.after(0, self._arreter_preview)
                else:
                    self.fenetre.after(0, lambda: self.log(
                        "Jeulin : détection incertaine, réessayez."))

        except Exception as e:
            self.fenetre.after(0, lambda err=e: self.log(f"{self.t('jeulin_err')} : {err}"))

    def _verifier_android(self):
        try:
            r = subprocess.run(['adb', 'devices'], capture_output=True, text=True, timeout=8)
            if "doesn't match" in r.stderr or "doesn't match" in r.stdout:
                self.android_disponible = False
                self.fenetre.after(0, lambda: self.statuts["Android"].configure(
                    text=self.t("adb_ver_pb"), fg=C_ORANGE))
                self.fenetre.after(0, lambda: self.log(self.t("android_adb_ver")))
                return
            appareils = [
                l.split('\t')[0]
                for l in r.stdout.strip().split('\n')[1:]
                if '\tdevice' in l
            ]
            if appareils:
                self.android_disponible = True
                self.android_id = appareils[0]
                self.fenetre.after(0, lambda: self.statuts["Android"].configure(
                    text=f"{self.t('connecte_android')} ({self.android_id})", fg=C_VERT))
                self.fenetre.after(0, lambda: self.log(
                    f"{self.t('android_ok')} : {self.android_id}"))
            else:
                self.android_disponible = False
                self.fenetre.after(0, lambda: self.statuts["Android"].configure(
                    text=self.t("non_detecte"), fg=C_ROUGE))
                self.fenetre.after(0, lambda: self.log(self.t("android_non")))
        except FileNotFoundError:
            self.android_disponible = False
            self.fenetre.after(0, lambda: self.statuts["Android"].configure(
                text=self.t("adb_absent"), fg=C_ROUGE))
            self.fenetre.after(0, lambda: self.log(self.t("android_adb_abs")))

    # Prévisualisation Jeulin

    def _demarrer_preview(self):
        """
        Ouvre la caméra et démarre la boucle.
        Si une preview était déjà ouverte (ex: après reconnexion), on ferme
        proprement l'ancien handle avant d'en ouvrir un nouveau.
        """
        if self.index_jeulin is None:
            return
        if self._preview_active:
            self._arreter_preview()
            time.sleep(0.3)

        import cv2
        cap = cv2.VideoCapture(self.index_jeulin)
        if not cap.isOpened():
            self.log("Prévisualisation Jeulin : impossible d'ouvrir la caméra.")
            return

        cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        for _ in range(5):
            cap.read()

        # Fixer l'exposition en mode manuel AVANT de démarrer le flux
        # exposure_auto=1 = manuel, exposure_auto=3 = auto (défaut driver)
        # Sans ça la caméra recalcule à chaque nouveau flux et surexpose à la capture
        self._appliquer_v4l2("exposure_auto", 1)
        self._appliquer_v4l2("exposure_time_absolute", self._val_exposure.get())


        self._preview_cap    = cap
        self._preview_active = True
        self._tick_preview()

    def _tick_preview(self):
        if not self._preview_active or self._preview_cap is None:
            return
        import cv2
        ok, frame = self._preview_cap.read()
        if ok:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img.thumbnail((616, 286), Image.NEAREST)
            photo = ImageTk.PhotoImage(img)
            self._photo_preview_tk = photo
            self.label_preview.configure(image=photo, text="", bg="#1A1A1A")
            self.label_preview.place(relx=0.5, rely=0.5, anchor="center")
        if self._preview_active:
            self._preview_job = self.fenetre.after(16, self._tick_preview)

    def _arreter_preview(self):
        self._preview_active = False
        if self._preview_job is not None:
            self.fenetre.after_cancel(self._preview_job)
            self._preview_job = None
        if self._preview_cap is not None:
            self._preview_cap.release()
            self._preview_cap = None
        self._photo_preview_tk = None
        self.label_preview.configure(
            image="", text="Prévisualisation arrêtée.\nActualisez la détection pour relancer.",
            bg="#1A1A1A", fg="#888888")

    # Nommage stackée

    def _prochain_nom_stackee(self, dossier, base):
        chemin = os.path.join(dossier, f"{base}_STACKEE.tiff")
        if not os.path.exists(chemin):
            return f"{base}_STACKEE.tiff"
        n = 2
        while True:
            nom = f"{base}_STACKEE_{n:02d}.tiff"
            if not os.path.exists(os.path.join(dossier, nom)):
                return nom
            n += 1

    # Déclenchement

    def _valider_champs(self):
        manquants = []
        if not self.champ_espece.get().strip():   manquants.append("Espèce")
        if not self.champ_individu.get().strip(): manquants.append("N° individu")
        if not self.champ_angle.get().strip():    manquants.append("Angle")
        if manquants:
            msg = f"{self.t('champs_manquants')}{', '.join(manquants)}"
            self.log(msg)
            self.lbl_erreur_champs.configure(text=msg)
            self.fenetre.after(4000, lambda: self.lbl_erreur_champs.configure(text=""))
            return False
        self.lbl_erreur_champs.configure(text="")
        return True

    def _declencher_un(self, appareil):
        if not self._valider_champs():
            return
        if appareil == "Jeulin" and self._preview_active:
            self._arreter_preview()
            time.sleep(0.3)
        boutons = {"Canon": self.btn_canon, "Jeulin": self.btn_jeulin, "Android": self.btn_android}
        boutons[appareil].configure(state="disabled")
        threading.Thread(
            target=self._capture_un_appareil,
            args=(appareil,), daemon=True
        ).start()

    def _capture_un_appareil(self, appareil):
        from acquisition.nommage import (
            generer_nom_fichier, generer_chemin_dossier, prochain_numero_photo
        )
        espece       = self.champ_espece.get().strip()
        num_individu = int(self.champ_individu.get())
        angle        = self.champ_angle.get()
        extensions   = {"Canon": "jpg", "Jeulin": "png", "Android": "jpg"}
        ext          = extensions[appareil]
        dossier      = generer_chemin_dossier("images", appareil, espece, num_individu)
        num_photo    = prochain_numero_photo(dossier, espece, num_individu, appareil, angle, ext)
        nom          = generer_nom_fichier(espece, num_individu, appareil, angle, num_photo, ext)
        chemin       = os.path.join(dossier, nom)

        self.fenetre.after(0, lambda: self.log(f"{self.t('declench_log')} {appareil} : {nom}"))
        resultat = None

        if appareil == "Canon":
            if self.canon_disponible:
                try:
                    from acquisition.canon import prendre_photo_canon
                    resultat = prendre_photo_canon(chemin)
                    if resultat is None and self.android_disponible:
                        self.fenetre.after(0, lambda: self.log(
                            "Échec Canon. Si l'objectif est en mode AF, "
                            "passez-le en MF (interrupteur sur l'objectif). "
                            "Le téléphone branché peut perturber la capture."))
                except Exception as e:
                    self.fenetre.after(0, lambda err=e: self.log(f"{self.t('canon_err')} : {err}"))
            else:
                self.fenetre.after(0, lambda: self.log(self.t("canon_decon")))

        elif appareil == "Jeulin":
            if self.index_jeulin is not None:
                try:
                    from acquisition.jeulin import prendre_photo_jeulin
                    resultat = prendre_photo_jeulin(self.index_jeulin, chemin)
                except Exception as e:
                    self.fenetre.after(0, lambda err=e: self.log(f"{self.t('jeulin_err')} : {err}"))
                finally:
                    self.fenetre.after(500, self._demarrer_preview)
            else:
                self.fenetre.after(0, lambda: self.log(self.t("jeulin_decon")))

        elif appareil == "Android":
            if self.android_disponible and self.android_id:
                try:
                    from acquisition.android import prendre_photo_android
                    resultat = prendre_photo_android(self.android_id, chemin)
                except Exception as e:
                    self.fenetre.after(0, lambda err=e: self.log(f"Android erreur : {err}"))
            else:
                self.fenetre.after(0, lambda: self.log(self.t("android_decon")))

        if resultat:
            self.fenetre.after(0, lambda r=resultat: self.log(
                f"{self.t('photo_ok')} : {os.path.basename(r)}"))
            self.fenetre.after(0, lambda r=resultat: self._mettre_a_jour_apercu(r))
        else:
            self.fenetre.after(0, lambda: self.log(f"{self.t('photo_echec')} {appareil}."))

        boutons = {"Canon": self.btn_canon, "Jeulin": self.btn_jeulin, "Android": self.btn_android}
        self.fenetre.after(0, lambda: boutons[appareil].configure(state="normal"))

    # Focus stacking

    def _lancer_stacking(self):
        selection = self.liste_photos.curselection()
        if len(selection) < 2:
            self.log(self.t("stack_sel_insuffisante"))
            self.lbl_stack_statut.configure(text=self.t("stack_sel_insuffisante"), fg=C_ROUGE)
            self.fenetre.after(4000, lambda: self.lbl_stack_statut.configure(text=""))
            return
        chemins = []
        for idx in selection:
            nom = self.liste_photos.get(idx)
            for c in self.chemins_session:
                if os.path.basename(c) == nom:
                    chemins.append(c)
                    break
        if len(chemins) < 2:
            self.log(self.t("stack_chemins_introuvables"))
            return
        premier  = os.path.basename(chemins[0])
        base     = premier.rsplit("_photo", 1)[0] if "_photo" in premier else os.path.splitext(premier)[0]
        dossier  = os.path.dirname(chemins[0])
        nom_sortie    = self._prochain_nom_stackee(dossier, base)
        chemin_sortie = os.path.join(dossier, nom_sortie)
        self.log(f"{self.t('stack_debut')} {len(chemins)} {self.t('stack_images')} -> {nom_sortie}")
        self.lbl_stack_statut.configure(text=self.t("stack_en_cours"), fg=C_ORANGE)
        self.btn_stack.configure(state="disabled")
        threading.Thread(
            target=self._executer_stacking,
            args=(chemins, chemin_sortie), daemon=True
        ).start()

    def _executer_stacking(self, chemins, chemin_sortie):
        try:
            from traitement.stacking import focus_stacking
            resultat = focus_stacking(chemins, chemin_sortie)
            if resultat:
                self.fenetre.after(0, lambda: self.log(
                    f"{self.t('stack_ok')} : {os.path.basename(resultat)}"))
                self.fenetre.after(0, lambda: self.lbl_stack_statut.configure(
                    text=self.t("stack_ok_court"), fg=C_VERT))
                self.fenetre.after(0, lambda r=resultat: self._mettre_a_jour_apercu(r))
            else:
                self.fenetre.after(0, lambda: self.log(self.t("stack_echec")))
                self.fenetre.after(0, lambda: self.lbl_stack_statut.configure(
                    text=self.t("stack_echec"), fg=C_ROUGE))
        except Exception as e:
            self.fenetre.after(0, lambda err=e: self.log(f"Stacking erreur : {err}"))
            self.fenetre.after(0, lambda: self.lbl_stack_statut.configure(
                text=self.t("stack_echec"), fg=C_ROUGE))
        self.fenetre.after(0, lambda: self.btn_stack.configure(state="normal"))
        self.fenetre.after(5000, lambda: self.lbl_stack_statut.configure(text=""))

    # Aperçu photo

    def _mettre_a_jour_apercu(self, chemin_photo, ajouter_liste=True):
        self.derniere_photo = chemin_photo
        self.label_nom_photo.configure(text=os.path.basename(chemin_photo))
        self.btn_supprimer.configure(state="normal")
        if os.path.exists(chemin_photo):
            try:
                img = Image.open(chemin_photo)
                img.thumbnail((310, 225), Image.LANCZOS)
                self.photo_tk = ImageTk.PhotoImage(img)
                self.label_apercu.configure(
                    image=self.photo_tk, text="", bg="#E4E4E4", cursor="hand2")
            except Exception:
                self.label_apercu.configure(
                    image="", text="[aperçu non disponible]",
                    bg="#E4E4E4", cursor="arrow")
        else:
            self.label_apercu.configure(
                image="", text=f"Fichier introuvable :\n{os.path.basename(chemin_photo)}",
                bg="#E4E4E4", cursor="arrow")
        if ajouter_liste:
            nom = os.path.basename(chemin_photo)
            self.liste_photos.insert(0, nom)
            self.chemins_session.insert(0, chemin_photo)

    def _afficher_photo_selectionnee(self, event):
        selection = self.liste_photos.curselection()
        if not selection:
            return
        idx = selection[-1]
        nom = self.liste_photos.get(idx)
        for c in self.chemins_session:
            if os.path.basename(c) == nom:
                self._mettre_a_jour_apercu(c, ajouter_liste=False)
                return
        for racine, _, fichiers in os.walk("images"):
            if nom in fichiers:
                self._mettre_a_jour_apercu(os.path.join(racine, nom), ajouter_liste=False)
                return

    def _agrandir_photo(self, event=None):
        if not self.derniere_photo or not os.path.exists(self.derniere_photo):
            return
        fen = tk.Toplevel(self.fenetre)
        fen.title(os.path.basename(self.derniere_photo))
        fen.configure(bg="black")
        try:
            img = Image.open(self.derniere_photo)
            img.thumbnail((900, 700), Image.LANCZOS)
            ph = ImageTk.PhotoImage(img)
            lbl = tk.Label(fen, image=ph, bg="black")
            lbl.image = ph
            lbl.pack(padx=10, pady=10)
            tk.Button(fen, text=self.t("fermer"), font=("Arial", 10),
                bg=C_ROUGE, fg="white", relief="flat",
                command=fen.destroy).pack(pady=(0, 10))
        except Exception as e:
            tk.Label(fen, text=f"Impossible d'ouvrir l'image :\n{e}",
                fg="white", bg="black", font=("Arial", 11)).pack(padx=20, pady=20)

    def _supprimer_photo_apercu(self):
        if not self.derniere_photo:
            return
        self._supprimer_fichiers([self.derniere_photo])

    def _supprimer_photos_selectionnees(self):
        selection = self.liste_photos.curselection()
        if not selection:
            self.log("Aucune photo sélectionnée.")
            return
        noms = [self.liste_photos.get(i) for i in selection]
        chemins = []
        for nom in noms:
            for c in self.chemins_session:
                if os.path.basename(c) == nom:
                    chemins.append(c)
                    break
        if not chemins:
            return
        msg = (f"Supprimer cette photo ?\n\n{noms[0]}" if len(chemins) == 1
               else f"Supprimer ces {len(chemins)} photos ?\n\n" +
                    "\n".join(noms[:5]) + (f"\n... et {len(noms)-5} autre(s)" if len(noms) > 5 else ""))
        if not messagebox.askyesno("Confirmer la suppression", msg):
            return
        self._supprimer_fichiers(chemins)

    def _supprimer_fichiers(self, chemins):
        supprimes = []
        for chemin in chemins:
            try:
                if os.path.exists(chemin):
                    os.remove(chemin)
                    supprimes.append(chemin)
            except Exception as e:
                self.log(f"Impossible de supprimer {os.path.basename(chemin)} : {e}")
        if not supprimes:
            return
        noms_supprimes = {os.path.basename(c) for c in supprimes}
        self.chemins_session = [
            c for c in self.chemins_session if os.path.basename(c) not in noms_supprimes]
        for i in range(self.liste_photos.size() - 1, -1, -1):
            if self.liste_photos.get(i) in noms_supprimes:
                self.liste_photos.delete(i)
        if self.derniere_photo and os.path.basename(self.derniere_photo) in noms_supprimes:
            self.derniere_photo = None
            self.label_apercu.configure(image="", text="Photo supprimée.", bg="#E4E4E4")
            self.label_nom_photo.configure(text="")
            self.btn_supprimer.configure(state="disabled")
        self.log(f"{len(supprimes)} photo(s) supprimée(s).")

    def _ouvrir_guide(self):
        import webbrowser
        try:
            from text import GUIDE_SECTIONS_FR, GUIDE_SECTIONS_EN
        except ImportError:
            pass
        g = tk.Toplevel(self.fenetre)
        g.title(self.t("guide_titre"))
        g.geometry("780x680")
        g.configure(bg=C_BG)
        g.resizable(True, True)
        entete = tk.Frame(g, bg=C_BARRE, height=50)
        entete.pack(fill="x")
        entete.pack_propagate(False)
        tk.Label(entete, text=self.t("guide_titre"),
                 font=("Arial", 14, "bold"), fg="white", bg=C_BARRE
                 ).pack(side="left", padx=16, pady=12)
        frame_texte = tk.Frame(g, bg=C_BG)
        frame_texte.pack(fill="both", expand=True)
        texte = tk.Text(frame_texte, font=("Arial", 10), bg="white", fg="#1A1A1A",
            wrap="word", padx=20, pady=14, relief="flat", spacing1=2, spacing3=5, cursor="arrow")
        sc = tk.Scrollbar(frame_texte, command=texte.yview)
        texte.configure(yscrollcommand=sc.set)
        texte.pack(side="left", fill="both", expand=True)
        sc.pack(side="right", fill="y")
        C_GRIS = "#5A4060"
        texte.tag_configure("titre",   font=("Arial", 16, "bold"), foreground=C_BARRE, justify="center", spacing1=10, spacing3=6)
        texte.tag_configure("sous",    font=("Arial", 11, "bold"), foreground=C_BARRE, justify="center", spacing1=4,  spacing3=10)
        texte.tag_configure("h1",      font=("Arial", 12, "bold"), foreground=C_BARRE, spacing1=14, spacing3=4)
        texte.tag_configure("section", font=("Arial", 10, "bold"), foreground=C_GRIS,  spacing1=8,  spacing3=2)
        texte.tag_configure("code",    font=("Courier", 9), foreground="#F0D8EC", background="#2D1F3A", spacing1=1, spacing3=1, lmargin1=30, lmargin2=30)
        texte.tag_configure("normal",  font=("Arial", 10), foreground="#1A1A1A", justify="left", spacing3=4)
        ancres = {}
        def inserer(contenu):
            for ligne in contenu.split("\n"):
                if ligne.startswith("§TITRE§") and ligne.endswith("§"):
                    texte.insert("end", ligne[7:-1] + "\n", "titre")
                elif ligne.startswith("§SOUS§") and ligne.endswith("§"):
                    texte.insert("end", ligne[6:-1] + "\n", "sous")
                elif ligne.startswith("§H1§") and ligne.endswith("§"):
                    texte.insert("end", ligne[4:-1] + "\n", "h1")
                elif ligne.startswith("§CODE§"):
                    texte.insert("end", "  " + ligne[6:] + "\n", "code")
                elif ligne.startswith("§ANCRE§") and ligne.endswith("§"):
                    ancres[ligne[7:-1]] = texte.index("end")
                elif ligne.startswith("§IMG§"):
                    pass
                elif ligne.startswith("§LIEN§"):
                    parties = ligne[6:].rstrip("§").split("§")
                    if len(parties) >= 2:
                        cible, label = parties[0], parties[1]
                        tag = f"lien_{cible.replace('.','_').replace('/','_').replace(':','_')}"
                        if cible.startswith("http"):
                            texte.tag_configure(tag, font=("Arial", 10), foreground="#1A5276", underline=True)
                            texte.tag_bind(tag, "<Button-1>", lambda e, u=cible: webbrowser.open(u))
                        else:
                            texte.tag_configure(tag, font=("Arial", 10), foreground=C_BARRE, lmargin1=20)
                            texte.tag_bind(tag, "<Button-1>", lambda e, a=cible: texte.see(ancres.get(a, "1.0")))
                        texte.tag_bind(tag, "<Enter>", lambda e: texte.configure(cursor="hand2"))
                        texte.tag_bind(tag, "<Leave>", lambda e: texte.configure(cursor="arrow"))
                        texte.insert("end", "  " + label + "\n", tag)
                elif ligne == "":
                    texte.insert("end", "\n")
                else:
                    texte.insert("end", ligne + "\n", "normal")
        contenu = GUIDE_FR if self.langue == "FR" else GUIDE_EN
        inserer(contenu)
        texte.configure(state="disabled")
        tk.Button(g, text=self.t("fermer"), font=("Arial", 10), bg=C_BARRE, fg="white",
            relief="flat", padx=20, pady=6, command=g.destroy).pack(pady=(6, 12))


if __name__ == "__main__":
    app = InterfaceAcquisition()

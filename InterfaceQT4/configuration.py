# -*- coding: utf-8 -*-
# Copyright (C) 2007-2024   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
    Ce module sert pour charger les parametres de configuration d'EFICAS
"""
import os, sys, types, re
import traceback
from Extensions.i18n import tr


class configBase(object):
    # -------------------------------
    def __init__(self, appliEficas, repIni):
    # -------------------------------

        # Classe de base permettant de lire, afficher
        # et sauvegarder les fichiers utilisateurs
        # On a deux directories : la directory generale (Repertoire d install + Nom du code
        #                       Par exemple : ~/Install_Eficas/EficasV1_14/Openturns_Wrapper
        # et la directorie de l utilisateur
        #                       HOME/.Eficas_Openturns
        # Le fichier prefs.py va etre lu dans la directory generale
        #         puis surcharge eventuellement par celui contenu dans ${PREFS_CATA_$CODE}
        #         par celui de l utilisateur
        # le fichier de catalogue va etre lu dans la directory de l utilisateur s il exite
        # dans le fichier general sinon

        self.appliEficas = appliEficas
        self.code = appliEficas.code
        self.salome = appliEficas.salome
        if self.salome:
            self.name = "editeur_salome.ini"
        else:
            self.name = "editeur.ini"
        self.rep_mat = None
        self.repIni = repIni

        if self.code == None:
            self.code = ""
        self.rep_user = os.path.join(
            os.path.expanduser("~"), ".config/Eficas", self.code
        )
        # else :
        #        self.rep_user   = os.path.join('C:/','.config/Eficas',self.code)

        self.setValeursParDefaut()

        if self.code != "":
            self.lectureFichierIniStandard()
            self.lectureFichierIniIntegrateur()
            self.lectureFichierIniUtilisateur()

        if self.boutonDsMenuBar:
            self.closeAutreCommande = True
            self.closeFrameRechercheCommande = True

        # Particularite des schemas MAP
        if hasattr(self, "make_ssCode"):
            self.make_ssCode(self.ssCode)

        if not os.path.isdir(self.savedir):
            self.savedir = os.path.join(
                os.path.expanduser("~"), ".config/Eficas", self.code
            )

    def setValeursParDefaut(self):
    # -----------------------------

        # Valeurs par defaut
        if not os.path.isdir(self.rep_user):
            os.makedirs(self.rep_user)
        self.path_doc = os.path.abspath(os.path.join(self.repIni, "..", "Doc"))
        self.exec_acrobat = "acroread"
        nomDir = "Eficas_" + self.code
        self.savedir = os.path.abspath(os.path.join(os.path.expanduser("~"), nomDir))
        # if sys.platform[0:5]=="linux" :
        # self.savedir   = os.path.abspath(os.path.join(os.environ['HOME'],nomDir))
        # else:
        #  self.savedir = os.path.abspath('C:/')
        self.modeNouvCommande = "initial"
        self.affiche = "alpha"
        self.closeAutreCommande = False
        self.closeFrameRechercheCommande = False
        self.closeFrameRechercheCommandeSurPageDesCommandes = False
        self.closeEntete = False
        self.closeArbre = False
        self.demandeLangue = False
        self.suiteTelemac = False
        self.nombreDeBoutonParLigne = 0
        self.translatorFichier = None
        self.dicoImages = {}
        self.dicoIcones = {}
        self.afficheCommandesPliees = True
        self.afficheFirstPlies = False
        self.simpleClic = False
        self.afficheOptionnelVide = False
        self.afficheListesPliees = True
        self.boutonDsMenuBar = False
        self.ficIcones = None
        self.repIcones = None
        self.differencieSiDefaut = False
        self.typeDeCata = "Python"
        self.closeParenthese = False
        self.closeOptionnel = False
        self.afficheFactOptionnel = False
        self.enleverActionStructures = False
        self.enleverPoubellePourCommande = False
        self.enleverParametres = False
        self.enleverSupprimer = False
        self.ajoutExecution = False
        self.utilParExtensions = []
        self.rendVisiblesLesCaches = False
        self.pasDeMCOptionnels = False

        self.dumpXSD = False
        self.withXSD = False
        self.afficheIhm = True

        # self.afficheUQ=False
        self.afficheUQ = True

    # --------------------------------------
    def lectureFichierIniStandard(self):
    # --------------------------------------

        name = "prefs_" + self.appliEficas.code
        try:
            prefsCode = __import__(name)
        except:
            self.catalogues = []
            print("pas de fichier de prefs")
            return
        for k in dir(prefsCode):
            if k[0:1] != "__" and k[-1:-2] != "__":
                valeur = getattr(prefsCode, k)
                setattr(self, k, valeur)

    # --------------------------------------
    def lectureFichierIniIntegrateur(self):
    # --------------------------------------
        # Verifie l'existence du fichier "standard"
        # appelle la lecture de ce fichier
        clef = "PREFS_CATA_" + self.code
        try:
            repIntegrateur = os.path.abspath(os.environ[clef])
        except:
            return

        fic_ini_integrateur = os.path.join(repIntegrateur, self.name)
        if not os.path.isfile(fic_ini_integrateur):
            return
        with open(fic_ini_integrateur) as fd:
            txt = fd.read()
        d = locals()
        try:
            exec(txt, d)
        except:
            try:
                from PyQt5.QtWidgets import QMessageBox

                QMessageBox.critical(
                    None,
                    tr("Import du fichier de Configuration"),
                    tr(
                        "Erreur a la lecture du fichier de configuration %s ",
                        str(fic_ini_integrateur),
                    ),
                )
            except:
                print(
                    "Erreur a la lecture du fichier de configuration %s ",
                    str(fic_ini_integrateur),
                )
            return
        self.labels_eficas.append("rep_aide")
        for k in self.labels_eficas:
            try:
                setattr(self, k, d[k])
            except:
                pass
        # Glut pour les repertoires materiaux
        # et pour la doc
        for k in d:
            if (k[0:8] == "rep_mat_") or (k[0:8] == "rep_doc_"):
                setattr(self, k, d[k])

    # --------------------------------------
    def lectureFichierIniUtilisateur(self):
    # --------------------------------------
        # Surcharge les parametres standards par les parametres utilisateur s'ils existent
        self.fic_ini_utilisateur = os.path.join(self.rep_user, self.name)
        if not os.path.isfile(self.fic_ini_utilisateur):
            return
        with open(fic_ini_utilisateur) as fd:
            txt = fd.read()
        d = locals()
        try:
            exec(txt, d)
        except:
            l = traceback.format_exception(
                sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
            )
            try:
                from PyQt5.QtWidgets import QMessageBox

                QMessageBox.critical(
                    None,
                    tr("Import du fichier de Configuration"),
                    tr(
                        "Erreur a la lecture du fichier de configuration %s ",
                        str(fic_ini_integrateur),
                    ),
                )
            except:
                print(
                    "Erreur a la lecture du fichier de configuration %s ",
                    str(fic_ini_integrateur),
                )
        for k in self.labels_user:
            try:
                setattr(self, k, d[k])
            except:
                pass
        for k in d:
            if (k[0:8] == "rep_mat_") or (k[0:8] == "rep_doc_"):
                setattr(self, k, d[k])

    # --------------------------------------
    def saveParams(self):
    # --------------------------------------
        # sauvegarde
        # les nouveaux parametres dans le fichier de configuration utilisateur
        #
        texte = ""
        for clef in self.labels_user:
            if hasattr(self, clef):
                valeur = getattr(self, clef)
                texte = texte + clef + "      = " + repr(valeur) + "\n"
        # Glut pour les repertoires materiaux
        # et pour la doc
        for k in dir(self):
            if (k[0:8] == "rep_mat_") or (k[0:8] == "rep_doc_"):
                valeur = getattr(self, k)
                texte = texte + k + " = " + repr(valeur) + "\n"

        f = open(self.fic_ini_utilisateur, "w+")
        f.write(texte)
        f.close()


#


def makeConfig(appliEficas, rep):
    return configBase(appliEficas, rep)

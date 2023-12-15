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
    # -----------------------------
    def __init__(self, appliEficas):
    # -----------------------------
        """
         Classe de base permettant de  lire les fichiers de preference 
             1) de l installation eficas  : prefs.py (ou prefs_salome.py) dans
                la directory du catalogue
             2) contenu dans la variable d environnement : ${PREFS_CATA_$CODE}
             Cela permet d avoir une installation partagée d Eficas avec une possibilité de 
             moduler les préférences selon les machines
             3)le(s) fichier(s) de preference utilisateurs : 
             prefs_code.ini ou pref_salome_code.ini 
             contenu dans la directory $HOME/.config/Eficas/code
                        
         Cette classe peut etre surchargee dans le fichier configuration_code.py
         dans la directory qui contient le catalogue
        """

        self.appliEficas = appliEficas
        self.code = appliEficas.code
        if self.code == None: return
        self.salome = appliEficas.salome

        if self.salome: name = "prefs_eficas_salome.ini"
        else: name = "prefs_eficas.ini"
        if sys.platform == 'linux' : repUser = os.path.join( os.path.expanduser("~"))
        else : repUser = os.path.join('C:/','.config/Eficas',self.code)
        self.fichierPrefsUtilisateur = os.path.join(repUser, name)

        self.labelsEficas = ('PdfReader', 'saveDir', 'modeNouvCommande', 'afficheUQ', 'closeAutreCommande', 'closeFrameRechercheCommande', 
           'closeFrameRechercheCommandeSurPageDesCommandes', 'closeEntete', 'closeArbre', 'demandeLangue', 'suiteTelemac', 
           'nombreDeBoutonParLigne', 'translatorFichier', 'dicoImages', 'dicoIcones', 'afficheCommandesPliees', 'afficheFirstPlies', 
           'simpleClic', 'afficheOptionnelVide', 'afficheListesPliees', 'boutonDsMenuBar', 'ficIcones', 
           'repIcones', 'differencieSiDefaut', 'typeDeCata', 'closeParenthese', 'closeOptionnel', 
           'afficheFactOptionnel', 'enleverActionStructures', 'enleverPoubellePourCommande', 'enleverParametres',
           'enleverSupprimer', 'ajoutExecution', 'utilParExtensions', 'rendVisiblesLesCaches',
           'pasDeMCOptionnels', 'dumpXSD', 'withXSD', 'afficheIhm', 'catalogues' )

        self.labelsUser = ('PdfReader', 'saveDir', ' closeArbre', 'demandeLangue', 
           'nombreDeBoutonParLigne', 'translatorFichier', 'afficheCommandesPliees', 'afficheFirstPlies',
           'simpleClic', 'afficheOptionnelVide', 'afficheListesPliees', 'differencieSiDefaut') 


        self.setValeursParDefaut()

        if self.code != "":
            self.lectureFichierIniStandard()
            self.lectureFichierIniIntegrateur()
            self.lectureFichierIniUtilisateur()

        # coherence des parametres -)
        if self.boutonDsMenuBar:
            self.closeAutreCommande = True
            self.closeFrameRechercheCommande = True

        if not os.path.isdir(self.saveDir):
            if sys.platform == 'linux' :
               self.saveDir = os.path.join( os.path.expanduser("~"), 'Eficas', self.code)
            else :
               self.saveDir = os.path.join('C:/','Eficas',self.code)

    def setValeursParDefaut(self):
    # ----------------------------

        # Valeurs par defaut
        self.pathDoc = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","Doc"))
        self.PedfReader = "acroread"
        nomDir = "Eficas_" + self.code
        self.saveDir = os.path.abspath(os.path.join(os.path.expanduser("~"), nomDir))
        self.modeNouvCommande = "ini"
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
        self.afficheUQ = True

        # pour garder ce qui existait pour Aster
        self.repMat = None

    # --------------------------------------
    def lectureFichierIniStandard(self):
    # --------------------------------------

        if self.salome : name = "prefs_salome_" + self.appliEficas.code
        else : name = "prefs_" + self.appliEficas.code
        if self.appliEficas.fichierCata != None :
            dirCata=os.path.dirname(self.appliEficas.fichierCata)
            sys.path.append(os.path.abspath(dirCata))
            self.appliEficas.listePathAEnlever.append(dirCata)
        try:
            prefsCode = __import__(name)
        except:
            self.catalogues = []
            print("pas de fichier de prefs")
            return
        for k in dir(prefsCode):
            if k in self.labelsEficas:
                valeur=getattr(prefsCode,k)
                setattr(self,k,valeur)

    # --------------------------------------
    def lectureFichierIniIntegrateur(self):
    # --------------------------------------
        # Verifie l'existence du fichier "standard"
        # appelle la lecture de ce fichier
        clef = "PREFS_CATA_" + self.code
        if clef in os.environ.keys(): fic = os.environ[clef]
        else : return
        fichierPrefsIntegrateur = os.path.abspath(fic)
        if not os.path.isfile(fichierPrefsIntegrateur): return
        try : 
            with open(fichierPrefsIntegrateur) as fd: txt = fd.read()
        except:
            titre = tr("Import du fichier de Configuration")
            texte = "Erreur a la lecture du fichier de configuration {} ".format(str(fichierPrefsIntegrateur))
            self.appliEficas.afficheMessage(titre, texte)
            return
        d = {}
        try:
            exec(txt, d)
        except:
            titre = tr("Import du fichier de Configuration")
            texte = "Erreur a la l execution du fichier de configuration {} ".format(str(fichierPrefsIntegrateur))
            self.appliEficas.afficheMessage(titre, texte)
            return

        for k in d:
            if k in self.labelsEficas:
                try:
                    setattr(self, k, d[k])
                except:
                    pass

    # --------------------------------------
    def lectureFichierIniUtilisateur(self):
    # --------------------------------------
        # Surcharge les parametres standards par les parametres utilisateur s'ils existent
        if not os.path.isfile(self.fichierPrefsUtilisateur): return
        try :
            with open(self.fichierPrefsUtilisateur) as fd: txt = fd.read()
        except:
            titre = tr("Import du fichier de Configuration"),
            texte = "Erreur a la lecture du fichier de configuration {} ".format(str(fichierPrefsUtilisateur))
            self.appliEficas.afficheMessage(titre, texte)
            return
        d = {}
        try:
            exec(txt, d)
        except:
            titre = tr("Import du fichier de Configuration"),
            texte = "Erreur a la l execution du fichier de configuration {} ".format(str(fichierPrefsUtilisateur))
            self.appliEficas.afficheMessage(titre, texte)
            return
        for k in d:
            if k in self.labelsUser:
                try:
                    setattr(self, k, d[k])
                except:
                    pass

    # --------------------------------------
    def saveParams(self):
    # --------------------------------------
        # sauvegarde
        # les nouveaux parametres dans le fichier de configuration utilisateur
        #
        texte = ""
        for clef in self.labelsUser:
            if hasattr(self, clef):
                valeur = getattr(self, clef)
                texte = texte + clef + "      = " + repr(valeur) + "\n"
        f = open(self.fichierPrefsUtilisateur, "w+")
        f.write(texte)
        f.close()


def makeConfig(appliEficas):
    return configBase(appliEficas)

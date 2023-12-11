# -*- coding: iso-8859-1 -*-
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
import os, sys

from Extensions.eficas_exception import EficasException
from Extensions import param2
from InterfaceGUI.getVersion import getEficasVersion
from viewManagerSsIhm import MyViewManagerSsIhm
from Editeur import session


class AppliSsIhm:
    """
    Class implementing the main user interface.
    """

    def __init__(
        self,
        code=None,
        salome=1,
        parent=None,
        multi=False,
        langue="fr",
        ssIhm=True,
        labelCode=None,
        genereXSD=False,
        versionCode=None,
        ssCode=None,
        fichierCata=None,
        GUIDir=None,
    ):
        """
        Constructor
        """
        version = getEficasVersion()
        self.VERSION_EFICAS = "Eficas QT5 Salome " + version
        self.labelCode = labelCode
        if not GUIDir:
            self.GUIDir = "InterfaceQT4"
        else:
            self.GUIDir = GUIDir

        self.salome = salome
        self.ssIhm = True
        self.code = code
        self.genereXSD = genereXSD
        self.versionCode = versionCode
        self.ssCode = ssCode

        self.dict_reels = {}
        self.fichierIn = None
        self.fichierOut = None

        self.recent = []
        self.ficRecents = {}
        self.mesScripts = {}
        self.listeAEnlever = []
        self.ListePathCode = [
            "Adao",
            "ADAO",
            "Carmel3D",
            "Telemac",
            "CF",
            "MAP",
            "ZCracks",
            "SEP",
            "SPECA",
            "PSEN_Eficas",
            "PSEN_N1",
        ]
        self.listeCode = [
            "Adao",
            "ADAO",
            "Carmel3D",
            "Telemac",
            "CF",
            "MAP",
            "ZCracks",
            "SEP",
            "SPECA",
            "PSEN_Eficas",
            "PSEN_N1",
        ]
        self.repIcon = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "Editeur", "icons"
        )

        if fichierCata == None:
            self.fichierCata = session.d_env.fichierCata
        else:
            self.fichierCata = fichierCata
        if session.d_env.labelCode:
            self.labelCode = session.d_env.labelCode
        self.withXSD = session.d_env.withXSD

        if self.salome:
            try:
                from Accas import eficasSalome
                Accas.SalomeEntry = eficasSalome.SalomeEntry
            except:
                print("eficas hors salome")

        self.multi = multi
        if self.multi:
            print("pas de multi sans ihm")

        if langue == "fr":
            self.langue = langue
        else:
            self.langue = "ang"

        if self.multi == False:
            self.definitCode(code, ssCode)
            if code == None:
                return

        self.suiteTelemac = False
        self.viewmanager = MyViewManagerSsIhm(self)
        self.withUQ = False

    def ajoutUQ(self):
        self.withUQ = True
        self.formatFichierIn = "pythonUQ"  # par defaut

    def definitCode(self, code, ssCode):
        self.code = code
        self.ssCode = ssCode
        if self.code == None:
            return  # pour le cancel de la fenetre choix code

        try:
            name = "prefs_" + self.code
            prefsCode = __import__(name)
            self.repIni = prefsCode.repIni
        except:
            self.repIni = os.path.dirname(os.path.abspath(__file__))

        if ssCode != None:
            self.formatFichierOut = ssCode  # par defaut
            prefsCode.NAME_SCHEME = ssCode
        else:
            self.formatFichierIn = "python"  # par defaut
            self.formatFichierOut = "python"  # par defaut

        nameConf = "configuration_" + self.code
        try:
            configuration = __import__(nameConf)
            self.maConfiguration = configuration.make_config(self, self.repIni)
        except:
            from InterfaceQT4.configuration import makeConfig

            # self.maConfiguration = configuration.makeConfig(self,prefsCode.repIni)
            self.maConfiguration = makeConfig(self, self.repIni)

        if hasattr(self, "maConfiguration") and self.maConfiguration.translatorFichier:
            from Extensions import localisation

            localisation.localise(
                None,
                self.langue,
                translatorFichier=self.maConfiguration.translatorFichier,
            )
        if self.withXSD:
            self.maConfiguration.withXSD = True

    def getSource(self, file):
        # appele par Editeur/session.py
        import convert

        p = convert.plugins["python"]()
        p.readfile(file)
        texte = p.convert("execnoparseur")
        return texte

    def initEditor(self, fichier=None, jdc=None, units=None, include=0):
        if (hasattr(self, "editor")) and self.editor != None:
            print("un seul editeur par application")
            sys.exit()
        self.editor = self.viewmanager.getNewEditorNormal()

    def initEditorNormal(self, fichier=None, jdc=None, units=None, include=0):
        if (hasattr(self, "editor")) and self.editor != None:
            print("un seul editeur par application")
            sys.Exit()
        # self.editor = JDCEditorSsIhm(self,fichier, jdc, self.myQtab,units=units,include=include)
        self.editor = self.viewmanager.getNewEditorNormal()

    def fileNew(self):
        self.editor = self.initEditor()

    def getEditor(self):
        if (hasattr(self, "editor")) and self.editor != None:
            return self.editor
        self.initEditor()
        return self.editor

    def fileOpen(self, fichier):
        fichierIn = os.path.abspath(fichier)
        try:
            monEditor = self.viewmanager.handleOpen(fichierIn)
        except EficasException as exc:
            print("poum")
            monEditor = None
        return monEditor

    def fileSave(self):
        if self.editor == None:
            return False
        ok, newName = editor.saveFileAs()
        print("ok, newName ", ok, newName)

    def fileSaveAs(self, fileName):
        if self.editor == None:
            return False
        ok = editor.saveFileAs()
        print("ok ", ok)

    def dumpXsd(self, avecEltAbstrait=False):
        currentCata = CONTEXT.getCurrentCata()
        texteXSD = currentCata.dumpXsd(avecEltAbstrait)
        return texteXSD
        # if self.maConfiguration.afficheIhm==False : exit()
        # else : return texteXSD


# ,self.fileSaveAs
# ,self.fileClose
# ,self.fileExit
# ,self.jdcRapport
# ,self.jdcRegles
# ,self.jdcFichierSource
# ,self.visuJdcPy


if __name__ == "__main__":
    # Modules Eficas
    monEficas = AppliSsIhm(code="Adao", salome=0, labelCode="V83")

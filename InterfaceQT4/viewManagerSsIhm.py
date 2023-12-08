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



try:
    from builtins import str
    from builtins import object
except:
    pass

import os
from Extensions.i18n import tr


# --------------------------------
class JdcSsIhmHandler(object):
    # --------------------------------
    # retourne a l utilisateur

    def __init__(self, viewManager):
        #  --------------------------------------
        self.viewManagerSsIhm = viewManager

    def viewJdcPy(self):
        #  ---------------------
        self.viewManagerSsIhm.handleViewJdcPy(self)

    def viewJdcSource(self):
        #  ---------------------
        self.viewManagerSsIhm.handleViewJdcSource(self)

    def getFileName(self):
        #  ---------------------
        self.viewManagerSsIhm.getFileName(self)

    def viewJdcRapport(self):
        #  ---------------------
        self.viewManagerSsIhm.handleViewJdcRapport(self)

    def getJdcRapport(self):
        #  ---------------------
        return self.viewManagerSsIhm.handleGetJdcRapport(self)

    def getDicoPython(self):
        #  -------------------------
        return self.viewManagerSsIhm.generDico(self)

    def isJdcValid(self):
        #  -------------------------
        return self.viewManagerSsIhm.isJdcValid(self)

    def fileSaveAs(self, fileName):
        #  -------------------------
        return self.viewManagerSsIhm.fileSaveAs(self, fileName)

    def fileLegerSaveAs(self, fileName):
        #  -----------------------------------
        return self.viewManagerSsIhm.fileLegerSaveAs(self, fileName)

    def handleSortieUQ(self, fileName):
        #  -----------------------------------
        return self.viewManagerSsIhm.handleSortieUQ(self, fileName)

    def handleExeUQ(self, fileName):
        #  -----------------------------------
        # est-ce que cela a un sens de faire l exe hors IHM ?
        return self.viewManagerSsIhm.handleExeUQ(self, fileName)


# --------------------------------
class MyViewManagerSsIhm(object):
    # --------------------------------
    # Symetrique de ViewManager mais pas d heritage entre les 2
    # dans le viewManager pas de souci pour savoir qui est le jdc sur lequel on travaille
    # ici en revanche.... c est moins sur . voir avec le fichier

    #  --------------------------------
    def __init__(self, appliEficas):
        #  --------------------------------
        self.appliEficas = appliEficas
        self.tabWidgets = []
        self.mesIndexes = {}
        self.dictEditors = {}
        self.untitledCount = 0
        self.doubles = {}

    #  ------------------------------------------------------
    def handleOpen(self, fichier=None, units=None):
        #  ------------------------------------------------------
        result = None
        if fichier is None:
            print("nom de fichier obligatoire")
            return None

        for handler in self.dictEditors:
            editor = self.dictEditors[handler]
            if self.samePath(fichier, editor.getFileName()):
                print("fichier deja ouvert . pas de nouvel editor")
                return handler

        monNewHandler = self.getNewEditor(fichier, units)
        return monNewHandler

    #  ----------------------------------------------------------------------
    def getNewEditor(self, fichier=None, jdc=None, units=None, include=0):
        #  ----------------------------------------------------------------------
        # il faudrait decider entre e handler ou non
        # le cas d usage n est pas tout a fait identique  :
        # avec handler pour les utilisateurs avance
        # sans pour les utilisateurs encore plus ancvances et les tests

        from InterfaceQT4.editorSsIhm import JDCEditorSsIhm

        editor = JDCEditorSsIhm(
            self.appliEficas, fichier, jdc, units=units, include=include
        )

        if editor.jdc:  # le fichier est bien un jdc
            monHandler = JdcSsIhmHandler(self)
            self.dictEditors[monHandler] = editor
            return monHandler
        else:
            print("impossible de construire le jdc")
            return None

    #  --------------------------------------------------------------------------------
    def getNewEditorNormal(self, fichier=None, jdc=None, units=None, include=0):
        #  --------------------------------------------------------------------------------

        from InterfaceQT4.editorSsIhm import JDCEditorSsIhm

        editor = JDCEditorSsIhm(
            self.appliEficas, fichier, jdc, units=units, include=include
        )
        self.editor = editor
        return editor

    #  -----------------------------
    def samePath(self, f1, f2):
        #  ------------------------------
        """
        compare two paths.
        """
        if f1 is None or f2 is None:
            return 0
        if os.path.normcase(os.path.normpath(f1)) == os.path.normcase(
            os.path.normpath(f2)
        ):
            return 1
        return 0

    #  ---------------------------------
    def handleViewJdcPy(self, handler):
        #  ---------------------------------
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        self.dictEditors[handler].viewJdcPy()

    #  ---------------------------------
    def getFileName(self, handler):
        #  ---------------------------------
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        return self.dictEditors[handler].getFileName()

    #  ---------------------------------------------
    def handleViewJdcSource(self, handler):
        #  ---------------------------------------------
        print(handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        self.dictEditors[handler].viewJdcSource()

    #  ---------------------------------------------
    def handleViewJdcRapport(self, handler):
        #  ---------------------------------------------
        print(handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        self.dictEditors[handler].viewJdcRapport()

    #  ---------------------------------------------
    def handleGetJdcRapport(self, handler):
        #  ---------------------------------------------
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        return self.dictEditors[handler].getJdcRapport()

    #  ---------------------------------------------
    def handleViewJdcRapport(self, handler):
        #  ---------------------------------------------
        print(handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        self.dictEditors[handler].viewJdcRapport()

    #  ---------------------------------------------
    def generDico(self, handler):
        #  ---------------------------------------------
        print(handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        return self.dictEditors[handler].generDico()

    #  ---------------------------------------------
    def isJdcValid(self, handler):
        #  ---------------------------------------------
        print(handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        return self.dictEditors[handler].jdc.isValid()

    #  ---------------------------------------------
    def fileSaveAs(self, handler, fileName):
        #  ---------------------------------------------
        print(handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        return self.dictEditors[handler].saveFile(fileName)

    #  ---------------------------------------------
    def fileLegerSaveAs(self, handler, fileName):
        #  ---------------------------------------------
        #        print (handler)
        if not (handler in self.dictEditors):
            print("editor non trouve")
            return
        self.dictEditors[handler].saveFileLegerAs(fileName)

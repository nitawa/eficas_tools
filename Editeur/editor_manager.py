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

import os
from uuid import uuid1

# --------------------------
class EditorManager(object):
# --------------------------
    """
    classe mere des managers d editeur pour Qt et le web
    permettent de gerer plusieurs ouvertures de fichiers simultannees en IHM
    utilisee sans etre derivee pour le dumpXSD ou les transformations 
    """
    # remplace par l index du viewManager 

    # --------------------------------
    def __init__(self, appliEficas):
    # --------------------------------
        self.appliEficas = appliEficas
        self.mesIndexes = {}
        self.dictEditors = {}
        self.editors = []
        self.doubles = {}


    # ----------------------------------------------------------------
    def getEditor(self, fichier=None, jdc=None, units=None, include=0):
    # ----------------------------------------------------------------
        """
          Retourne un nouvel editeur ou None si doublon 
        """

        if fichier == None :
            self.appliEficas.afficheMessage('Eficas sans Ihm', 
                 'nom de fichier obligatoire pour obtenir un editor')
            return None
        for indexEditor in self.dictEditors:
            editor = self.dictEditors[indexEditor]
            if self.samePath(fichier, editor.getFileName()):
               self.appliEficas.afficheMessage('Eficas sans Ihm', 'Fichier deja ouvert')
               return None
        from Editeur.editor import Editor
        editor = Editor(self.appliEficas, fichier, jdc, units, include)
        if not editor.jdc :
            self.appliEficas.afficheMessage('Eficas sans Ihm', 'impossible d allouer un editor')
            return None
        self.editors.append(editor)
        idEditor = uuid1().hex
        self.dictEditors[idEditor] = editor
        editor.idEditor = idEditor
        return editor

    # ------------------------
    def getEditorById(self,id):
    # ------------------------
        if id in self.dictEditors:
            editor = self.dictEditors[indexEditor]
            return editor
        return None

    # --------------------------------
    def setCurrentEditorById(self,id):
    # --------------------------------
        print ('a Programmer')
        return True
      

    # -------------------------
    def samePath(self, f1, f2):
    # --------------------------
        """
        compare two paths.
        """
        if f1 is None or f2 is None: return 0
        if os.path.normcase(os.path.normpath(f1)) == os.path.normcase( os.path.normpath(f2)):
            return 1
        return 0

    #-------------------------------
    def indexChanged(self, newIndex):
    #--------------------------------
        if newIndex in self.dictEditors:
            editor = self.dictEditors[newIndex]
            if editor.jdc != None:
                CONTEXT.unsetCurrentJdC()
                CONTEXT.setCurrentJdC(editor.jdc)
            self.appliEficas.maConfiguration = editor.maConfiguration
            self.appliEficas.code = editor.maConfiguration.code
            self.appliEficas.setWindowTitle(editor.titre)
            self.appliEficas.construitMenu()
            return 1
        else :
            return 0


    # -----------------------------
    def getFileName(self, index):
    # -------------------------------
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        return self.dictEditors[index].getFileName()


    # ---------------------------------------------
    def handleGetJdcRapport(self, index):
    # ---------------------------------------------
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        return self.dictEditors[index].getJdcRapport()

    # ---------------------------------------------
    def handleViewJdcRapport(self, index):
    # ---------------------------------------------
        # print(index)
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        self.dictEditors[index].viewJdcRapport()

    # ---------------------------------------------
    def generDico(self, index):
    # ---------------------------------------------
        # print(index)
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        return self.dictEditors[index].generDico()

    # ---------------------------------------------
    def isJdcValid(self, index):
    # ---------------------------------------------
        # print(index)
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        return self.dictEditors[index].jdc.isValid()

    # ---------------------------------------------
    def fileSaveAs(self, index, fileName):
    # ---------------------------------------------
        # print(index)
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        return self.dictEditors[index].saveFile(fileName)

    # ---------------------------------------------
    def fileLegerSaveAs(self, index, fileName):
    # ---------------------------------------------
    #      print (index)
        if not (index in self.dictEditors):
            # print("editor non trouve")
            return
        self.dictEditors[index].saveFileLegerAs(fileName)





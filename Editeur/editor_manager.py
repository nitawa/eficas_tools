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
from multiprocessing import Lock

debug = 1
# --------------------------
class EditorManager(object):
# --------------------------
    """
    classe mere du manager d editeur pour Qt 
    permet de gerer plusieurs ouvertures de fichiers simultannees en Web ou TUI
    utilisee sans etre derivee  dans ces 2 cas
    """
    # remplace par l index du viewManager 

    # --------------------------------
    def __init__(self, appliEficas):
    # --------------------------------
        self.appliEficas = appliEficas
        self.mesIndexes = {}
        self.editors = []
        self.doubles = {}
        self.lock = Lock()
        self.dictEditors = {}
    # TODO : doit on prevoir l inverse ? a t on besoin pour une session de connaitre tous ces editeurs
    # reflechir au close
    # TODO


    # -----------------------------------------------------
    def getEditor(self, fichier=None, jdc=None, include=0):
    # ------------------------------------------------------
        """
          Retourne un nouvel editeur ou None si doublon 
        """
        # TODO : reflechir
        print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print ('getEditor dans editor : pas programme --> derive en QT, utiliser getTUIEditor ou getWebEditor')
        print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return None

    # ----------------------------------------------------------------------------------------
    def getTUIEditor(self,sId = None, cataFile = None, dataSetFile=None, jdc=None, include=0):
    # -----------------------------------------------------------------------------------------
        """
          Retourne un nouvel editeur ou None si doublon
        """
        if cataFile == None :
            self.appliEficas.afficheMessage(sId, 'Eficas',
                 'nom de catalogue obligatoire pour obtenir un editor')
            return (None, 1, 'nom de catalogue obligatoire pour obtenir un editor')
        with self.lock :
            for editor in self.dictEditors.values():
                if self.samePath(dataSetFile, editor.getDataSetFileName()) and self.samePath(cataFile, editor.getCataFileName()):
                    break
            else:
                from editor import Editor
                editor = WebEditor(self.appliEficas, cataFile, dataSetFile)

            if editor.jdc:  # le fichier est bien un jdc
                self.dictEditors[editor.editorId]=editor
                self.editors.append(editor)
                if  editor.editorId in self.appliEficas.dictEditorIdSessionId :
                   self.appliEficas.dictEditorIdSessionId[editor.editorId].append(sId)
                else :
                   self.appliEficas.dictEditorIdSessionId[editor.editorId]=[sId,]
            else:
                return (None, 1, 'impossible d allouer l editor')

    # ----------------------------------------------------------------------------------------
    def getWebEditor(self,sId = None, cataFile = None, dataSetFile=None, jdc=None, include=0):
    # -----------------------------------------------------------------------------------------
        """
          Retourne un nouvel editeur ou None si doublon
        """
        if cataFile == None :
            self.appliEficas.afficheMessage(sId, 'Eficas',
                 'nom de catalogue obligatoire pour obtenir un editor')
            return (None, 1, 'nom de catalogue obligatoire pour obtenir un editor')
        with self.lock :
            for editor in self.dictEditors.values():
                if self.samePath(dataSetFile, editor.getDataSetFileName()) and self.samePath(cataFile, editor.getCataFileName()):
                    break
            else:
                from InterfaceGUI.Web.web_editor import WebEditor
                editor = WebEditor(self.appliEficas, cataFile, dataSetFile)

            if editor.jdc:  # le fichier est bien un jdc
                self.dictEditors[editor.editorId]=editor
                self.editors.append(editor)
                if  editor.editorId in self.appliEficas.dictEditorIdSessionId :
                   self.appliEficas.dictEditorIdSessionId[editor.editorId].append(sId)
                else :
                   self.appliEficas.dictEditorIdSessionId[editor.editorId]=[sId,]
            else:
                return (None, 1, 'impossible d allouer l editor')
            return (editor, 0, '')


    # --------------------------
    def getEditorById(self, eId):
    # ---------------------------
        debug = 1
        if eId in self.dictEditors:
           return (self.dictEditors[eId], 0, "")
        if debug : print ("getEditorById : {} non trouve ".format(eId))
        return (None, 1, "getEditorById : {} non trouve ".format(eId))
 

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
    # cette fonction n a de sens qu en QT ou ?
    # comment gerer le contexte?
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


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
from Accas.extensions.eficas_translation import tr
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo

Dictextensions = {"MAP": ".map"}

#------------------------#
class ViewManager(object):
#------------------------#
    def __init__(self, appliEficas):
    #--------------------------------
        self.appliEficas = appliEficas
        self.tabWidgets = []
        self.mesIndexes = {}
        self.appliEficas = appliEficas
        self.editors = []
        self.dictEditors = {}
        self.untitledCount = 0
        self.doubles = {}

        self.myQtab = self.appliEficas.myQtab

        self.myQtab.currentChanged.connect(self.indexChanged)
        self.myQtab.tabCloseRequested.connect(self.closeTab)

    def indexChanged(self):
    #----------------------
        index = self.myQtab.currentIndex()
        if index in self.dictEditors:
            editor = self.dictEditors[index]
            if editor.jdc != None:
                CONTEXT.unsetCurrentJdC()
                CONTEXT.setCurrentJdC(editor.jdc)
            self.appliEficas.maConfiguration = editor.maConfiguration
            self.appliEficas.code = editor.maConfiguration.code
            self.appliEficas.setWindowTitle(editor.titre)
            self.appliEficas.construitMenu()

    def handleOpen(self, fichier=None, patron=0, units=None):
    #--------------------------------------------------------
        result = None
        if fichier is None:
            if self.appliEficas.demande == True:
                self.appliEficas.definitCode(None, None)
                if self.appliEficas.code == None:
                    return

            if self.appliEficas.code in Dictextensions:
                chaine = "JDC (*" + Dictextensions[self.appliEficas.code] + ");;"
                extensions = tr(chaine + "All Files (*)")
            elif self.appliEficas.code == "TELEMAC":
                extensions = tr("CAS (*.cas);;All Files (*)")
            else:
                extensions = tr("Fichiers JDC (*.comm);;" "Tous les Fichiers (*)")

            fichier = QFileDialog.getOpenFileName(
                self.appliEficas,
                tr("Ouvrir Fichier"),
                self.appliEficas.maConfiguration.saveDir,
                extensions,
            )
            fichier = fichier[0]
        if len(fichier) == 0:
            return None
        fichier = os.path.abspath(fichier)
        ulfile = os.path.abspath(fichier)
        self.appliEficas.maConfiguration.saveDir = os.path.split(ulfile)[0]
        self.appliEficas.addToRecentList(fichier)
        maPage = self.getEditor(fichier, units=units)
        if maPage:
            result = maPage
        if maPage:
            self.myQtab.setTabText(
                self.myQtab.indexOf(maPage), os.path.basename(fichier)
            )
        return result

    def closeTab(self, indexAFermer):
    #--------------------------------
        self.handleClose(indexAFermer=indexAFermer)

    def handleClose(self, doitSauverRecent=1, texte=tr("&Quitter"), indexAFermer=None):
    #----------------------------------------------------------------------------------
        if doitSauverRecent:
            self.appliEficas.sauveRecents()
        if indexAFermer == None:
            index = self.myQtab.currentIndex()
        else:
            index = indexAFermer
        if index < 0:
            return
        res = self.checkDirty(self.dictEditors[index], texte)
        if res == 2:
            return 2  # l utilisateur a annule
        idx = index
        while idx < len(self.dictEditors) - 1:
            self.dictEditors[idx] = self.dictEditors[idx + 1]
            idx = idx + 1
        del self.dictEditors[len(self.dictEditors) - 1]
        try:
            del self.doubles[self.dictEditors[index]]
        except:
            pass
        self.myQtab.removeTab(index)
        return res

    def run(self):
    #-------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.run()

    def saveRun(self):
    #------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.saveRun()

    def handleCloseAll(self, texte=tr("Quitter")):
    #---------------------------------------------
        res = 0
        self.appliEficas.sauveRecents()
        while len(self.dictEditors) > 0:
            self.myQtab.setCurrentIndex(0)
            res = self.handleClose(0, texte)
            if res == 2:
                return res  # l utilsateur a annule
        return res

    def handleRechercher(self):
    #--------------------------
        # print "passage dans handleRechercher"
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleRechercher()

    def handleRechercherDsCatalogue(self):
    #-------------------------------------
        # print "passage dans handleRechercher"
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleRechercherDsCatalogue()

    def handleDeplier(self):
    #-----------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleDeplier()

    def handleEditCopy(self):
    #------------------------
        # print "passage dans handleEditCopy"
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleEditCopy()

    def handleEditCut(self):
    #-----------------------
        # print "passage dans handleEditCut"
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleEditCut()

    def handleEditPaste(self):
    #-------------------------
        # print "passage dans handleEditPaste"
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleEditPaste()

    def handleSupprimer(self):
    #-------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleSupprimer()

    def handleAjoutEtape(self, nomEtape):
    #------------------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleAjoutEtape(nomEtape)

    def newEditor(self, include=0):
    #------------------------------
        if self.appliEficas.demande == True:
            self.appliEficas.definitCode(None, None)
            if self.appliEficas.code == None:
                return
        maPage = self.getEditor(include=include)

    def newIncludeEditor(self):
    #--------------------------
        self.newEditor(include=1)

    def handleViewJdcFichierSource(self):
    #------------------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        self.dictEditors[index].viewJdcSource()

    def ouvreArbre(self):
    #--------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        self.dictEditors[index].ouvreArbre()

    def fermeArbre(self):
    #--------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        self.dictEditors[index].fermeArbre()

    def ajoutCommentaire(self):
    #--------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.ajoutCommentaire()

    def handleViewJdcRegles(self):
    #-----------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        self.dictEditors[index].viewJdcRegles()

    def handleGestionParam(self):
    #----------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            QMessageBox.warning(
                self.appliEficas,
                tr("Creation Parametre indisponible"),
                tr("les parametres sont lies a un jeu de donnees"),
            )
            return
        self.dictEditors[index].gestionParam()

    def handleViewJdcRapport(self):
    #------------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        self.dictEditors[index].viewJdcRapport()

    def handleViewJdcPy(self):
    #-------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        self.dictEditors[index].viewJdcPy()

    def handleSave(self):
    #--------------------
        index = self.myQtab.currentIndex()
        if index < 0: return
        editor = self.dictEditors[index]
        if editor in self.doubles:
            QMessageBox.warning(
                None,
                tr("Fichier Duplique"),
                tr("Le fichier ne sera pas sauvegarde."),
            )
            return
        ok, newName = editor.saveFile()
        if ok:
            fileName = os.path.basename(newName)
            self.myQtab.setTabText(index, fileName)
        return ok

    def handleSortieUQ(self):
    #------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        ok, newName = editor.saveUQFile()
        return ok

    def handleSauvePourPersalys(self):
    #---------------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        ok = editor.sauvePourPersalys()
        return ok

    def handleExeUQ(self):
    #---------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        ok = editor.exeUQ()
        return ok

    def handleSaveLigne(self):
    #-------------------------
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        ok, newName = editor.saveLigneFile()
        return ok

    def handleSaveAs(self):
    #----------------------
        index = self.myQtab.currentIndex()
        editor = self.dictEditors[index]
        oldName = editor.fichier
        ok, newName = editor.saveFileAs()
        if ok:
            fileName = os.path.basename(newName)
            self.myQtab.setTabText(index, fileName)
        if editor in self.doubles:
            if oldName != newName:
                del self.doubles[editor]
        return ok

    def displayJDC(self, jdc, fn=None):
    #----------------------------------
        """
        Public slot to display a file in an editor.
        @param fn name of file to be opened
        # insert filename into list of recently opened files
        """
        titre = None
        if fn != None:
            titre = fn.split("/")[-1]
        editor = self.getEditor(fichier=fn, jdc=jdc, include=1)
        self.appliEficas.addToRecentList(editor.getFileName())

    def getEditor(self, fichier=None, jdc=None, units=None, include=0):
    #------------------------------------------------------------------
        newWin = 0
        double = None
        indexEditor = 0
        for indexEditor in self.dictEditors:
            editor = self.dictEditors[indexEditor]
            if self.samePath(fichier, editor.getFileName()):
                msgBox = QMessageBox()
                msgBox.setWindowTitle(tr("Fichier"))
                msgBox.setText(tr("Le fichier <b>%s</b> est deja ouvert", str(fichier)))
                msgBox.addButton(tr("&Duplication"), 0)
                msgBox.addButton(tr("&Abandonner"), 1)
                abort = msgBox.exec_()
                if abort:
                    break
                double = editor
        else:
            from qt_editor import QtEditor
            editor = QtEditor( self.appliEficas, fichier, jdc, self.myQtab, units=units, include=include,)
            if double != None:
                self.doubles[editor] = double
            if editor.jdc:  # le fichier est bien un jdc
                self.editors.append(editor)
                newWin = 1
            else:
                editor.closeIt()

        if newWin:
            self.addView(editor, fichier)
        elif editor.jdc:
            self.myQtab.setCurrentIndex(indexEditor)

        index = self.myQtab.currentIndex()
        if index != -1:
            self.dictEditors[index] = editor
        return editor

    def addView(self, win, fichier=None):
    #------------------------------------
        if fichier is None:
            self.untitledCount += 1
            self.myQtab.addTab(
                win, tr("Fichier non encore nomme") + str(self.untitledCount)
            )
            # self.myQtab.addTab(win, str(self.appliEficas.code))
        else:
            liste = fichier.split("/")
            txt = liste[-1]
            if not QFileInfo(fichier).isWritable():
                txt = "%s (ro)" % txt
            self.myQtab.addTab(win, txt)
        self.myQtab.setCurrentWidget(win)
        self.currentEditor = win
        win.setFocus()

    def getOpenStartDir(self):
    #-------------------------
        # TODO PN --> Les Preferences
        try:
            userDir = os.path.expanduser("~/Eficas_install/")
            return userDir
        except:
            return ""

    def samePath(self, f1, f2):
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

    def checkDirty(self, editor, texte):
        """
        Private method to check dirty status and open a message window.

        @param editor editor window to check
        @return flag indicating successful reset of the dirty flag (boolean)
        """
        res = 1
        if (editor.modified) and (editor in self.doubles):
            msgBox = QMessageBox(None)
            msgBox.setWindowTitle(tr("Fichier Duplique"))
            msgBox.setText(tr("Le fichier ne sera pas sauvegarde."))
            msgBox.addButton(texte, 0)
            msgBox.addButton(tr("&Annuler"), 1)
            res = msgBox.exec_()
            if res == 0:
                return 1
            return 2
        if editor.modified:
            fn = editor.getFileName()
            if fn is None:
                fn = tr("Noname")
            msgBox = QMessageBox(None)
            msgBox.setWindowTitle(tr("Fichier Modifie"))
            msgBox.setText(tr("Le fichier ne sera pas sauvegarde."))
            msgBox.addButton(tr("&Sauvegarder"), 1)
            msgBox.addButton(tr("&Quitter sans sauvegarder"), 0)
            msgBox.addButton(tr("&Annuler"), 2)
            res = msgBox.exec_()
            if res == 2:
                return res
            if res == 0 and self.appliEficas.maConfiguration.afficheUQ:
                if fn is None:
                    ret, fichier = editor.saveUQFile(self)
                else:
                    ret, fichier = editor.saveUQFile(self, fn)
                return 2
            if res == 0:
                (ok, newName) = editor.saveFile()
                if ok:
                    fileName = os.path.basename(newName)
                    index = self.myQtab.currentIndex()
                    self.myQtab.setTabText(index, fileName)
                return ok
        return res

    def handleAjoutGroup(self, listeGroup):
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        editor.handleAjoutGroup(listeGroup)

    def handleFonctionUtilisateur(self, laFonctionUtilisateur, lesArguments):
        # Peut-etre a blinder un peu plus sur le nb d argument
        index = self.myQtab.currentIndex()
        if index < 0:
            return
        editor = self.dictEditors[index]
        if editor.getEtapeCourante() == None:
            QMessageBox.information(
                self.appliEficas,
                tr("Selectionner une etape"),
                tr(
                    "Le texte ne peut pas etre insere dans un fichier vide,\nCreer un materiau vide ou une zone vide et inserer le catalogue apres"
                ),
            )
            return

        listeParam = []
        for p in lesArguments:
            if hasattr(editor, p):
                listeParam.append(getattr(editor, p))
            if p == "editor":
                listeParam.append(editor)
            if p == "etapeCourante":
                listeParam.append(editor.getEtapeCourante())
        laFonctionUtilisateur(*listeParam)

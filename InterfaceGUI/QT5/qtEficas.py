#!/usr/bin/env python
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
#pathUi = os.path.abspath(os.path.dirname(__file__), '..', '..', 'UiQT5')
#if not pathUi not in sys.path : sys.path.append(pathUi)

from PyQt5.QtWidgets import ( QApplication, QMainWindow, QGridLayout, QBoxLayout, QMenu, QAction, QMessageBox,)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


from Editeur import session
from UiQT5.myMain import Ui_Eficas
from InterfaceGUI.QT5.viewManager import MyViewManager
from InterfaceGUI.qtEficasSsIhm import AppliSsIhm

from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException
from Extensions import param2


class Appli(AppliSsIhm, Ui_Eficas, QMainWindow):
    """
    Class implementing the main user interface.
    """

    def __init__(
        self,
        code=None,
        salome=1,
        parent=None,
        multi=False,
        langue="en",
        ssIhm=False,
        labelCode=None,
        GUIPath="InterfaceGUI.QT5",
    ):
        """
        Constructor
        """
        if ssIhm == True:
            print("mauvaise utilisation de la classe Appli. Utiliser AppliSsIm SVP")
            exit()

        AppliSsIhm.__init__(
            self,
            code,
            salome,
            parent,
            multi=multi,
            langue=langue,
            ssIhm=True,
            labelCode=labelCode,
        )
        QMainWindow.__init__(self, parent)
        Ui_Eficas.__init__(self)

        self.ssIhm = False
        self.multi = multi
        self.demande = multi  # voir PSEN
        self.GUIPath = GUIPath

        if self.multi == False:
            self.definitCode(code, None)
            if self.code == None:
                return
        else:
            self.definitCode(code, None)
            if self.code == None:
                return

        self.suiteTelemac = False
        if hasattr(self, "maConfiguration"):
            if self.maConfiguration.demandeLangue:
                from InterfaceGUI.QT5.monChoixLangue import MonChoixLangue

                widgetLangue = MonChoixLangue(self)
                ret = widgetLangue.exec_()
            self.suiteTelemac = self.maConfiguration.suiteTelemac

        if (
            not self.salome
            and hasattr(self, "maConfiguration")
            and hasattr(self.maConfiguration, "lang")
        ):
            self.langue = self.maConfiguration.lang
        from Extensions import localisation

        app = QApplication
        if hasattr(self, "maConfiguration"):
            localisation.localise(
                None,
                self.langue,
                translatorFichier=self.maConfiguration.translatorFichier,
            )
        self.setupUi(self)

        # if parent != None : self.parentCentralWidget = parent.centralWidget()
        # else              : self.parentCentralWidget = None

        if not self.salome:
            if hasattr(self, "maConfiguration") and hasattr(
                self.maConfiguration, "taille"
            ):
                self.taille = self.maConfiguration.taille
            else:
                self.taille = 1700

            self.resize(self.taille, self.height())

        icon = QIcon(self.repIcon + "/parametres.png")
        self.actionParametres.setIcon(icon)
        if hasattr(self, "maConfiguration") and self.maConfiguration.boutonDsMenuBar:
            self.frameEntete.setMaximumSize(QSize(16777215, 100))
            self.frameEntete.setMinimumSize(QSize(0, 100))
        if (
            hasattr(self, "maConfiguration")
            and self.maConfiguration.enleverActionStructures
        ):
            self.enleverActionsStructures()
        if hasattr(self, "maConfiguration") and self.maConfiguration.enleverParametres:
            self.enleverParametres()
        if hasattr(self, "maConfiguration") and self.maConfiguration.enleverSupprimer:
            self.enleverSupprimer()

        if hasattr(self, "frameEntete"):
            self.myQtab.removeTab(0)
            self.blEnteteGlob = QBoxLayout(2, self.frameEntete)
            self.blEnteteGlob.setSpacing(0)
            self.blEnteteGlob.setContentsMargins(0, 0, 0, 0)

            self.blEntete = QBoxLayout(0)
            self.blEntete.insertWidget(0, self.toolBar)
            self.blEntete.insertWidget(0, self.menubar)
            self.blEnteteGlob.insertLayout(0, self.blEntete)

        if hasattr(self, "maConfiguration") and self.maConfiguration.boutonDsMenuBar:
            self.blEnteteCommmande = QBoxLayout(0)
            self.blEnteteCommmande.insertWidget(0, self.toolBarCommande)
            self.toolBarCommande.setIconSize(QSize(96, 96))
            self.blEnteteGlob.insertLayout(-1, self.blEnteteCommmande)
        else:
            self.toolBarCommande.close()

        if (
            hasattr(self, "maConfiguration")
            and self.maConfiguration.closeEntete == True
            and self.salome
        ):
            self.closeEntete()

        eficas_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.viewmanager = MyViewManager(self)
        self.recentMenu = QMenu(tr("&Recents"))
        # self.menuFichier.insertMenu(self.actionOuvrir,self.recentMenu)

        # actionARemplacer ne sert que pour l insert Menu
        if hasattr(self, "actionARemplacer"):
            self.menuFichier.insertMenu(self.actionARemplacer, self.recentMenu)
            self.menuFichier.removeAction(self.actionARemplacer)
            self.connecterSignaux()
        self.toolBar.addSeparator()

        if self.code != None:
            self.construitMenu()

        self.setWindowTitle(self.VERSION_EFICAS)
        try:
            # if 1 :
            # print ('attention try devient if 1')
            self.ouvreFichiers()
        except EficasException as exc:
            # except:
            print("je suis dans le except")
            if self.salome == 0:
                exit()

        # self.adjustSize()

    def closeEntete(self):
        self.menuBar().close()
        self.toolBar.close()
        self.frameEntete.close()

    def definitCode(self, code, ssCode):
        self.code = code
        self.ssCode = ssCode
        if self.code == None:
            self.cleanPath()
            from InterfaceGUI.QT5.monChoixCode import MonChoixCode

            widgetChoix = MonChoixCode(self)
            ret = widgetChoix.exec_()
            # widgetChoix.show()
        if self.code == None:
            return  # pour le cancel de la fenetre choix code
        AppliSsIhm.definitCode(self, self.code, ssCode)

        # PN --> pb d exception qui font planter salome
        # plus supporte en python 3
        # app=QApplication
        # if hasattr(prefsCode,'encoding'):
        #   import sys
        #   reload(sys)
        #   sys.setdefaultencoding(prefsCode.encoding)

    def construitMenu(self):
        self.initPatrons()
        self.initRecents()
        self.initAides()
        for intituleMenu in (
            "menuTraduction",
            "menuOptions",
            "menuMesh",
            "menuExecution",
            "menuN1",
        ):
            if hasattr(self, intituleMenu):
                menu = getattr(self, intituleMenu)
                menu.setAttribute(Qt.WA_DeleteOnClose)
                menu.close()
                delattr(self, intituleMenu)
        for intituleAction in ("actionExecution", "actionSaveRun"):
            if hasattr(self, intituleAction):
                action = getattr(self, intituleAction)
                self.toolBar.removeAction(action)
        if self.code.upper() in Appli.__dict__:
            Appli.__dict__[self.code.upper()](
                self,
            )
        if self.suiteTelemac:
            self.lookSuiteTelemac()
        self.metMenuAJourUtilisateurs()
        if hasattr(self, "maConfiguration") and self.maConfiguration.ajoutExecution:
            self.ajoutExecution()

    def initAides(self):
        # print "je passe la"
        repAide = os.path.dirname(os.path.abspath(__file__))
        fileName = "index.html"
        self.docPath = repAide + "/../Aide"
        if hasattr(self, "maConfiguration") and hasattr(
            self.maConfiguration, "docPath"
        ):
            self.docPath = self.maConfiguration.docPath
        if hasattr(self, "maConfiguration") and hasattr(
            self.maConfiguration, "fileName"
        ):
            fileName = self.maConfiguration.fileName
        self.fileDoc = os.path.join(self.docPath, fileName)
        self.actionCode.setText(tr("Aide specifique ") + str(self.code))
        if not os.path.isfile(self.fileDoc):
            self.fileDoc = ""
            self.docPath = ""
            self.actionCode.setEnabled(False)
            return

        self.actionCode.setEnabled(True)
        self.menuAide.addAction(self.actionCode)

    def newN1(self):
        ssCode = None
        code = "PSEN_N1"
        self.cleanPath()
        dirCode = os.path.abspath(
            os.path.join(os.path.abspath(__file__), "../..", "ProcessOutputs_Eficas")
        )
        sys.path.insert(0, dirCode)
        self.code = code
        self.definitCode(code, ssCode)
        self.initRecents()
        self.multi = True
        self.demande = False
        self.fileNew()

    def newPSEN(self):
        ssCode = None
        code = "PSEN"
        self.cleanPath()
        dirCode = os.path.abspath(
            os.path.join(os.path.abspath(__file__), "../..", code)
        )
        sys.path.insert(0, dirCode)
        self.code = code
        self.definitCode(code, ssCode)
        self.multi = True
        self.demande = False
        self.fileNew()

    def ajoutUQ(self):
        AppliSsIhm.ajoutUQ(self)
        self.menuUQ = self.menubar.addMenu(tr("Incertitude"))
        self.actionSaveUQ = QAction(self)
        self.actionSaveUQ.setText(
            tr("Sauvegarde des fichiers pour l'étude incertaine")
        )
        self.menuUQ.addAction(self.actionSaveUQ)
        self.actionSaveUQ.triggered.connect(self.handleSortieUQ)
        self.actionExeUQ = QAction(self)
        self.actionExeUQ.setText(tr("Sauvegarde et Lancement de l'étude"))
        self.menuUQ.addAction(self.actionExeUQ)
        self.actionExeUQ.triggered.connect(self.handleExeUQ)
        self.actionSauvePersalys = QAction(self)
        self.actionSauvePersalys.setText(tr("Sauvegarde du script Persalys"))
        self.menuUQ.addAction(self.actionSauvePersalys)
        self.actionSauvePersalys.triggered.connect(self.handleSauvePourPersalys)
        # self.actionEnregistrer.setDisabled(True)
        # self.actionEnregistrer_sous.setDisabled(True)

    def ajoutN1(self):
        return
        self.menuN1 = self.menubar.addMenu(tr("Process Output"))
        self.actionN1 = QAction(self)
        self.actionN1.setText(tr("Process Output"))
        self.menuN1.addAction(self.actionN1)
        self.actionN1.triggered.connect(self.newN1)

        if hasattr(self, "actionOpenProcess"):
            return

        self.actionOpenProcess = QAction(self)
        self.actionOpenProcess.setText(tr("Open Process_Output File"))
        self.menuN1.addAction(self.actionOpenProcess)
        self.actionOpenProcess.triggered.connect(self.openProcess)

    def ajoutExecution(self):
        self.menuExecution = self.menubar.addMenu(tr("&Run"))
        self.actionExecution = QAction(self)
        if sys.platform[0:5] == "linux":
            icon6 = QIcon(self.repIcon + "/roue.png")
            self.actionExecution.setIcon(icon6)
        else:
            self.actionExecution.setText(tr("Run"))
        self.actionExecution.setObjectName("actionExecution")
        self.menuExecution.addAction(self.actionExecution)
        if not (self.actionExecution in self.toolBar.actions()):
            self.toolBar.addAction(self.actionExecution)
        self.actionExecution.setText(tr("Run"))
        self.actionExecution.triggered.connect(self.run)

    def ajoutSauveExecution(self):
        self.actionSaveRun = QAction(self)
        icon7 = QIcon(self.repIcon + "/export_MAP.png")
        self.actionSaveRun.setIcon(icon7)
        self.actionSaveRun.setObjectName("actionSaveRun")
        self.menuExecution.addAction(self.actionSaveRun)
        if not (self.actionSaveRun in self.toolBar.actions()):
            self.toolBar.addAction(self.actionSaveRun)
        self.actionSaveRun.setText(tr("Save Run"))
        self.actionSaveRun.triggered.connect(self.saveRun)

    def griserActionsStructures(self):
        self.actionCouper.setEnabled(False)
        self.actionColler.setEnabled(False)
        self.actionCopier.setEnabled(False)
        self.actionSupprimer.setEnabled(False)

    def enleverActionsStructures(self):
        self.toolBar.removeAction(self.actionCopier)
        self.toolBar.removeAction(self.actionColler)
        self.toolBar.removeAction(self.actionCouper)
        self.menuEdition.removeAction(self.actionCouper)
        self.menuEdition.removeAction(self.actionCopier)
        self.menuEdition.removeAction(self.actionColler)

    def enleverParametres(self):
        self.toolBar.removeAction(self.actionParametres)
        self.menuJdC.removeAction(self.actionParametres)

    def enleverSupprimer(self):
        self.toolBar.removeAction(self.actionSupprimer)

    def enlevernewInclude(self):
        self.actionNouvel_Include.setVisible(False)

    def enleverRechercherDsCatalogue(self):
        self.actionRechercherDsCatalogue.setVisible(False)

    def connectRechercherDsCatalogue(self):
        if hasattr(self, "rechercherDejaLa"):
            return
        self.rechercherDejaLa = True
        self.actionRechercherDsCatalogue.triggered.connect(
            self.handleRechercherDsCatalogue
        )

    def ajoutSortieComplete(self):
        if hasattr(self, "actionSortieComplete"):
            return
        self.actionSortieComplete = QAction(self)
        self.actionSortieComplete.setText(tr("Sortie Complete"))
        self.menuFichier.insertAction(
            self.actionEnregistrer_sous, self.actionSortieComplete
        )
        self.actionSortieComplete.triggered.connect(self.handleSortieComplete)

    def MT(self):
        self.enlevernewInclude()
        self.toolBar.addSeparator()

    def ZCRACKS(self):
        self.enlevernewInclude()
        self.toolBar.addSeparator()
        self.ajoutExecution()

        self.menuOptions = self.menubar.addMenu("menuOptions")
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.setTitle(tr("Options"))

    def ADAO(self):
        self.enleverActionsStructures()
        self.enlevernewInclude()

    def ASTER(self):
        self.menuTraduction = self.menubar.addMenu("menuTraduction")
        self.menuTraduction.addAction(self.actionTraduitV11V12)
        self.menuTraduction.addAction(self.actionTraduitV10V11)
        self.menuTraduction.addAction(self.actionTraduitV9V10)
        self.menuTraduction.setTitle(tr("Traduction"))

        self.menuFichier.addAction(self.actionSauveLigne)

        self.menuOptions = self.menubar.addMenu("menuOptions")
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.addAction(self.actionLecteur_Pdf)
        self.menuOptions.setTitle(tr("Options"))

    def CARMEL3D(self):
        # if self.salome == 0 : return
        self.enlevernewInclude()
        self.menuMesh = self.menubar.addMenu(tr("Gestion Maillage"))
        self.menuMesh.setObjectName("Mesh")
        self.menuMesh.addAction(self.actionChercheGrpMaille)
        # self.griserActionsStructures()

    def CARMELCND(self):
        self.enlevernewInclude()
        self.enleverRechercherDsCatalogue()
        self.ajoutExecution()
        self.ajoutSauveExecution()
        self.griserActionsStructures()

    def MAP(self):
        self.enlevernewInclude()
        self.toolBar.addSeparator()
        self.ajoutExecution()
        self.ajoutSauveExecution()
        self.menuOptions = self.menubar.addMenu("menuOptions")
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.setTitle(tr("Options"))

    def MAPIDENTIFICATION(self):
        self.enlevernewInclude()
        self.enleverSupprimer()
        # self.ajoutExecution()
        self.enleverRechercherDsCatalogue()
        self.enleverActionsStructures()
        self.enleverParametres()

    def PSEN(self):
        try:
            self.action_Nouveau.triggered.disconnect(self.fileNew)
        except:
            pass
        try:
            self.action_Nouveau.triggered.disconnect(self.newPSEN)
        except:
            pass

        self.action_Nouveau.triggered.connect(self.newPSEN)
        self.enleverActionsStructures()
        self.enleverParametres()
        self.enleverRechercherDsCatalogue()
        self.enlevernewInclude()
        self.ajoutExecution()
        self.ajoutN1()
        self.ajoutHelpPSEN()
        self.ajoutIcones()

    def PSEN_N1(self):
        self.enleverActionsStructures()
        self.enleverParametres()
        self.enleverRechercherDsCatalogue()
        self.enlevernewInclude()
        self.ajoutExecution()
        self.ajoutIcones()

    def TELEMAC(self):
        self.enleverActionsStructures()
        self.enlevernewInclude()
        self.connectRechercherDsCatalogue()
        self.ajoutSortieComplete()

    def lookSuiteTelemac(self):
        self.enleverActionsStructures()
        self.enlevernewInclude()
        self.enleverParametres()
        self.enleverSupprimer()
        self.enleverRechercherDsCatalogue()

    def ajoutHelpPSEN(self):
        self.actionParametres_Eficas.setText("Help PSEN")
        self.actionParametres_Eficas.triggered.connect(self.aidePSEN)

    def ChercheGrpMesh(self):
        Msg, listeGroup = self.ChercheGrpMeshInSalome()
        if Msg == None:
            self.viewmanager.handleAjoutGroup(listeGroup)
        else:
            print("il faut gerer les erreurs")

    def ChercheGrpMaille(self):
        # Normalement la variable self.salome permet de savoir si on est ou non dans Salome
        try:
            Msg, listeGroup = self.ChercheGrpMailleInSalome()  # recherche dans Salome
            # Msg = None; listeGroup = None # recherche manuelle, i.e., sans Salome si ligne precedente commentee
        except:
            raise ValueError("Salome non ouvert")
        if Msg == None:
            self.viewmanager.handleAjoutGroup(listeGroup)
        else:
            print("il faut gerer les erreurs")

    def ChercheGrp(self):
        # Msg,listeGroup=self.ChercheGrpMailleInSalome()
        # if Msg == None :
        #   self.viewmanager.handleAjoutGroup(listeGroup)
        # else :
        # print "il faut gerer "
        pass

    def ajoutIcones(self):
        # Pour pallier les soucis de repertoire d icone
        # print self.repIcon
        icon = QIcon(self.repIcon + "/new_file.png")
        self.action_Nouveau.setIcon(icon)
        icon1 = QIcon(self.repIcon + "/ouvrir.png")
        self.actionOuvrir.setIcon(icon1)
        icon2 = QIcon(self.repIcon + "/save.png")
        self.actionEnregistrer.setIcon(icon2)
        icon6 = QIcon(self.repIcon + "/delete.png")
        self.actionSupprimer.setIcon(icon6)
        icon7 = QIcon(self.repIcon + "/roue.png")
        self.actionExecution.setIcon(icon7)

    def connecterSignauxQT4(self):
        self.connect(
            self.recentMenu, SIGNAL("aboutToShow()"), self.handleShowRecentMenu
        )

        self.connect(self.action_Nouveau, SIGNAL("triggered()"), self.fileNew)
        self.connect(self.actionNouvel_Include, SIGNAL("triggered()"), self.newInclude)
        self.connect(self.actionOuvrir, SIGNAL("triggered()"), self.fileOpen)
        self.connect(self.actionEnregistrer, SIGNAL("triggered()"), self.fileSave)
        self.connect(
            self.actionEnregistrer_sous, SIGNAL("triggered()"), self.fileSaveAs
        )
        self.connect(self.actionFermer, SIGNAL("triggered()"), self.fileClose)
        self.connect(self.actionFermer_tout, SIGNAL("triggered()"), self.fileCloseAll)
        self.connect(self.actionQuitter, SIGNAL("triggered()"), self.fileExit)

        self.connect(self.actionEficas, SIGNAL("triggered()"), self.aidePPal)
        self.connect(self.actionVersion, SIGNAL("triggered()"), self.version)
        self.connect(self.actionParametres, SIGNAL("triggered()"), self.gestionParam)

        self.connect(self.actionCouper, SIGNAL("triggered()"), self.editCut)
        self.connect(self.actionCopier, SIGNAL("triggered()"), self.editCopy)
        self.connect(self.actionColler, SIGNAL("triggered()"), self.editPaste)
        self.connect(self.actionSupprimer, SIGNAL("triggered()"), self.supprimer)
        self.connect(self.actionRechercher, SIGNAL("triggered()"), self.rechercher)
        self.connect(
            self.actionDeplier_replier, SIGNAL("triggered()"), self.handleDeplier
        )

        self.connect(
            self.actionRapport_de_Validation, SIGNAL("triggered()"), self.jdcRapport
        )
        self.connect(self.actionRegles_du_JdC, SIGNAL("triggered()"), self.jdcRegles)
        self.connect(
            self.actionFichier_Source, SIGNAL("triggered()"), self.jdcFichierSource
        )
        self.connect(self.actionFichier_Resultat, SIGNAL("triggered()"), self.visuJdcPy)

        # Pour Aster
        self.actionTraduitV9V10 = QAction(self)
        self.actionTraduitV9V10.setObjectName("actionTraduitV9V10")
        self.actionTraduitV9V10.setText(tr("TraduitV9V10"))
        self.actionTraduitV10V11 = QAction(self)
        self.actionTraduitV10V11.setObjectName("actionTraduitV10V11")
        self.actionTraduitV10V11.setText(tr("TraduitV10V11"))
        self.actionTraduitV11V12 = QAction(self)
        self.actionTraduitV11V12.setObjectName("actionTraduitV11V12")
        self.actionTraduitV11V12.setText(tr("TraduitV11V12"))
        self.actionSauveLigne = QAction(self)
        self.actionSauveLigne.setText(tr("Sauve Format Ligne"))

        # self.connect(self.actionParametres_Eficas,SIGNAL("triggered()"),self.optionEditeur)
        self.connect(self.actionLecteur_Pdf, SIGNAL("triggered()"), self.optionPdf)
        self.connect(
            self.actionTraduitV9V10, SIGNAL("triggered()"), self.traductionV9V10
        )
        self.connect(
            self.actionTraduitV10V11, SIGNAL("triggered()"), self.traductionV10V11
        )
        self.connect(
            self.actionTraduitV11V12, SIGNAL("triggered()"), self.traductionV11V12
        )
        self.connect(self.actionSauveLigne, SIGNAL("triggered()"), self.sauveLigne)

        # Pour Carmel
        self.actionChercheGrpMaille = QAction(self)
        self.actionChercheGrpMaille.setText(tr("Acquiert groupe mailles"))
        self.connect(
            self.actionChercheGrpMaille, SIGNAL("triggered()"), self.ChercheGrpMaille
        )

        # Pour CarmelCND
        self.actionChercheGrp = QAction(self)
        self.actionChercheGrp.setText(tr("Acquisition Groupe Maille"))
        self.connect(self.actionChercheGrp, SIGNAL("triggered()"), self.ChercheGrp)

        # Pour Aide
        self.actionCode = QAction(self)
        self.actionCode.setText(tr("Specificites Maille"))
        self.connect(self.actionCode, SIGNAL("triggered()"), self.aideCode)

    def connecterSignaux(self):
        self.recentMenu.aboutToShow.connect(self.handleShowRecentMenu)
        self.action_Nouveau.triggered.connect(self.fileNew)
        self.actionNouvel_Include.triggered.connect(self.newInclude)
        self.actionOuvrir.triggered.connect(self.fileOpen)
        self.actionEnregistrer.triggered.connect(self.fileSave)
        self.actionEnregistrer_sous.triggered.connect(self.fileSaveAs)
        self.actionFermer.triggered.connect(self.fileClose)
        self.actionFermer_tout.triggered.connect(self.fileCloseAll)
        self.actionQuitter.triggered.connect(self.fileExit)

        self.actionEficas.triggered.connect(self.aidePPal)
        self.actionVersion.triggered.connect(self.version)
        self.actionParametres.triggered.connect(self.gestionParam)
        self.actionCommentaire.triggered.connect(self.ajoutCommentaire)

        self.actionCouper.triggered.connect(self.editCut)
        self.actionCopier.triggered.connect(self.editCopy)
        self.actionColler.triggered.connect(self.editPaste)
        self.actionSupprimer.triggered.connect(self.supprimer)
        self.actionRechercher.triggered.connect(self.rechercher)
        self.actionDeplier_replier.triggered.connect(self.handleDeplier)

        self.actionRapport_de_Validation.triggered.connect(self.jdcRapport)
        self.actionRegles_du_JdC.triggered.connect(self.jdcRegles)
        self.actionFichier_Source.triggered.connect(self.jdcFichierSource)
        self.actionFichier_Resultat.triggered.connect(self.visuJdcPy)
        self.actionAfficher_l_Arbre.triggered.connect(self.ouvreArbre)
        self.actionCacher_l_Arbre.triggered.connect(self.fermeArbre)

        # Pour Aster
        self.actionTraduitV9V10 = QAction(self)
        self.actionTraduitV9V10.setObjectName("actionTraduitV9V10")
        self.actionTraduitV9V10.setText(tr("TraduitV9V10"))
        self.actionTraduitV10V11 = QAction(self)
        self.actionTraduitV10V11.setObjectName("actionTraduitV10V11")
        self.actionTraduitV10V11.setText(tr("TraduitV10V11"))
        self.actionTraduitV11V12 = QAction(self)
        self.actionTraduitV11V12.setObjectName("actionTraduitV11V12")
        self.actionTraduitV11V12.setText(tr("TraduitV11V12"))
        self.actionSauveLigne = QAction(self)
        self.actionSauveLigne.setText(tr("Sauve Format Ligne"))

        # self.actionParametres_Eficas.triggered.connect(self.optionEditeur)
        self.actionTraduitV9V10.triggered.connect(self.traductionV9V10)
        self.actionTraduitV10V11.triggered.connect(self.traductionV10V11)
        self.actionTraduitV11V12.triggered.connect(self.traductionV11V12)
        self.actionSauveLigne.triggered.connect(self.sauveLigne)

        # Pour Carmel
        self.actionChercheGrpMaille = QAction(self)
        self.actionChercheGrpMaille.setText(tr("Acquiert Groupe Maille"))

        # Pour CarmelCND
        self.actionChercheGrp = QAction(self)
        self.actionChercheGrp.setText(tr("Accquisition Groupe Maille"))
        self.actionChercheGrp.triggered.connect(self.ChercheGrp)

        # Pour Aide
        self.actionCode = QAction(self)
        self.actionCode.setText(tr("Specificites Maille"))
        self.actionCode.triggered.connect(self.aideCode)

    def handleDeplier(self):
        self.viewmanager.handleDeplier()

    def handleSortieUQ(self):
        self.viewmanager.handleSortieUQ()

    def handleExeUQ(self):
        self.viewmanager.handleExeUQ()

    def handleSauvePourPersalys(self):
        self.viewmanager.handleSauvePourPersalys()

    def ajoutCommentaire(self):
        self.viewmanager.ajoutCommentaire()

    def ouvreFichiers(self):
        # Ouverture des fichiers de commandes donnes sur la ligne de commande
        cwd = os.getcwd()
        self.dir = cwd
        for study in session.d_env.studies:
            os.chdir(cwd)
            d = session.getUnit(study, self)
            self.viewmanager.handleOpen(fichier=study["comm"], units=d)

    def getSource(self, file):
        # appele par Editeur/session.py
        import convert

        p = convert.plugins["python"]()
        p.readfile(file)
        texte = p.convert("execnoparseur")
        return texte

    def initPatrons(self):
        # Mise a jour du menu des fichiers recemment ouverts
        from Editeur import listePatrons

        if not (self.code in listePatrons.sous_menus):
            if hasattr(self, "menuPatrons"):
                self.menuPatrons.setAttribute(Qt.WA_DeleteOnClose)
                self.menuPatrons.close()
                delattr(self, "menuPatrons")
            return
        if not hasattr(self, "menuPatrons"):
            self.menuPatrons = QMenu(self.menubar)
            self.menuPatrons.setObjectName("menuPatrons")
            self.menubar.addAction(self.menuPatrons.menuAction())
            self.menuPatrons.setTitle(tr("Patrons"))
        else:
            self.menuPatrons.clear()
        self.listePatrons = listePatrons.listePatrons(self.code)
        idx = 0
        for nomSsMenu in self.listePatrons.liste:
            ssmenu = self.menuPatrons.addMenu(nomSsMenu)
            for fichier in self.listePatrons.liste[nomSsMenu]:
                id = ssmenu.addAction(fichier)
                self.ficPatrons[id] = fichier
                self.id.triggered.connect(self.handleOpenPatrons)
                #   self.Patrons.setItemParameter(id,idx)
                idx = idx + 1

    def initRecents(self):
        self.recent = []
        try:
            rep = os.path.join(os.path.expanduser("~"), ".config/Eficas", self.code)
            monFichier = rep + "/listefichiers_" + self.code
            index = 0
            f = open(monFichier)
            while index < 9:
                ligne = f.readline()
                if ligne != "":
                    l = (ligne.split("\n"))[0]
                    self.recent.append(l)
                index = index + 1
        except:
            pass

        try:
            f.close()
        except:
            pass

    def addToRecentList(self, fn):
        while fn in self.recent:
            self.recent.remove(fn)
        self.recent.insert(0, fn)
        if len(self.recent) > 9:
            self.recent = self.recent[:9]

    def addToRecentListQT4(self, fn):
        """
        Public slot to add a filename to the list of recently opened files.

        @param fn name of the file to be added
        """
        self.recent.removeAll(fn)
        self.recent.prepend(fn)
        if len(self.recent) > 9:
            self.recent = self.recent[:9]
        index = 0
        self.sauveRecents()

    def sauveRecents(self):
        try:
            rep = self.maConfiguration.rep_user
            monFichier = rep + "/listefichiers_" + self.code
        except:
            return
        try:
            f = open(monFichier, "w")
            if len(self.recent) == 0:
                return
            index = 0
            while index < len(self.recent):
                ligne = str(self.recent[index]) + "\n"
                f.write(ligne)
                index = index + 1
        except:
            pass
        try:
            f.close()
        except:
            pass

    def traductionV11V12(self):
        from .gereTraduction import traduction

        traduction(self.maConfiguration.repIni, self.viewmanager, "V11V12")

    def traductionV10V11(self):
        from .gereTraduction import traduction

        traduction(self.maConfiguration.repIni, self.viewmanager, "V10V11")

    def traductionV9V10(self):
        from .gereTraduction import traduction

        traduction(self.maConfiguration.repIni, self.viewmanager, "V9V10")

    def version(self):
        from .monVisu import DVisu

        titre = tr("version ")
        monVisuDialg = DVisu(parent=self, fl=0)
        monVisuDialg.setWindowTitle(titre)
        if self.code != None:
            monVisuDialg.TB.setText(self.VERSION_EFICAS + tr(" pour ") + self.code)
        else:
            monVisuDialg.TB.setText(self.VERSION_EFICAS)
        monVisuDialg.adjustSize()
        monVisuDialg.show()

    def aidePPal(self):
        repAide = os.path.dirname(os.path.abspath(__file__))
        maD = os.path.join(repAide, "..", "Doc")
        try:
            indexAide = os.path.join(maD, "index.html")
            if sys.platform[0:5] == "linux":
                cmd = "xdg-open " + indexAide
            else:
                cmd = "start " + indexAide
            os.system(cmd)
        except:
            QMessageBox.warning(
                self, tr("Aide Indisponible"), tr("l'aide n est pas installee ")
            )

    def aidePSEN(self):
        repAide = os.path.dirname(os.path.abspath(__file__))
        maD = os.path.join(repAide, "..", "Doc")
        try:
            indexAide = os.path.join(maD, "index.html")
            if sys.platform[0:5] == "linux":
                cmd = "xdg-open " + indexAide
            else:
                cmd = "start " + indexAide
            os.system(cmd)
        except:
            QMessageBox.warning(
                self, tr("Aide Indisponible"), tr("l'aide n est pas installee ")
            )

    def aideCode(self):
        if self.code == None:
            return
        try:
            # if 1 :
            if sys.platform[0:5] == "linux":
                cmd = "xdg-open " + self.fileDoc
            else:
                cmd = "start " + self.fileDoc
            os.system(cmd)
        except:
            # else:
            QMessageBox.warning(
                self, tr("Aide Indisponible"), tr("l'aide n est pas installee ")
            )

    def optionEditeur(self):
        try:
            name = "monOptions_" + self.code
        except:
            QMessageBox.critical(
                self, tr("Parametrage"), tr("Veuillez d abord choisir un code")
            )
            return
        try:
            # if 1:
            optionCode = __import__(name)
        except:
            # else :
            QMessageBox.critical(
                self,
                tr("Parametrage"),
                tr("Pas de possibilite de personnalisation de la configuration "),
            )
            return
        monOption = optionCode.Options(
            parent=self, modal=0, configuration=self.maConfiguration
        )
        monOption.show()

    def optionPdf(self):
        from monOptionsPdf import OptionPdf

        monOption = OptionPdf(parent=self, modal=0, configuration=self.maConfiguration)
        monOption.show()

    def handleSortieComplete(self):
        return self.viewmanager.saveCompleteCurrentEditor()

    def handleShowRecentMenu(self):
        """
        Private method to set up recent files menu.
        """
        self.recentMenu.clear()

        for rp in self.recent:
            id = self.recentMenu.addAction(rp)
            self.ficRecents[id] = rp
            id.triggered.connect(self.handleOpenRecent)
        self.recentMenu.addSeparator()
        self.recentMenu.addAction(tr("&Effacer"), self.handleClearRecent)

    def handleOpenPatrons(self):
        idx = self.sender()
        fichier = (
            self.repIni
            + "/../Editeur/Patrons/"
            + self.code
            + "/"
            + self.ficPatrons[idx]
        )
        self.viewmanager.handleOpen(fichier=fichier, patron=1)

    def handleOpenRecent(self):
        idx = self.sender()
        fichier = self.ficRecents[idx]
        self.viewmanager.handleOpen(fichier=fichier, patron=0)

    def handleClearRecent(self):
        self.recent = []
        self.sauveRecents()

    def handleRechercherDsCatalogue(self):
        if not self.viewmanager:
            return
        self.viewmanager.handleRechercherDsCatalogue()

    def fileNew(self):
        try:
            self.viewmanager.newEditor()
        except EficasException as exc:
            msg = str(exc)
            if msg != "":
                QMessageBox.warning(self, tr("Erreur"), msg)

    def openProcess(self):
        ssCode = None
        code = "PSEN_N1"
        self.cleanPath()
        dirCode = os.path.abspath(
            os.path.join(os.path.abspath(__file__), "../..", "ProcessOutputs_Eficas")
        )
        sys.path.insert(0, dirCode)
        self.code = code
        self.definitCode(code, ssCode)
        self.multi = True
        self.demande = False
        self.initRecents()
        self.fileOpen()

    def fileOpen(self):
        try:
            self.viewmanager.handleOpen()
        except EficasException as exc:
            msg = str(exc)
            if msg != "":
                QMessageBox.warning(self, tr("Erreur"), msg)

    def sauveLigne(self):
        return self.viewmanager.sauveLigneCurrentEditor()

    def fileSave(self):
        return self.viewmanager.saveCurrentEditor()

    def fileSaveAs(self):
        return self.viewmanager.saveAsCurrentEditor()

    def fileClose(self):
        self.viewmanager.handleClose(texte="&Fermer")

    def fileCloseAll(self):
        self.viewmanager.handleCloseAll(texte="&Fermer")

    def fileExit(self):
        # On peut sortir sur Abort
        res = self.viewmanager.handleCloseAll()
        if res != 2:
            self.close()
        return res

    def editCopy(self):
        self.viewmanager.handleEditCopy()

    def editCut(self):
        self.viewmanager.handleEditCut()

    def editPaste(self):
        self.viewmanager.handleEditPaste()

    def rechercher(self):
        self.viewmanager.handleRechercher()

    def run(self):
        self.viewmanager.run()

    def saveRun(self):
        self.viewmanager.saveRun()

    def supprimer(self):
        self.viewmanager.handleSupprimer()

    def jdcFichierSource(self):
        self.viewmanager.handleViewJdcFichierSource()

    def jdcRapport(self):
        self.viewmanager.handleViewJdcRapport()

    def jdcRegles(self):
        self.viewmanager.handleViewJdcRegles()

    def gestionParam(self):
        self.viewmanager.handleGestionParam()

    def visuJdcPy(self):
        self.viewmanager.handleViewJdcPy()

    def ouvreArbre(self):
        self.viewmanager.ouvreArbre()

    def fermeArbre(self):
        self.viewmanager.fermeArbre()

    def newInclude(self):
        self.viewmanager.newIncludeEditor()

    def cleanPath(self):
        for pathCode in self.ListePathCode:
            try:
                aEnlever = os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..", pathCode)
                )
                sys.path.remove(aEnlever)
            except:
                pass
        for pathCode in self.listeAEnlever:
            try:
                sys.path.remove(aEnlever)
            except:
                pass

    def closeEvent(self, event):
        res = self.fileExit()
        if res == 2:
            event.ignore()

    def remplitIconesCommandes(self):
        if self.maConfiguration.boutonDsMenuBar == False:
            return
        if not hasattr(self, "readercata"):
            return
        from monLayoutBouton import MonLayoutBouton

        if hasattr(self, "monLayoutBoutonRempli"):
            return
        self.monLayoutBoutonRempli = MonLayoutBouton(self)

    def handleAjoutEtape(self, nomEtape):
        self.viewmanager.handleAjoutEtape(nomEtape)

    def metMenuAJourUtilisateurs(self):
        self.lesFonctionsUtilisateurs = {}
        if self.code not in self.mesScripts:
            return
        if not hasattr(self.mesScripts[self.code], "dict_menu"):
            return
        for monMenu in iter(self.mesScripts[self.code].dict_menu.items()):
            titre, lesFonctions = monMenu
            self.menuOptions = self.menubar.addMenu("menuOptions")
            self.menuOptions.setTitle(tr(titre))
            for elt in lesFonctions:
                laFonctionUtilisateur, label, lesArguments = elt
                action = QAction(self)
                action.setText(label)
                # action.triggered.connect(self.appelleFonctionUtilisateur)
                self.menuOptions.addAction(action)
                self.lesFonctionsUtilisateurs[action] = (
                    laFonctionUtilisateur,
                    lesArguments,
                )
            self.menuOptions.triggered.connect(self.handleFonctionUtilisateur)

    def handleFonctionUtilisateur(self, action):
        (laFonctionUtilisateur, lesArguments) = self.lesFonctionsUtilisateurs[action]
        self.viewmanager.handleFonctionUtilisateur(laFonctionUtilisateur, lesArguments)


if __name__ == "__main__":
    # Modules Eficas
    rep = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__), "..", "Adao"))
    )
    sys.path.append(rep)
    from Adao import prefs
    from Adao import prefs_Adao

    from Editeur import import_code
    from Editeur import session

    # Analyse des arguments de la ligne de commande
    options = session.parse(sys.argv)
    code = options.code

    app = QApplication(sys.argv)
    # app.setMainWidget(mw) (qt3)
    Eficas = Appli()
    Eficas.show()

    # mw.ouvreFichiers()
    # mw.show()

    res = app.exec_()
    sys.exit(res)

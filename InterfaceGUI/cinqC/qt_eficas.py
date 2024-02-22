#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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

from UiQT5.myMain5C import Ui_Eficas5C
from InterfaceGUI.QT5.qtEficas import QtEficasAppli
from PyQt5.QtWidgets import  QAction, QMessageBox
from Accas.extensions.eficas_translation import tr



class QtEficasAppli(Ui_Eficas5C, QtEficasAppli):
    """
    Class implementing the 5C user interface.
    """

    def __init__(self,code='5C', salome=0, multi = 0, versionCode=None,  langue='en', GUIPath="InterfaceGUI.cinqC",appWeb=None):
        super().__init__(code=code, salome=salome, multi=multi, langue=langue, versionCode=versionCode, GUIPath=GUIPath)
        self.withXSD = True
        self.GUIPath = GUIPath
        self.editorManager.getEditor()
        

    def connecterSignaux(self) :
        # Pour Aide
        self.actionCode = QAction(self)
        self.actionCode.setText(tr("Aide 5C"))
        self.actionCode.triggered.connect(self.aideCode)
        self.actionOuvrir.triggered.connect(self.openFile) 


    def openFile(self) :
        print ('aChanger')
        print ( self.editorManager)


    def closeEvent(self,event):
        print ('fermer la database ?? ')
        #res=self.fileExit()
        #if res==2 : event.ignore()



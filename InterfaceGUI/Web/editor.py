# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import absolute_import
from __future__ import print_function

import types,sys,os, re
import traceback


# Modules Eficas
from Extensions.i18n import tr

from Editeur         import session
from Editeur         import comploader
from Editeur         import Objecttreeitem
from InterfaceGUI.Web import browser

debug = False

from InterfaceGUI.editorSsIhm    import JDCEditorSsIhm


class JDCWebEditor(JDCEditorSsIhm):
# ------------------------------- #
    """
       Editeur de jdc
    """

    def __init__ (self,appliEficas,fichier = None, jdc= None, connecteur = None ):
    #------------------------------------------------------------------------
        
        self.connecteur=connecteur
        JDCEditorSsIhm.__init__(self,appliEficas,fichier)
        self.dicoIdNode={}
        comploader.chargerComposants('Web')
        self.tree=None
        if self.jdc:
            self.jdc_item=Objecttreeitem.makeObjecttreeitem( self, "nom", self.jdc )
            if self.jdc_item :
               self.tree = browser.JDCTree( self.jdc_item,  self )


    def getNodeById(self,nodeId ):
    #-----------------------------
        if nodeId in self.dicoIdNode : return self.dicoIdNode[nodeId]
        else : return None

    def reconstruitChaineDIndex(self,nodeId):
    #---------------------------------------
        if nodeId in self.dicoIdNode : 
           node=self.dicoIdNode[nodeId]
           return JDCEditorSsIhm.reconstruitChaineDIndex(self,node)
        else : return None


    def getDicoObjetsCompletsPourTree(self,obj) :
    #-----------------------------------
        #print ('editor getDicoObjetsCompletsPourTree pour ' ,self, obj)
        if self.tree == None : return {}
        return obj.getDicoObjetsCompletsPourTree()

    def getDicoObjetsPourWeb(self,obj) :
    #-----------------------------------
        if self.tree == None : return {}
        return obj.getDicoObjetsPourWeb()

    def getDicoForFancy(self,obj) :
    #-----------------------------------
        if self.tree == None : return {}
        return obj.getDicoForFancy()

    def afficheInfos(self,txt,couleur=None):
    #---------------------------------------
        self.connecteur.toWebApp('afficheInfos', txt, couleur) 
        JDCEditorSsIhm.afficheInfos(self,txt,couleur)

    def afficheAlerte(self,titre,message):
    #-------------------------------------
        self.connecteur.toWebApp('afficheAlerte', titre ,  message) 
        JDCEditorSsIhm.afficheAlerte(self,titre,message)



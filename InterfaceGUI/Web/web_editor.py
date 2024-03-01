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
from Accas.extensions.eficas_translation import tr
from Accas.extensions.eficas_exception import EficasException
from Editeur.loggingEnvironnement import loggingEnvironnement, fonctionLoguee


from InterfaceGUI.Common import comploader
from InterfaceGUI.Common import objecttreeitem
from InterfaceGUI.Web import browser

debug = False

from Editeur.editor import Editor


# -------------------- #
class WebEditor(Editor):
# -------------------- #
    """
       Editeur de jdc
    """

    #--------------------------------------------------------------------------
    def __init__ (self,appliEficas,fichier = None, jdc= None, session = None ):
    #--------------------------------------------------------------------------
        
        self.connecteur=appliEficas
        self.dicoIdNode={}
        Editor.__init__(self,appliEficas,fichier)
        comploader.chargerComposants('Web')
        self.tree=None
        if self.jdc:
            self.jdc_item=objecttreeitem.makeObjecttreeitem( appliEficas, "nom", self.jdc )
            if self.jdc_item :
               self.tree = browser.JDCTree( self.jdc_item,  self )



    #-----------------------------
    @fonctionLoguee
    def getNodeById(self,nodeId ):
    #-----------------------------
        if nodeId in self.dicoIdNode : return self.dicoIdNode[nodeId]
        else : return None

    #---------------------------------------
    @fonctionLoguee
    def reconstruitChaineDIndex(self,nodeId):
    #---------------------------------------
        """ utilise pour logguer les fonctions """
        if nodeId in self.dicoIdNode : 
           node=self.dicoIdNode[nodeId]
           if node.object  == self.jdc : 
               return 'monEficasConnecteur.monEditeur.tree.racine.item.idUnique'
           chaine="['key']"
           templateChaine='["children"][{}]'
           aTraiter=node.object
           while hasattr(aTraiter,'parent') and aTraiter.parent:
               chaine=templateChaine.format(aTraiter.getIndexDsParent())+chaine
               aTraiter=aTraiter.parent
           chaine='d'+chaine
           return (chaine)
        else : return None


    #-----------------------------
    @fonctionLoguee
    def getDicoForFancy(self,obj) :
    #-----------------------------
        if self.tree == None : return {}
        return obj.getDicoForFancy()

    #-------------------------------------
    @fonctionLoguee
    def afficheMessage(self,txt,couleur=None):
    #---------------------------------------
        self.connecteur.toWebApp('afficheMessage', txt, couleur) 
        Editor.afficheMessage(self,'message to webapp',txt,couleur)

    #-------------------------------------
    @fonctionLoguee
    def afficheAlerte(self,titre,message):
    #-------------------------------------
        self.connecteur.toWebApp('afficheAlerte', titre ,  message) 
        Editor.afficheMessage(self,titre,message)

    #---------------------------
    @fonctionLoguee
    def getListeCommandes(self):
    #---------------------------
        return (self.jdc.getListeCmd())

    #---------------------------------
    @fonctionLoguee
    def updateSDName(self,id,sdnom) :
    #---------------------------------
         monNode=self.getNodeById(id)
         if not monNode : return  (False, 'Node {} non trouve'.format(id))
         return monNode.fauxNoeudGraphique.updateSDName(sdnom)

    #---------------------------------
    @fonctionLoguee
    def changeValeur(self,id,valeur) :
    #---------------------------------
         """
         id : identifiant unique
         valeur : valeur saisie dans le formulaire
         doit-on mettre l ancienne valeur en retour qui serait utile si validité = Non
         """
         monNode=self.getNodeById(id)
         if not monNode : return  (id, False, 'Node {} non trouve'.format(id))
         #print (' change Valeur', monNode)
         #(idUnique, commentaire, validite)=monNode.fauxNoeudGraphique.traiteValeurSaisie(valeur)
         #print ('retour ChangeValeur',idUnique, commentaire, validite )
         # 
         return monNode.fauxNoeudGraphique.traiteValeurSaisie(valeur)


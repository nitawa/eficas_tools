# -*- coding: iso-8859-1 -*-
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
# Modules Python
import traceback

# Modules Eficas
from InterfaceGUI.Web import typeNode
from InterfaceGUI.Web import browser
from InterfaceGUI.Common.politiquesValidation import PolitiqueUnique
from InterfaceGUI.Common.politiquesValidation import PolitiquePlusieurs
from InterfaceGUI.Common import objecttreeitem
from InterfaceGUI.Common.simp_treeItem_commun import SIMPTreeItemCommun


class Node(browser.JDCNode,typeNode.PopUpMenuNodeMinimal):

    def traiteValeurSaisie(self,  valeur): 
        if self.item.get_definition().max==1 : self.politique = PolitiqueUnique (self, self.editor)
        else  : self.politique = PolitiquePlusieurs(self, self.editor)
        if self.item.definition.validators != None :
            if self.item.definition.validators.verifItem(valeur) !=1 :
                commentaire=self.node.item.definition.validators.infoErreurItem()
                return (self.item.idUnique, False ,commentaire)
        nouvelleValeurFormat=self.politique.getValeurTexte(valeur)
        validite,commentaire=self.politique.recordValeur(nouvelleValeurFormat)
        if not validite : 
            return (self.item.idUnique, False, commentaire)
        return (self.item.idUnique, True, commentaire)
        
class SIMPTreeItem(SIMPTreeItemCommun):
    itemNode = Node

import Accas
treeitem = SIMPTreeItem
objet = Accas.MCSIMP



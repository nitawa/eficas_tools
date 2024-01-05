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
from __future__ import absolute_import
from Editeur  import Objecttreeitem
from InterfaceGUI.cinqC import browser
from InterfaceGUI.cinqC import compoproc


class Node(browser.JDCNode):

    def getPanel(self):
        from InterfaceGUI.QT5.monWidgetCommande import MonWidgetCommande
        return MonWidgetCommande(self,self.editor,self.item.object)


class SelectionTreeItem(compoproc.ProcEtapeTreeItem):
    itemNode=Node

currentCata = CONTEXT.getCurrentCata()
treeitem = SelectionTreeItem
objet = currentCata.cata.identifiantSelection

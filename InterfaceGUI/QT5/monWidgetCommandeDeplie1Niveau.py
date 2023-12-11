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
# Modules Python
# Modules Eficas

import types, os
import traceback

from PyQt5.QtGui import QIcon
from InterfaceGUI.QT5.monWidgetCommande import MonWidgetCommande
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy


class MonWidgetCommandeDeplie1Niveau(MonWidgetCommande):
    # Attention au MCLIST qui ne sont pas des MCFACT
    # il faut donc surcharger un certain nb de fonction ici pour eux

    def __init__(self, node, editor, etape):
        # print ("debut de ---------------------- init de MonWidgetCommandeDeplie1Niveau ",node.item.nom)
        MonWidgetCommande.__init__(self, node, editor, etape)
        self.node.plieToutEtReaffiche = self.plieToutEtReaffiche
        spacerItem = QSpacerItem(21, 600, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayoutCommande.addItem(spacerItem)

    def afficheMots(self):
        # Attention
        # Attention --> cette methode surcharge les methodes des Nodes Fils
        # Attention
        # print ("debut de ---------------------- ds afficheMots de MonWidgetCommandeDeplie1Niveau ",self.node.item.nom)
        # traceback.print_stack()
        repIcon = self.editor.appliEficas.repIcon
        fichier = os.path.join(repIcon, "deleteRondVide.png")
        icon = QIcon(fichier)
        for node in self.node.children:
            node.plie = True
            node.setPlieChildren()
            if node.appartientAUnNoeudPlie == True:
                continue

            node.plieToutEtReaffiche = self.plieToutEtReaffiche
            node.deplieToutEtReaffiche = self.deplieToutEtReaffiche
            node.affichePanneau = self.affichePanneau
            node.getPanel = self.getPanel

            widget = node.getPanelGroupe(self, self.maCommande)
            self.listeFocus.append(node.fenetre)

            try:
                node.fenetre.RBDeplie.setCheckable(False)
                node.fenetre.RBDeplie.setEnabled(False)
                node.fenetre.RBDeplie.setIcon(icon)
            except:
                pass

            if node.item.object.isMCList():
                node.setDeplie = self.setDepliePourMCList

                for c in node.children:
                    c.setDeplie = self.setDepliePourNode
                    c.plieToutEtReaffiche = self.plieToutEtReaffiche
                    c.deplieToutEtReaffiche = self.deplieToutEtReaffiche
                    c.getPanel = self.getPanel
                    c.affichePanneau = self.affichePanneau
                    try:
                        c.fenetre.RBDeplie.setCheckable(False)
                        c.fenetre.RBDeplie.setEnabled(False)
                        c.fenetre.RBDeplie.setIcon(icon)
                    except:
                        pass
            else:
                node.setDeplie = self.setDepliePourNode

        # print ("fin ------------------------ afficheMots de MonWidgetCommandeDeplie1Niveau ",self.node.item.nom)

    def afficheSuivant(self, aAfficher):
        fenetre = self.node.tree.itemCourant.fenetre
        fenetre.afficheSuivant(aAfficher)

    def setDepliePourNode(self):
        noeudCourant = self.node.tree.itemCourant
        noeudCourant.setDeplieChildren()
        if self.editor.fenetreCentraleAffichee == noeudCourant.fenetre:
            return
        noeudCourant.afficheCeNiveau()
        pass

    # -------------------------------------------- Methodes qui surchargent les noeuds fils

    def setDepliePourMCList(self):
        # print ('je surcharge setDeplie pour MCList')
        pass

    def setPlieChildren(self):
        # print ('je surcharge setPlieChildren')
        pass

    def setDeplieChildren(self):
        # print ('je surcharge setDeplieChildren')
        pass

    def plieToutEtReaffiche(self):
        # print ('je surcharge plieToutEtReaffiche', self.node.item.nom)
        pass

    def deplieToutEtReaffiche(self):
        # print ('je surcharge deplieToutEtReaffiche', self.node.tree.itemCourant.item.getLabelText())
        pass

    def plieToutEtReafficheSaufItem(self):
        # print ('je surcharge plieToutEtReaffiche', self.node.tree.itemCourant.item.getLabelText())
        pass

    def affichePanneau(self):
        # print ('je surcharge affichePanneau', self.node.tree.itemCourant.item.getLabelText())
        node = self.node.tree.itemCourant
        while (
            not (hasattr(node, "fenetreIhm"))
            or node.treeParent.fenetreIhm != "deplie1Niveau"
        ):
            node = node.treeParent
        self.node.tree.setCurrentItem(node)

        item = node.item
        if (
            item.getLabelText()[0]
            == self.editor.fenetreCentraleAffichee.labelNomCommande.text()
        ):
            return
        node.setDeplieChildren()
        node.afficheCeNiveau()
        self.editor.fenetreCentraleAffichee.labelNomCommande.setText(
            item.getLabelText()[0]
        )
        self.editor.fenetreCentraleAffichee.labelDoc.setText(item.getFr())

    def getPanel(self):
        # print ('surcharge ds getPanel')
        pass

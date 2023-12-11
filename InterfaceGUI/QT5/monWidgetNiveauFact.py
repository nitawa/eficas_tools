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
import types, os

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from desWidgetNiveauFact import Ui_WidgetNiveauFact
from InterfaceGUI.QT5.monWidgetOptionnel import MonWidgetOptionnel
from InterfaceGUI.QT5.groupe import Groupe

from Extensions.i18n import tr

class MonWidgetNiveauFact(Ui_WidgetNiveauFact, Groupe):
    """ """

    def __init__(self, node, editor, definition, obj):
        self.listeAffichageWidget = []
        self.listeBoutonAChanger = []
        Groupe.__init__(self, node, editor, None, definition, obj, 1, self)
        from InterfaceGUI.QT5 import composimp

        if isinstance(self.node, composimp.Node):
            widget = self.node.getPanelGroupe(self, self.maCommande)
            self.listeBoutonAChanger.append(widget.RBValide)
        self.afficheOptionnel()
        self.inhibe = False
        self.labelDoc.setText(self.node.item.getFr())
        self.labelNomCommande.setText(self.node.item.getLabelText()[0])

    def reaffiche(self, nodeAVoir=None):
        self.node.setDeplieChildren()
        self.node.afficheCeNiveau()
        self.editor.fenetreCentraleAffichee.labelDoc.setText(self.node.item.getFr())
        self.editor.fenetreCentraleAffichee.labelNomCommande.setText(
            self.node.item.getLabelText()[0]
        )

    def getPanel(self):
        # necessaire pour handleOnItem de browser.py
        # non appele
        pass

    def donnePremier(self):
        # print "dans donnePremier"
        QApplication.processEvents()
        if self.listeAffichageWidget != []:
            self.listeAffichageWidget[0].setFocus(7)
        QApplication.processEvents()
        # print self.focusWidget()

    def focusNextPrevChild(self, next):
        # on s assure que ce n est pas un chgt de fenetre
        # print "je passe dans focusNextPrevChild"
        if self.editor.fenetreCentraleAffichee != self:
            return True
        f = self.focusWidget()

        if f not in self.listeAffichageWidget:
            i = 0
            while not hasattr(f, "AAfficher"):
                if f == None:
                    i = -1
                    break
                f = f.parentWidget()
            if hasattr(f, "AAfficher"):
                f = f.AAfficher
            if i != -1:
                i = self.listeAffichageWidget.index(f)
        else:
            i = self.listeAffichageWidget.index(f)
        if (i == len(self.listeAffichageWidget) - 1) and next and not self.inhibe:
            try:
                self.listeAffichageWidget[1].setFocus(7)
                w = self.focusWidget()
                self.inhibe = 1
                w.focusPreviousChild()
                self.inhibe = 0
                return True
            except:
                pass

        if i == 0 and next == False and not self.inhibe:
            if hasattr(self.editor.fenetreCentraleAffichee, "scrollArea"):
                self.editor.fenetreCentraleAffichee.scrollArea.ensureWidgetVisible(
                    self.listeAffichageWidget[-1]
                )
            self.listeAffichageWidget[-2].setFocus(7)
            self.inhibe = 1
            w = self.focusWidget()
            w.focusNextChild()
            self.inhibe = 0
            return True

        if i == 0 and next == True and not self.inhibe:
            self.listeAffichageWidget[0].setFocus(7)
            self.inhibe = 1
            w = self.focusWidget()
            w.focusNextChild()
            self.inhibe = 0
            return True

        if i > 0 and next == False and not self.inhibe:
            if isinstance(self.listeAffichageWidget[i - 1], QRadioButton):
                self.listeAffichageWidget[i - 1].setFocus(7)
                return True
        return QWidget.focusNextPrevChild(self, next)

    def etablitOrdre(self):
        # si on boucle on perd l'ordre
        i = 0
        while i + 1 < len(self.listeAffichageWidget):
            self.setTabOrder(
                self.listeAffichageWidget[i], self.listeAffichageWidget[i + 1]
            )
            i = i + 1

    def afficheSuivant(self, f):
        # print ('ds afficheSuivant')
        try:
            i = self.listeAffichageWidget.index(f)
            next = i + 1
        except:
            next = 1
        if next == len(self.listeAffichageWidget):
            next = 0
        try:
            self.listeAffichageWidget[next].setFocus(7)
        except:
            pass

    def afficheOptionnel(self):
        # N a pas de parentQt. doit donc etre redefini
        # print ('ds afficheOptionnel')
        if self.editor.maConfiguration.closeOptionnel:
            return
        if self.editor.widgetOptionnel != None:
            self.monOptionnel = self.editor.widgetOptionnel
        else:
            self.editor.inhibeSplitter = 1
            self.monOptionnel = MonWidgetOptionnel(self.editor)
            self.editor.widgetOptionnel = self.monOptionnel
            self.editor.splitter.addWidget(self.monOptionnel)
            self.editor.ajoutOptionnel()
            self.editor.inhibeSplitter = 0
        self.monOptionnel.vireTous()

        liste, liste_rouge = self.ajouteMCOptionnelDesBlocs()
        self.monOptionnel.parentCommande = self
        self.monOptionnel.titre(self.obj.nom)
        self.monGroupe = self.monOptionnel.afficheOptionnel(liste, liste_rouge, self)

    def setValide(self):
        Groupe.setValide(self)
        for bouton in self.listeBoutonAChanger:
            couleur = self.node.item.getIconName()
            monIcone = QIcon(self.repIcon + "/" + couleur + ".png")
            bouton.setIcon(monIcone)


class MonWidgetNiveauFactTableau(MonWidgetNiveauFact):
    def __init__(self, node, editor, definition, obj):
        MonWidgetNiveauFact.__init__(self, node, editor, definition, obj)

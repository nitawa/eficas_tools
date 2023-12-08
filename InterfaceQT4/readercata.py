# -*-  coding: utf-8 -*-
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
"""
    Ce module sert a lire un catalogue et a construire
    un objet CataItem pour Eficas.
    Il s'appuie sur la classe READERCATA
"""
# Modules Python
import os, sys

# Modules Eficas
from Noyau.N_CR import CR
from Editeur.catadesc import CatalogDescription

import analyse_catalogue
import analyse_catalogue_initial
import autre_analyse_cata
import uiinfo
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException


# -------------------------------
class ReaderCataCommun(object):
    # -------------------------------

    def askChoixCatalogue(self, cataListeChoix):
        # ____________________________________________
        """
        Ouvre une fenetre de selection du catalogue dans le cas où plusieurs
        ont ete definis dans Accas/editeur.ini
        """
        try:
            from PyQt5.QtWidgets import QDialog
        except:
            print("Pas de choix interactif sans qt")
            return

        code = getattr(self.appliEficas.maConfiguration, "code", None)
        if code != None:
            title = tr("Choix d une version du code ") + str(code)
        else:
            title = tr("Choix d une version ")

        from InterfaceQT4.monChoixCata import MonChoixCata

        widgetChoix = MonChoixCata(
            self.appliEficas, [cata.labelCode for cata in cataListeChoix], title
        )
        ret = widgetChoix.exec_()

        lab = str(self.VERSION_EFICAS) + " "
        lab += tr(" pour ")
        lab += str(self.code)
        lab += tr(" avec le catalogue ")
        if ret == QDialog.Accepted:
            cata = cataListeChoix[widgetChoix.CBChoixCata.currentIndex()]
            self.fichierCata = cata.fichierCata
            self.labelCode = cata.labelCode
            self.appliEficas.formatFichierOut = cata.formatFichierOut
            self.appliEficas.formatFichierIn = cata.formatFichierIn
            lab += self.labelCode
            self.appliEficas.setWindowTitle(lab)
            widgetChoix.close()
        else:
            widgetChoix.close()
            raise EficasException()

    def choisitCata(self):
        # ____________________

        listeCataPossibles = []
        #self.commandesOrdreCatalogue = []

        listeTousLesCatas = []
        for catalogue in self.appliEficas.maConfiguration.catalogues:
            if isinstance(catalogue, CatalogDescription):
                listeTousLesCatas.append(catalogue)
            elif isinstance(catalogue, tuple):
                listeTousLesCatas.append(CatalogDescription.createFromTuple(catalogue))
            else:
                print(("Catalog description cannot be interpreted: ", catalogue))

        if self.labelCode is None:
            listeCataPossibles = listeTousLesCatas
        else:
            for catalogue in listeTousLesCatas:
                if catalogue.code == self.code and catalogue.ssCode == self.ssCode:
                    listeCataPossibles.append(catalogue)

        if len(listeCataPossibles) == 0:
            try:
                QMessageBox.critical(
                    self.QWParent,
                    tr("Import du catalogue"),
                    tr("Pas de catalogue defini pour le code ") + self.code,
                )
            except:
                print("Pas de catalogue defini pour le code " + self.code)
            if self.appliEficas.salome == 0:
                sys.exit(1)
            self.appliEficas.close()
            return

        if self.labelCode is not None:
            # La version a ete fixee
            for cata in listeCataPossibles:
                if self.labelCode == cata.labelCode:
                    self.fichierCata = cata.fichierCata
                    self.labelCode = cata.labelCode
                    self.appliEficas.formatFichierOut = cata.formatFichierOut
                    self.appliEficas.formatFichierIn = cata.formatFichierIn
        else:
            cataChoiceList = []
            for cata in listeCataPossibles:
                if cata.selectable:
                    if cata.default:
                        cataChoiceList.insert(0, cata)
                    else:
                        cataChoiceList.append(cata)

        # le catalogue est fixe dans la ligne de commande
        if self.appliEficas.fichierCata != None:
            trouve = False
            for catalogue in listeTousLesCatas:
                if os.path.abspath(catalogue.fichierCata) == (
                    os.path.abspath(self.appliEficas.fichierCata)
                ):
                    listeCataPossibles = (catalogue,)
                    trouve = True
                    break
            if not trouve:
                catalogue = CatalogDescription.createFromTuple(
                    (
                        self.code,
                        self.code,
                        self.appliEficas.fichierCata,
                        "python",
                        "python",
                    )
                )
                listeCataPossibles = (catalogue,)

        if len(listeCataPossibles) == 0:
            try:
                from PyQt5.QtWidgets import QMessageBox, QDialog

                QMessageBox.critical(
                    self.QWParent,
                    tr("Import du catalogue"),
                    tr("Pas de catalogue defini pour le code ") + self.code,
                )
            except:
                print("Pas de catalogue defini pour le code " + self.code)
            self.appliEficas.close()
            if self.appliEficas.salome == 0:
                sys.exit(1)
            return

        # le label est fixe dans la ligne de commande
        if self.labelCode is not None:
            # La version a ete fixee
            for cata in listeCataPossibles:
                if self.labelCode == cata.labelCode:
                    self.fichierCata = cata.fichierCata
                    self.appliEficas.formatFichierIn = cata.formatFichierIn
                    self.appliEficas.formatFichierOut = cata.formatFichierOut
        else:
            cataListeChoix = []
            for cata in listeCataPossibles:
                if cata.default:
                    cataListeChoix.insert(0, cata)
                else:
                    cataListeChoix.append(cata)

            if len(cataListeChoix) == 0:
                try:
                    from PyQt5.QtWidgets import QMessageBox

                    QMessageBox.critical(
                        self.QWParent,
                        tr("Import du catalogue"),
                        tr("Aucun catalogue trouve"),
                    )
                except:
                    print("Pas de catalogue defini pour le code " + self.code)
                self.appliEficas.close()
                if self.appliEficas.salome == 0:
                    sys.exit(1)

            elif len(cataListeChoix) == 1:
                self.fichierCata = cataListeChoix[0].fichierCata
                self.labelCode = cataListeChoix[0].labelCode
                self.appliEficas.formatFichierOut = cataListeChoix[0].formatFichierOut
                self.appliEficas.formatFichierIn = cataListeChoix[0].formatFichierIn

            else:
                # plusieurs catalogues sont disponibles : il faut demander a l'utilisateur
                # lequel il veut utiliser ...
                if self.appliEficas.ssIhm:
                    print("Unable to know which catafile is choosen")
                    exit()
                self.askChoixCatalogue(cataListeChoix)
                self.demandeCatalogue = True

        if self.fichierCata == None:
            if self.appliEficas.salome == 0:
                print(
                    (
                        "Pas de catalogue pour code %s, version %s"
                        % (self.code, self.labelCode)
                    )
                )
                sys.exit(1)
            else:
                self.appliEficas.close()
                return


# ------------------------------------
class ReaderCata(ReaderCataCommun):
    # ------------------------------------

    def __init__(self, QWParent, appliEficas):
        # _______________________________________

        self.QWParent = QWParent
        self.appliEficas = self.QWParent.appliEficas
        self.VERSION_EFICAS = self.appliEficas.VERSION_EFICAS
        self.demandeCatalogue = False
        self.code = self.appliEficas.code
        self.titre = self.appliEficas.code
        self.ssCode = self.appliEficas.ssCode
        # on positionne par defaut mais est-ce vraiment necessaire
        self.appliEficas.formatFichierIn = "python"
        self.appliEficas.formatFichierOut = "python"
        self.labelCode = self.appliEficas.labelCode
        self.fichierCata = self.appliEficas.fichierCata
        self.openCata()
        self.traiteIcones()
        self.cataitem = None
        self.creeDicoInverse()
        if self.code == "TELEMAC":
            self.creeDicoCasToCata()

    def openCata(self):
        """
        Ouvre le catalogue standard du code courant, cad le catalogue present
        dans le repertoire Cata
        """
        # import du catalogue
        if self.fichierCata == None:
            self.choisitCata()

        self.cata = self.importCata(self.fichierCata)
        if self.code == "NonConnu":
            self.code = self.cata.JdC.code
        modeleMetier = None
        dicoEltDif = {}
        if not (self.appliEficas.genereXSD):
            if self.appliEficas.maConfiguration.withXSD or self.appliEficas.withXSD:
                try:
                    import pyxb
                except:
                    self.QWParent.informe(
                        "environnement", "please source pyxb environment"
                    )
                    exit()
                try:
                    nomCataXsd = os.path.splitext(os.path.basename(self.fichierCata))[0]
                    fichierCataTrunc = os.path.splitext(
                        os.path.basename(self.fichierCata)
                    )[0]
                    nomCataXsd = fichierCataTrunc + "_driver"

                    if os.path.dirname(self.fichierCata) == "":
                        pathCata = "./raw/" + nomCataXsd + ".py"
                    else:
                        pathCata = (
                            os.path.dirname(self.fichierCata)
                            + "/raw/"
                            + nomCataXsd
                            + ".py"
                        )

                    self.cata.fileModeleMetier = (
                        os.path.dirname(self.fichierCata)
                        + "/raw/"
                        + nomCataXsd
                        + ".xsd"
                    )
                    import imp

                    modeleMetier = imp.load_source(nomCataXsd, pathCata)
                    # print ('nomCataXsd , pathCata ',nomCataXsd,pathCata)
                    try:
                        # if 1 :
                        # monObjetAnnotation = getattr(modeleMetier,'PNEFdico_'+self.code)
                        monObjetAnnotation = getattr(modeleMetier, "PNEFdico")
                        texte = monObjetAnnotation.__doc__
                    except:
                        texte = None
                    if texte != None and texte != "":
                        l = {}
                        texte = "dicoEltDif = " + texte
                        exec(texte, globals(), l)
                        dicoEltDif = l["dicoEltDif"]
                    # print ('dans readerCata _________', dicoEltDif)

                except:
                    if self.appliEficas.ssIhm == False:
                        print("______________ poum import cata_genere ")
                    self.QWParent.informe(
                        "XSD driver", "unable to load xsd driver", critique=False
                    )
                    modeleMetier = None

        self.cata.DicoNomTypeDifferentNomElt = dicoEltDif

        if hasattr(self.cata, "implement"):
            self.cata.JdC.implement = self.cata.implement
        else:
            self.cata.JdC.implement = ""
        if hasattr(self.cata, "importedBy"):
            self.cata.JdC.importedBy = self.cata.importedBy
        else:
            self.cata.JdC.importedBy = []
        self.cata.JdC.labelCode = self.labelCode
        if not (hasattr(self.cata, "dict_condition")):
            self.cata.dict_condition = {}

        # pointeur pour le dumpXSD
        self.cata.JdC.cata = self.cata

        self.cata.modeleMetier = modeleMetier
        if not self.cata:
            # try:
            # from PyQt5.QtWidgets import QMessageBox, QDialog
            # QMessageBox.critical( self.QWParent, tr("Import du catalogue"),tr("Impossible d'importer le catalogue ")+ self.fichierCata)
            # except :
            #  print ("Impossible d'importer le catalogue "+ self.fichierCata)
            self.QWParent.informe(
                "Catalogue", "Impossible d'importer le catalogue " + self.fichierCata
            )
            self.appliEficas.close()
            if self.appliEficas.salome == 0:
                sys.exit(1)
        #
        # analyse du catalogue (ordre des mots-cles)
        #
        # retrouveOrdreCataStandard fait une analyse textuelle du catalogue
        # remplace par retrouveOrdreCataStandardAutre qui utilise une numerotation
        # des mots cles a la creation
        # print (dir(self.cata))
        self.retrouveOrdreCataStandardAutre()
        if self.appliEficas.maConfiguration.modeNouvCommande == "initial":
            self.retrouveOrdreCataStandard()
        if hasattr(self.cata, "ordreDesCommandes"):
            self.ordreDesCommandes = self.cata.ordreDesCommandes
        else:
            self.ordreDesCommandes = None

        if hasattr(self.cata, "Classement_Commandes_Ds_Arbre"):
            self.Classement_Commandes_Ds_Arbre = self.cata.Classement_Commandes_Ds_Arbre
        else:
            self.Classement_Commandes_Ds_Arbre = ()
        if hasattr(self.cata, "enum"):
            try:
                _temp = __import__(
                    self.cata.enum,
                    globals(),
                    locals(),
                    ["DicoEnumCasFrToEnumCasEn", "TelemacdicoEn"],
                    0,
                )
                self.DicoEnumCasFrToEnumCasEn = _temp.DicoEnumCasFrToEnumCasEn
                self.TelemacdicoEn = _temp.TelemacdicoEn
            except:
                pass

        # print self.cata.ordreDesCommandes

        #
        # analyse des donnees liees l'IHM : UIinfo
        #
        uiinfo.traite_UIinfo(self.cata)

        #
        # traitement des clefs documentaires
        #

        self.titre = (
            self.VERSION_EFICAS
            + " "
            + tr(" avec le catalogue ")
            + os.path.basename(self.fichierCata)
        )
        if self.appliEficas.ssIhm == False:
            self.appliEficas.setWindowTitle(self.titre)
        self.appliEficas.titre = self.titre
        self.QWParent.titre = self.titre

        # incertitude --> change le convert
        if hasattr(self.cata, "avecIncertitude"):
            self.appliEficas.ajoutUQ()
        if hasattr(self.cata, "modifieCatalogueDeterministe"):
            self.cata.modifieCatalogueDeterministe(self.cata)

    def importCata(self, cata):
        """
        Realise l'import du catalogue dont le chemin d'acces est donne par cata
        """
        nom_cata = os.path.splitext(os.path.basename(cata))[0]
        rep_cata = os.path.dirname(cata)
        sys.path[:0] = [rep_cata]
        self.appliEficas.listeAEnlever.append(rep_cata)

        # PNPNPN pas propre __ A reflechir
        if "cata_Vimmp" in list(sys.modules.keys()):
            del sys.modules["cata_Vimmp"]

        if nom_cata in list(sys.modules.keys()):
            del sys.modules[nom_cata]

        for k in sys.modules:
            if k[0 : len(nom_cata) + 1] == nom_cata + ".":
                del sys.modules[k]

        mesScriptsNomFichier = "mesScripts_" + self.code.upper()
        try:
            self.appliEficas.mesScripts[self.code] = __import__(mesScriptsNomFichier)
        except:
            pass

        # if 1 :
        try:
            o = __import__(nom_cata)
            return o
        except Exception as e:
            self.QWParent.informe("catalog python", "unable to load catalog file")
            import traceback

            traceback.print_exc()
            return 0

    def retrouveOrdreCataStandardAutre(self):
        """
        Construit une structure de donnees dans le catalogue qui permet
        a EFICAS de retrouver l'ordre des mots-cles dans le texte du catalogue.
        Pour chaque entite du catlogue on cree une liste de nom ordreMC qui
        contient le nom des mots cles dans le bon ordre
        """
        (
            self.cata_ordonne_dico,
            self.appliEficas.liste_simp_reel,
        ) = autre_analyse_cata.analyseCatalogue(self.cata)
        # print ('_________________________________________', self)
        # print (self.cata_ordonne_dico)
        # self.appliEficas.liste_simp_reel = ()
        # self.cata_ordonne_dico = {}

    def retrouveOrdreCataStandard(self):
        """
        Retrouve l'ordre des mots-cles dans le catalogue, cad :
        Attention s appuie sur les commentaires
        """
        nom_cata = os.path.splitext(os.path.basename(self.fichierCata))[0]
        rep_cata = os.path.dirname(self.fichierCata)
        self.commandesOrdreCatalogue = analyse_catalogue_initial.analyseCatalogue( self.fichierCata)
        # print self.commandesOrdreCatalogue

    def traiteIcones(self):
        if self.appliEficas.maConfiguration.ficIcones == None:
            return
        try:
            ficIcones = self.appliEficas.maConfiguration.ficIcones
            fichierIcones = __import__(ficIcones, globals(), locals(), [], 0)
            self.appliEficas.maConfiguration.dicoIcones = (
                fichierIcones.dicoDesIcones.dicoIcones
            )
            self.appliEficas.maConfiguration.dicoImages = (
                fichierIcones.dicoDesIcones.dicoImages
            )
        except:
            print("Pas de fichier associe contenant des liens sur les icones ")
            self.appliEficas.maConfiguration.dicoIcones = {}

    def creeDicoInverse(self):
        self.dicoInverse = {}
        self.dicoMC = {}
        if not self.cata:
            return
        listeEtapes = self.cata.JdC.commandes
        for e in self.cata.JdC.commandes:
            self.traiteEntite(e)

    def creeDicoCasToCata(self):
        if hasattr(self.cata, "dicoCasEn"):
            _temp = __import__(
                self.cata.dicoCasEn, globals(), locals(), ["DicoCasEnToCata"], 0
            )
            if self.appliEficas.langue == "ang":
                self.dicoCasToCata = _temp.dicoCasEnToCata
            else:
                self.dicoCasToCata = _temp.dicoCasFrToCata

    def traiteEntite(self, e):
        boolIn = 0
        for nomFils, fils in list(e.entites.items()):
            self.dicoMC[nomFils] = fils
            self.traiteEntite(fils)
            boolIn = 1
        if boolIn == 0:
            liste = []
            moi = e
            while hasattr(moi, "pere"):
                liste.append((moi.nom, moi))
                moi = moi.pere
            liste.append((moi.nom, moi))
            self.dicoInverse[e.nom] = liste
            self.dicoInverse[tr(e.nom)] = liste

    def creeRubrique(self, e, dico, niveau):
        from Accas import A_BLOC

        decale = niveau * "   "
        # if niveau != 0 :
        #    if isinstance(e,A_BLOC.BLOC): print decale, e.condition
        #    else :                           print decale, e. nom
        for nom, fils in list(e.entites.items()):
            if list(fils.entites.items()) != []:
                self.creeRubrique(fils, dico, niveau + 1)
            # else : print (niveau+1)*"   ", nom

    # def dumpToXsdEficas(self):
    # Pas sur qu on ait jamais besoin de cela
    #    pass
    # from Efi2Xsd import readerEfficas
    # newSchema=   xml = open('Cata_MED_FAM.xml').read()
    # SchemaMed = efficas.CreateFromDocument(xml)
    # SchemaMed.alimenteCata(self.cata)

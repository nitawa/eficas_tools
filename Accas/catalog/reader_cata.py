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
from Accas.processing.P_CR import CR
from Accas.catalog.catadesc import CatalogDescription
from Accas.catalog import analyse_ordre_catalogue
from Accas.catalog import analyse_ordre_impose
from Accas.catalog import uiinfo
from Accas.extensions.eficas_translation import tr
from Accas.extensions.eficas_exception import EficasException


# -----------------------------
class ReaderCataCommun(object):
# -----------------------------

    def askChoixCatalogue(self, cataListeChoix):
    #____________________________________________
        """
        Ouvre une fenetre de selection du catalogue dans le cas où plusieurs
        ont ete definis dans Accas/editeur.ini
        """
        if self.appliEficas == None :
            print("Pas de choix interactif sans qt")
            return

        code = getattr(self.appliEficas.maConfiguration, "code", None)
        if code != None: title = tr("Choix d une version du code ") + str(code)
        else: title = tr("Choix d une version ")

        # a Reflechir
        # Pourquoi 2 fois MonChoixCata -- je ne comprends pas mais cela fonctionne
        pathGui='InterfaceGUI.'+ self.appliEficas.GUIPath + '.monChoixCata'
        MonChoixCata =__import__(pathGui, globals(), locals(), ['MonChoixCata,'])
        widgetChoix = MonChoixCata.MonChoixCata(
            self.appliEficas, [cata.versionCode for cata in cataListeChoix], title
        )
        ret = widgetChoix.exec_()
        #if ret == QDialog.Accepted:
        if ret == 1:
            cata = cataListeChoix[widgetChoix.CBChoixCata.currentIndex()]
            self.fichierCata = cata.fichierCata
            self.versionCode = cata.versionCode
            self.appliEficas.formatFichierOut = cata.formatFichierOut
            self.appliEficas.formatFichierIn = cata.formatFichierIn
            titre='{} pour {} avec le catalogue {}'.format(self.appliEficas.versionEficas,self.code,self.versionCode)
            self.appliEficas.setWindowTitle(titre)
            widgetChoix.close()
        else:
            widgetChoix.close()
            raise EficasException()

    def choisitCata(self):
    #--------------------#

        listeCataPossibles = []

        listeTousLesCatas = []
        for catalogue in self.appliEficas.maConfiguration.catalogues:
            if isinstance(catalogue, CatalogDescription):
                listeTousLesCatas.append(catalogue)
            elif isinstance(catalogue, tuple):
                listeTousLesCatas.append(CatalogDescription.createFromTuple(catalogue))
            else:
                print(("Catalog description cannot be interpreted: ", catalogue))

        if self.versionCode is None:
            listeCataPossibles = listeTousLesCatas
        else:
            # a priori impossible sans l idee du sousCode
            for catalogue in listeTousLesCatas:
                if catalogue.code == self.code and catalogue.versionCode == self.versionCode:
                    listeCataPossibles.append(catalogue)

        if len(listeCataPossibles) == 0:
            self.appliEficas.afficheMessage(
                    tr("Import du catalogue"),
                    tr("Pas de catalogue defini pour le code {}".format(self.code)))
            self.appliEficas.close()
            if self.appliEficas.salome == 0: sys.exit(1)
            return

        if self.versionCode is not None:
            # La version a ete fixee
            for cata in listeCataPossibles:
                if self.versionCode == cata.versionCode:
                    self.fichierCata = cata.fichierCata
                    self.versionCode = cata.versionCode
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
                if os.path.abspath(catalogue.fichierCata) == ( os.path.abspath(self.appliEficas.fichierCata)):
                    listeCataPossibles = (catalogue,)
                    trouve = True
                    break
            if not trouve:
                # utilise par Telemac
                catalogue = CatalogDescription.createFromTuple(
                    ( self.code, self.code, self.appliEficas.fichierCata, "python", "python",)
                )
                listeCataPossibles = (catalogue,)

        if len(listeCataPossibles) == 0:
            self.appliEficas.afficheMessage(
                 tr("Import du catalogue"),
                 tr("Pas de catalogue defini pour le code ") + self.code,
            )
            self.appliEficas.close()
            if self.appliEficas.salome == 0: sys.exit(1)
            return

        # le label est fixe dans la ligne de commande
        if self.versionCode is not None:
            # La version a ete fixee
            for cata in listeCataPossibles:
                if self.versionCode == cata.versionCode:
                    self.fichierCata = cata.fichierCata
                    self.appliEficas.formatFichierIn = cata.formatFichierIn
                    self.appliEficas.formatFichierOut = cata.formatFichierOut
        else:
            cataListeChoix = []
            for cata in listeCataPossibles:
                if cata.default: cataListeChoix.insert(0, cata)
                else: cataListeChoix.append(cata)

            if len(cataListeChoix) == 0:
                self.appliEficas.afficheMessage( 
                    tr("Import du catalogue"),
                    tr("Aucun catalogue trouve"),)
                self.appliEficas.close()
                if self.appliEficas.salome == 0: sys.exit(1)

            elif len(cataListeChoix) == 1:
                self.fichierCata = cataListeChoix[0].fichierCata
                self.versionCode = cataListeChoix[0].versionCode
                self.appliEficas.formatFichierOut = cataListeChoix[0].formatFichierOut
                self.appliEficas.formatFichierIn = cataListeChoix[0].formatFichierIn

            else:
                # plusieurs catalogues sont disponibles : il faut demander a l'utilisateur
                # lequel il veut utiliser ...
                print ('PN : --> passer la commande askChoixCatalogue dans Editor avec sortie pour non QT / non Web')
                #self.appliEficas.afficheMessage( tr("Import du catalogue"), tr('Aucun catalogue choisi'), critique = True)
                self.demandeCatalogue = True
                self.askChoixCatalogue(cataListeChoix)

        if self.fichierCata == None:
            if self.appliEficas.salome == 0:
                print( "Pas de catalogue pour code %s, version %s" % (self.code, self.versionCode))
                sys.exit(1)
            else:
                self.appliEficas.close()
                return


# ------------------------------------
class ReaderCata(ReaderCataCommun):
# ------------------------------------

    def __init__(self, appliEficas, editor):
    # _________________________________

        self.appliEficas = appliEficas
        self.editor = editor
        self.versionEficas = self.appliEficas.versionEficas
        self.demandeCatalogue = False
        self.code = self.appliEficas.code
        self.titre = self.appliEficas.code
        # on positionne par defaut mais est-ce vraiment necessaire
        self.appliEficas.formatFichierIn = "python"
        self.appliEficas.formatFichierOut = "python"
        self.versionCode = self.appliEficas.versionCode
        self.fichierCata = self.appliEficas.fichierCata
        self.openCata()
        self.traiteIcones()
        self.cataitem = None
        self.creeDicoInverse()
        if self.code == "TELEMAC":
            self.creeDicoCasToCata()

    def openCata(self):
    # _________________
        """
        Ouvre le catalogue standard du code courant, cad le catalogue present
        dans le repertoire Cata
        """
        # import du catalogue
        if self.fichierCata == None:
            self.choisitCata()

        self.cata = self.importCata(self.fichierCata)
        if self.code == "NonConnu": self.code = self.cata.JdC.code
        modeleMetier = None
        dicoEltDif = {}
        if not(self.appliEficas.genereXSD) and self.appliEficas.withXSD:
                try:
                    import pyxb
                except:
                    self.appliEficas.afficheMessage(
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

                except Exception as e :
                    self.appliEficas.afficheMessage( "XSD driver", "unable to load xsd driver" + str(e), critique=False)
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
        self.cata.JdC.versionCode = self.versionCode
        if not (hasattr(self.cata, "dict_condition")):
            self.cata.dict_condition = {}

        # pointeur pour le dumpXSD
        self.cata.JdC.cata = self.cata

        self.cata.modeleMetier = modeleMetier
        if not self.cata:
            self.appliEficas.afficheMessage(
                "Catalogue", "Impossible d'importer le catalogue " + self.fichierCata
            )
            self.appliEficas.close()
            if self.appliEficas.salome == 0:
                sys.exit(1)
        #
        # retrouveOrdreCataStandard fait une analyse textuelle du catalogue
        # retrouveOrdreCataImpose utilise une numerotation des mots cles a la creation
        self.retrouveOrdreCata()
        self.retrouveOrdreCataImpose()
        if hasattr(self.cata, "ordreDesCommandes"): 
           self.ordreDesCommandes = self.cata.ordreDesCommandes
        else:
           self.ordreDesCommandes = []
           for cmd in self.cata.JdC.commandes:
               self.ordreDesCommandes.append(cmd.nom)

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

        self.titre = (
            self.versionEficas + tr(" avec le catalogue ")
            + os.path.basename(self.fichierCata)
        )
        self.editor.titre = self.titre
        if hasattr(self.appliEficas, 'setWindowTitle') :
            self.appliEficas.setWindowTitle(self.titre)

        # incertitude ou modification du Catalogue
        if hasattr(self.cata, "avecIncertitude"): self.appliEficas.ajoutUQ()
        if hasattr(self.cata, "modifieCatalogueDeterministe"):
            self.cata.modifieCatalogueDeterministe(self.cata)

    def importCata(self, fichierCata):
        """
        Realise l'import du catalogue dont le chemin d'acces est donne par cata
        """
         
        nomCata = os.path.splitext(os.path.basename(fichierCata))[0]
        repCata = os.path.abspath(os.path.dirname(fichierCata))
        sys.path[:0] = [repCata]
        self.appliEficas.listePathAEnlever.append(repCata)

        if nomCata in list(sys.modules.keys()):
            del sys.modules[nomCata]

        for k in sys.modules:
            if k[0 : len(nomCata) + 1] == nomCata + ".":
                del sys.modules[k]

        # permettait d ajouter des scripts appelables par des fonctions supplementaires
        # dans l ihm
        # par exemple  permet d ajouter des morceaux dans le jeu de données
        # mecanisme mis en place pout MT et laisse pour pouvoir eventuellement
        # etre repris 
        # mesScriptsNomFichier = "mesScripts_" + self.code.upper()
        # try: self.appliEficas.mesScripts[self.code] = __import__(mesScriptsNomFichier)
        # except: pass

        try:
            #import importlib.util
            from importlib import util
            cataSpec = util.spec_from_file_location(nomCata, fichierCata)
            leCata = util.module_from_spec(cataSpec)
            cataSpec.loader.exec_module(leCata)
            return leCata
        except Exception as e:
            self.appliEficas.afficheMessage("catalog python", "unable to load catalog file")
            import traceback
            traceback.print_exc()
            exit(1) 

    def retrouveOrdreCata(self):
        """
        Construit une structure de donnees dans le catalogue qui permet
        a EFICAS de retrouver l'ordre des mots-cles dans le texte du catalogue.
        Pour chaque entite du catalogue on cree une liste de nom ordreMC qui
        contient le nom des mots cles dans le bon ordre
        """
        self.dicoCataOrdonne, self.appliEficas.liste_simp_reel = analyse_ordre_catalogue.analyseCatalogue(self.cata)

    def retrouveOrdreCataImpose(self):
        """
        Retrouve l'ordre des mots-cles dans le catalogue, cad :
        Attention s appuie sur les commentaires
        """
        nomCata = os.path.splitext(os.path.basename(self.fichierCata))[0]
        repCata = os.path.dirname(self.fichierCata)
        self.commandesOrdreCatalogue = analyse_ordre_impose.analyseCatalogue( self.fichierCata)

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

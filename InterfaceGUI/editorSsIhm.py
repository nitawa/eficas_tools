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

import types, sys, os, re
import subprocess
import traceback

# Modules Eficas

import convert, generator
from Editeur import session
from Editeur import comploader
from Editeur import Objecttreeitem

DictExtensions = {"MAP": ".map", "TELEMAC": ".cas"}
debug = False


class JDCEditorSsIhm:
# ------------------- #
    """
    Editeur de jdc
    """

    # ---------------------------------------------
    # Methodes Communes ou appelees depuis avec Ihm
    # ---------------------------------------------

    def __init__(self, appliEficas, fichier=None, jdc=None, units=None, include=0):
    # -----------------------------------------------------------------------------------#
        # paticularisee avec Ihm

        if debug:
            print("dans le init de JDCEditorSsIhm")
        self.appliEficas = appliEficas
        self.fichier = fichier
        self.fichierComplet = fichier
        if fichier != None:
            self.extensionFichier = os.path.splitext(fichier)[1]
        else:
            self.extensionFichier = None
        self.jdc = jdc
        self.first = True
        self.jdc_item = None
        self.dicoNouveauxMC = {}
        self.dicoNouveauxFact = {}
        self.dict_reels = {}
        self.liste_simp_reel = []

        if self.appliEficas != None:
            self.salome = self.appliEficas.salome
        else:
            self.salome = 0

        # ces attributs sont mis a jour par definitCode appelee par newEditor
        self.code = self.appliEficas.maConfiguration.code
        self.maConfiguration = self.appliEficas.maConfiguration

        if ( not hasattr(self.appliEficas, "readercata")
            or self.appliEficas.readercata.demandeCatalogue == True
            or self.appliEficas.multi == True):

            if self.maConfiguration.typeDeCata == "XML":
                from InterfaceGUI import readercataXML as readercata
            else:
                from InterfaceGUI import readercata
            self.readercata = readercata.ReaderCata(self.appliEficas, self)
            self.appliEficas.readercata = self.readercata
            self.appliEficas.code = self.code
        else:
            self.readercata = self.appliEficas.readercata

        if self.readercata : 
            self.titre = self.readercata.titre

        self.formatFichierOut = self.appliEficas.formatFichierOut
        self.formatFichierIn = self.appliEficas.formatFichierIn

        # if self.appliEficas.maConfiguration.dumpXSD==True : self.appliEficas.dumpXsd()
        self.dict_reels = {}
        self.liste_simp_reel = []
        self.dicoNouveauxMC = {}
        self.dicoNouveauxFact = {}

        try:
            self.maConfiguration.generator_module
            _module = __import__(self.maConfiguration.generator_module)
            info = _module.entryPoint()
            generator.plugins.addEntryPoint(info)
        except:
            pass

        try:
            self.maConfiguration.convert_module
            # print self.maConfiguration.convert_module
            _module = __import__(self.maConfiguration.convert_module)
            info = _module.entryPoint()
            convert.plugins.addEntryPoint(info)
        except:
            pass

        self.maConfiguration.mesGenerators = generator
        self.maConfiguration.mesconvertisseurs = convert
        try: self.XMLGenerator = generator.plugins["xml"]()
        except: self.XMLGenerator = None
        try: self.pythonGenerator = generator.plugins["python"]()
        except: self.pythonGenerator = None

        if self.formatFichierOut in generator.plugins.keys():
            self.generator = generator.plugins[self.formatFichierOut]()

        self.fileInfo = None
        self.lastModified = 0

        self.modified = False
        self.isReadOnly = False

        # ------- construction du jdc --------------

        if self.readercata.cata == None: 
           if self.fichier is not None: 
              print ('fichier comm mais pas de cata')
           return  # Sortie Salome

        self.nouveau = 0
        if self.fichier is not None:  #  fichier jdc fourni
            if jdc == None:
                # print ('PNPN : chgt try en if')
                try:
                    # if 1 :
                    self.jdc = self.readFile(self.fichier)
                except:
                    print("mauvaise lecture du fichier")
                if self.salome:
                    try:
                        self.appliEficas.addJdcInSalome(self.fichier)
                    except:
                        print("mauvais enregistrement dans Salome")
            else:
                self.jdc = jdc

            if self.jdc is not None and units is not None:
                self.jdc.recorded_units = units
                self.jdc.old_recorded_units = units

        else:
            if not self.jdc:  #  nouveau jdc
                if not include:
                    self.jdc = self._newJDC(units=units)
                else:
                    self.jdc = self._newJDCInclude(units=units)
                self.nouveau = 1

        if self.jdc:
            self.jdc.editor = self
            self.jdc.lang = self.appliEficas.langue
            self.jdc.aReafficher = False
            txt_exception = None
            if not jdc:
                if self.extensionFichier == ".xml":
                    if self.appliEficas.maConfiguration.withXSD:
                        self.jdc.analyseXML()
                    else:
                        print("run MDM with -x option  (MDM for XML)")
                        exit()
                else:
                    self.jdc.analyse()
                    if hasattr(self, "monConvert") and hasattr(
                        self.monConvert, "traitementApresLoad"
                    ):
                        self.monConvert.traitementApresLoad(self.jdc)
                txt_exception = self.jdc.cr.getMessException()
            if txt_exception:
                self.jdc = None
                self.informe("pb chargement jdc", txt_exception)

    # -------------------------------#
    def readFile(self, fn):
    # --------------------------------#
        """
        Public slot to read the text from a file.
        @param fn filename to read from (string or QString)
        """

        # charge un JDC
        # paticularisee avec Ihm

        fn = str(fn)
        jdcName = os.path.basename(fn)

        # Il faut convertir le contenu du fichier en fonction du format
        formatIn = self.appliEficas.formatFichierIn
        if self.extensionFichier == ".xml" and self.appliEficas.maConfiguration.withXSD:
            formatIn = "xml"
        if formatIn in convert.plugins:
            # Le convertisseur existe on l'utilise
            monConvert = convert.plugins[formatIn]()
            monConvert.readfile(fn)

            if monConvert.text == "":
                self.nouveau = 1
            # print ('PNPN --> CIST a faire')

            if formatIn != "xml":
                pareil, texteNew = self.verifieChecksum(monConvert.text)
                if not pareil:
                    self.informe(
                        ("fichier modifie"),
                        ("Attention! fichier change hors EFICAS"),
                        False,
                    )
                monConvert.text = texteNew
                memeVersion, texteNew = self.verifieVersionCataDuJDC(monConvert.text)
                if memeVersion == 0:
                    texteNew = self.traduitCatalogue(texteNew)
                monConvert.text = texteNew
                text = monConvert.convert("exec", self.appliEficas)
                if not monConvert.cr.estvide():
                    self.afficheInfos("Erreur a la conversion", "red")
            else:
                text = monConvert.text
        else:
            self.afficheInfos("Type de fichier non reconnu", "red")
            self.informe(
                "Type de fichier non reconnu",
                "EFICAS ne sait pas ouvrir le type de fichier "
                + self.appliEficas.formatFichierIn,
            )
            return None

        CONTEXT.unsetCurrentStep()

        # jdc=self.readercata.cata[0].JdC(procedure=text,
        # le jdc  n est pas charge
        if not (hasattr(self.readercata, "cata_ordonne_dico")):
            return
        jdc = self.readercata.cata.JdC(
            procedure=text,
            appliEficas=self.appliEficas,
            cata=self.readercata.cata,
            cata_ord_dico=self.readercata.cata_ordonne_dico,
            nom=jdcName,
            repMat=self.maConfiguration.repMat,
        )
        self.modified = False
        self.monConvert = monConvert
        return jdc

    # ---------------------------------------#
    def _newJDC(self, texte = "", units=None):
    # ---------------------------------------#
        """
        Initialise un nouveau JDC avec le texte passe en parametre
        """
        self.modified = 1
        CONTEXT.unsetCurrentStep()

        if hasattr(self.readercata.cata, "TEXTE_NEW_JDC"):
            texte = self.readercata.cata.TEXTE_NEW_JDC

        jdc = self.readercata.cata.JdC(
            procedure=texte,
            appliEficas=self.appliEficas,
            cata=self.readercata.cata,
            cata_ord_dico=self.readercata.cata_ordonne_dico,
            repMat=self.maConfiguration.repMat,
        )

        jdc.lang = self.appliEficas.langue
        if units is not None:
            jdc.recorded_units = units
            jdc.old_recorded_units = units
        jdc.editor = self
        return jdc

    # --------------------------------#
    def _newJDCInclude(self, units=None):
    # --------------------------------#
        """
        Initialise un nouveau JDC vierge
        """
        import Extensions.jdc_include

        JdC_aux = Extensions.jdc_include.JdC_include
        CONTEXT.unsetCurrentStep()

        # jaux=self.readercata.cata[0].JdC( procedure="",
        jaux = self.readercata.cata.JdC(
            procedure="",
            appliEficas=self.appliEficas,
            cata=self.readercata.cata,
            cata_ord_dico=self.readercata.cata_ordonne_dico,
            repMat=self.maConfiguration.repMat,
        )
        jaux.editor = self
        jaux.analyse()

        J = JdC_aux(
            procedure="",
            appliEficas=self.appliEficas,
            cata=self.readercata.cata,
            cata_ord_dico=self.readercata.cata_ordonne_dico,
            jdc_pere=jaux,
            repMat=self.maConfiguration.repMat,
        )
        J.editor = self
        J.analyse()
        if units is not None:
            J.recorded_units = units
            J.old_recorded_units = units
        return J

    # -----------------------#
    def getSource(self, file):
    # -----------------------#

        # Il faut convertir le contenu du fichier en fonction du format
        if self.formatFichierIn in convert.plugins:
            # Le convertisseur existe on l'utilise
            p = convert.plugins[self.formatFichierIn]()
            p.readfile(file)
            text = p.convert("execnoparseur")
            if not p.cr.estvide():
                self.afficheInfos("Erreur a la conversion", "red")
            return text
        else:
            # Il n'existe pas c'est une erreur
            self.afficheInfos("Type de fichier non reconnu", "red")
            self.informe(
                "Type de fichier non reconnu",
                "EFICAS ne sait pas ouvrir le type de fichier "
                + self.appliEficas.formatFichierIn,
            )
            return None

    # ----------------------------------------------#
    def __generateTempFilename(self, prefix, suffix):
    # ----------------------------------------------#
        import tempfile

        (fd, filename) = tempfile.mkstemp(prefix=prefix, suffix=suffix)
        os.close(fd)
        return filename

    # -----------------------#
    def generDico(self):
    # -----------------------#
        if "dico" in generator.plugins:
            self.generator = generator.plugins["dico"]()
            # print (self.generator)
            jdc_formate = self.generator.gener(self.jdc)
            # print (jdc_formate)
            dico = self.generator.Dico
            # print (dico)
            return dico

    # --------------------------------#
    def generDicoPourWeb(self, obj=None):
        # --------------------------------#
        if obj == None:
            obj = self.jdc
        if "dico" in generator.plugins:
            self.generator = generator.plugins["dico"]()
            jdc_formate = self.generator.gener(self.jdc)
            dico = self.generator.Dico
            return dico

    # -----------------------#
    def generDicoPython(self):
    # -----------------------#
        if "dico" in generator.plugins:
            self.generator = generator.plugins["dico"]()
            dico = self.generator.generDico(self.jdc)
            return dico

    # -----------------------#
    def viewJdcSource(self):
    # -----------------------#
        if self.fichier == None:
            return
        if os.path.isfile(self.fichier):
            f = open(self.fichier, "r")
            texteSource = f.read()
            f.close()
            self._viewText(texteSource, "JDC_SOURCE")
        else:
            self._viewText("file doesn't exist", "JDC_SOURCE")

    # -----------------------#
    def viewJdcPy(self):
    # -----------------------#
        strSource = str(self.getTextJDC(self.formatFichierOut))
        self._viewText(strSource, "JDC_RESULTAT")

    # -----------------------#
    def viewJdcRapport(self):
    # -----------------------#
        # on ajoute les regles
        strRapport = str(self.jdc.report())
        self._viewText(strRapport, "JDC_RAPPORT")

    # -----------------------#
    def viewJdcRegles(self):
    # -----------------------#
        # on ajoute les regles
        texte_global, test_global = self.jdc.verifRegles()
        self._viewText(texte_global, "JDC_REGLES")

    # -----------------------#
    def getJdcRapport(self):
    # -----------------------#
        # on ajoute les regles
        strRapport = str(self.jdc.report())
        return strRapport

    # ---------------------#
    def getFileName(self):
    # ---------------------#
        return self.fichier

    # -------------------#
    def initModif(self):
    # -------------------#
        """
        Met l'attribut modified a 'o' : utilise par Eficas pour savoir
        si un JDC doit etre sauvegarde avant destruction ou non
        """
        self.modified = True

    # --------------------------------------------------#
    def writeFile(self, fn, txt=None, formatLigne="beautifie"):
    # --------------------------------------------------#
        """
        Public slot to write the text to a file.

        @param fn filename to write to string
        @return flag indicating success
        """

        fn = str(fn)

        if txt == None:
            txt = self.getTextJDC(self.formatFichierOut, formatLigne=formatLigne)
            eol = "\n"
            if len(txt) >= len(eol):
                if txt[-len(eol) :] != eol:
                    txt += eol
            else:
                txt += eol
            txt = self.ajoutVersionCataDsJDC(txt)
            if self.code != "PSEN" and self.code != "PSEN_N1":
                checksum = self.getChecksum(txt)
            else:
                checksum = ""
            txt = txt + checksum
        if self.code == "TELEMAC":
            return 1
        try:
            f = open(fn, "w")
            f.write(txt)
            f.close()
            return 1
        except IOError as why:
            print(
                "Sauvegarde du Fichier",
                "Le fichier" + str(fn) + "n a pas pu etre sauvegarde :",
                str(why),
            )
            self.afficheInfos(
                "Le fichier" + str(fn) + "n a pas pu etre sauvegarde ", "red"
            )
            return 0

    # -----------------------------------------------------------#
    def getTextJDC(self, format=None, pourRun=0, formatLigne="beautifie"):
    # -----------------------------------------------------------#
        if self.code == "MAP" and not (format in generator.plugins):
            format = "MAP"
        if format == None:
            format = self.formatFichierOut
        if format in generator.plugins:
            # Le generateur existe on l'utilise
            self.generator = generator.plugins[format]()
            try:
                jdc_formate = self.generator.gener(
                    self.jdc,
                    format=formatLigne,
                    config=self.appliEficas.maConfiguration,
                    appliEficas=self.appliEficas,
                )
                if pourRun:
                    jdc_formate = self.generator.textePourRun
                if self.code == "TELEMAC":
                    jdc_formate = self.generator.texteDico
            except ValueError as e:
                self.informe("Erreur a la generation", str(e), "red")
                return

            if not self.generator.cr.estvide():
                self.informe(
                    "Erreur a la generation",
                    "EFICAS ne sait pas convertir ce JDC",
                    "red",
                )
                return ""
            else:
                return jdc_formate
        else:
            # Il n'existe pas c'est une erreur
            self.informe("Format inconnu", self.format + " non reconnu")
            return ""

    # ------------------------------#
    def verifieChecksum(self, text):
    # ------------------------------#
        # Attention : souci sous Windows
        #
        indexDeb = text.find("#CHECKSUM:")
        if indexDeb < 0:
            return 1, text
        indexFin = text.find(":FIN CHECKSUM")
        checkAvant = text[indexDeb : indexFin + 13]
        textJDC = text[0:indexDeb] + text[indexFin + 13 : -1]
        if self.code != "PSEN" and self.code != "PSEN_N1":
            checksum = self.getChecksum(textJDC)
            pareil = checkAvant == checksum
        else:
            pareil = 1
        return pareil, textJDC

    # ---------------------------#
    def getChecksum(self, texte):
    # ---------------------------#
        try:
            import hashlib

            newtexte = texte.replace('"', '\\"')
            hash_checksum = hashlib.md5()
            hash_checksum.update(newtexte.encode("utf-8"))
            checksum = hash_checksum.hexdigest()
            ligne = "#CHECKSUM:" + checksum + ":FIN CHECKSUM"
        except:
            try:
                newtexte = texte.replace('"', '\\"')
                commande = 'echo "' + newtexte + '"|md5sum'
                a = os.popen(commande)
                checksum = a.read()
                a.close()
            except:
                checksum = "Fichier trop long \n"
            ligne = "#CHECKSUM:" + checksum[0:-1] + ":FIN CHECKSUM"
        return ligne

    # ----------------------#
    def getDico(self):
    # ---------------------#
        if "dicoImbrique" in generator.plugins:
            self.generator = generator.plugins["dicoImbrique"]()
            # print (self.generator)
            jdc_formate = self.generator.gener(self.jdc)
            dico = self.generator.Dico
            return dico
        else:
            self.afficheInfos(
                tr("Format %s non reconnu", "Dictionnaire Imbrique"), "red"
            )
            return ""

    # -----------------------------------------#
    def chercheGroupes(self):
    # -----------------------------------------#
        listeMA, listeNO = self.getTextJDC("GroupMA")
        return listeMA, listeNO

    # -----------------------------------------#
    def chercheDico(self):
    # -----------------------------------------#
        dicoCourant = {}
        format = self.appliEficas.formatFichierOut
        if format in generator.plugins:
            # Le generateur existe on l'utilise
            self.generator = generator.plugins[format]()
            jdc_formate = self.generator.gener(
                self.jdc, format="beautifie", config=self.appliEficas.maConfiguration
            )
            dicoCourant = self.generator.dico
        return dicoCourant

    # -----------------------------------------------------------------#
    def saveFileLegerAs(self, fileName=None):
    # -----------------------------------------------------------------#
        if fileName != None:
            self.fichier = fileName
            return self.saveFileLeger(fileName)
        return self.saveFileLeger()

    # -----------------------------------------------------------------#
    def saveFileComplet(self, fichier=None, formatLigne="beautifie"):
    # -----------------------------------------------------------------#
        fn = fichier
        self.generator = generator.plugins[self.format]()
        print(self.generator)
        if hasattr(self.generator, "writeComplet"):
            self.generator.writeComplet(
                fichier,
                self.jdc,
                config=self.appliEficas.maConfiguration,
                appliEficas=self.appliEficas,
            )

    # -----------------------------------#
    def saveUQFile(self, fichier=None):
    # ------------------------------------#
        if fichier == None:
            self.informe("Sauvegarde", "nom de fichier obligatoire pour sauvegarde")
            return 0, None
        self.fichier = fichier
        self.generator = generator.plugins["UQ"]()
        ret, comm = self.generator.creeNomsFichiers(fichier)
        # print (ret,comm)
        if not ret:
            self.informe("Sauvegarde UQ", self.generator.commentaire)
            return ret, None
        ret = self.generator.gener(self.jdc)
        if not ret:
            self.informe("Sauvegarde UQ", self.generator.commentaire)
            return ret, None
        if ret == 2:
            self.informe("Sauvegarde UQ", self.generator.commentaire, critique=False)
            self.modified = False
            return 1, fichier
        ret = self.generator.writeUQ(fichier)
        if not ret:
            self.informe("Sauvegarde UQ", self.generator.commentaire)
        else:
            self.informe(
                "Sauvegarde UQ",
                "Sauvegardes des fichiers .comm, _det.comm  effectuées.\n"
                "Création des fichiers _UQ.py et _@det.comm.",
                critique=False,
            )
        self.modified = False
        return ret, fichier

    # ------------------------------------------#
    def sauvePourPersalys(self, fichier=None):
    # -------------------------------------------#
        if fichier == None:
            self.informe(
                "Sauvegarde Etude Persalys",
                "nom de fichier obligatoire pour sauvegarde",
            )
            return 0, None
        self.generator = generator.plugins["UQ"]()
        ret, comm = self.generator.creeNomsFichiers(fichier)
        if not ret:
            self.informe("Sauvegarde Etude Persalys", self.generator.commentaire)
        fichierPersalys = self.generator.fichierUQExe
        ret = self.generator.gener(self.jdc)
        if not ret:
            self.informe("Sauvegarde Etude Persalys", self.generator.commentaire)
            return ret, None
        txt = self.generator.txtScriptPersalys.split(
            "################ CUT THE FILE HERE IF YOU WANT TO IMPORT IT IN THE SALOME PERSALYS MODULE ################"
        )[0]
        try:
            with open(fichierPersalys, "w") as f:
                f.write(txt)
                f.close()
            self.informe(
                "Sauvegarde Etude Persalys",
                "Le fichier " + str(fichierPersalys) + " a été sauvegardé",
                critique=False,
            )
            return 1, " "
        except IOError as why:
            self.informe(
                "Sauvegarde Etude Persalys",
                "Le fichier " + str(fichierPersalys) + " n a pas pu etre sauvegardé",
            )
            return 0, str(why)

    # -----------------------------------------------#
    def exeUQ(self, fichier=None, path=None):
    # ------------------------------------------------#
        self.informe("Pas prevu pour l instant")
        return ret, None

    # ---------------------------------------------
    # Methodes Surchargees par avecIhm
    # ---------------------------------------------

    # --------------------------------#
    def ajoutCommentaire(self):
    # --------------------------------#
        print("pas programme sans Ihm")
        print("prevenir la maintenance du besoin")

    # --------------------------------------#
    def informe(self, titre, txt, critique=True):
    # --------------------------------------#
        # methode differenre avec et sans ihm
        if critique:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(titre)
        print(txt)
        if critique:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # --------------------------------------#
    def afficheInfos(self, txt, couleur=None):
    # --------------------------------------#
        # methode differenre avec et sans ihm
        print(txt)

    # -----------------------------------------------------------------------#
    def _viewText(self, txt, caption="FILE_VIEWER", largeur=1200, hauteur=600):
    # --------------------------------------------------------------------#
        print("_____________________________")
        print(txt)
        print("_____________________________")

    # -----------------------------------------------------------------#
    def saveFile(self, fichier, formatLigne="beautifie"):
    # -----------------------------------------------------------------#
        """
        Public slot to save the text to a file.

        @param path directory to save the file in (string or QString)
        @return tuple of two values (boolean, string) giving a success indicator and
            the name of the saved file
        """

        self.fichierOut = fichier
        if not (self.writeFile(fichier, formatLigne=formatLigne)):
            return (0, None)
        if self.jdc.cata.modeleMetier and self.jdc.isValid():
            if self.generator != self.XMLGenerator:
                self.XMLGenerator.gener(self.jdc)
                self.XMLGenerator.writeDefault(fichier)
                return (1, self.fichier)
        if self.jdc.isValid() and hasattr(self.generator, "writeDefault"):
            self.generator.writeDefault(fichier)
        elif self.code == "TELEMAC" and hasattr(self.generator, "writeDefault"):
            self.generator.writeDefault(fichier)
        self.modified = 0
        return (1, self.fichier)

    #

    # ----------------------------------------------#
    def sauveLigneFile(self):
    # ----------------------------------------------#
        self.modified = 1
        return self.saveFile(formatLigne="Ligne")

    # -----------------------------------#
    def updateJdc(self, itemApres, texte):
    # ------------------------------------#
        # ajoute une etape  de JdC a partir d un texte
        monItem = itemApres
        etape = monItem.item.object
        CONTEXT.setCurrentStep(etape)
        etape.buildIncludeInclude(texte)
        self.tree.racine.buildChildren()

    # -----------------------------------#
    def updateJdcEtape(self, itemApres, texte):
    # ------------------------------------#
        # ajoute une etape  de JdC a partir d un texte
        monItem = itemApres
        etape = monItem.item.object
        CONTEXT.set_current_step(etape)
        try:
            ok = etape.build_includeEtape(texte)
        except:
            ok = 0
        if not ok:
            QMessageBox.information(
                self, tr("Import texte"), tr("Impossible d importer le texte")
            )
        self.tree.racine.build_children()
        return ok

    # -------------------------------------#
    def deleteEtape(self, etape):
    # -------------------------------------#
        # dans le JDC
        self.jdc.suppentite(etape)

    # -------------------------------------#
    def deleteMC(self, etape, MCFils, listeAvant=()):
    # -------------------------------------#
        # dans le JDC
        ouChercher = etape
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if monMC != None:
            ouChercher.suppentite(monMC)
        ouChercher.state = "changed"
        ouChercher.isvalid()

    # --------------------------------------------------------#
    def ajoutMC(self, etape, MCFils, valeurs, listeAvant=()):
    # --------------------------------------------------------#
        # dans le JDC
        debug = False
        if debug:
            print("ajoutMC", etape, MCFils, valeurs, listeAvant)
        ouChercher = etape
        if debug:
            print(ouChercher)
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if monMC == None:
            monMC = ouChercher.addEntite(MCFils)
        monMC.valeur = valeurs
        monMC.val = valeurs
        monMC.state = "changed"
        monMC.isvalid()
        return 1

    # --------------------------------------------------------#
    def ajoutMCinMCFactUnique(self, etape, MCFils, valeurs, listeAvant=()):
        # Attention si +sieursMCFACT
    # --------------------------------------------------------#
        # dans le JDC
        debug = False
        if debug:
            print("ajoutMC", etape, MCFils, valeurs, listeAvant)
        ouChercher = etape
        if debug:
            print(ouChercher)
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
        # Attention si +sieursMCFACT
        ouChercher = ouChercher[0]
        if debug:
            print(ouChercher)
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if monMC == None:
            monMC = ouChercher.addEntite(MCFils)
        monMC.valeur = valeurs
        monMC.val = valeurs
        monMC.state = "changed"
        monMC.isValid()
        return 1

    # ----------------------------------------------#
    def ajoutMCFact(self, etape, MCFils, listeAvant=()):
    # ----------------------------------------------#
        # dans le JDC
        ouChercher = etape
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
        monMC = etape.getChild(ouChercher, restreint="oui")
        if monMC == None:
            monMC = ouChercher.addEntite(MCFils)
        monMC.isvalid()

    # -----------------------------------------------------------------#
    def setValeurMCSimpInEtape(self, etape, listeAvant, valeur):
    # -----------------------------------------------------------------#
        # pour VP
        monObj = etape
        for mot in listeAvant:
            monObj = monObj.getChild(mot, restreint="oui")
            if monObj == None:
                return False
        if monObj == None:
            return False
        if monObj.valeur != valeur:
            # PNPN le setValeur fait des bugs --> pourquoi
            # monObj.setValeur(valeur)
            monObj.valeur = valeur
            monObj.isValid()
        return True

    # -------------------------------------------------#
    def getValeur(self, nomEtape, MCFils, listeAvant=()):
    # -------------------------------------------------#
        # dans le JDC

        debug = 0
        ouChercher = None
        for e in self.jdc.etapes:
            if e.nom == nomEtape:
                ouChercher = e
                break
        if debug:
            print("etape trouvee", ouChercher)
        if ouChercher == None:
            return None
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
            if debug:
                print(mot, ouChercher)
            if ouChercher == None:
                return None
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if debug:
            print("monMC", monMC)
        if monMC == None:
            return None
        return monMC.valeur

    # -------------------------------------------------#
    def getMCDsEtape(self, etape, MCFils, listeAvant=()):
    # -------------------------------------------------#
        # dans le JDC

        if etape == None:
            return None
        ouChercher = etape
        debug = 0
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
            if debug:
                print(mot, ouChercher)
            if ouChercher == None:
                return None
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if debug:
            print("monMC", monMC)
        return monMC

    # -----------------------------------------------------------#
    def setValeur(self, nomEtape, MCFils, valeur, listeAvant=()):
    # --------------------------------------------------------#
        # dans le JDC

        ouChercher = None
        for e in self.jdc.etapes:
            if e.nom == nomEtape:
                ouChercher = e
                break
        if ouChercher == None:
            return None
        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
            # print (mot, ouChercher)
            if ouChercher == None:
                return None
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        monMC.set_valeur(valeur)
        monMC.isvalid()

    # -----------------------------------------------------------#
    def changeIntoMC(self, etape, MCFils, valeurs, listeAvant=()):
    # -----------------------------------------------------------#
        # dans le JDC
        ouChercher = etape
        if isinstance(etape, str):
            ouChercher = None
            for e in self.jdc.etapes:
                if e.nom == etape:
                    ouChercher = e
                    break
        if ouChercher == None:
            return

        for mot in listeAvant:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
            if ouChercher == None:
                return
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if monMC == None:
            monMC = ouChercher.addEntite(MCFils)

        monMC.definition.into = valeurs
        from Noyau.N_VALIDATOR import IntoProtocol

        monMC.definition.intoProto = IntoProtocol(
            "into",
            into=monMC.definition.into,
            val_min=monMC.definition.val_min,
            val_max=monMC.definition.val_max,
        )
        monMC.state = "changed"
        monMC.isvalid()

    # -------------------------------------------------------------------#
    def reCalculeValiditeMCApresChgtInto(self, nomEtape, MCFils, listeAvant=()):
    # -------------------------------------------------------------------#
        # dans le JDC
        for e in self.jdc.etapes:
            if e.nom == nomEtape:
                ouChercher = e
                break

        for mot in listeAvant:
            try:
                ouChercher = ouChercher.getChild(mot, restreint="oui")
            # Le mot clef n est pas la
            except:
                return 0
        try:
            monMC = ouChercher.getChild(MCFils, restreint="oui")
        # Le mot clef n est pas la
        except:
            return 0
        if monMC == None:
            return 0

        if hasattr(monMC.definition, "into"):
            if type(monMC.definition.into) == types.FunctionType:
                maListeDeValeur = monMC.definition.into()
            else:
                maListeDeValeur = monMC.definition.into
        else:
            return 0

        monMC.state = "changed"
        return 1

    def dumpXsd(self, avecEltAbstrait=False):
    # -----------------------------------------#
        if not self.readercata.cata:
            return
        texteXSD = self.readercata.cata.JdC.dumpXsd(avecEltAbstrait)
        return texteXSD

    def dumpStructure(self):
    # ----------------------------#
        texteStructure = self.readercata.cata.JdC.dumpStructure()
        return texteStructure

    def dumpGitStringFormat(self):
    # ----------------------------#
        texteGitStringFormat = self.readercata.cata.JdC.dumpGitStringFormat()
        return texteGitStringFormat

    # -------------------------------------#
    def changeDefautDefMC(self, nomEtape, listeMC, valeurs):
    # -------------------------------------#
        # dans le MDD

        # if isinstance (etape, str):
        #  for e in self.jdc.etapes:
        #    if e.nom == etape : etape=e; break
        # if etape == None : return
        definitionEtape = getattr(self.jdc.cata, nomEtape)
        # definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        ouChercher = definitionEtape
        if len(listeMC) > 1:
            for mc in listeMC[0:-1]:
                mcfact = ouChercher.entites[mc]
                ouChercher = mcfact

        mcAccas = ouChercher.entites[listeMC[-1]]
        mcAccas.defaut = valeurs
        return 1

    # ------------------------------------------------#
    def changeIntoDefMC(self, etape, listeMC, valeurs, rechercheParNom=False):
    # ------------------------------------------------#
        # dans le MDD
        # definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        # definitionEtape=getattr(self.jdc.cata,nomEtape)
        print("changeIntoDefMC ", etape, listeMC, valeurs)
        # ouChercher = getattr(self.jdc.cata, etape.nom)
        if rechercheParNom:
            ouChercher = getattr(self.jdc.cata, etape)
        else:
            ouChercher = getattr(self.jdc.cata, etape.nom)

        # if len(listeMC) > 1 :
        #   for mc in listeMC[0:-1]:
        #     mcfact=ouChercher.entites[mc]
        #     ouChercher=mcfact
        # mcAccas=ouChercher.entites[listeMC[-1]]

        for mc in listeMC:
            mcAccas = ouChercher.entites[mc]
            ouChercher = mcAccas
            if ouChercher == None:
                return 0

        if hasattr(mcAccas, "into"):
            oldValeurs = mcAccas.into
        else:
            oldValeurs = None

        if oldValeurs == valeurs:
            return 1
        mcAccas.into = valeurs
        from Noyau.N_VALIDATOR import IntoProtocol

        mcAccas.intoProto = IntoProtocol(
            "into", into=valeurs, val_min=mcAccas.val_min, val_max=mcAccas.val_max
        )
        return 1

    # -------------------------------------------------------------#
    def deleteDefinitionMC(self, etape, listeAvant, nomDuMC):
    # -------------------------------------------------------------#
        # dans le MDD
        # print 'in deleteDefinitionMC', etape,listeAvant,nomDuMC
        if isinstance(etape, str):
            for e in self.jdc.etapes:
                if e.nom == etape:
                    etape = e
                    break
        if etape == None:
            return
        # definitionEtape=getattr(self.jdc.cata[0],etape)
        definitionEtape = getattr(self.jdc.cata, etape)
        ouChercher = definitionEtape
        for k in listeAvant:
            ouChercher = ouChercher.entites[k]
        MCADetruire = ouChercher.entites[nomDuMC]
        ouChercher.ordreMC.remove(nomDuMC)
        print("remove de ", nomDuMC)
        del ouChercher.entites[nomDuMC]
        del self.dicoNouveauxMC[nomDuMC]

    # -------------------------------------------------------------#
    def ajoutDefinitionMC(self, nomEtape, listeAvant, nomDuMC, typ, **args):
    # -------------------------------------------------------------#
        # dans le MDD
        # definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        definitionEtape = getattr(self.jdc.cata, nomEtape)
        ouChercher = definitionEtape
        for k in listeAvant:
            ouChercher = ouChercher.entites[k]
        from Accas import A_SIMP

        Nouveau = A_SIMP.SIMP(typ, **args)
        Nouveau.pere = ouChercher
        Nouveau.nom = nomDuMC
        # Nouveau.ordreMC=[]
        ouChercher.entites[nomDuMC] = Nouveau
        ouChercher.ordreMC.append(nomDuMC)
        # print ('ajout de ', nomDuMC)
        # traceback.print_stack()
        # ajout CIST sauvegarde
        if nomDuMC in self.dicoNouveauxMC:
            del self.dicoNouveauxMC[nomDuMC]
        self.dicoNouveauxMC[nomDuMC] = (
            "ajoutDefinitionMC",
            nomEtape,
            listeAvant,
            nomDuMC,
            typ,
            args,
        )
        # print self.dicoNouveauxMC

    # ---------------------------------------------------------------------#
    def ajoutDefinitionMCFact(self, nomEtape, listeAvant, nomDuMC, listeMC, **args):
    # ---------------------------------------------------------------------#
        # dans le MDD
        print("ajoutDefinitionMCFact", nomDuMC)
        # definitionEtape=getattr(self.jdc.cata[0],nomEtape)
        definitionEtape = getattr(self.jdc.cata, nomEtape)
        ouChercher = definitionEtape
        for k in listeAvant:
            ouChercher = ouChercher.entites[k]
        from Accas import A_SIMP

        for mc in listeMC:
            nomMC = mc[0]
            typMC = mc[1]
            argsMC = mc[2]
            nouveauMC = A_SIMP.SIMP(typMC, **argsMC)
            nouveauMC.nom = nomMC
            args[nomMC] = nouveauMC
        from Accas import A_FACT

        nouveauFact = A_FACT.FACT(**args)
        nouveauFact.pere = ouChercher
        nouveauFact.nom = nomDuMC
        from Editeur.autre_analyse_cata import traite_entite

        traite_entite(nouveauFact, [])
        ouChercher.entites[nomDuMC] = nouveauFact
        ouChercher.ordreMC.append(nomDuMC)
        self.dicoNouveauxFact[nomDuMC] = (
            "ajoutDefinitionMC",
            nomEtape,
            listeAvant,
            nomDuMC,
            listeMC,
            args,
        )
        # print self.dicoNouveauxMC

    # ----------------------------------------------------#

    # ----------------------------------------------------#
    def changeIntoMCandSet(self, etape, listeMC, into, valeurs):
    # ----------------------------------------------------#
        # dans le MDD et le JDC

        self.changeIntoDefMC(etape, listeMC, into)

        if isinstance(etape, str):
            for e in self.jdc.etapes:
                if e.nom == etape:
                    etape = e
                    break
        if etape == None:
            return

        ouChercher = etape
        for mot in listeMC[:-1]:
            ouChercher = ouChercher.getChild(mot, restreint="oui")
            if ouChercher == None:
                return
        MCFils = listeMC[-1]
        monMC = ouChercher.getChild(MCFils, restreint="oui")
        if monMC == None:
            monMC = etape.addEntite(MCFils)

        monMC.definition.into = into
        monMC.valeur = valeurs
        monMC.val = valeurs
        monMC.state = "changed"
        monMC.isvalid()

    # -------------------------------------#
    def ajoutVersionCataDsJDC(self, txt):
    # -------------------------------------#
        # if not hasattr(self.readercata.cata[0],'VERSION_CATALOGUE'): return txt
        if not hasattr(self.readercata.cata, "VERSION_CATALOGUE"):
            return txt
        ligneVersion = (
            "#VERSION_CATALOGUE:"
            + self.readercata.cata.VERSION_CATALOGUE
            + ":FIN VERSION_CATALOGUE\n"
        )
        texte = txt + ligneVersion
        return texte

    # -------------------------------------#
    def verifieVersionCataDuJDC(self, text):
    # -------------------------------------#
        memeVersion = False
        indexDeb = text.find("#VERSION_CATALOGUE:")
        indexFin = text.find(":FIN VERSION_CATALOGUE")
        if indexDeb < 0:
            self.versionCataDuJDC = "sans"
            textJDC = text
        else:
            self.versionCataDuJDC = text[indexDeb + 19 : indexFin]
            textJDC = text[0:indexDeb] + text[indexFin + 23 : -1]

        self.versionCata = "sans"
        if hasattr(self.readercata.cata, "VERSION_CATALOGUE"):
            self.versionCata = self.readercata.cata.VERSION_CATALOGUE

        if self.versionCata == self.versionCataDuJDC:
            memeVersion = True
        return memeVersion, textJDC

    # -------------------------------#
    def traduitCatalogue(self, texte):
    # -------------------------------#
        nomTraducteur = ( "traduit" + self.readercata.code + self.versionCataDuJDC + "To" + self.versionCata)
        sys.path.append( os.path.abspath( os.path.join( os.path.dirname(__file__), "..","Traducteur")))
        try:
            traducteur = __import__(nomTraducteur)
            monTraducteur = traducteur.MonTraducteur(texte)
            nouveauTexte = monTraducteur.traduit()
            return nouveauTexte
        except:
            return texte

    # ------------------#
    def insertInDB(self):
    # -------------------#
        debug = True
        if debug:
            print("insertInDB ", self.jdc, self.readercata.cata)
        texte = self.jdc.prepareInsertInDB()
        if debug:
            print(texte)

    # -------------------------------------------------#
    def dumpStringDataBase(self, nomDataBaseACreer=None):
    # -------------------------------------------------#
        texteStringDataBase = self.readercata.cata.JdC.dumpStringDataBase( nomDataBaseACreer)
        return texteStringDataBase


if __name__ == "__main__":
    print("a faire")

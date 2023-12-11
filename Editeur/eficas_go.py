#!/usr/bin/env python
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
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

# Modules Python

import sys, os

repIni = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

if sys.version_info[0] < 3:
    print("Must be using Python 3")
    sys.exit()


def lanceEficas(code=None, multi=False, langue="en", labelCode=None, GUI='QT5', salome=0):
# ---------------------------------------------------------------------------------------
    """
      Lance l'appli EFICAS avec Ihm QT
    """
    try:
        from PyQt5.QtWidgets import QApplication
    except:
        print("Please, set qt environment")
        return

    from Editeur import session

    options = session.parse(sys.argv)
    if options.code != None:
        code = options.code

    pathGui='InterfaceGUI.QT5.qtEficas'
    qtEficas =__import__(pathGui, globals(), locals(), ['qtEficas',])

    app = QApplication(sys.argv)
    Eficas = qtEficas.Appli(code=code, salome=salome, multi=multi, langue=langue, labelCode=labelCode, GUI=GUI)
    Eficas.show()

    res = app.exec_()
    sys.exit(res)


def getEficasSsIhm( code=None, multi=False, langue="en", ssCode=None, labelCode=None,
    forceXML=False, genereXSD=False, fichierCata=None,):
# -----------------------------------------------------------------------------------
    """
    instancie l'appli EFICAS sans Ihm
    """
    from Editeur import session

    options = session.parse(sys.argv)
    if options.code != None:
        code = options.code
    if forceXML:
        options.withXSD = True

    from InterfaceQT4.qtEficasSsIhm import AppliSsIhm

    Eficas = AppliSsIhm( code=code, salome=0, multi=multi, langue=langue,
        ssCode=ssCode, labelCode=labelCode, genereXSD=genereXSD, fichierCata=fichierCata,)
    return Eficas


def genereXSD(code=None):
# -----------------------
    from Editeur import session

    options = session.parse(sys.argv)
    if code != None:
        options.code = code
    if options.fichierCata == None:
        print("Use -c cata_name.py")
        return

    monEficasSsIhm = getEficasSsIhm(code=options.code, genereXSD=True)
    monEditor = monEficasSsIhm.getEditor()
    # texteXSD=monEficasSsIhm.dumpXsd(avecEltAbstrait=options.avecEltAbstrait)
    texteXSD = monEditor.dumpXsd(avecEltAbstrait=options.avecEltAbstrait)

    fichierCataTrunc = os.path.splitext(os.path.basename(options.fichierCata))[0]
    # if fichierCataTrunc[0:4] in ('cata','Cata'): fichierCataTrunc=fichierCataTrunc[4:]
    # if fichierCataTrunc[0] in ('_','-') : fichierCataTrunc=fichierCataTrunc[1:]
    fileXSD = fichierCataTrunc + ".xsd"

    f = open(str(fileXSD), "w")
    f.write(str(texteXSD))


def genereXML(code=None):
    # -----------------------
    from Editeur import session

    options = session.parse(sys.argv)
    if code != None:
        options.code = code
    if options.fichierCata == None:
        print("Use -c cata_name.py")
        return
    try:
        fichier = options.comm[0]
    except:
        fichier = None
    if fichier == None:
        print("comm file is needed")
        return

    monEficasSsIhm = getEficasSsIhm(code=options.code, forceXML=True)

    from .editorSsIhm import JDCEditorSsIhm

    monEditeur = JDCEditorSsIhm(monEficasSsIhm, fichier)
    if options.fichierXMLOut == None:
        fichierXMLOut = fichier[: fichier.rfind(".")] + ".xml"
    else:
        fichierXMLOut = options.fichierXMLOut
    if not (monEditeur.jdc.isValid()):
        print("Fichier comm is not valid")
        return
    # print ('Fichier comm is not valid')
    monEditeur.XMLgenerator.gener(monEditeur.jdc)
    monEditeur.XMLgenerator.writeDefault(fichierXMLOut)


def genereStructure(code=None):
    # ------------------------------
    from Editeur import session

    options = session.parse(sys.argv)
    if code != None:
        options.code = code
    if options.fichierCata == None:
        print("Use -c cata_name.py")
        return

    monEficasSsIhm = getEficasSsIhm(code=options.code, genereXSD=True)
    monEditor = monEficasSsIhm.getEditor()
    texteStructure = monEditor.dumpStructure()

    fichierCataTrunc = os.path.splitext(os.path.basename(options.fichierCata))[0]
    fileStructure = fichierCataTrunc + ".txt"
    f = open(str(fileStructure), "w")
    f.write(str(texteStructure))
    f.close()


def validateDataSet(code=None):
    # ------------------------------
    from Editeur import session

    options = session.parse(sys.argv)
    if code != None:
        options.code = code
    if options.fichierCata == None:
        print("Use -c cata_name.py")
        return
    fichier = options.comm[0]
    if fichier == None:
        print("comm file is needed")
        return
    from .editorSsIhm import JDCEditorSsIhm

    monEficasSsIhm = getEficasSsIhm(code=options.code)
    monEditeur = JDCEditorSsIhm(monEficasSsIhm, fichier)
    if not (monEditeur.jdc.isValid()):
        print(monEditeur.getJdcRapport())
    else:
        print("Jdc is valid")
    return monEditeur.jdc.isValid()


def validateFonction(laFonction, debug=False):
    # -------------------------------
    # ici un singleton pour avoir l editor, le catalogue et...
    monEficasSsIhm = getEficasSsIhm(code="Essai")
    monEditor = monEficasSsIhm.getEditor()
    print("_______ validateFonction", laFonction, laFonction.__name__)
    from functools import wraps
    from collections import OrderedDict
    from inspect import getargspec

    @wraps(laFonction)
    def fonctionValidee(*args, **kwargs):
        laFonctionName = laFonction.__name__
        if debug:
            print(
                "Appel {} avec args={} et kwargs={}".format(
                    laFonction.__name__, args, kwargs
                )
            )
        laDefDeLaFonctionDansAccas = getattr(monEditor.readercata.cata, laFonctionName)
        objConstruit = laDefDeLaFonctionDansAccas.makeObjetPourVerifSignature(
            *args, **kwargs
        )
        if objConstruit.isValid():
            ret = laFonction(*args, **kwargs)
            return ret
        else:
            print("mauvais arguments")
            print(objConstruit.CR())
            return None

    return fonctionValidee

    # maClasseAccas=getattr(self.cata,objEtape.monNomClasseAccas)
    return fonctionValidee

    return laFonction


def createFromDocumentAccas(fichierCata=None, fichier=None, code=None):
    # ------------------------------------------------------------
    if fichier == None:
        print("file is needed")
        return None
    if fichierCata == None:
        print("cata file is needed")
        return None

    from Noyau.N_OBJECT import activeSurcharge

    activeSurcharge()

    from .editorSsIhm import JDCEditorSsIhm

    monEficasSsIhm = getEficasSsIhm(code="Essai", fichierCata=fichierCata)
    monEditeur = JDCEditorSsIhm(monEficasSsIhm, fichier)
    return monEditeur.jdc
    # from Noyau


# --------------------------- toutes les fonctions après sont obseletes
def lanceEficas_ssIhm(
    code=None, fichier=None, ssCode=None, version=None, debug=False, langue="en"
):
    """
    Lance l'appli EFICAS SsIhm
    """
    # Analyse des arguments de la ligne de commande
    print("deprecated")
    from Editeur import session

    options = session.parse(sys.argv)
    if version != None and options.version == None:
        options.version = version
    if fichier == None:
        fichier = options.comm[0]
    if code == None:
        code = options.code

    from .qtEficas import Appli

    Eficas = Appli(code=code, salome=0, ssCode=ssCode, ssIhm=True, langue=langue)

    from .ssIhm import QWParentSSIhm

    parent = QWParentSSIhm(code, Eficas, version)

    from . import readercata

    if not hasattr(Eficas, "readercata"):
        monreadercata = readercata.ReaderCata(parent, Eficas)
        Eficas.readercata = monreadercata

    from .editor import JDCEditor

    monEditeur = JDCEditor(Eficas, fichier)
    return monEditeur


def lanceEficas_ssIhm_chercheGroupes(
    code=None, fichier=None, ssCode=None, version=None
):
    print("deprecated")
    monEditeur = lanceEficas_ssIhm(code, fichier, ssCode, version)
    print((monEditeur.chercheGroupes()))


def lanceEficas_ssIhm_cherche_cr(code=None, fichier=None, ssCode=None, version=None):
    print("deprecated")
    monEditeur = lanceEficas_ssIhm(code, fichier, ssCode, version)
    print((monEditeur.jdc.cr))


def lanceEficas_ssIhm_reecrit(
    code=None,
    fichier=None,
    ssCode=None,
    version=None,
    ou=None,
    cr=False,
    debug=False,
    leger=False,
    langue="ang",
):
    print("deprecated")
    # print 'lanceEficas_ssIhm_reecrit', fichier
    monEditeur = lanceEficas_ssIhm(code, fichier, ssCode, version, langue=langue)
    if ou == None:
        fileName = fichier.split(".")[0] + "_reecrit.comm"
        fn = fichier.split(".")[0] + "_cr.txt"
    else:
        f = fichier.split(".")[0] + "_reecrit.comm"
        f1 = os.path.basename(f)
        fn = fichier.split(".")[0] + "_cr.txt"
        f2 = os.path.basename(fn)
        fileName = os.path.join(ou, f1)
        fileCr = os.path.join(ou, f2)
    debut = False
    if debug:
        import cProfile, pstats, StringIO

        pr = cProfile.Profile()
        pr.enable()
        monEditeur.saveFileAs(fileName=fileName)
        pr.disable()
        s = StringIO.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getValue())

    elif not leger:
        monEditeur.saveFileAs(fileName=fileName)
    else:
        monEditeur.saveFileLegerAs(fileName=fileName)
    if cr:
        f = open(fileCr, "w")
        f.write(str(monEditeur.jdc.report()))
        f.close()


def lanceEficas_param(
    code="Adao", fichier=None, version="V0", macro="ASSIMILATION_STUDY"
):
    """
    Lance l'appli EFICAS pour trouver les noms des groupes
    """
    print("deprecated")
    # Analyse des arguments de la ligne de commande
    from Editeur import session

    options = session.parse(sys.argv)

    from .qtEficas import Appli

    from .ssIhm import QWParentSSIhm

    Eficas = QWParentSSIhm(code, version)

    from . import readercata

    if not hasattr(Eficas, "readercata"):
        monreadercata = readercata.ReaderCata(parent, Eficas)
        Eficas.readercata = monreadercata

    from .editor import JDCEditor

    monEditeur = JDCEditor(Eficas, fichier)
    texte = loadJDC(fichier)
    parameters = getJdcParameters(texte, macro)
    return parameters


def getJdcParameters(jdc, macro):
    """
    This function converts the data from the specified macro of the
    specified jdc text to a python dictionnary whose keys are the
    names of the data of the macro.
    """
    print("deprecated")
    context = {}
    source = "def args_to_dict(**kwargs): return kwargs \n"
    source += "%s = _F = args_to_dict          \n" % macro
    source += "parameters=" + jdc + "                        \n"
    source += "context['parameters'] = parameters         \n"
    code = compile(source, "file.py", "exec")
    eval(code)
    parameters = context["parameters"]
    return parameters


def loadJDC(filename):
    """
    This function loads the text from the specified JdC file. A JdC
    file is the persistence file of Eficas (*.comm).
    """
    print("deprecated")
    fcomm = open(filename, "r")
    jdc = ""
    for line in fcomm.readlines():
        if not (line[0] == "#"):
            jdc += "%s" % line

    # Warning, we have to make sure that the jdc comes as a simple
    # string without any extra spaces/newlines
    return jdc.strip()


if __name__ == "__main__":
    import sys

    sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "..")))
    lanceEficas(code=None, multi=True)

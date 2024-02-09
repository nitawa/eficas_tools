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


def lanceEficas(code=None, multi=False, langue="en", labelCode=None, GUIPath='QT5', salome=0):
# -------------------------------------------------------------------------------------------
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

    if GUIPath == 'QT5' or GUIPath == 'cinqC' :
        pathAbso=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','InterfaceGUI',GUIPath))
        if pathAbso not in sys.path : sys.path.insert(0,pathAbso)

    from qt_eficas import QtEficasAppli
    app = QApplication(sys.argv)
    Eficas = QtEficasAppli(code=code, salome=salome, multi=multi, langue=langue, labelCode=labelCode, GUIPath=GUIPath)
    Eficas.show()

    res = app.exec_()
    sys.exit(res)


def getEficas( code=None, multi=False, langue="en", ssCode=None, labelCode=None,
    forceXML=False, genereXSD=False, fichierCata=None,GUIPath=None, salome = False):
# -----------------------------------------------------------------------------------
    """
    instancie l'appli EFICAS sans Ihm
    """

    from Editeur import session
    options = session.parse(sys.argv)
    if options.code != None:
        code = options.code
    if forceXML: options.withXSD = True

    if GUIPath in ('QT5',  'cinqC', 'Web') :
        pathAbso=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','InterfaceGUI',GUIPath))
        if pathAbso not in sys.path : sys.path.insert(0,pathAbso)

    from Editeur.eficas_appli import EficasAppli
    Eficas = EficasAppli( code=code, salome=salome, multi=multi, langue=langue,
        ssCode=ssCode, labelCode=labelCode, genereXSD=genereXSD, fichierCata=fichierCata)
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

    monEficas = getEficas(code=options.code, genereXSD=True)
    monEditor = monEficas.getEditor()
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

    monEficas = getEficas(code=options.code, forceXML=True)

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

    monEficas = getEficas(code=options.code, genereXSD=True)
    monEditor = monEficas.getEditor()
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

    monEficas = getEficas(code=options.code)
    monEditeur = JDCEditorSsIhm(monEficasSsIhm, fichier)
    if not (monEditeur.jdc.isValid()):
        print(monEditeur.getJdcRapport())
    else:
        print("Jdc is valid")
    return monEditeur.jdc.isValid()


# Les deux fonctions ci-après ne sont pas utilisees mais 
# restent des idees interessantes

def validateFonction(laFonction, debug=False):
# ---------------------------------------------
# permet de verifier les arguments d une fonction python
# exposee dans un catalogue
# ceci etait juste une essai mais garde au cas ou  
    monEficas = getEficas(code="Essai")
    monEditor = monEficas.getEditor()
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



def createObjetPythonFromDocumentAccas(fichierCata=None, fichier=None, code=None):
# --------------------------------------------------------------------------------
# activeSurcharge permet de surcharger [ pour
# acceder aux objets Accas comme en python
# Attention peu testé et uniquement en lecture
    if fichier == None:
        print("file is needed")
        return None
    if fichierCata == None:
        print("cata file is needed")
        return None

    from Accas.processing.P_OBJECT import activeSurcharge
    activeSurcharge()
    from .editorSsIhm import JDCEditorSsIhm

    monEficas = getEficas(code="Essai", fichierCata=fichierCata)
    monEditeur = JDCEditorSsIhm(monEficas, fichier)
    return monEditeur.jdc


if __name__ == "__main__":
    pass

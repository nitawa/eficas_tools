# -*- coding: utf-8 -*-
# copyright 2012 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
"""

"""

import os

try:
    from PyQt5.QtCore import QTranslator
    code_translator = QTranslator()
    eficas_translator = QTranslator()
except:
    code_translator = None
    eficas_translator = None
    print("pas d import de qt, pas de traduction")


def localise(application, locale=None, file=None, translatorFile=None, debug=False):
    """ 
    file contient les traductions eficas
    translatorFile contient les traductions specifiques au code
    pour l instant ne fonctionne qu avec qt
    """
    if code_translator == None:
        print("qt not avalaible, no translation")
        return

    from PyQt5.QtCore import QLibraryInfo
    from PyQt5.QtCore import QLocale
    from PyQt5.QtWidgets import QApplication
    monPath = os.path.join(os.path.dirname(__file__), "..","..", "UiQT5")
    sys_locale = QLocale.system().name()

    if locale is None : locale = "fr"
    if locale == "ang": locale = "en"

    if file == None and translatorFile == None 	:
        if debug: print("pas de fichier de traduction a charger")
        return

    if file :
        print("chargement du fichier de traduction : ", file, monPath)
        if eficas_translator.load(file, monPath) :
          if debug : print( file, " loaded")
        else  : 
          print( 'pb au chargement du fichier de traduction :', file)
        QApplication.installTranslator(eficas_translator)

    if translatorFile :
        print("chargement du fichier de traduction specifique : ", translatorFile)
        if (code_translator.load(translatorFile)) and debug : print(translatorFile, " loaded")
        elif code_translator.load(translatorFile + "_" + locale) and debug:
            print(translatorFile + "_" + locale + " loaded")
        elif debug: print( "Unable to load Code translator! No file or No translation" + translatorFile)
        if debug: print(QApplication.installTranslator(code_translator))
        else: QApplication.installTranslator(code_translator)


if __name__ == "__main__":
    import sys
    localise(sys.argv[1])

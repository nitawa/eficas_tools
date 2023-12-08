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


def localise(application, locale=None, file=None, translatorFichier=None, debug=False):
    """ """
    if code_translator == None:
        print("qt not avalaible, no translation")
        return
    from PyQt5.QtCore import QLibraryInfo
    from PyQt5.QtCore import QLocale
    from PyQt5.QtWidgets import QApplication

    monPath = os.path.join(os.path.dirname(__file__), "..", "UiQT5")

    sys_locale = QLocale.system().name()

    if locale is None:
        locale = "fr"
    if locale == "ang":
        locale = "en"

    if file != None and debug:
        print("chargement de ", file, monPath)
        print(eficas_translator.load(file, monPath))
        print(QApplication.installTranslator(eficas_translator))
    elif eficas_translator.load("eficas_" + locale, monPath):
        QApplication.installTranslator(eficas_translator)
    elif debug:
        print("Unable to load Eficas translator!")

    if debug:
        print("translatorFichier :", translatorFichier)
    if translatorFichier != None:
        if (code_translator.load(translatorFichier)) and debug:
            print(translatorFichier, " loaded")
        elif code_translator.load(translatorFichier + "_" + locale) and debug:
            print(translatorFichier + "_" + locale + " loaded")
        elif debug:
            print(
                "Unable to load Code translator! No file or No translation"
                + translatorFichier
            )
        if debug:
            print(QApplication.installTranslator(code_translator))
        else:
            QApplication.installTranslator(code_translator)


if __name__ == "__main__":
    import sys

    localise(sys.argv[1])

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
#    permet de lancer  EFICAS en n affichant rien



class appliEficasSSIhm(object):
    def __init__(self, code):
        self.VERSION_EFICAS = "Sans Ihm"
        self.code = code
        self.ssCode = None
        self.salome = None
        self.top = None
        self.indice = 0
        self.dict_reels = {}
        self.listeAEnlever = []

        name = "prefs_" + self.code
        try:
            prefsCode = __import__(name)
        except:
            name = "prefs_" + self.code.upper()
            self.code = self.code.upper()
            prefsCode = __import__(name)

        self.repIni = prefsCode.repIni
        self.format_fichier = "python"  # par defaut

        nameConf = "configuration_" + self.code
        configuration = __import__(nameConf)
        self.CONFIGURATION = configuration.make_config(self, prefsCode.repIni)


class QWParentSSIhm(object):
    def __init__(self, code, version_code):
        self.ihm = "QT"
        self.code = code
        self.version_code = version_code
        self.format_fichier = "python"  # par defaut

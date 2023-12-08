# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
    Ce module contient le chargeur dynamique de plugins (emprunte a HappyDoc)
"""

import glob, os, sys, traceback
from collections import UserDict


class PluginLoader(UserDict):
    def __init__(self, module):
        UserDict.__init__(self)
        self.plugin_dir = module.__path__[0]
        self.plugin_setName = module.__name__
        _module_list = glob.glob(
            os.path.join(
                self.plugin_dir,
                "%s*py" % self.plugin_setName,
            )
        )
        _module_list.sort()

        for _module_name in _module_list:
            _module_name = os.path.basename(_module_name)[:-3]
            _import_name = "%s.%s" % (self.plugin_setName, _module_name)

            try:
                _module = __import__(_import_name)
            except:
                sys.stderr.write("\n--- Plugin Module Error ---\n")
                traceback.print_exc()
                sys.stderr.write("---------------------------\n\n")
                continue
            try:
                _module = getattr(_module, _module_name)
            except AttributeError:
                sys.stderr.write("ERROR: Could not retrieve %s\n" % _import_name)

            try:
                info = _module.entryPoint()
            except AttributeError:
                pass
            else:
                self.addEntryPoint(info)

    def addEntryPoint(self, infoDict):
        name = infoDict["name"]
        factory = infoDict["factory"]
        self[name] = factory

#!/usr/bin/env python
# Copyright (C) 2007-2012   EDF R&D
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
import sys, os
from pathlib import Path

code="ReacteurNumerique" 

try :
    eficasPath=os.environ['EFICAS_ROOT_DIR']
except :
    print ('Please, set EFICAS_ROOT_DIR')
    exit(1)
sys.path.append(os.path.join(os.path.abspath(eficasPath)))

name='prefs_' + code
prefFile = Path(name + ".py")
if prefFile.is_file():
    try : 
        __import__(name)
    except : 
        print ('Unable to import {}').format(prefFile)
        exit(1)
from Editeur import eficas_go
eficas_go.lanceEficas(code=code,GUIPath='QT5')

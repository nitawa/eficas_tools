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
from Noyau import N_FACT
from Ihm import I_ENTITE
from Accas import A_MCFACT
from Accas import A_MCLIST
from Efi2Xsd.AccasXsd import X_FACT


class FACT(N_FACT.FACT, X_FACT, I_ENTITE.ENTITE):
    """
    Accas class for catalog definition keyword FACT
    """
    class_instance = A_MCFACT.MCFACT
    list_instance = A_MCLIST.MCList

    def __init__(self, *tup, **args):
        I_ENTITE.ENTITE.__init__(self)
        N_FACT.FACT.__init__(self, *tup, **args)


from Noyau import N_OBJECT
from Ihm import I_OBJECT

class ErrorObj(I_OBJECT.ErrorObj, N_OBJECT.ErrorObj):
    pass


N_OBJECT.ErrorObj = ErrorObj

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
from Noyau import N_MCBLOC
from Validation import V_MCBLOC
from Ihm import I_MCBLOC
from Efi2Xsd.MCAccasXML import X_MCBLOC


class MCBLOC(I_MCBLOC.MCBLOC, N_MCBLOC.MCBLOC, X_MCBLOC, V_MCBLOC.MCBLOC):
    """
    class of BLOC objet
    """

    def __init__(self, val, definition, nom, parent, dicoPyxbDeConstruction=None):
        N_MCBLOC.MCBLOC.__init__(
            self,
            val,
            definition,
            nom,
            parent,
            dicoPyxbDeConstruction=dicoPyxbDeConstruction,
        )
        V_MCBLOC.MCBLOC.__init__(self)

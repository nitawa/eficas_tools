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
from Noyau import N_PROC_ETAPE
from Validation import V_PROC_ETAPE
from Ihm import I_PROC_ETAPE
from Efi2Xsd.MCAccasXML import X_MCCOMPO


class PROC_ETAPE(
    I_PROC_ETAPE.PROC_ETAPE, V_PROC_ETAPE.PROC_ETAPE, X_MCCOMPO, N_PROC_ETAPE.PROC_ETAPE
):
    """
    Accas class for dataset object PROC_ETAPE
    """

    def __init__(self, oper=None, args={}):
        N_PROC_ETAPE.PROC_ETAPE.__init__(self, oper=oper, args=args)
        V_PROC_ETAPE.PROC_ETAPE.__init__(self)

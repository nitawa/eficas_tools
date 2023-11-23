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
from __future__ import absolute_import
from Noyau import N_REGLE
from Validation import V_PRESENT_PRESENT
from Ihm import I_PRESENT_PRESENT


class PRESENT_PRESENT(I_PRESENT_PRESENT.PRESENT_PRESENT,
                      V_PRESENT_PRESENT.PRESENT_PRESENT,
                      N_REGLE.REGLE):
    """
    Accas class for catalog rule PRESENT_PRESENT
    """
    pass

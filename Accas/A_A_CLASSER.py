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
from Noyau import N_REGLE
from Validation import V_A_CLASSER
from Ihm import I_A_CLASSER


class A_CLASSER(V_A_CLASSER.A_CLASSER, N_REGLE.REGLE, I_A_CLASSER.A_CLASSER):
    """
    Accas class for catalog rule A_CLASSER 
    It is absolutely necessary that V_A_CLASSER be first in the inheritance
    """
    # to do --> prevoir un X_A_CLASSER pour la projection XSD 
    # Est-ce possible en 1ere passe ou faut-il modifier pendant une 2nd passe ?
    # ajouter une methode dump a tous les objets ?
    pass

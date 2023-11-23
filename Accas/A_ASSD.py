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

from Ihm import I_ASSD
from Ihm import I_LASSD
from Ihm import I_FONCTION
from Noyau import N_ASSD
from Noyau import N_GEOM
from Noyau import N_FONCTION
from Noyau import N_CO
from Noyau import N_UserASSD
from Noyau import N_UserASSDMultiple

# On ajoute la classe ASSD dans l'heritage multiple pour recreer
# une hierarchie d'heritage identique a celle de Noyau
# pour faire en sorte que isinstance(o,ASSD) marche encore apres
# derivation


class ASSD(I_ASSD.ASSD, N_ASSD.ASSD):
    pass

# class LASSD(I_LASSD.LASSD,N_LASSD.LASSD):pass
class LASSD(I_LASSD.LASSD):
    pass

class UserASSD(N_UserASSD.UserASSD, ASSD):
    pass

class UserASSDMultiple(N_UserASSDMultiple.UserASSDMultiple, UserASSD):
    pass

class assd(N_ASSD.assd, I_ASSD.assd, ASSD):
    pass

class FONCTION(N_FONCTION.FONCTION, I_FONCTION.FONCTION, ASSD):
    def __init__(self, etape=None, sd=None, reg="oui"):
        N_FONCTION.FONCTION.__init__(self, etape=etape, sd=sd, reg=reg)
        I_FONCTION.FONCTION.__init__(self, etape=etape, sd=sd, reg=reg)

class formule(I_FONCTION.formule, N_FONCTION.formule, ASSD):
    def __init__(self, etape=None, sd=None, reg="oui"):
        N_FONCTION.formule.__init__(self, etape=etape, sd=sd, reg=reg)
        I_FONCTION.formule.__init__(self, etape=etape, sd=sd, reg=reg)

class formule_c(formule):
    pass

# On conserve fonction (ceinture et bretelles)
# fonction n'existe plus dans N_FONCTION on le remplace par formule
class fonction(N_FONCTION.formule, I_FONCTION.fonction, ASSD):
    """ obsolete class : use formule instead"""
    def __init__(self, etape=None, sd=None, reg="oui"):
        N_FONCTION.formule.__init__(self, etape=etape, sd=sd, reg=reg)
        I_FONCTION.fonction.__init__(self, etape=etape, sd=sd, reg=reg)

class GEOM(N_GEOM.GEOM, I_ASSD.GEOM, ASSD):
    pass

class geom(N_GEOM.geom, I_ASSD.geom, ASSD):
    pass

class CO(N_CO.CO, I_ASSD.CO, ASSD):
    pass

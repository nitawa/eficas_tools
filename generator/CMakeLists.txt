# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2024  EDF R&D                 
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================


install ( FILES __init__.py generator_python.py Formatage.py generator_aplat.py 
               generator_dicoImbrique.py generator_dico.py generator_modification.py generator_vers3DSalome.py
               generator_TELEMAC.py generator_map.py generator_GroupMA.py 
          DESTINATION ${CMAKE_INSTALL_PREFIX}/generator
        )



# Installation des fichiers : CARMEL
if (WITH_CARMEL)
  install ( FILES generator_CARMEL3D_frequentiel.py generator_CARMEL3D_temporel.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/generator
          )
endif (WITH_CARMEL)




### Local Variables:
### mode: cmake
### End:

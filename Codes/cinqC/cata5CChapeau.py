# -*- coding: utf-8 -*-

# TODO: Create a main object that point on the different subobjects and force its name

# EFICAS
from Accas import  JDC_CATA_SINGLETON
VERSION_CATALOGUE = "V_0"

JdC = JDC_CATA_SINGLETON(code="Gui5C")

from cataJobPerformance         import MyJobPerformance
from cataJobSelection           import Selection
from cataJobSelection           import PresentationLabels
from cataProfileResultat        import MyProfileResultat

dElementsRecursifs = {}
dElementsRecursifs['functionsJobStatistics'] = defFunction


# definition sert pour la selection
identifiantSelection = Selection


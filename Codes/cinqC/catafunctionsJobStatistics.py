# -*- coding: utf-8 -*-

# TODO: Create a main object that point on the different subobjects and force its name

# EFICAS
from Accas import SIMP, JDC_CATA_SINGLETON, PROC, FACT

# Warning: The names of these variables are defined by EFICAS
JdC = JDC_CATA_SINGLETON(code="functionsJobStatistics")
VERSION_CATALOGUE = "V_0"


def defFunction(profondeur):
   if profondeur < 10 :
      return FACT(statut='f', nomXML='functionsJobStatistics',max='**',
        label    = SIMP(statut='o', typ='TXM'),
        cpuTime  = SIMP(statut='o', typ='R', min=0, unite='seconds'),
        fractionOfTotalTime = SIMP(statut='o', typ='R', min=0),
        calls = SIMP(statut='o', typ='I', min=0),
        depth = SIMP(statut='o', typ='I', min=0),
        fractionOfCallerTime = SIMP(statut='o', typ='R', min=0, unite = 'percent'),
        functionsJobStatistics = defFunction( profondeur+1)
      )
   else : 
      return FACT(
         monNom = SIMP( statut='o', typ='TXM'),
      )

if JdC.code in ( 'functionsJobStatistics' ,) :
  dElementsRecursifs = {}
  dElementsRecursifs['functionsJobStatistics'] = defFunction


#if JdC.code in ( 'functionsJobStatistics', 'Gui5C') :
if JdC.code in ( 'functionsJobStatistics') :
  functionsJobStatistics = PROC( nom = "functionsJobStatistics",
     functions = defFunction(0)
)

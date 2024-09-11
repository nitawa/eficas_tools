# -*- coding: utf-8 -*-

# TODO: Create a main object that point on the different subobjects and force its name

# EFICAS
from Accas import SIMP, JDC_CATA_SINGLETON, PROC, FACT

# Warning: The names of these variables are defined by EFICAS
JdC = JDC_CATA_SINGLETON(code="stepsStatMemory")
VERSION_CATALOGUE = "V_0"


def defStepsStatMemory(statut):
    return FACT(statut=statut, nomXML='statMemory',max=1,
        label    = SIMP(statut='o', typ='TXM'),
        malloc_count  = SIMP(statut='o', typ='I', min=0, fr='nb d appels a malloc' ),
        malloc_total_memory  = SIMP(statut='o', typ='R', min=0, unite='bytes'),
        malloc_max_memory  = SIMP(statut='o', typ='R', min=0, unite='bytes'),
    )

if JdC.code in ( 'stepsStatMemory') :
  stepsStatMemory = PROC( nom = "stepsStatMemory",
     statMemory = defStepsStatMemory('o')
)

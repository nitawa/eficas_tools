# -*- coding: utf-8 -*-

# EFICAS
from Accas import  SIMP,  JDC_CATA, PROC, FACT, JDC_CATA_SINGLETON

JdC = JDC_CATA_SINGLETON(code="JobPerformance")
VERSION_CATALOGUE = "V_0"

from catafunctionsJobStatistics import defFunction
from cataInterrogeDB            import chercheVersion

MyJobPerformance = PROC( nom = "MyJobPerformance",
     sha1 = SIMP(statut='o', typ='TXM', ),
     testName = SIMP(statut='o', typ='TXM',),
     version = SIMP(statut='o', typ='TXM', into=chercheVersion, intoXML=[]), 
     date = SIMP(statut='o', typ='date', typeXSD='xs:date'), 
     CMakeBuildType = SIMP(statut='o', typ='TXM', into=('Release','Debug','RelWithDebInfo')), 
     execution = SIMP(statut='o', typ='TXM', into=('par','seq')), 
     procs = SIMP(statut='o', typ='I', min=0),
     host = SIMP(statut='o', typ='TXM',),
     OS = SIMP(statut='o', typ='TXM',),
     JobStatistics = FACT(statut = 'o',
       totalCpuTime = SIMP(statut='o', typ='R', min=0, unite='seconds'),
       functionsJobStatistics = defFunction(0)
     ),
)

dElementsRecursifs = {}
dElementsRecursifs['functionsJobStatistics'] = defFunction
dPrimaryKey = {}
dPrimaryKey['JobPerformance'] = 'sha1'
dPrimaryKey['JobStatistics'] = 'sha1'

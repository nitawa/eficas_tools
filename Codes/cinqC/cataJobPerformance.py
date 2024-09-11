# -*- coding: utf-8 -*-

# EFICAS
from Accas import  SIMP,  JDC_CATA, PROC, FACT, JDC_CATA_SINGLETON

JdC = JDC_CATA_SINGLETON(code="JobPerformance")
VERSION_CATALOGUE = "V_0"

from catafunctionsJobStatistics import defCPUByFunction
from catastepsStatMemory        import defStepsStatMemory
from cataInterrogeDB            import chercheVersion

JobPerformance = PROC( nom = "JobPerformance",
     sha1 = SIMP(statut='o', typ='TXM', ),
     testName = SIMP(statut='o', typ='TXM',),
     version = SIMP(statut='o', typ='TXM', into=chercheVersion, intoXML=[]), 
     date = SIMP(statut='o', typ='date', typeXSD='xs:date'), 
     CMakeBuildType = SIMP(statut='o', typ='TXM', into=('Release','Debug','RelWithDebInfo')), 
     execution = SIMP(statut='o', typ='TXM', into=('par','seq')), 
     procs = SIMP(statut='o', typ='I', min=0),
     host = SIMP(statut='o', typ='TXM',),
     OS = SIMP(statut='o', typ='TXM',),
     CPUStatistics = FACT(statut = 'f',
       totalCpuTime = SIMP(statut='o', typ='R', min=0, unite='seconds'),
       functionsJobStatistics = defCPUByFunction(10, 'f')
     ),
     MemoryStatistics = defStepsStatMemory('f'),
)

dElementsRecursifs = {}
dElementsRecursifs['functionsJobStatistics'] = defCPUByFunction
dPrimaryKey = {}
dPrimaryKey['JobPerformance'] = 'sha1'
dPrimaryKey['JobStatistics'] = 'sha1'

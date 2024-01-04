# -*- coding: utf-8 -*-
# 
# Ce catalogue permet de decrire la partie Selection du GUI
# il doit etre en coherence avec les meta données de la database
#

# Eficas
from Accas import  SIMP, JDC_CATA, PROC, JDC_CATA_SINGLETON
from Accas import  AU_MOINS_UN, PRESENT_PRESENT

JdC = JDC_CATA_SINGLETON(code="JobIdentification")
#JdC = JDC_CATA(code="JobIdentification")

from cataInterrogeDB import chercheVersion
from cataInterrogeDB import chercheTestName
from cataInterrogeDB import chercheSha1
from cataInterrogeDB import chercheDate
from cataInterrogeDB import chercheOS
from cataInterrogeDB import chercheProcs
from cataInterrogeDB import chercheHost
from cataInterrogeDB import chercheCMakeBuildType
from cataInterrogeDB import chercheExecution

Selection = PROC( nom = "Selection",
     regles = (
     # A affiner avec un validateur AND_NOT_NONE qui n existe pas
              AU_MOINS_UN('sha1','testName','sha1Debut','date','dateDebut','version','CMakeBuildType','execution','OS','procs','host'),
              PRESENT_PRESENT('sha1Debut','sha1Fin'),
              PRESENT_PRESENT('dateDebut','dateFin'),
              ),
     fenetreIhm='InterfaceGUI.cinqC.monWidgetSelection',
     testName  = SIMP(statut='o', typ='TXM',  affichage=('selection',0,0), into = chercheTestName ,fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C'),
     sha1      = SIMP(statut='o', typ='TXM',  affichage=('selection',1,0), into = chercheSha1, fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C'),
     sha1Debut = SIMP(statut='o', typ='TXM',  affichage=('selection',1,1), into = chercheSha1, fenetreIhm='InterfaceGUI.cinqC.monWidgetSimpSelection5C'),
     sha1Fin   = SIMP(statut='o', typ='TXM',  affichage=('selection',1,2), into = chercheSha1, fenetreIhm='InterfaceGUI.cinqC.monWidgetSimpSelection5C'),
     date      = SIMP(statut='o', typ='date', typeXSD='xs:date', into = chercheDate, affichage=('selection',3,0), fenetreIhm='InterfaceGUI.cinqC.monWidgetDateSelection5C'), 
     dateDebut = SIMP(statut='o', typ='date', typeXSD='xs:date', into = chercheDate, affichage=('selection',3,1), fenetreIhm='InterfaceGUI.cinqC.monWidgetDateSelection5C'), 
     dateFin   = SIMP(statut='o', typ='date', typeXSD='xs:date', into = chercheDate, affichage=('selection',3,2), fenetreIhm='InterfaceGUI.cinqC.monWidgetDateSelection5C'), 
     version   = SIMP(statut='o', typ='TXM',  into=chercheVersion, affichage=('selection',2,0), fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C'), 
     CMakeBuildType = SIMP(statut='o', typ='TXM', into= chercheCMakeBuildType, affichage=('selection',2,1), fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C'), 
     execution = SIMP(statut='o', typ='TXM', into=chercheExecution , affichage=('selection',2,2), fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C', defaut='seq'), 
     OS        = SIMP(statut='o', typ='TXM', affichage=('selection',4,0), fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C',  into=chercheOS),
     procs     = SIMP(statut='o', typ='I', min=0, affichage=('selection',4,1), fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C', into=chercheProcs),
     host      = SIMP(statut='o', typ='TXM', affichage=('selection',4,2), fenetreIhm='InterfaceGUI.cinqC.monWidgetCBSelection5C', into=chercheHost),
)
PresentationLabels = PROC ( nom = 'PresentationLabels',
     fenetreIhm='InterfaceGUI.cinqC.monWidgetLabels',
     labels = SIMP(statut='o', typ='TXM', into = [], max='**', homo='SansOrdreNiDoublon',),
) 

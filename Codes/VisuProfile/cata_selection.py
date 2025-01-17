# -*- coding: utf-8 -*-
# 
# Ce catalogue permet de decrire la partie Selection du GUI
# il doit etre en coherence avec les meta données de la database
#
import time

# Eficas
from Accas import SIMP, JDC_CATA, PROC, JDC_CATA_SINGLETON
from Accas import AU_MOINS_UN, PRESENT_PRESENT
from Accas import infFrereMC, supFrereMC
from interrogeDB import cherche_code_name
from interrogeDB import cherche_test_name
from interrogeDB import cherche_max_timestamp
#from interrogeDB import cherche_min_sha1, cherche_max_sha1

# PN Attention, Eficas réappelle la fonction si elle est directement dans le into
# ici l 'appel n 'est fait qu 'une fois
into_code_name = cherche_code_name()
into_test_name = cherche_test_name()

from datetime import datetime, timedelta
lastTimeStamp = cherche_max_timestamp()[0][0]
aWeekBeforeDT = datetime.fromtimestamp(lastTimeStamp) - timedelta(days=7)
aWeekBefore = aWeekBeforeDT.timestamp()
listSha1Min = cherche_Sha1_From_Date( aWeekBefore)
sha1Min = listSha1Min[0]
listSha1Max = cherche_Sha1_From_Date( lastTimeStamp)
sha1Max = listSha1Max[0]


JdC = JDC_CATA_SINGLETON(code="ProfileSelection")
Selection = PROC( nom = "Selection",
    fenetreIhm='InterfaceGUI.VisuProfile.monWidgetSelection',
    code_name  =  SIMP(statut='o', typ='TXM', into = into_code_name,
                  fenetreIhm='InterfaceGUI.VisuProfile.monWidgetCBSelectionVP',
                  affichage=('selection',0,0),
                  ),
    test_name  =  SIMP(statut='o', typ='TXM', into = into_test_name,
                  fenetreIhm='InterfaceGUI.VisuProfile.monWidgetCBSelectionVP',
                  affichage=('selection',0,1),
                  ),
    timestamp_debut =  SIMP(statut='o', typ='I', typeXSD='xs:int',
                  fenetreIhm='InterfaceGUI.VisuProfile.monWidgetDateVP',
                  affichage=('selection',1,0),
                  validators=[infFrereMC(frere='timestamp_fin'),],
                  defaut = aWeekBefore,
                  ),
    timestamp_fin   =  SIMP(statut='o', typ='I', typeXSD='xs:int',
                  fenetreIhm='InterfaceGUI.VisuProfile.monWidgetDateVP',
                  affichage=('selection',1,1),
                  validators=[supFrereMC(frere='timestamp_debut'),],
                  defaut = lastTimeStamp,
                  ),
    sha1_debut =  SIMP(statut='o', typ='TXM',
                  fenetreIhm='InterfaceGUI.VisuProfile.monWidgetSimpSelectionVP',
                  affichage=('selection',2,0),
                  into = listSha1Min,
                  defaut = minSha1,
                  ),
    sha1_fin   =  SIMP(statut='o', typ='TXM',
                  fenetreIhm='InterfaceGUI.VisuProfile.monWidgetSimpSelectionVP',
                  affichage=('selection',2,1),
                  into = listSha1Max,
                  defaut = maxSha1,
                  ),
)
PresentationLabels = PROC ( nom = 'PresentationLabels',
     fenetreIhm='InterfaceGUI.VisuProfile.monWidgetLabels',
     labels = SIMP(statut='o', typ='TXM', into = [], max='**', homo='SansOrdreNiDoublon',),
) 

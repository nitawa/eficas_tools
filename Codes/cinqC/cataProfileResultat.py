# EFICAS
from Accas import  FACT, SIMP, JDC_CATA, PROC, JDC_CATA_SINGLETON
JdC = JDC_CATA_SINGLETON(code="ProfileResultat")

MyProfileResultat = PROC( nom = "MyProfileResultat",
      fenetreIhm='InterfaceGUI.cinqC.monWidgetProfile',
      sha1Id = SIMP( statut='o', typ='TXM'),
      cpuTotalTime  = SIMP(statut='o', typ='R', min=0),
      fonction   = FACT(statut='f', max='**',
        label    = SIMP(statut='o', typ='TXM'),
        cpuTime  = SIMP(statut='o', typ='R', min=0),
        calls    = SIMP(statut='o', typ='I', min=0),
        fractionOfTotalTime = SIMP(statut='o', typ='R', min=0),
      )
)

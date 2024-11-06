# -*- coding: utf-8 -*-

# EFICAS
from Accas import  SIMP,  JDC_CATA, PROC, FACT, JDC_CATA_SINGLETON

# Permet de trouver les into

JdC = JDC_CATA_SINGLETON(code="ProfileNS")
VERSION_CATALOGUE = "V_0"


def defFunction(profondeur, statut):
# profondeur : profondeur de la recursivite
# statut : obligatoire ou facultatif
# le statut devient facultatif des le second appel
   if profondeur > 0 :
      return FACT(statut=statut, nomXML='function',max='**',
        name      = SIMP(statut='o', typ='TXM'),
        cpu_time  = SIMP(statut='o', typ='R', val_min=0, unite='seconds'),
        total_fraction = SIMP(statut='o', typ='R', val_min=0, unite = 'percent'),
        calls = SIMP(statut='o', typ='I', val_min=0),
        depth = SIMP(statut='o', typ='I', val_min=0),
        caller_fraction = SIMP(statut='o', typ='R', val_min=0, unite = 'percent'),
        function = defFunction( profondeur-1, 'f')
      )
   else : 
      return FACT()


Profile = PROC( nom = "Profile",
     run_id = FACT(statut='o', max=1, min =1,
         sha1 = SIMP(statut='o', typ='TXM', val_min=0),
         code_name = SIMP(statut='o', typ='TXM',),
         test_name = SIMP(statut='o', typ='TXM',),
         version = SIMP(statut='o', typ='TXM',), 
         timestamp = SIMP(statut='o', typ='I', val_min=0), 
         build_type = SIMP(statut='o', typ='TXM', into=('Release','Debug','RelWithDebInfo')), 
         execution = SIMP(statut='o', typ='TXM', into=('par','seq')), 
         procs = SIMP(statut='o', typ='I', val_min=0),
         # 0 si la valeur n est pas significative
         host = SIMP(statut='o', typ='TXM',),
         OS = SIMP(statut='o', typ='TXM',),
     ),
     time_profile = FACT(statut = 'f',
       total_cpu_time  = SIMP(statut='o', typ='R', val_min=0, unite='seconds'),
       function = defFunction(10, 'o')
     ),
     memory_profile = FACT(statut ='f',
       count = FACT(statut ='o',
          malloc = SIMP(statut='o', typ='I', val_min=0 ),
          calloc = SIMP(statut='o', typ='I', val_min=0),
          realloc = SIMP(statut='o', typ='I',val_min=0 ),
          free = SIMP(statut='o', typ='I', val_min=0 ),
        ),
       allocation = FACT(statut ='o',
          malloc_size  = SIMP(statut='o', typ='I', unite ="bytes", val_min=0),
          realloc_size  = SIMP(statut='o', typ='I', unite ="bytes", val_min=0),
          calloc_size  = SIMP(statut='o', typ='I', unite ="bytes", val_min=0),
          peak_size  = SIMP(statut='o', typ='I', unite ="bytes", val_min=0),
        ),
    ),
)

dElementsRecursifs = {}
dElementsRecursifs['function'] = defFunction
dPrimaryKey = {'Profile' : 'run_id', 'time_profile' : 'run_id', 'memory_profile' : 'run_id' }
dForeignKey = {'time_profile' : ('run_id', 'run_id', 'Profile'),'memory_profile' : ('run_id', 'run_id', 'Profile'),}
dUnique = {'Profile' : ('sha1','code_name','test_name','version','timestamp','build_type', 'execution', 'procs', 'host', 'OS') }

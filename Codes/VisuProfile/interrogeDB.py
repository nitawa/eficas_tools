import sys, os
if os.path.dirname(os.path.abspath(__file__)) not in sys.path :
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
if os.path.join ((os.path.dirname(os.path.abspath(__file__))), '..'):
    sys.path.insert(0,os.path.join((os.path.dirname(os.path.abspath(__file__))), '../../InterfaceGUI/VisuProfile'))
    sys.path.insert(0,os.path.join((os.path.dirname(os.path.abspath(__file__))), '../..'))
    sys.path.insert(0,os.path.join((os.path.dirname(os.path.abspath(__file__))), '../../Accas'))

from connectDB import connectDB  

def selectRowsInTable(nomChamp, nomTable, distinct = False, debug = False, label=None ) :
    if debug : print ('debut selectRowsInTable')
    monConnecteur = connectDB (debug = debug)
    if debug : print ('monConnecteur', monConnecteur)
    if distinct : instruction   = "select distinct {} from {};".format(nomChamp, nomTable)
    else        : instruction   = "select {} from {};".format(nomChamp, nomTable)
    if debug : print ('monConnecteur', monConnecteur)
    #  resultatExec = liste contenant des n uplet ((lechamp,),)
    resultatExec= monConnecteur.executeSelect(instruction, debug = debug)
    if debug : print ('resultatExec', resultatExec)
    return resultatExec

def selectWithFonction(nomChamp, nomTable, fonction, debug = False ) :
    if debug : print ('debut selectWithFonction avec {}'.format(fonction) )
    monConnecteur = connectDB (debug = debug)
    if debug : print ('monConnecteur', monConnecteur)
    instruction   = "select {} ( {} ) from {};".format(fonction,nomChamp, nomTable)
    resultatExec= monConnecteur.executeSelect(instruction,  debug = debug)
    if debug : print ('resultatExec', resultatExec)
    return resultatExec

def executeSelect(instruction, debug = False ) :
    if debug : print ('debut selectOrdered avec {}'.format(ordre,) )
    monConnecteur = connectDB (debug = debug)
    resultatExec= monConnecteur.executeSelect(instruction,  debug = debug)
    if debug : print ('resultatExec', resultatExec)
    return resultatExec

def listeDeListesToListeSimple(listeDeListes, debug = False) :
    if debug : print ('debut listeDeListesToListeSimple', listeDeListes,)
    listeRetour   = []
    for liste in listeDeListes:
        for tupleChamp in liste :
            listeRetour.append(tupleChamp)
    if debug : print ('debut listeRetour', listeRetour,)
    return listeRetour

def cherche_sha1() :
    return selectRowsInTable ('sha1', 'Profile', distinct=True)

def cherche_min_sha1() :
    return selectWithFonction ('sha1', 'Profile', 'MIN')

def cherche_max_sha1() :
    return selectWithFonction ('sha1', 'Profile', 'MAX')

def cherche_sha1_for_date(timestamp):
    d1=timestamp
    d2=timestamp
    instruction = ' select sha1 from profile where timestamp between {} and {} ordered by timestamp'.format(d1, d2)
    return executeSelect(instruction)

def cherche_code_name(debug = False) :
    resultat = selectRowsInTable ('code_name', 'Profile', distinct=True, debug = debug)
    listeRetour = listeDeListesToListeSimple(resultat, debug = debug)
    return listeRetour

def cherche_test_name(debug = False) :
    resultat = selectRowsInTable ('test_name', 'Profile', distinct=True, debug = debug)
    listeRetour = listeDeListesToListeSimple(resultat, debug = debug)
    return listeRetour

def cherche_version() :
    return selectRowsInTable ('version', 'Profile', distinct=True)

def cherche_timestamp() :
    return selectRowsInTable ('timestamp', 'Profile', distinct=True)

def cherche_OS():
    return selectRowsInTable ('OS', 'Profile', distinct=True)

def cherche_procs():
    return selectRowsInTable ('procs', 'Profile', distinct=True)

def cherche_host():
    return selectRowsInTable ('host', 'Profile', distinct=True)

def cherche_time_profile():
    return selectRowsInTable ('time_profile', 'Profile')

def cherche_name():
    return selectRowsInTable ('name', 'time_profile')

def cherche_build_type():
    return selectRowsInTable ('build_type', 'Profile', distinct=True)

def cherche_max_timestamp():
    return selectWithFonction ('timestamp', 'Profile', 'MAX')

if __name__ == "__main__":
    #print ('liste Sha1', cherche_sha1()) 
    #print ('liste test_name', cherche_test_name()) 
    print ('max sha1 :', cherche_max_sha1())
    print ('min sha1 :', cherche_min_sha1())
    #print ('liste code_name', cherche_code_name()) 
    #print ('liste version', cherche_version())
    #print ('liste timestamp', cherche_timestamp())
    #print ('liste build_type',  cherche_buildtype())
    #print ('liste OS',  cherche_OS())
    #print ('liste Procs',  chercheProcs())
    #print ('liste Host', chercheHost())
    #print ('liste CMakeBuildType', chercheCMakeBuildType())
    #print ('liste Labels', chercheLabels())


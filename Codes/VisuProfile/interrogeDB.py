import sys, os
if os.path.dirname(os.path.abspath(__file__)) not in sys.path :
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
if os.path.join ((os.path.dirname(os.path.abspath(__file__))), '..'):
    sys.path.insert(0,os.path.join((os.path.dirname(os.path.abspath(__file__))), '../InterfaceGUI.cinqC'))

from connectDB import connectDB  

def selectRowsInTable(nomChamp, nomTable, distinct = False) :
    if distinct : instruction   = "select distinct {} from {};".format(nomChamp, nomTable)
    else        : instruction   = "select {} from {};".format(nomChamp, nomTable)
    monConnecteur = connectDB()
    listeRetour   = []
    # liste contenant des 1 uplet ((lechamp,),)
    for listeTupleChamp in monConnecteur.executeSelectDB(instruction):
        for tupleChamp in listeTupleChamp :
            listeRetour.append(tupleChamp)
    monConnecteur.closeDB()
    return listeRetour

def selectRecordInTable(nomChamp, valeurChamp, nomTable, ) :
    instruction   = "select *  from {} where {} = {};".format(nomTable, nomChamp, valeurChamp,)
    monConnecteur = connectDB()
    listeTupleChamp  =  monConnecteur.executeSelectDB(instruction):
    print (listeTupleChamp)

def cherche_sha1() :
    return selectRowsInTable ('sha1', 'Profile', distinct=True)

def cherche_code_name() :
    return selectRowsInTable ('code_name', 'Profile', distinct=True)

def cherche_test_name() :
    return selectRowsInTable ('test_name', 'Profile', distinct=True)

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

if __name__ == "__main__":
    print ('liste Sha1', cherche_sha1()) 
    print ('liste test_name', cherche_test_name()) 
    print ('liste code_name', cherche_code_name()) 
    print ('liste version', cherche_version())
    print ('liste timestamp', cherche_timestamp())
    print ('liste build_type',  cherche_buildtype())
    print ('liste OS',  cherche_OS())
    print ('liste Procs',  chercheProcs())
    print ('liste Host', chercheHost())
    print ('liste CMakeBuildType', chercheCMakeBuildType())
    print ('liste Labels', chercheLabels())


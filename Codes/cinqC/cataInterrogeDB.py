import sys, os
if os.path.dirname(os.path.abspath(__file__)) not in sys.path :
    sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
if os.path.join ((os.path.dirname(os.path.abspath(__file__))), '..'):
    sys.path.insert(0,os.path.join((os.path.dirname(os.path.abspath(__file__))), '../InterfaceGUI.cinqC'))

from connectDB import connectDB  

def chercheChamp(nomChamp, nomTable, distinct = False) :
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

def chercheSha1() :
    return chercheChamp ('sha1', 'jobperformance', distinct=True)

def chercheTestName() :
    return chercheChamp ('testname', 'jobperformance', distinct=True)

def chercheVersion() :
    return chercheChamp ('version', 'jobperformance', distinct=True)

def chercheDate() :
    return chercheChamp ('date', 'jobperformance', distinct=True)

def chercheExecution() :
    return chercheChamp ('execution', 'jobperformance', distinct=True)

def chercheOS():
    return chercheChamp ('OS', 'jobperformance', distinct=True)

def chercheProcs():
    return chercheChamp ('procs', 'jobperformance', distinct=True)

def chercheHost():
    return chercheChamp ('host', 'jobperformance', distinct=True)

def chercheCMakeBuildType():
    return chercheChamp ('CMakeBuildType', 'jobperformance', distinct=True)

def chercheFunctionsJobStatistics():
    return chercheChamp ('functionsJobStatistics', 'jobperformance')

def chercheLabels():
    return chercheChamp ('Labels', 'jobperformance')

if __name__ == "__main__":
    print ('liste Sha1', chercheSha1()) 
    print ('liste testName', chercheTestName()) 
    print ('liste Version',  chercheVersion())
    print ('liste Date',  chercheDate())
    print ('liste Execution',  chercheExecution())
    print ('liste OS',  chercheOS())
    print ('liste Procs',  chercheProcs())
    print ('liste Host', chercheHost())
    print ('liste CMakeBuildType', chercheCMakeBuildType())
#    print ('liste XML', chercheFunctionsJobStatistics())
    print ('liste Labels', chercheLabels())


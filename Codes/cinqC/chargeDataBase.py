#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys, os, pathlib

if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if os.path.join((os.path.dirname(os.path.abspath(__file__))), ".."):
    sys.path.insert( 0, os.path.join((os.path.dirname(os.path.abspath(__file__))), "../InterfaceGUI.cinqC"),)

from argparse import ArgumentParser, FileType
import cataJobPerformance_driver as mdm
import datetime
import subprocess
from connectDB import connectDB

xsltPath = os.path.dirname(os.path.abspath(__file__))


dictColumn = {
    "JobPerformance": (
        "sha1", "testName", "version", "date", "CMakeBuildType", "execution", "procs", "host",
        "OS", ("JobStatistics", "totalCpuTime"), "labels",
        ("JobStatistics", "functionsJobStatistics"),
        )
}

connecteurTexte = "dbname=test user=performance"


class parseur(ArgumentParser):
# ----------------------------#

    def __init__(self):
    # -----------------#
        program = "chargeDataBase"
        description = "lit un fichier XML de performance et le charge dans la database"
        super().__init__(prog=program, description=description)
        self.add_argument( "-f", "--fileName", nargs="*", required=True,
            help="name of performance file(s) , aboslute ou relative to directory specified with -d option",
        )
        self.add_argument( "-d", "--directoryName", type=pathlib.Path,
            help="directory containing file if path is relative",
        )
        self.add_argument( "-r", "--rangeFile", type=int,
            help="range of files in order to process file1.xml, file2.xml. The file name has then to be file.xml",
        )

    def parse_args(self):
    # -----------------#
        args = super().parse_args()
        if args.rangeFile:
            newFileNameList = []
            splitF = args.fileName[0].split(".xml")
            if len(splitF) != 2 and splitF[1] != "":
                print("FileName has to be as file.xml")
                self.print_usage()
                exit(2)
            baseFile = splitF[0]
            for i in range(args.rangeFile):
               newFileNameList.append(baseFile + str(i) + ".xml")
            args.fileName = newFileNameList
        if args.directoryName:
            if not(os.path.isdir(args.directoryName)):
                print("Directory {} does not exist".format(args.directoryName))
                self.print_usage()
                exit(2)
            newFileNameList = []
            for f in args.fileName:
                newFileNameList.append(os.path.join(args.directoryName, f))
            args.fileName = newFileNameList

        newFileNameList = []
        for f in args.fileName:
            if not os.path.isfile(f):
                print("cannot access file {}".format(f))
                continue
            newFileNameList.append(f)
        args.fileName = newFileNameList
        if args.fileName==[]:
            print ('no file to process')
            self.print_usage()
            exit(2)
        return args


# -------------------------------#
class connectDBCharge(connectDB):
    # -------------------------------#
    """
    lit un fichier XML de perfomance et le charge dans la database
    code exit : 1 erreur database, 2 autres erreurs
    herite de connectDB qui gere les connexions à la database
    la chaine de connexion  connecteurTexte est definie au global
    Attention, si dans un lot de fichier, un est en erreur dans la database, le job s arrete
    """

    def chargeXMLFile(self, fileName, debug=0):
        # -------------------------------------------#
        """
        appelle les fonctions qui
           1) lisent le fichier XML passe en argument
           2) preparent le insert
           3) executent le insert grace a connectDB
           4) commit
        """
        self.litXMLFile(fileName)
        self.textColumn = "INSERT INTO JobPerformance ("
        self.textValues = "VALUES ("
        self.lesValeurs = []
        try : 
            self.prepareInsertInDatabase(self.rootElt, "JobPerformance", fileName)
        except Exception as e:
           raise(e)
           return
        self.textColumn = self.textColumn[0:-1] + ") "
        self.textValues = self.textValues[0:-1] + ") "
        self.textInsert = self.textColumn + self.textValues
        if debug: print("self.textColumn : ", self.textColumn)
        if debug: print("self.textValues : ", self.textValues)
        if debug: print("self.lesValeurs : ", self.lesValeurs)
        if debug: print("\n\n\n")
        self.executeInsertDB(self.textInsert, self.lesValeurs)
        self.commitDB()
   

    def litXMLFile(self, fileName):
        # -----------------------------#
        """
        lit le fichier XML grace a pyxb
        """
        debug=0
        try:
            self.jdd = mdm.CreateFromDocument(open(fileName).read())
            self.rootElt = self.jdd.MyJobPerformance[0]
            if debug : print ( self.jdd.toDOM().toprettyxml())
        except Exception as e:
            print("impossible de lire le fichier", fileName)
            print("exception", e)
            exit(2)

    def prepareInsertInDatabase(self, elt, typeDeTable, fileName, debug=0):
        # ------------------------------------------------------------------------#
        """
        Cherche les valeurs dans l objet Pyxb selon la liste dans le dictColumn
        Il faudrait lire le cata pour en déduire les colonnes
        Attention aux valeurs optionnelles non traitees
        """
        if debug:
            print("prepareInsertInDatabase avec", elt, typeDeTable)
        if typeDeTable not in dictColumn.keys():
            print(
                "conversion du type {} vers la database non prévue ".format(typeDeTable)
            )
            exit(2)
        for pathElt in dictColumn[typeDeTable]:
            if debug:
                print("traitement de pathElt", pathElt)
            ouChercher = elt
            if type(pathElt) not in (list, tuple):
                listeAChercher = (pathElt,)
            else:
                listeAChercher = pathElt
            for sousElt in listeAChercher:
                if debug:
                    print("traitement de sousElt", sousElt, "dans", ouChercher)
                if sousElt == "labels":
                    try:
                        v = self.chercheLabel(fileName)
                    except Exception as e:
                        print("impossible de lire les labels dans le fichier", fileName)
                        raise(e)
                else:
                    try:
                        v = getattr(ouChercher, sousElt)
                        if debug: print("getattr ", ouChercher, sousElt)
                        if sousElt == "totalCpuTime": v = v.value()
                        if sousElt == "functionsJobStatistics":
                             v = self.jdd.toDOM().toxml()
                            #v = v[0].toDOM(element_name="JobStatistics").toxml()
                    except:
                        print("pas de valeur pour", sousElt)
                        print("gerer les elements nuls SVP")
                        v = None
                        continue
                if debug:
                    print("valeur de sousElt", v)
                ouChercher = v
                if debug:
                    print("________________")
            self.textColumn += sousElt + ","
            # ARRAY [] = colonne multivaluee
            if sousElt == "labels":
                self.textValues += "ARRAY[%s],"
                self.lesValeurs.append(list(v))
            else:
                self.textValues += "%s,"
                self.lesValeurs.append(v)
            if debug:
                print("self.textColumn : ", self.textColumn)
            if debug:
                print("self.textValues : ", self.textValues)
            if debug:
                print("self.lesValeurs : ", self.lesValeurs)

    def chercheLabel(self, fileName):
        # ------------------------------#
        """
        appelle un xquery sur le fichier XML pour recuperer la liste des labels presents
        """
        result = set()
        try:
            xqueryFile = os.path.join(xsltPath, "getlabels.xq")
            cmd = "saxonb-xquery  -s:{} -q:{}".format(fileName, xqueryFile)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            (output, err) = p.communicate()
        except Exception as e:
            print("impossible d executer le xquery getlabels.xq sur", fileName)
            print("exception", e)
            exit(2)
        chaine = str(output).split("resultXQUERY")[1][4:-6]
        for f in chaine.split('",'):
            f = f.lstrip()
            if f[0] == '"':
                f = f[1:]
            result.add(f)
        return result


if __name__ == "__main__":
    # -----------------------#
    # fileNameBase = (
    #     "/home/A96028/5C/BaseDeDonnees/data/performance/base_XML/job_performance_"
    # )
    monParseur = parseur()
    args = monParseur.parse_args()
    monConnecteur = connectDBCharge()
    for fileName in args.fileName:
        try:
            monConnecteur.chargeXMLFile(fileName)
            print ('file {} processed'.format(fileName))
        except Exception as e:
            print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print("impossible de charger", fileName)
            print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print("exception", e)

    monConnecteur.closeDB()

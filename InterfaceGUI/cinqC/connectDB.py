#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

import cataJobPerformance_driver as mdm
import psycopg2

connecteurTexte = "dbname=test user=performance"


class connectDB:
    """
    lit un fichier XML de perfomance et le charge dans la database
    code exit : 1 erreur database, 2 autres erreur
    """

    def __init__(self, debug = 0):
    #----------------------------#
        """
           connexion a la database
           ouverture du curseur
        """
        try:
            self.connecteur = psycopg2.connect(connecteurTexte)
        except Exception as e:
            print("impossible de se connecter avec connecteur", connecteurTexte)
            print("exception", e)
            self.closeDB()
            exit(1)
        try:
            self.curseur = self.connecteur.cursor()
        except Exception as e:
            print("impossible de creer un curseur")
            print("exception", e)
            self.closeDB()
            exit(1)

    def executeSelectDB(self, instruction, debug = 0):
    #--------------------------------------------------------#
        if debug:
            print("executeSelectDB avec ", instruction )
        try:
            self.curseur.execute(instruction)
            resultat = self.curseur.fetchall() 
            if debug : print ("resultat ", resultat)
            return resultat
        except Exception as e:
            print("probleme a l execution de", instruction)
            print("exception", e)
            exit(1)

    def executeInsertDB(self, instruction, valeur, debug = 0):
    #-------------------------------------------------------#
        if debug:
            print("executeInsertDB avec ", instruction, " ", valeur)
        try:
            self.curseur.execute(instruction, valeur)
        except Exception as e:
            print("impossible d executer", instruction)
            print("avec les valeurs", valeur)
            print("exception", e)
            exit(1)

    def commitDB(self):
    #-----------------#
        try:
            self.connecteur.commit()
        except Exception as e:
            print("impossible d executer le commit")
            print("exception", e)
            self.closeDB()
            exit(1)

    def closeDB(self):
    #----------------#
        try:
            self.curseur.close()
        except Exception as e:
            print("impossible d executer le close du curseur")
            print("exception", e)
            exit(1)
        try:
            self.connecteur.close()
        except Exception as e:
            print("impossible d executer le close du connecteur")
            print("exception", e)
            exit(1)

if __name__ == "__main__":
     pass


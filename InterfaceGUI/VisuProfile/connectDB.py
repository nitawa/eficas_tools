#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import psycopg2


connecteurTexte = "dbname=odyssee_test user=admin_odyssee_test"


class connectDB:
    """
    code exit : 1 erreur database, 2 autres erreur
    """

    def __init__(self, debug = 0):
    #----------------------------#
        """
           connexion a la database
           ouverture du curseur
        """
        if debug : print ('init du connect')
        try:
            self.connecteur = psycopg2.connect(connecteurTexte)
        except Exception as e:
            print("impossible de se connecter avec connecteur", connecteurTexte)
            print("exception", e)
            self.closeDB()
            exit(1)
        if debug : print ('connecteur', self.connecteur)
        try:
            self.curseur = self.connecteur.cursor()
        except Exception as e:
            print("impossible de creer un curseur")
            print("exception", e)
            self.closeDB()
            exit(1)
        if debug : print ('curseur', self.curseur)

    def executeSelectDB(self, instruction, debug = 0):
    #------------------------------------------------#
        if debug: print("executeSelectDB avec ", instruction )
        try:
            if debug : print ('ici excute')
            self.curseur.execute(instruction)
            if debug : print ('apres excute')
            try :
                resultat = self.curseur.fetchall() 
            except Exception as e:
                print("probleme au fetch  l execution de", instruction)
                print("exception", e)
                return None 
        except Exception as e:
            print("probleme a l execution de", instruction)
            print("exception", e)
            return None 

    def executeDBInstruction(self, instruction, debug = 0):
    #-------------------------------------------------------#
        if debug: print("executeInsertDB avec ", instruction)
        try:
            self.curseur.execute(instruction)
            try :
                resultat = self.curseur.fetchall() 
            except : 
                resultat = None
            if debug : print ('resultat', resultat)
            return resultat
        except Exception as e:
            print("impossible d executer", instruction)
            print("exception", e)

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


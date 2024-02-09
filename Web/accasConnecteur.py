#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
   Ce module sert a lancer EFICAS configure pour le Web 
"""
# Modules Python
import os, sys
import os, sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))


# Modules Eficas

from collections import OrderedDict
import pprint


if sys.version_info[0] < 3:
    print("Must be using Python 3")
    sys.exit()

class AccasConnecteur :
    def __init__(self,code, fichierCata=None, langue=None, fichierComm=None,appWeb=None) :
    #-------------------------------------------------------------------------------------

        self.appWeb=appWeb

        if code == None : multi = True
        else : multi = False
        from Editeur.eficas_go import getEficasSsIhm
        self.monEficas=getEficasSsIhm(code=code, salome=0, multi=multi, langue=langue,fichierCata=fichierCata, GUIPath='Web')

        if self.monEficas == None : 
           self.toWebApp('afficheInfos', 'erreur à la construction de l appli Eficas', 'rouge')
           return
        # faire l equivalent du viewmanager
        if fichierCata == None and fichierComm : 
           self.toWebApp('afficheInfos', 'pour ouvrir un JDC, il faut connaitre le catalogue', 'rouge')
           return 
        self.litFichierComm(fichierComm)

    def toWebApp(self,fction,*args, **kwargs):
    #-----------------------------------------
        #if fction =='propageValide' :
        debug=0
        if debug  : print ('PNPNPN : self.appWeb.toWebApp', fction, *args, **kwargs)
        if self.appWeb == None  : 
           #if fction =='propageValide' : print ('self.appWeb.toWebApp propageValide', self.monEditeur.getNodeById(args[0]).nom)
           return
        self.appWeb.fromConnecteur(fction, *args, **kwargs)
        
    def litFichierComm(self,fichierComm=None):
    #-----------------------------------------
        from InterfaceGUI.Web.editor import JDCWebEditor
        self.monEditeur=JDCWebEditor(self.monEficas,fichierComm,connecteur=self)

    def getListeCommandes(self):
    #---------------------------
        if self.monEditeur == None : return
        return (self.monEditeur.jdc.getListeCmd())

    def getListeMotsClesFilsPossibles(self,nomCommande):
    #-----------------------------------------
        # ici il faut programmer getListeMotsClesFilsPossibles dans P_ENTITE
        # Pour l instant on renvoie entites
        # doit aussi pouvoir etre appele sur FACT et BLOC
        maCommande= getattr(self.monEditeur.jdc.cata,nomCommande)
        laListe=maCommande.entites
        return laListe

    #def generDicoPourWeb(self) :
    #---------------------------------
    #    dico=self.monEditeur.generDicoPourWeb()
    #    return dico

    #def getDicoObjetsPourWeb(self,obj) :
    #---------------------------------
    #    dico=self.monEditeur.getDicoObjetsPourWeb(obj)
    #    return dico

    #def getDicoObjetsCompletsPourTree(self,obj) :
    #    dico=self.monEditeur.getDicoObjetsCompletsPourTree(obj)
    #    return dico
        
    def getDicoForFancy(self,obj,debug=0) :
    #---------------------------------
        dico=self.monEditeur.getDicoForFancy(obj)
        if debug :
           import pprint
           pprint.pprint (dico)
        return dico

    #def traiteDico(self,dico):
    #---------------------------------
    #    for k,v in dico.items():
    #        monNode=self.monEditeur.getNodeById(k)
    #        try    : print ('label', monNode.getLabelText())
    #        except : print ('monNode', monNode)  # non operationnel pour jdc
    #        try : print ('validite :', monNode.isValid())
    #        except : pass # non operationnel pour jdc
    #        if type(v) is OrderedDict : self.traiteDico(v)
    #        else : print ('valeur :', v)
        
    def changeValeur(self,id,valeur) :
    #---------------------------------
         """
         id : identifiant unique
         valeur : valeur saisie dans le formulaire
         doit-on mettre l ancienne valeur en retour qui serait utile si validité = Non 
         """ 
         monNode=self.monEditeur.getNodeById(id)
         #print (' change Valeur', monNode)
         #(idUnique, commentaire, validite)=monNode.fauxNoeudGraphique.traiteValeurSaisie(valeur)
         #print ('retour ChangeValeur',idUnique, commentaire, validite )
         return monNode.fauxNoeudGraphique.traiteValeurSaisie(valeur)

    def updateSDName(self,id,sdnom) :
    #---------------------------------
         monNode=self.monEditeur.getNodeById(id)
         return monNode.fauxNoeudGraphique.updateSDName(sdnom)

    def suppNode(self,id):
    #-------------------
        
        monNode=self.monEditeur.getNodeById(id)
        print ('monNode', monNode)
        retour=monNode.fauxNoeudGraphique.delete()
        return retour

    def appendChild(self,id,name,pos=None):
    #-------------------------------------
        """
        Methode pour ajouter un objet fils name a l objet associe au noeud id.
        On peut l'ajouter en debut de liste (pos='first'), en fin (pos='last')
        ou en position pos_ieme de la liste. 
        retour = nouvelIdUnique ou None 
        """
        monNode=self.monEditeur.getNodeById(id)
        if monNode.fauxNoeudGraphique == None :
           print ('PNPN pas de noeud Graphique associe a l id')
           return
        if debug : print (monNode.fauxNoeudGraphique)
        retour = monNode.fauxNoeudGraphique.appendChild(name,pos)
        return retour

    def saveFile(self,fileName):
    #----------------------------
        """
        sauve le .comm dans fileName (si fileName = None, 
        alors la sauvegarde est faite dans le fichier courant)
        retour = True/False et le nom du fichier sauvegarde
        """
        return self.monEditeur.saveFile(fileName)


if __name__ == "__main__":
    import prefs
    name='prefs_'+prefs.code
    __import__(name)
    code=prefs.code
    monEficasConnecteur=accasConnecteur(code, langue='ang')

    testAjoutSuppProc=0
    if testAjoutSuppProc : 
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Procs.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        r=monEficasConnecteur.appendChild(idRacine,'MonProc',0)
        print ('ajout de MonProc en postion 0', r)
        r=monEficasConnecteur.appendChild(idRacine,'MonProc2',1)
        print ('ajout de MonProc2 en postion 1', r)
        r=monEficasConnecteur.appendChild(idRacine,'MonProc2','last')
        print ('ajout de MonProc2 en postion last', r)
        r=monEficasConnecteur.appendChild(idRacine,'MonProc2','first')
        print ('ajout de MonProc2 en postion first', r)
        r=monEficasConnecteur.appendChild(idRacine,'MonProc2',)
        print ('ajout de MonProc2 sans poistion ne fonctionne pas', r)
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        etape2=d['children'][0]['key']
        print ('je detruis' ,etape2)
        r=monEficasConnecteur.suppNode(etape2)
        print (r)
        monProc2=d['children'][0]['key']
        r=monEficasConnecteur.appendChild(monProc2,'Fact2')
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutProc.comm')

    testAjoutSuppFact2=0
    if testAjoutSuppFact2 : 
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Procs.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        r=monEficasConnecteur.appendChild(idRacine,'MonProc2','last')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        monProc2=d['children'][2]['key']
        r=monEficasConnecteur.appendChild(monProc2,'Fact2')
        #print (r)
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutFact2.comm')
    
    testAjoutSuppFact=0
    if testAjoutSuppFact : 
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Fact.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        monProc2=d['children'][0]['key']
        print ('id monProc2 : ', monProc2)
        #r=monEficasConnecteur.appendChild(monProc2,'Fact2')
        #print ('ajout de Fact2 dans monProc2 reussi', r)
        #r=monEficasConnecteur.appendChild(monProc2,'Fact2')
        #print ('ajout de  Fact2 dans monProc2 inadequat', r)
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        fact11=d['children'][0]['children'][2]['key']
        fact12=d['children'][0]['children'][3]['key']
        fact13=d['children'][0]['children'][4]['key']
        fact14=d['children'][0]['children'][5]['key']
        pprint.pprint(d)
        #print (d)
        #monFact2=d['children'][0]['children'][3]['key']
        #print (monFact2)
        #r=monEficasConnecteur.suppNode(monFact2)
        #print (r)
        #fact11=d['children'][0]['children'][2]['key']
        #monNode=monEficasConnecteur.monEditeur.getNodeById(fact11)
        #print ('monNode', monNode)
        r=monEficasConnecteur.suppNode(fact11)
        r=monEficasConnecteur.suppNode(fact12)
        r=monEficasConnecteur.suppNode(fact13)
        print ('________________________________________________')
        print ('________________________________________________')
        print ('________________________________________________')
        print ('________________________________________________')
        print ('________________________________________________')
        r=monEficasConnecteur.suppNode(fact14)
        print (r)
        #r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        #r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        #r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        #r=monEficasConnecteur.appendChild(monProc2,'Fact2')
        #r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        #print (d)
        #d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #pprint.pprint(d)
        #r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        #print (r)
        #d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #fact12=d['children'][0]['children'][3]['key']
        #print(d['children'][0]['children'][3]['title'])
        #r=monEficasConnecteur.appendChild(fact12,'paramInFact1')
        #fact1=d['children'][0]['children'][2]
        #print (fact1)
        #fact11=d['children'][0]['children'][2]['key']
        #print (fact11)
        #print ('******************************************************')
        #r=monEficasConnecteur.suppNode(fact11)
        #r=monEficasConnecteur.appendChild(fact11,'paramInFact1')
        #d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #paramInFact12=d['children'][0]['children'][2]['children'][0]['key']
        #r=monEficasConnecteur.suppNode(paramInFact12)
        #print (r)
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutFact.comm')
        exit()

    testChangeValeur=0
    if testChangeValeur :
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Fact.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        print ('idRacine', idRacine)
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #pprint.pprint(d)
    
        monProc=d['children'][0]['key']
        print ('monProc', monProc)
        param1=d['children'][0]['children'][0]['key']
        print ('param1', param1)
        r=monEficasConnecteur.changeValeur(param1,'65')
        param12=d['children'][0]['children'][1]['key']
        print ('param12', param12)
        r=monEficasConnecteur.changeValeur(param12,'9')
        r=monEficasConnecteur.appendChild(monProc,'param11')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        param11=d['children'][0]['children'][1]['key']
        print ('param11', param11)
        r=monEficasConnecteur.changeValeur(param11,'11') 
    
        print ('______________ creation du bloc _____________________')
        r=monEficasConnecteur.changeValeur(param1,'2')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #pprint.pprint(d)
        param1_inBloc=d['children'][0]['children'][3]['key']
        # on supprime le bloc
        r=monEficasConnecteur.changeValeur(param1_inBloc,'1')
        # on le rajoute (pb du bloc dans le bloc) 
        r=monEficasConnecteur.changeValeur(param1_inBloc,'2')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        param1_inBlocDeBloc=d['children'][0]['children'][4]['key']
        r=monEficasConnecteur.changeValeur(param1_inBlocDeBloc,'2')
        print ('______________ creation du bloc _____________________')
        param2_inBloc=d['children'][0]['children'][6]['key']
        r=monEficasConnecteur.changeValeur(param1_inBlocDeBloc,'2')
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/changeValeur.comm')
        exit()
    
        # creation du bloc
        #r=monEficasConnecteur.changeValeur(i,'2')
        #d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #(ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutProcEtBloc.comm')
        #pprint.pprint(d)
    
        # suppression du bloc
        #r=monEficasConnecteur.changeValeur(i,'1')
        #d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #(ok,newFile)=monEficasConnecteur.saveFile('/tmp/suppressionBloc.comm')
        #pprint.pprint(d)
    
        # ajout du Fact2
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        e=d['children'][2]['key']
        r=monEficasConnecteur.appendChild(e,'Fact2')
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutFact2.comm')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        mf=d['children'][2]['children'][4]['key']
        print (mf)
        r=monEficasConnecteur.appendChild(mf,'paramFacultatif')
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutFacultatif.comm')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        mf=d['children'][2]['children'][4]['children'][1]['key']
        r=monEficasConnecteur.suppNode(mf)
        print (r)
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutFacultatifEtSuppresse.comm')
        # essai enlever un mot clef qu on ne peut pas enlever
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        mf=d['children'][2]['children'][1]['key']
        r=monEficasConnecteur.suppNode(mf) 
        print (r)
        #(ok,newFile)=monEficasConnecteur.saveFile('/tmp/ajoutPuisSuppresFact2.comm')
        #d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        #pprint.pprint(d)
    #print ('_________', r)
    
    testPropageValide = 0
    if testPropageValide : 
        monEficasConnecteur.litFichierComm('propageValide.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        #r=monEficasConnecteur.appendChild(idRacine,'MonProc',0)
        #print ('ajout de MonProc en position 0', r)
        #r=monEficasConnecteur.appendChild(idRacine,'MonProc2','last')
        r=monEficasConnecteur.appendChild(idRacine,'MonProc','last')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        param1PLast = d['children'][1]['children'][0]['key']
        r=monEficasConnecteur.changeValeur(param1PLast,'1')
        (ok,newFile)=monEficasConnecteur.saveFile('/tmp/propageValide.comm')
        print ('ajout de MonProc2 en postion last', r)

    testUpdateInfo = 0
    if testUpdateInfo : 
        print ('________________________ testUpdateInfo ___________________________')
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Fact.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        print ('idRacine', idRacine)
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        badMonProc2 = d['children'][0]['children'][0]['key']
        r=monEficasConnecteur.appendChild(badMonProc2,'Fact1')
        monProc2 = d['children'][0]['key']
        #print ('idProc2', monProc2)
        #print (d)
        r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        r=monEficasConnecteur.appendChild(monProc2,'Fact1')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        print (['children'][0])

    testAjoutSimpListe=0
    if testAjoutSimpListe : 
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Procs.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        r=monEficasConnecteur.appendChild(idRacine,'MonProc2','last')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        monProc2=d['children'][2]['key']

    testNommeProc=1
    if testNommeProc : 
        monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Procs.comm')
        idRacine=monEficasConnecteur.monEditeur.tree.racine.item.idUnique
        r=monEficasConnecteur.appendChild(idRacine,'MonOper','last')
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        monOper=d['children'][2]['key']
        bOk, message = monEficasConnecteur.updateSDName(monOper,'toto')
        print ('in testNommeProc, bOk, message', bOk, message)
        d=monEficasConnecteur.getDicoForFancy(monEficasConnecteur.monEditeur.tree.racine)
        monParam=d['children'][2]['children'][0]['key']
        r=monEficasConnecteur.changeValeur(monParam,'65')
        bOk, message = monEficasConnecteur.updateSDName(monOper,'toto')
        print ('in testNommeProc, bOk, message', bOk, message)

    #print ( '\n Fichier /home/A96028/QT5GitEficasTravail/Web/eficas/WebTest/web_tres_simple_avec_2Procs.comm')
    #monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Procs.comm')
    #pprint.pprint (monEficasConnecteur.getDicoObjetsCompletsPourTree(monEficasConnecteur.monEditeur.tree.racine))

    #print ( '\n Fichier /home/A96028/QT5GitEficasTravail/Web/eficas/WebTest/web_tres_simple_avec_Bloc.comm')
    #monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_Bloc.comm')
    #print (monEficasConnecteur.generDicoPourWeb())
    #print (monEficasConnecteur.getDicoObjetsPourWeb(monEficasConnecteur.monEditeur.tree.racine))
    #pprint.pprint (monEficasConnecteur.getDicoObjetsCompletsPourTree(monEficasConnecteur.monEditeur.tree.racine))
    #print ('\n')

    #print ( '\n Fichier /home/A96028/QT5GitEficasTravail/Web/eficas/WebTest/web_tres_simple_avec_2Fact.comm')
    #monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_2Fact.comm')
    #print (monEficasConnecteur.generDicoPourWeb())
    #monDicoAAfficher = (monEficasConnecteur.getDicoObjetsPourWeb(monEficasConnecteur.monEditeur.tree.racine))
    #monEficasConnecteur.traiteDico(monDicoAAfficher)
    #pprint.pprint (monEficasConnecteur.getDicoObjetsCompletsPourTree(monEficasConnecteur.monEditeur.tree.racine))

    #print ('/home/A96028/QT5GitEficasTravail/Web/eficas/WebTest/web_tres_simple_avec_Fact.comm')
    #monEficasConnecteur.litFichierComm('../WebTest/web_tres_simple_avec_Fact.comm')
    #print (monEficasConnecteur.generDicoPourWeb())
    #pprint.pprint (monEficasConnecteur.getDicoObjetsCompletsPourTree(monEficasConnecteur.monEditeur.tree.racine))
    #print ('\n')


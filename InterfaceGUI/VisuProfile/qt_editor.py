# -*- coding: utf-8 -*-
# Copyright (C) 2007-2024   EDF R&D
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
import traceback
import os
import subprocess
import datetime, time
from copy import copy

# Modules Eficas
from Accas.extensions.eficas_translation import tr

from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui     import QPalette
from PyQt5.QtCore    import Qt

from Editeur.editor            import Editor
from UiQT5.editorVP            import Ui_editorVP
from InterfaceGUI.Common       import comploader
from InterfaceGUI.Common       import objecttreeitem
from InterfaceGUI.VisuProfile  import browser
from InterfaceGUI.VisuProfile.connectDB import connectDB

import Accas.IO.writer as generator


dicoFonctionSelection = {'code_name' : 'initApresChgtCode', 'test_name' : 'initApresChgtChamp', 
                         'host' : 'initApresChgtChamp', 'procs' : 'initApresChgtChamp', 
                         'OS' :  'initApresChgtChamp', 'build_type' : 'initApresChgtChamp', 
                         'version' : 'initApresChgtChamp', 'execution' : 'initApresChgtChamp',
                         'performance' : 'setTypePerformance'}
listeDesChampsAChanger = ('test_name' ,'host', 'procs', 'OS', 'build_type', 'execution', 'version')

class QtEditor(Ui_editorVP, Editor, QWidget):
# ------------------------------------------ #
    """
       Editeur de jdc VisuProfile
    """

    def __init__(self, appliEficas, cataFile=None, dataSetFile=None, formatIn='python', formatOut='python', QWParent=None, jdc=None  , include = None):
    #----------------------------------------------------------------------------------------------------------------------------

        debug = 0
        if debug : print ('__init__ de QtEditorVP :', appliEficas,dataSetFile, jdc, QWParent)

        QWidget.__init__(self,None)
        self.setupUi(self)
        Editor.__init__( self, appliEficas=appliEficas, cataFile=cataFile, dataSetFile=dataSetFile, 
                         formatIn = formatIn , formatOut=formatOut , jdc=jdc, include = include)
        comploader.chargerComposants(self.appliEficas.GUIPath)
        self.initQTSignals()
        self.inhibeSplitter=0
        self.widgetOptionnel=None
        self.fenetreCentraleAffichee=self
        self.listeDesListesOuvertes=set()
        self.listeAffichageWidget=[]
        self.afficheListesPliees=False
        self.QWParent=QWParent
        self.node_selected = []
        self.message=''
        self.widgetResultats = None
        self.lesIds = []
        self.lesLabels = []
        self.dictLabels = {}
        self.listeSha1 = []
        self.enteteQTree = 'premier'
        self.connecteur = connectDB()
        self.gitDir=appliEficas.gitDir
        self.typePerformance = 'CPU'

        # a envisager si on garde une selection ?
        self.generatorCondition = generator.plugins['VPRequeteSelection']()
        self.initSelection()

        #self.formatFichierOut =  self.appliEficas.formatFichierOut
        #self.formatFichierIn =  self.appliEficas.formatFichierOut
        self.formatFichierOut = formatOut 
        self.formatFichierIn =  formatIn
        self.node_selected = []
        self.message=''

        # a remettre au gout du jour si on a besoin d un tr
        #    from Accas.extensions import localisation
        #    localisation.localise(self.appliEficas.langue,translatorFile='VisuProfile')
        self.jdcResultats=self._newJDC(texte='')
        self.jdcResultats.analyseXML()
        self.afficheResultats(self.jdcResultats,[],[])


    def initSelection(self) :
    #------------------------
        debug = 0
        if debug : print ('initSelection', texte)
        defSelection = self.readercata.cata.identifiantSelection
        texte = defSelection.nom +'()'
        if debug : print ('texte ' , texte)
        # PNPN : on peut peut-etre sauvagarder et relire des selections anterieures?
        self.jdcSelection=self._newJDC(texte=texte)
        self.jdcSelection.analyse()
        self.etapeSelection = self.jdcSelection.etapes[0]
        if debug : print (self.jdcSelection.etapes)
        self.jdcSelectionItem = objecttreeitem.makeObjecttreeitem( self, "nom", self.jdcSelection )
        if self.jdcSelectionItem :
           self.treeJdcSelection = browser.JDCTree( self.jdcSelectionItem, self )
           if debug : print (self.treeJdcSelection)
           self.widgetSelection = self.treeJdcSelection.racine.children[0].fenetre
           self.editorVPLayout.insertWidget(0,self.widgetSelection)
           self .initCode('','')
         

    def searchActived(self):
    #------------------------
        debug = 1
        if debug: print ('searchActived')
        if debug: print ('traite', self.typePerformance)
        if self.typePerformance == 'CPU' : self.afficheCPU()
        if self.typePerformance == 'Memory' : self.afficheMemory()

    def afficheCPU(self, debug =1):
    #-----------------------------
       self.afficheLabels()

    def initQTSignals(self) :
    #------------------------
        #print ('ds initQTSignals')
        pass


    def afficheCommentaire(self,message):
    #------------------------------------
        #self.labelCommentaire.setText(message)
        # a reprogrammer
        debug = 0
        if debug : print (message)

    def  afficheSuivant(self,f):
    #----------------------------
        #print ('ds afficheSuivant')
        try :
            i=self.listeAffichageWidget.index(f)
            next=i+1
            if (next==len(self.listeAffichageWidget) ): next =0
            try : self.listeAffichageWidget[next].setFocus(7)
            except : pass
        except : pass

    def afficheLabels(self, debug = 1): 
    #-----------------------------------
        condition = self.generatorCondition.genereConditionSelection(self.jdcSelection)
        condition += 'and sha1 in {}'.format(tuple(self.listeSha1))
        self.listeRunId = self.readercata.cata.cherche_in_profile('run_id', condition = condition)
        print (self.listeRunId)
        # on enleve le ;
        #maRequeteId = self.genereRequeteSelectionId()[0:-1] 
        #if maRequeteId == "" : return
        #if debug : print (' 1ere Requete in afficheLesLabel : ',  maRequeteId)
        #maRequete = 'select distinct name from time_profile where run_id in ({})'.format(maRequeteId)
        #if debug : print ('Requete in afficheLabels : ',  maRequeteId)
        #self.lesLabels = self.appelleExecutionRequete(maRequete)
        #if debug : print (self.lesLabels)


    def genereRequeteSelectionId(self): 
    #----------------------------------
        debug = 1
        condition = self.generatorCondition.genereConditionSelection(self.jdcSelection)
        condition += 'and sha1 in {}'.format(tuple(self.listeSha1))
        #self.generator = generator.plugins['VPRequeteSelection']()
        #if debug : print (self.jdcSelection)
        #retour, titre, requete  = self.generator.genereRequeteSelection(self.jdcSelection)
        #if debug : print ('genereRequeteSelection ', retour, titre, requete)
        #if not retour : 
        #   self.afficheMessage(titre, requete)
        #   return  ''
        if debug : print (condition)
        if debug : print (conditionSha1)
        #return requete

    def afficheLabelsOld(self, debug = 0): 
    #-----------------------------------
        #debug = 1
        maRequete = self.genereRequeteSelectionId() 
        if maRequete == "" : return
        if debug : print (' 1ere Requete in chercheLesLabesl : ',  maRequete)
        self.lesIds = self.appelleExecutionRequete(maRequete)
       
        if debug : print (' lesIds in chercheLesLabesl : ',  self.lesIds)
        if self.lesIds == None or len(self.lesIds) == 0 : 
           self.afficheMessage('Bad Selection', 'unable to find a job with these criteria', False)
        return  
        if len(self.lesIds) == 1 :
           maRequete = 'select labels from jobperformance where id = {}'.format(self.lesIds[0])
        else :
           maRequete = 'select labels from jobperformance where id in {}'.format(tuple(self.lesIds))
        if debug : print ('maRequete in chercheLesLabels : ',  maRequete)
        lesLabelsPossibles=set()
        lesLabels = self.appelleExecutionRequete(maRequete,False)
        if debug : print (lesLabels)
        # on connait la structure qui contient les labels 
        index=0
        for listeListeLabelID in lesLabels :
            for listeLabelID in listeListeLabelID :
                for listelabel in listeLabelID :
                    self.dictLabels[self.lesIds[index]]=listelabel
                    index=index+1
                    for label in listelabel :
                        lesLabelsPossibles.add(label)
        lesLabelsPossibles=list(lesLabelsPossibles)
        if debug : print ('lesLabelsPossibles in chercheLesLabesl : ',  lesLabelsPossibles)
        if debug : print ('dicLabels in chercheLesLabesl : ',  self.dictLabels)
        retour = self.changeIntoDefMC('PresentationLabels',('labels',),lesLabelsPossibles, rechercheParNom=True)
        if not retour : self.afficheMessage ('pb sur les labels', 'prevenir la maintenance')
        if debug : print ('init JDC LesLabels')
        texte =  'PresentationLabels();'
        if debug : print ('texte newJDC' , texte)
        self.jdcLabels=self._newJDC(texte=texte)
        self.jdcLabels.analyse()
        jdcLabelsItem = objecttreeitem.makeObjecttreeitem( self, "nom", self.jdcLabels )
        if jdcLabelsItem :
           treeJdcLabels = browser.JDCTree( jdcLabelsItem, self )
           widgetLabels = treeJdcLabels.racine.children[0].fenetre
           widgetLabels.show()

        texteCondition  = self.generatorCondition.genereConditionSelection(self.jdcSelection)
        return requete
         
    def metAJourSelection(self, nomChamp, texteValeur,  debug = 0):
    #--------------------------------------------------------------#
       if debug : print ('metAJourSelection pour ' , label, texteValeur)
       if nomChamp in dicoFonctionSelection : 
           fonct = dicoFonctionSelection[nomChamp]
           if debug : print ('appel de fonction ' , QtEditor.__dict__[fonct])
           QtEditor.__dict__[fonct](self, nomChamp, texteValeur)

    def initCode(self, nomChamp, valeur):
    #----------------------------------#
    # nomChamp est juste pour pouvoir appeler la fonction
       mcCodeName = self.treeJdcSelection.racine.children[0].item.getChild('code_name')
       if mcCodeName.valeur != None : self.initApresChgtCode()

    def initApresChgtCode(self, debug = 0):
    #-------------------------------------#
       #debug = 1
       if debug : print ('init pour Code ')
       condition  = self.generatorCondition.genereConditionSelection(self.jdcSelection)
       if debug : print ('condition', condition)
       listeTestName = self.readercata.cata.cherche_test_name(condition = condition)
       self.rechercheMCMetAJourInto('test_name', listeTestName)

    def initApresChgtChamp(self, nomChamp, valeur):
    #--------------------------------------------#
       debug = 0
       condition  = self.generatorCondition.genereConditionSelection(self.jdcSelection)
       for champ in listeDesChampsAChanger :
            if debug : print (champ)
            if champ == nomChamp : continue
            if debug : print ('traite')
            listeInto = self.readercata.cata.cherche_in_profile(champ, condition = condition)
            if debug : print (listeInto)
            if len(listeInto) > 1 :
                listeChamp = self.etapeSelection.definition.chercheDefinition(champ)
                if len(listeChamp) == 1 :
                    if 'TXM' in listeChamp[0].type : listeInto.append('All')
            self.rechercheMCMetAJourInto(champ, listeInto)
       self.initSha1()

    def initSha1(self):
    #-------------------
       condition  = self.generatorCondition.genereConditionSelection(self.jdcSelection)
       self.listeSha1 = self.readercata.cata.cherche_in_profile('sha1', condition = condition)
       self.ordonneListeSha1()
       print (self.listeSha1Inverse)
       self.rechercheMCMetAJourInto('sha1_debut', self.listeSha1)
       self.rechercheMCMetAJourInto('sha1_fin', self.listeSha1Inverse)
       self.rechercheMCMetAJourValeur('sha1_debut', self.listeSha1[0])
       self.rechercheMCMetAJourValeur('sha1_fin', self.listeSha1Inverse[0])

    def rechercheMCMetAJourInto(self, mcName, liste):
    #------------------------------------------------
       try :
       #print ('PNPNPN : Attention chgt try en if')
       #if 1 :
          mcObj = self.etapeSelection.getChild(mcName)
          mcObj.definition.changeInto(liste,self.jdcSelection)
          mcObj.initRedessine()
       except : 
          self.afficheMessage('pb', 'prevenir la maintenance',)

    def rechercheMCMetAJourValeur(self, mcName, valeur):
    #------------------------------------------------
       try :
       #print ('PNPNPN : Attention chgt try en if')
       #if 1 :
          mcObj = self.etapeSelection.getChild(mcName)
          mcObj.setValeur(valeur)
          mcObj.initRedessine()
       except : 
          self.afficheMessage('pb', 'prevenir la maintenance',)

    def ordonneListeSha1(self, debug=1):
    #-----------------------------------
        newList=[]
        self.dictSha1Date={}
        for sha1 in self.listeSha1 :
            print (sha1)
            #cmd = 'git --git-dir=/home/A96028/cocagne/.git --work-tree=/home/A96028/cocagne  log -1 --format=format:%cD {}'.format(hex(i)[2:])
            #cmd = 'git --git-dir=/home/A96028/cocagne/.git --work-tree=/home/A96028/cocagne  log -1 --format=format:%cD {}'.format(i)
            cmd = 'git --git-dir={}/.git --work-tree={} log -1 --format=format:%ci {}'.format(self.gitDir, self.gitDir,sha1)
            #if debug : print (cmd)
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            #if debug : print (result)
            if result.returncode == 0 :
               dateString = result.stdout
               element = datetime.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S +%f')
               tuple = element.timetuple()
               timestamp = time.mktime(tuple)
               self.dictSha1Date[sha1] = timestamp
               if debug : print (sha1, dateString, timestamp)
               where=0
               for i in newList :
                   if self.dictSha1Date[i] > timestamp : break
                   where+=1 
               if debug : print (sha1, where)
               newList.insert(where, sha1)
        self.listeSha1 = newList
        self.listeSha1Inverse = copy(newList)
        self.listeSha1Inverse.reverse()
        if debug : print ('self.listeSha1', self.listeSha1)


    def afficheMessage(self,titre,message,critique=True):
    #----------------------------------------------------
        if critique :
           from PyQt5.QtWidgets import QMessageBox
           QMessageBox.critical(None, titre, message)
        else :
           from PyQt5.QtWidgets import QMessageBox
           QMessageBox.information(None, titre, message)

    def afficheMessageQt(self, message, couleur=Qt.black):
    # ----------------------------------------------#
        if couleur == "red": couleur = Qt.red
        if not hasattr(self,'sb') : 
           if couleur == "red": 
              titre = "error"
              critique = True
           else : 
              titre = "info"
              critique = False
           self.afficheMessage(titre, message,critique)
           return
        if self.sb:
            mapalette = self.sb.palette()
            mapalette.setColor(QPalette.WindowText, couleur)
            self.sb.setPalette(mapalette)
            self.sb.showMessage(message, 4000)
            self.couleur = couleur


    def appelleExecutionRequete(self,requete,chercheUneSeuleValeur=True, debug = 0):
    #-------------------------------------------------------------------------------
        debug =  1
        if debug : print ('_________________________________________')
        if debug : print ('_________________________________________')
        if debug : print ('_________________________________________')
        if debug : print ('_________________________________________')
        if debug : print ('_________________________________________')
        if debug : print (requete)
        #if debug : print ('self.connecteur', self.connecteur)

        retourRequete =  self.connecteur.executeSelect(requete)
        if retourRequete == None or retourRequete == []:
            titre = 'Pas de Resultat'
            txt = 'la requete "{}" n a aucun résultat'.format(requete)
            self.afficheMessage(titre, txt)
            return 


    def afficheResultats(self,jdcResultat, listeId, listeLabels):
    #------------------------------------------------------------
        # Attention aux differences de niveaux entre CataVPChapeau et CataJobProfile
        # on s appuie sur le 1er element et non le jdc
        self.jdcResultats = jdcResultat
        if self.widgetResultats : self.editorVPLayout.removeWidget(self.widgetResultats)
        from InterfaceGUI.VisuProfile.monWidgetProfile import MonWidgetProfile
        self.widgetResultats=MonWidgetProfile(self,jdcResultat, listeId,listeLabels)
        self.editorVPLayout.insertWidget(1,self.widgetResultats)


    def getValuesOfAllMC(self,obj,McPath):
    #------------------------------------
        return obj.getValuesOfAllMC(McPath)
 

    def selectXYWhereCondition(self, MCPath1, MCPath2, MCARetourner, MCCondition, valeur):
    #-----------------------------------------------------------------------------------
    # est-ce que cette signature est bonne ou faut il indiquer le jdc  ?
        return self.jdcResultats.selectXYWhereCondition(MCPath1, MCPath2, MCARetourner, MCCondition, valeur)
        

    def selectXY(self, MCPath1, MCPath2):
    #------------------------------------
        return self.jdcResultats.selectXY(MCPath1, MCPath2)


    def setTypePerformance(self, nomChamp, valeur):
    #---------------------------------------------
       self.typePerformance = valeur 
       

    def afficheInfosForId (self,id):
    #----------------------------
        maRequete = 'select sha1, testName, version,date, CMakeBuildType,execution,procs, host, OS, totalCputime from jobperformance where id = {}'.format(id)
        lesInfos = self.appelleExecutionRequete(maRequete)
        print (lesInfos)
        #texte="Selection(sha1='{}',testName='{}',version='{}',date='{}', CMakeBuildType='{}',execution='{}',procs={}, host='{}', OS='{}');'.format(lesInfos[0],lesInfos[1],lesInfos[2],lesInfos[3],lesInfos[4],lesInfos[5],lesInfos[6],lesInfos[7],lesInfos[8],lesInfos[9])
        #jdcAAfficher=self._newJDC(texte=texte)
        #jdcAAfficher.analyse()



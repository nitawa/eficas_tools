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

# Modules Eficas
from Accas.extensions.eficas_translation import tr

from PyQt5.QtWidgets           import QWidget
from Editeur.editor            import Editor
from UiQT5.editor5C            import Ui_editor5C
from InterfaceGui.common       import comploader
from InterfaceGui.common       import Objecttreeitem
from InterfaceGUI.cinqC        import browser
from InterfaceGUI.cinqC.connectDB import connectDB
import Accas.IO.writer as generator



class QtEditor(Ui_editor5C, Editor, QWidget):
# ------------------------------------------ #
    """
       Editeur de jdc 5C
    """

    def __init__ (self,appliEficas,fichier = None, jdc=None, QWParent=None, units = None, include=0):
    #------------------------------------------------------------------------------------------------

        debug = 0
        if debug : print ('__init__ de QtEditor5C :', appliEficas,fichier, jdc, QWParent)

        QWidget.__init__(self,None)
        self.setupUi(self)
        appliEficas.maConfiguration.withXSD=1
        Editor.__init__(self,appliEficas, fichier, jdc=jdc)
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
        self.enteteQTree = 'premier'

        # a envisager si on garde une selection ?
        self.initSelection()

        self.formatFichierOut =  self.appliEficas.formatFichierOut
        self.formatFichierIn =  self.appliEficas.formatFichierOut
        self.node_selected = []
        self.message=''

        #self.commandesOrdreCatalogue =self.readercata.commandesOrdreCatalogue
        nomFichierTranslation='translatorFile'+'_'+str(self.appliEficas.readercata.labelCode)
        if hasattr(self.appliEficas.maConfiguration,nomFichierTranslation) :
            translatorFile=getattr(self.appliEficas.maConfiguration,nomFichierTranslation)
            from Accas.extensions import localisation
            localisation.localise(None,self.appliEficas.langue,translatorFile=translatorFile)
        self.jdcResultats=self._newJDC(texte='')
        self.jdcResultats.analyseXML()
        self.afficheResultats(self.jdcResultats,[],[])


    def initSelection(self) :
    #------------------------
        debug=0
        if debug : print ('initSelection')
        defSelection = self.appliEficas.readercata.cata.identifiantSelection
        texte = defSelection.nom +'()'
        if debug : print ('texte newJDC' , texte)
        # PNPN : on peut peut-etre sauvagarder et relire des selections anterieures?
        self.jdcSelection=self._newJDC(texte=texte)
        self.jdcSelection.analyse()
        if debug : print (self.jdcSelection.etapes)
        self.jdcSelectionItem = Objecttreeitem.makeObjecttreeitem( self, "nom", self.jdcSelection )
        if self.jdcSelectionItem and self.appliEficas.ssIhm==False :
           self.treeJdcSelection = browser.JDCTree( self.jdcSelectionItem, self )
           if debug : print (self.treeJdcSelection)
           self.widgetSelection = self.treeJdcSelection.racine.children[0].fenetre
           self.editor5CLayout.insertWidget(0,self.widgetSelection)


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

    def afficheLabels(self): 
    #--------------------------
        debug = 0
        maRequete = self.genereRequeteSelectionId() 
        if maRequete == "" : return
        if debug : print (' 1ere Requete in chercheLesLabesl : ',  maRequete)
        self.lesIds = self.appelleExecutionRequete(maRequete)
        if debug : print (' lesIds in chercheLesLabesl : ',  self.lesIds)
        if len(self.lesIds) == 0 :
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
        jdcLabelsItem = Objecttreeitem.makeObjecttreeitem( self, "nom", self.jdcLabels )
        if jdcLabelsItem and self.appliEficas.ssIhm==False :
           treeJdcLabels = browser.JDCTree( jdcLabelsItem, self )
           widgetLabels = treeJdcLabels.racine.children[0].fenetre
           widgetLabels.show()


    def genereRequeteSelectionId(self): 
    #----------------------------------
        debug = 0
        self.generator = generator.plugins['5CRequeteSelection']()
        if debug : print (self.jdcSelection)
        retour, titre, requete  = self.generator.genereRequeteSelection(self.jdcSelection)
        if debug : print ('genereRequeteSelection ', retour, titre, requete)
        if not retour : 
           self.afficheMessage(titre, requete)
           return  ''
        return requete
         

    def afficheMessage(self,titre,message,critique=True):
    #----------------------------------------------------
        if self.appliEficas.ssIhm:
           print ('******************', titre, '*************')
           print (message)
           print ('*******************************')
        else:
           if critique :
              from PyQt5.QtWidgets import QMessageBox
              QMessageBox.critical(self, titre, message)
           else :
              from PyQt5.QtWidgets import QMessageBox
              QMessageBox.information(self, titre, message)


    def appelleExecutionRequete(self,requete,chercheUneSeuleValeur=True):
    #--------------------------------------------------------------------
        debug=0
        if debug : print ('_________________________________________')
        if debug : print (requete)

        monConnecteur = connectDB()
        newListe = []
        if not chercheUneSeuleValeur :
            if debug : print (monConnecteur.executeSelectDB(requete))
            for listeTupleChamp in monConnecteur.executeSelectDB(requete):
                if debug : print (listeTupleChamp)
                newListe.append(listeTupleChamp)
        else :
            for listeTupleChamp in monConnecteur.executeSelectDB(requete):
                for tupleChamp in listeTupleChamp:
                    newListe.append(tupleChamp)
        monConnecteur.closeDB()
        if debug : print('resultat ', newListe)
        if debug : print ('_________________________________________')
        return (newListe)



    def afficheResultats(self,jdcResultat, listeId, listeLabels):
    #------------------------------------------------------------
        # Attention aux differences de niveaux entre Cata5CChapeau et CataJobProfile
        # on s appuie sur le 1er element et non le jdc
        self.jdcResultats = jdcResultat
        if self.appliEficas.ssIhm==False :
             if self.widgetResultats : self.editor5CLayout.removeWidget(self.widgetResultats)
             from InterfaceGUI.cinqC.monWidgetProfile import MonWidgetProfile
             self.widgetResultats=MonWidgetProfile(self,jdcResultat, listeId,listeLabels)
             self.editor5CLayout.insertWidget(1,self.widgetResultats)


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


    def lanceXSLT(self):
    #-------------------
        debug=0
        if debug : print ('dans lanceXSLT')
        etape=self.jdcLabels.getEtapesByName('PresentationLabels')[0]
        listeLabelsChoisis = etape.getChild('labels').valeur
        if listeLabelsChoisis == None : return
        ou = os.path.dirname(os.path.abspath(__file__))
        xsltFile = os.path.join(ou, '..','cinqC','generate_profile.xslt')
        jdcResultatsAggreges=self._newJDC(texte='')
        jdcResultatsAggreges.analyse()
        listeId=list(self.dictLabels.keys())
        if debug : print ('listeLabelsChoisis', listeLabelsChoisis)
        debug=0
        for id in listeId:
            if debug : print (id)
            maRequete = 'select  functionsjobstatistics from jobperformance where id = {}'.format(id)
            if debug : print ('lanceXSLT , maRequete : ' , maRequete)
            texteXML = self.appelleExecutionRequete(maRequete)[0]
            labelTxt=''
            for label in listeLabelsChoisis :
                if label in self.dictLabels[id] : 
                   labelTxt=labelTxt+label+','
            labelTxt=labelTxt[0:-1]
            if debug : print ('lesLabels du Job', self.dictLabels[id])
            if debug : print ('labelTxt', labelTxt)
            # Appel du XSLT meme si pas de label pour avoir l etape
            # mais un peu stupide ??
            try:
                fileName = '/tmp/xml4saxon.xml'
                with open(fileName, 'w') as f: f.write(texteXML)
            except Exception as e:
                print (' impossible d ecrire le fichier {} avec le texte {} '.format(fileName,texteXML))
                print("exception", e)
                exit(1)
            try:
                cmd = "saxonb-xslt  -s:{} -xsl:{} label='{}'".format(fileName, xsltFile,labelTxt)
                if debug :  print ('lancement de ', cmd)
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                (outputXML, err) = p.communicate()
                if debug : print (id , 'traite')
                if debug : print (outputXML)
            except Exception as e:
                print("impossible d executer le xsslt generate_profile.xslt sur", fileName)
                print("exception", e)
                exit(1)
            jdcResultatsParId=self._newJDC(texte=outputXML)
            jdcResultatsParId.analyseXML()
            debug=1
            if debug :  
                 file='/tmp/result_'+str(id)+'.xml'
                 with open(file, 'wb') as f: f.write(outputXML)
            debug=0
            #     print ('fichier /tmp/essai.xml cree')
            # on remplace le sha1id par l id car le sha1 n est pas une clef primaire
            e=jdcResultatsParId.etapes[0]
            sha1Id=e.getChild('sha1Id')
            sha1Id.setValeur(str(id))
            jdcResultatsAggreges.register(jdcResultatsParId.etapes[0])
        debug=1
        if debug :  
            self.jdc=jdcResultatsAggreges
            texte=self.getTextJDC()
            with open('/tmp/essai.comm', 'w') as f: f.write(texte)
        self.afficheResultats(jdcResultatsAggreges, listeId, listeLabelsChoisis)

    def afficheInfosForId (self,id):
        maRequete = 'select sha1, testName, version,date, CMakeBuildType,execution,procs, host, OS, totalCputime from jobperformance where id = {}'.format(id)
        lesInfos = self.appelleExecutionRequete(maRequete)
        print (lesInfos)
        #texte="Selection(sha1='{}',testName='{}',version='{}',date='{}', CMakeBuildType='{}',execution='{}',procs={}, host='{}', OS='{}');'.format(lesInfos[0],lesInfos[1],lesInfos[2],lesInfos[3],lesInfos[4],lesInfos[5],lesInfos[6],lesInfos[7],lesInfos[8],lesInfos[9])
        #jdcAAfficher=self._newJDC(texte=texte)
        #jdcAAfficher.analyse()


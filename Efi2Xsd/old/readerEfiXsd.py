#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))


from Accas import *


# ds l init du SIMP il manque siValide et fenetreIhm

from mapDesTypes import dictSIMPEficasXML, dictSIMPXMLEficas
from mapDesTypes import dictFACTEficasXML, dictFACTXMLEficas
from mapDesTypes import dictPROCEficasXML, dictPROCXMLEficas
from mapDesTypes import dictOPEREficasXML, dictOPERXMLEficas
from mapDesTypes import dictBLOCEficasXML, dictBLOCXMLEficas
from mapDesTypes import dictPourCast
from mapDesTypes import listeParamDeTypeTypeAttendu, listeParamDeTypeStr, dictPourCast
from mapDesTypes import listeParamTjsSequence, listeParamSelonType


# ------------------------------
class objetDefinitionAccas:
# ------------------------------

   def argumentXMLToEficas(self):
   # ---------------------------
      # Attention, pas de validation pour l instant
      # il faut verifier la coherence entre les types contenus dans defaut, sug ... et le typeAttendu
      # tout cela dans une fonction verifie pas faite -)

      # Recuperation parametres
      self.dictArgsEficas={}
      for nomXMLArg in dir(self) :
          if nomXMLArg in self.dictATraiter :
              nomEficasArg=self.dictATraiter[nomXMLArg]
              argu=getattr(self,nomXMLArg)
              if argu==None : continue

              if type(nomEficasArg) == types.DictionaryType:
                 for nomXML in list(nomEficasArg.keys()):
                      arguDecoupe=getattr(argu,nomXML)
                      nomEficasDecoupe=nomEficasArg[nomXML]
                      if arguDecoupe == None : continue
                      self.dictArgsEficas[nomEficasDecoupe]=arguDecoupe
              else :
                self.dictArgsEficas[nomEficasArg] = argu
                    
      # Cast dans le bon type des parametres si necessaire
      if 'min' in list(self.dictArgsEficas.keys()): 
            self.dictArgsEficas['min']=int(self.dictArgsEficas['min'])

      if 'max' in list(self.dictArgsEficas.keys()): 
         if self.dictArgsEficas['max']== -1 :  self.dictArgsEficas['max']="**"
         else  :  self.dictArgsEficas['max']=int(self.dictArgsEficas['max'])

      for param in list(self.dictArgsEficas.keys()):
          if param in listeParamDeTypeStr :
             self.dictArgsEficas[param]=unicode(self.dictArgsEficas[param])
      
      # En 2.7 a revoir en 3 ? necessaire
      self.nomObj=str(self.nom)
     
   def getAccasEquivalent(self):
   # ---------------------------
       return self.nomObj, self.objAccas
#

# ---------------------------------------------------------
class objetComposeDefinitionAccas (objetDefinitionAccas):
# ---------------------------------------------------------
    def exploreArbre(self,cata):
    # --------------------------
      liste=[]
      for obj in self.content(): liste.append(obj)
      #liste.reverse()
      # PNPNPN essayer de comprendre reverse ou non

      for obj in liste: 
          if  hasattr(obj,'explore') : obj.explore(cata)
          if  hasattr(obj,'getAccasEquivalent') : 
              nom,objetAccas=obj.getAccasEquivalent()
              self.dictArgsEficas[nom]=objetAccas
     
# ----------------------------------------------------
class monSIMP (efficas.T_SIMP,  objetDefinitionAccas):
# ----------------------------------------------------

   def explore(self,cata):
   # --------------------
      #print ("je passe dans  explore pour SIMP ", self.nom)
      self.dictATraiter= dictSIMPXMLEficas
      self.argumentXMLToEficas()
      #print (self.dictArgsEficas)
      

      self.objAccas=A_SIMP.SIMP(**self.dictArgsEficas)
      self.objAccas.nom=self.nomObj

   def argumentXMLToEficas(self):
   # ----------------------------
      #print self.nom
      objetDefinitionAccas.argumentXMLToEficas(self)

      if self.attendTuple() :
          #nbDElts=type(listeDElt[0]) 
          print self.nomTypeAttendu


      self.traiteLesSequences()
      #self.convertitLesTypes()

   def attendListe(self):
   # ---------------
      if 'max' in self.dictArgsEficas :
        if self.dictArgsEficas['max'] > 1 : return True
        if self.dictArgsEficas['max'] == "**"  : return True
      return False

   def attendTuple(self):
   # -----------------
       if self.dictArgsEficas['typ'] != 'tuple' : return False
       return True
  
   def attendTXM(self):
   # ----------------
       if self.dictArgsEficas['typ'] == 'TXM' : return True
       return False
  

   def traiteLesSequences(self):
   # ---------------------------
       listeDeListe=self.attendListe()
       for param in listeParamTjsSequence :
          if  param in self.dictArgsEficas :
              if listeDeListe == False: 
                #print ('________________________________')
                listeDElt=[]
                for i in range(len(self.dictArgsEficas[param])):
                # ou typesimple ?
                # ici on ne sait pas si on est un type simple ou complexe ?
                    listeDElt.append(self.dictArgsEficas[param][i].content()[0])
                listeRetour=self.convertitListeDsLeBonType(listeDElt)
                #print (listeRetour)
                #print ('________________________________')
                self.dictArgsEficas[param]=listeRetour
              else :
                 listeResultat=[]
                 # on transforme en liste pour traiter chaque elt de la liste
                 for i in range(len(self.dictArgsEficas[param])):
                     if self.dictArgsEficas[param][i].typesimple != None :
                        lesElts=self.dictArgsEficas[param][i].typesimple
                     else :
                        lesElts=self.dictArgsEficas[param][i].content()
                     if (not(isinstance(lesElts,list)) and not (isinstance(lesElts,tuple))):
                        lesElts=(lesElts,)
                        lesEltsTransformes=self.convertitListeDsLeBonType(lesElts)
                     lesEltsTransformes=self.convertitListeDsLeBonType(lesElts)
                     listeResultat.append(lesEltsTransformes)
                 self.dictArgsEficas[param]=listeResultat
              #print ('fin de traiteLesSequences pour', self.nom, ' param :', param, 'listeResultat',self.dictArgsEficas[param])


   def convertitListeDsLeBonType(self,listeDElt):
   # -------------------------------------------
   # Cas des Tuples non traites
       typeAttendu = self.dictArgsEficas['typ']
       if typeAttendu in list(dictPourCast.keys()):
          nouvelleListe=[]
          castDsLeTypeAttendu=dictPourCast[typeAttendu]
          for valeurACaster in listeDElt :
              val=castDsLeTypeAttendu(valeurACaster)
              nouvelleListe.append(val)
          return nouvelleListe
       elif self.attendTuple() :
          nbDElts=type(listeDElt[0]).n
         
       else : return listeDElt
        
     

   def convertitLesTypes(self):
   # ------------------------
   # Cas des Tuples non traites
   # Cas des fonctions utilisateurs non traites

       typeAttendu = self.dictArgsEficas['typ']
       if typeAttendu in list(dictPourCast.keys()):
          castDsLeTypeAttendu=dictPourCast[typeAttendu]
          for param in listeParamDeTypeTypeAttendu :
             if param in list(self.dictArgsEficas.keys()):
                if param in listeParamEnListeSelonType or param in listeParamTjsEnListe : 
                   print ('typeAttendu',typeAttendu)
                   print (self.dictArgsEficas[param])
                   print (self.dictArgsEficas[param].content())
                   print (self.dictArgsEficas[param].content())
                   return
                valeurACaster=self.dictArgsEficas[param].typesimple
                if not isinstance(valeurACaster, (list, tuple)) :
                   val=castDsLeTypeAttendu(valeurACaster)
                   self.dictArgsEficas[param]=val
                else :
                   liste=[]
                   for val in valeurACaster : liste.append(castDsLeTypeAttendu(val))
                   self.dictArgsEficas[param]=liste


# -------------------------------------------------------
class monFACT(efficas.T_FACT, objetComposeDefinitionAccas):
# -------------------------------------------------------
   def explore(self,cata):
   # --------------------
      #print "je passe dans  explore pour FACT ", self.nom

      self.dictATraiter= dictFACTXMLEficas
      self.argumentXMLToEficas()
      self.exploreArbre(cata)
      self.objAccas=A_FACT.FACT(**self.dictArgsEficas)


# ---------------------------------------------------------
class monPROC(efficas.T_PROC, objetComposeDefinitionAccas):
# ---------------------------------------------------------
   def explore(self,cata):
   # --------------------
      print "je passe dans  explore pour PROC ", self.nom
      self.dictATraiter= dictPROCXMLEficas
      self.argumentXMLToEficas()
      self.exploreArbre(cata)
      self.dictArgsEficas['op']=None

      self.objAccas=A_PROC.PROC(**self.dictArgsEficas)
      setattr(cata, self.nomObj,self.objAccas)
      cata.contexteXML[self.nomObj]=self.objAccas

# ---------------------------------------------------------
class monOPER(efficas.T_OPER, objetComposeDefinitionAccas):
# ---------------------------------------------------------
   def explore(self,cata):
# ------------------------
      print "je passe dans  explore pour OPER", self.nom
      self.cata=cata
      self.dictATraiter= dictOPERXMLEficas
      self.argumentXMLToEficas()
      self.exploreArbre(cata)

      textCreationClasse='class '+str(self.typeCree)+'(ASSD): pass\n'
      exec(textCreationClasse,globals())
      maClasseCreee=globals()[self.typeCree]
      self.dictArgsEficas['sd_prod']  = maClasseCreee
      cata.contexteXML[self.typeCree] = maClasseCreee
      
      self.dictArgsEficas['op'] = None
      self.objAccas=A_OPER.OPER(**self.dictArgsEficas)
      setattr(cata, self.nomObj,self.objAccas)
      cata.contexteXML[self.nomObj] = self.objAccas

# ---------------------------------------------------------
class monBLOC(efficas.T_BLOC, objetComposeDefinitionAccas):
# ---------------------------------------------------------
   def explore(self,cata):
# ------------------------
      print ('je passe dans explore pour BLOC', self.nom)
      self.cata=cata
      self.dictATraiter= dictBLOCXMLEficas
      self.argumentXMLToEficas()
      self.exploreArbre(cata)
      self.objAccas=A_BLOC.BLOC(**self.dictArgsEficas)
      setattr(cata, self.nomObj,self.objAccas)
      cata.contexteXML[self.nomObj] = self.objAccas

# ------------------------------
class monCata(efficas.T_cata):
# ------------------------------
   def exploreCata(self):
      # PNPNPN --> il faut revoir ce mecanisme
      self.modeleMetier = None
   # On positionne le contexte ACCAS
      self.JdC = JDC_CATA (code = 'Atmo', execmodul = None,)
      self.contexteXML={}
      objAExplorer=self.commandes[0]
      for obj in objAExplorer.content(): 
         if  hasattr(obj,'explore') : obj.explore(self)
      #print dir(self.JdC)
      
     
   #def dumpXSD(self):
   #   for etape in self.contexteXML.values() :
   #       etape.dumpXSD()

efficas.T_SIMP._SetSupersedingClass(monSIMP)
efficas.T_FACT._SetSupersedingClass(monFACT)
efficas.T_PROC._SetSupersedingClass(monPROC)
efficas.T_OPER._SetSupersedingClass(monOPER)
efficas.T_BLOC._SetSupersedingClass(monBLOC)
efficas.T_cata._SetSupersedingClass(monCata)

if __name__ == "__main__":
#   print dir(efficas)
#   print dir(efficas.T_SIMP)

   #xml = open('cata_test1.xml').read()
   with open('cata.xml') as fd :
     xml=fd.read()
   SchemaMed = efficas.CreateFromDocument(xml)
   SchemaMed.exploreCata()
   #SchemaMed.dumpXSD()


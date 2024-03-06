# -*- coding: iso-8859-1 -*-
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
import os, sys


from Accas.extensions.eficas_exception import EficasException
from Editeur import session
from Editeur.getVersion import getEficasVersion
from Accas.extensions.eficas_translation import tr

from threading import Lock
sessionCount  = 0
lock = Lock()


activeLogging=0
if activeLogging :
   from Editeur.loggingEnvironnement import loggingEnvironnement, fonctionLoguee
else :
   fonctionLoguee = lambda func: func


#-----------------
class EficasAppli:
#-----------------
    """
    Class implementing the main user interface.
    """

    #---------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, code=None, versionCode=None, salome=1, multi=False, langue="fr", ssCode=None, cataFile=None, GUIPath=None, appWeb=None):
    #---------------------------------------------------------------------------------------------------------------------------------------------
        """
        Constructor d appli eficas. classe mere de appli-qtEficas et de appli-web eficas et utilisee sans IHM pour les
        transformations des catas en XSD, des comm en XML et de validation des donnees
        les parametres sont :
            nom du code (exple Adao)
            versionCode (version du code permet de retrouver le catalogue dans le fichier prefs : exple V10-4)
            salome  : lance ou non a partir de salome 
            multi (permet de ne pas specifier le code mais de le demander )
            langue des messages
            ssCode (utilise pour MAP permet de distinguer un patron specifique, un catalogue specifique...)
            fichier catalogue utilise
        """
        self.code = code
        self.ssCode = ssCode
        self.multi = multi
        self.salome = salome
        self.appWeb = appWeb
        self.dictEditorIdSessionId = {}
        self.dictTypeDeSession = {} # contient le type de la session ( QT, WEB pour rediriger les messages)

        version = getEficasVersion()
        self.versionEficas = "Eficas Salome " + version
        self.GUIPath = GUIPath
        self.dict_reels = {}
        self.fichierIn = None
        self.fichierOut = None

        self.ficRecents = {}
        self.mesScripts = {}
        self.listePathAEnlever = []

        if cataFile == None: self.cataFile = session.d_env.cataFile
        else: self.cataFile = cataFile

        self.versionCode = versionCode
        if session.d_env.versionCode: self.versionCode = session.d_env.versionCode

        if self.salome:
            try:
                from Accas import eficasSalome
                Accas.SalomeEntry = eficasSalome.SalomeEntry
            except  Exception as e:
                print ("impossible d importer les salome entry")
                print (str(e))

        if langue == "fr": self.langue = langue
        else: self.langue = "ang"

        if self.multi == False:
            self.definitCode(code, ssCode)
            if code == None: return
        else : 
            from Editeur.configuration import BaseConfiguration
            self.maConfiguration = BaseConfiguration(self)

        self.withUQ = False
        self.genereXSD = False
        from Editeur.editor_manager import EditorManager
        self.editorManager = EditorManager(self)
        # Attention n appelle pas openFiles car les classes derivees
        # changent l editorManager

    #--------------------
    def getVersion(self):
    #--------------------
        return getEficasVersion()

    #-----------------------------------
    def definitCode(self, code, ssCode):
    #-----------------------------------
        # ssCode sert pour Map
        self.code = code
        self.ssCode = ssCode
        if self.code == None: return  

        if ssCode != None:
            self.formatFichierOut = ssCode  # par defaut
            prefsCode.NAME_SCHEME = ssCode
        else:
            self.formatFichierIn = "python"  # par defaut
            self.formatFichierOut = "python"  # par defaut

        self.listePathAEnlever = []
        from Editeur.configuration import BaseConfiguration
        self.maConfiguration = BaseConfiguration(self)

        if hasattr(self, "maConfiguration") and self.maConfiguration.translatorFile:
            from Accas.extensions import localisation
            localisation.localise( None, self.langue,
                translatorFile=self.maConfiguration.translatorFile,)

        # Comment faire si Multi ?
        self.withXSD   = session.d_env.withXSD

    #-------------------------
    def getSource(self, file):
    #-------------------------
        # appele par Editeur/session.py
        import Accas.IO.reader

        p = convert.plugins["python"]()
        p.readfile(file)
        texte = p.convert("execnoparseur")
        return texte

    #------------------------------------------------------
    def getEditor(self, fichier=None, jdc=None, include=0):
    #------------------------------------------------------
        #PN reflechir a ce que cela veut dire d avoir plusieurs editeurs
        # en TUI
        if (hasattr(self, "editor")) and self.editor != None:
            print("un seul editeur par application eficas_appli sans Ihm ? ")
        #     sys.exit()
        self.editor = self.editorManager.getEditor(fichier, jdc, include)
        return self.editor

    #--------------------------------------------------------------------------------
    def getWebEditor(self, sId, cataFile = None, datasetFile=None, jdc=None, include=0):
    #--------------------------------------------------------------------------------
        debug = 1
        if sId == None : 
           titre = 'Requete non valide'
           message = 'Le parametre identifiant la Session Eficas est obligatoire'
           self.propageToWebApp('afficheMessage', titre+texte, 'rouge')
        self.dictTypeDeSession[sId]  =  'Web'
        (editor, CR, message)   = self.editorManager.getWebEditor(sId, cataFile,datasetFile, jdc, include)
        if debug : 
           print ('getWebEditor id de sesssion :', sId, ' editor : ', editor.editorId)
           print (editor, CR, message)
        return (editor, CR, message) 

    #------------------------------------------------------------------------------------------
    def getTUIEditor (self,sId = None, cataFile = None, datasetFile=None, jdc=None, include=0):
    #-------------------------------------------------------------------------------------------
        if sId == None : 
           self.affichageMessage('Requete non valide', 'Le parametre identifiant la Session Eficas est obligatoire',True)
        self.dictTypeDeSession[sId]  =  'TUI'
        (editor, CR, message)   = self.editorManager.getTUIEditor(sId, cata, fichier, fichier, jdc, include)
        return (editor, CR, message) 

    #---------------------------
    def getEditorById(self, eId):
    #----------------------------
        return self.editorManager.getEditorById(eId)

    #----------------------------------
    def setCurrentEditorById(self,id):
    #----------------------------------
        return self.editorManager.setCurrentEditorById(self,id)

    #------------------
    def fileSave(self):
    #-------------------
        return self.editorManager.saveFile()

    #------------------------------
    def fileSaveAs(self, fileName):
    #------------------------------
        return self.editorManager.saveFile()
        if self.editor == None:
            return False
        ok = editor.saveFileAs()
        print("ok ", ok)

    #-----------------------------------------
    def dumpXsd(self, avecEltAbstrait=False):
    #-----------------------------------------
        currentCata = CONTEXT.getCurrentCata()
        texteXSD = currentCata.dumpXsd(avecEltAbstrait)
        return texteXSD


    #-------------------
    def saveUQFile(self):
    #-------------------
        self.editorManager.saveUQFile()

    #----------------------
    def exeUQScript(self):
    #----------------------
        self.editorManager.exeUQScript()

    #----------------------
    def savePersalys(self):
    #----------------------
        self.editorManager.savePersalys()

    #----------------------
    def ajoutCommentaire(self):
    #----------------------
        self.editorManager.ajoutCommentaire()

    #----------------------
    def openFiles(self):
    #----------------------
        # Ouverture des fichiers de commandes donnes sur la ligne de commande
        cwd = os.getcwd()
        self.dir = cwd
        for study in session.d_env.studies:
            os.chdir(cwd)
            d = session.getUnit(study, self)
            self.editorManager.openFile(fichier=study["comm"])


    #---------------------
    def saveFullFile(self):
    #----------------------
    # Pour Telemac
        return self.editorManager.saveCompleteCurrentEditor()

    #-----------------
    def fileNew(self):
    #-------------------
        try:
            self.editorManager.getEditor()
        except EficasException as exc:
            msg = str(exc)
            if msg != "":
                QMessageBox.warning(self, tr("Erreur"), msg)


    #------------------------------
    def fileSaveInLigneFormat(self):
    #------------------------------
        return self.editorManager.fileSaveInLigneFormat()

    #------------------
    def fileSave(self):
    #------------------
        return self.editorManager.handleSave()

    #--------------------
    def fileSaveAs(self):
    #--------------------
        return self.editorManager.handleSaveAs()

    #-------------------
    def fileClose(self):
    #-------------------
        return self.editorManager.fileClose()

    #-------------------
    def closeAllFiles(self):
    #-------------------
        self.editorManager.closeAllFiles()

    #------------
    def run(self):
    #-------------
        self.editorManager.run()

    #----------------
    def saveRun(self):
    #----------------
        self.editorManager.saveRun()

    #--------------------------
    def getJdcFichierSource(self):
    #--------------------------
        return self.editorManager.getJdcFichierSource()

    #-----------------------
    def getJdcRapport(self):
    #-----------------------
        return self.editorManager.getJdcRapport()

    #-----------------------
    def getJjdcRegles(self):
    #-----------------------
        return self.editorManager.JdcRegles()

    #------------------------------
    def getJdcFichierResultat(self):
    #------------------------------
        self.editorManager.getJdcFichierResultat()

    #------------------------------------
    def handleAjoutEtape(self, nomEtape):
    #------------------------------------
        self.editorManager.handleAjoutEtape(nomEtape)

    #----------------
    def ajoutUQ(self):
    #----------------
        self.withUQ = True
        self.formatFichierIn = "pythonUQ"  # par defaut

    #----------------------
    def getSessionId(self):
    #----------------------
    # TODO doit on mettre le type de session en parametre ?
    # tant qu on a pas pris un editor la session est tague TUI
        global sessionCount
        try : 
            with lock:
                sessionCount += 1
                self.dictTypeDeSession[sessionCount]='TUI'
                return (sessionCount, 0, '')
        except :
            return (sessionCount, 1, 'impossible de donner un id : {}.format(str(e))')

    #---------------------------------------------------------------------------
    def propageToWebApp(self, fction, sessionId,  *args, **kwargs):
    #---------------------------------------------------------------------------
        #if fction =='propageValide' :
        debug=1
        if debug  : print ('PNPNPN : WebEficasAppli.toWebApp',  fction,  *args, **kwargs)
        if self.appWeb == None  : return
        self.appWeb.fromConnecteur(fction, sessionId,  *args, **kwargs)

    #--------------------------------------------------------------------------
    def afficheMessage (self, titre, texte, critical=True, emitEditorId = None ):
    #--------------------------------------------------------------------------
        print ('*******************************')
        if emitEditor != None :
            print ('message emis par ', emitEditorId)

        print (titre)
        print ('-------------------------------')
        print (texte)
        print ('-------------------------------')
        if critical : exit(1)

    #--------------------------------------------------------------------------
    # Est-ce que cela sera utilise ?
    def propageMessage (self, titre, texte, critical=True, emitEditorId = None ):
    #--------------------------------------------------------------------------
        if emitEditorId == None :
           self.afficheMessage(titre, texte, critical)
           return
        for sessionId in self.dictEditorIdSessionId[emitEditorId]:
            if self.dictTypeDeSession[sessionId] == 'TUI':
               self.afficheMessage(self, titre, texte, critical, emitEditorId )
            elif self.dictTypeDeSession[sessionId] == 'Web':
                if critical : self.propageToWebApp('afficheMessage', sessionId,  titre+texte, 'rouge')
                else : self.propageToWebApp('afficheMessage', sessionId, titre+texte)
            else :
                print ('propageInfo de Appli  : pb de type de session dans eficas')
                
    #-------------------------------------------------------------------------------------
    def propageChange (self, emitSessionId, emitEditorId, toAll , fction, *args, **kwargs):
    #--------------------------------------------------------------------------------------
        debug = 1
        if debug : 
           print ("------------------------------------------ Eficas")
           print ('propageChange avec les arguments ')
           print ( emitSessionId, emitEditorId, toAll , fction, *args, **kwargs)
           print (self.dictEditorIdSessionId)
           print ("------------------------------------------ ")
        for sessionId in self.dictEditorIdSessionId[emitEditorId]:
            print ('sessionId', sessionId)
            if not toAll and sessionId == emitSessionId : continue
            if self.dictTypeDeSession[sessionId] == 'TUI': 
                print ('la session est TUI, on ne fait rien')
                continue # Rien a faire le JDC est correcte
            elif self.dictTypeDeSession[sessionId] == 'Web': # on verra le QT apres
                print ('on propage pour ', sessionId )
                self.propageToWebApp(fction, sessionId,  *args, **kwargs)

    #---------------------------------------------------------------------------
    #PN --> normalement les codes retours et les messages de retour sont suffisants
    #def displayMessageInSid (self, Sid, titre, texte, critical=True ):
    #---------------------------------------------------------------------------

if __name__ == "__main__":
    # Modules Eficas
    pass

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

import os
from Accas.extensions.eficas_translation import tr
from Editeur.editor_manager import EditorManager

#-----------------------------------#
class WebEditorManager(EditorManager):
#-----------------------------------#
    """
    classe qui gere quel est l editor web actif
    """

    #--------------------------------
    def __init__(self, appliEficas):
    #--------------------------------
        super().__init__(appliEficas)
        self.dictSessions={}


    #---------------------------------------
    def afficheInfos(self,txt,couleur=None):
    #---------------------------------------
        """
          Est-ce que le web_manager a des infos a afficher ?
          sans session ?
        """
        self.appliEficas.toWebApp('afficheInfos', txt, couleur) 


    # ------------------------------------------------------
    def getEditor(self, fichier=None, jdc=None, session = 1 ):
    # ------------------------------------------------------
        """
          Retourne un nouvel editeur ou le meme si doublon
          gere la liste des connexions pour propager les infos
          a affiner : le nom du fichier n est pas determinant
          il faut aussi la machine dont il provient
        """
        for indexEditor in self.dictEditors:
            editor = self.dictEditors[indexEditor]
            if self.samePath(fichier, editor.getFileName()):
                double = editor
             
        else:
            from web_editor import WebEditor
            editor = WebEditor(self.appliEficas, fichier)
            if editor.jdc:  # le fichier est bien un jdc
                self.editors.append(editor)
            else:
                editor=None
        return editor



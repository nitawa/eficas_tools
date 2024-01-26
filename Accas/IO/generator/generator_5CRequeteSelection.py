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
"""Ce module contient le plugin generateur de fichier au format  Code_Carmel3D pour EFICAS.
"""

import traceback
from Accas.extensions.eficas_translation import tr
from Accas.IO.generator.generator_python import PythonGenerator


def entryPoint():
    """
    Retourne les informations necessaires pour le chargeur de plugins
    Ces informations sont retournees dans un dictionnaire
    # name: Le nom du plugin
    # factory: La factory pour creer une instance du plugin
    """
    return {
        "name": "5CRequeteSelection",
        "factory": RequeteSelectionGenerator,
    }


class RequeteSelectionGenerator(PythonGenerator):
    """
    Ce generateur parcourt un etapeSelectionet de type JDC et produit
    un texte pour requeter la base
    """

    # Les extensions de fichier permis?
    pass
    extensions = (".comm",)

    # ----------------------------------------------------------------------------------------
    def genereRequeteSelection(self, jdc):
        debug = 0

        texteRequete = "select id from JobPerformance where "
        etapeSelection = jdc.etapes[0]
        if debug:
            print("appelle genereRequeteSelection avec jdc", jdc)
        if debug:
            print("etapeSelection", etapeSelection)

        # L etapeSelection n est pas valide : Tout est obligatoire or tout n est pas rempli
        # On se contente de verifier les regles d afficher les regles non valides
        # en enelvant les motclefs invalides
        listeRegles = etapeSelection.getRegles()
        dictObjPresents = etapeSelection.dictMcPresents(restreint="oui")
        dictObjPresentsValides = {}

        for nomObj, obj in dictObjPresents.items():
            if obj.isValid():
                dictObjPresentsValides[nomObj] = obj
        if debug:
            print("dictObjPresentsValides", dictObjPresentsValides)

        commentaire = "Les données sont insuffisantes pour générer les requetes : \n"
        reglesOk = 1
        texteErreurs = []
        if len(listeRegles) > 0:
            for regle in listeRegles:
                if debug:
                    print(regle)
                texteRegle = regle.getText()
                texteMauvais, test = regle.verif(dictObjPresentsValides)
                if debug:
                    print(texteMauvais, test)
                if not test:
                    reglesOk = 0
                    texteErreurs.append(texteMauvais)
        if not reglesOk:
            return 0, commentaire, "".join(texteErreurs)

        separateur = ""
        for nomObj, obj in dictObjPresentsValides.items():
            texteRequete += separateur
            texteRequete += nomObj
            if nomObj.startswith("Debut"):
                operateur = ">"
            elif nomObj.endswith("Fin"):
                operateur = "<"
            else:
                operateur = "="
            texteRequete += operateur
            lesTypes = obj.getType()
            if "TXM" in lesTypes:
                texteRequete += "'"
            texteRequete += str(obj.valeur)
            if "TXM" in lesTypes:
                texteRequete += "'"
            separateur = " and "
        return 1, "requete generee : ", texteRequete

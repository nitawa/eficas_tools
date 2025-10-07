# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002, 2013  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================

# Find pyside2-uic executable
find_program(PYSIDE2_UIC_EXECUTABLE NAMES pyside2-uic pyside2-uic.bat)
if(NOT PYSIDE2_UIC_EXECUTABLE)
  message(FATAL_ERROR "pyside2-uic not found. Please install PySide2 and ensure pyside2-uic is in your PATH.")
endif()

set ( _PYFILES )
macro ( eficas_compile_ui uifile )
  get_filename_component ( _file_we ${uifile} NAME_WE )
  set ( _pyfile "${_file_we}.py" )
  set ( _main_py "${CMAKE_CURRENT_BINARY_DIR}/${_file_we}_main.py" )
  configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/ui_py.in
    ${_main_py}
    @ONLY
    NEWLINE_STYLE UNIX
  )
  # Generate the python file and append the __main__ block
  add_custom_command (
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile}
    COMMAND ${PYSIDE2_UIC_EXECUTABLE} -o ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile} ${CMAKE_CURRENT_SOURCE_DIR}/${uifile}
    COMMAND ${CMAKE_COMMAND} -E cat ${_main_py} >> ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile}
    MAIN_DEPENDENCY ${CMAKE_CURRENT_SOURCE_DIR}/${uifile}
    COMMENT "Compiling ${uifile} with pyside2-uic and appending __main__ block"
    )
  list ( APPEND _PYFILES ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile} )
endmacro ( eficas_compile_ui )

set(UI_FILES
  myMain.ui
  desBaseWidget.ui
  desChoixCata.ui
  desChoixCode.ui
  desChoixCommandes.ui
  desChoixLangue.ui
  desRecherche.ui
  desRechercheCatalogue.ui
  desSelectVal.ui
  desViewTexte.ui
  desViewRegles.ui
  desVisu.ui
  desWidgetCreeParam.ui
  desWidgetCommande.ui
  desWidgetFormule.ui
  desWidgetOptionnel.ui
  desGroupeOptionnel.ui
  Tuple2.ui
  Tuple3.ui
  Tuple4.ui
  Tuple5.ui
  Tuple6.ui
  Tuple7.ui
  Tuple8.ui
  Tuple9.ui
  Tuple10.ui
  desPBOptionnelMT.ui
  desWidgetBloc.ui
  desWidgetCB.ui
  desWidgetCBIntoSug.ui
  desWidgetCommentaire.ui
  desWidgetDate.ui
  desWidgetFact.ui
  desWidgetFactPlie.ui
  desWidgetFactTableau.ui
  desWidgetHeure.ui
  desWidgetInactif.ui
  desWidgetInformation.ui
  desWidgetIntoSug.ui
  desWidgetMatrice.ui
  desWidgetNiveauFact.ui
  desWidgetParam.ui
  desWidgetPlusieursBase.ui
  desWidgetPlusieursInto.ui
  desWidgetPlusieursIntoOrdonne.ui
  desWidgetPlusieursTuple.ui
  desWidgetPlusieursPlie.ui
  desWidgetRadioButton.ui
  desWidget4a6RadioButton.ui
  desWidgetSDCOInto.ui
  desWidgetSimpBase.ui
  desWidgetSimpBool.ui
  desWidgetSimpComplexe.ui
  desWidgetSimpFichier.ui
  desWidgetSimpSalome.ui
  desWidgetSimpTxt.ui
  desWidgetTableau.ui
  desWidgetTuple2.ui
  desWidgetTuple3.ui
  desWidgetTuple4.ui
  desWidgetTuple5.ui
  desWidgetTuple6.ui
  desWidgetTuple7.ui
  desWidgetTuple8.ui
  desWidgetTuple9.ui
  desWidgetTuple10.ui
  desWidgetUniqueSDCO.ui
  desWidgetVide.ui
)

foreach(uifile ${UI_FILES})
  set(UI_CLASS ${uifile})
  string(REPLACE ".ui" "" UI_CLASS ${UI_CLASS})
  eficas_compile_ui(${uifile})
endforeach()

add_custom_target ( CompileUI ALL DEPENDS ${_PYFILES}
                    COMMENT "Built UI files"
                  )

install ( FILES ${_PYFILES}
          DESTINATION ${CMAKE_INSTALL_PREFIX}/UiQT5
        )

# Rules to compile TS files
SET(TSFILES eficas_en.ts
            eficas_fr.ts)

SET(QMFILES)
FOREACH(input ${TSFILES})
  GET_FILENAME_COMPONENT(base ${input} NAME_WE)
  SET(output ${CMAKE_CURRENT_BINARY_DIR}/${base}.qm)
  SET(QMFILES ${QMFILES} ${output})
  ADD_CUSTOM_COMMAND(OUTPUT ${output}
    COMMAND ${QT_LRELEASE_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${input} -qm ${output}
    #    EXECUTE_PROCESS(COMMAND \${MYLRELEASE} \${MYTSFILE} -qm \${MYFULLDIR}/\${MYOUTQMFILE})
    MAIN_DEPENDENCY ${input})
ENDFOREACH(input ${TSFILES})

ADD_CUSTOM_TARGET(CompileTS ALL DEPENDS ${QMFILES})
INSTALL(FILES ${QMFILES} DESTINATION ${CMAKE_INSTALL_PREFIX}/UiQT5)

### Local Variables:
### mode: cmake
### End:

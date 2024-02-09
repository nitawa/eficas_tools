# ./raw/cataProfileResultat_driver.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1003192bf68b85e553436b558a22889d4ec630b9
# Generated 2023-11-16 11:25:23.719466 by PyXB version 1.2.7.dev1 using Python 3.9.2.final.0
# Namespace odyssee/cocagne/CataProfileResultat

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c4a65e42-c02c-4a8d-bf4d-30cacf38e1a0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.7.dev1'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('odyssee/cocagne/CataProfileResultat', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: {odyssee/cocagne/CataProfileResultat}AccasAssd
class AccasAssd (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccasAssd')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 7, 1)
    _Documentation = None
AccasAssd._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AccasAssd', AccasAssd)
_module_typeBindings.AccasAssd = AccasAssd

# Atomic simple type: {odyssee/cocagne/CataProfileResultat}T_sha1Id
class T_sha1Id (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1Id')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 11, 1)
    _Documentation = None
T_sha1Id._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1Id', T_sha1Id)
_module_typeBindings.T_sha1Id = T_sha1Id

# Atomic simple type: {odyssee/cocagne/CataProfileResultat}T_cpuTotalTime
class T_cpuTotalTime (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTotalTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 15, 1)
    _Documentation = None
T_cpuTotalTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_cpuTotalTime', T_cpuTotalTime)
_module_typeBindings.T_cpuTotalTime = T_cpuTotalTime

# Atomic simple type: {odyssee/cocagne/CataProfileResultat}T_label
class T_label (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_label')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 19, 1)
    _Documentation = None
T_label._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_label', T_label)
_module_typeBindings.T_label = T_label

# Atomic simple type: {odyssee/cocagne/CataProfileResultat}T_cpuTime
class T_cpuTime (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 23, 1)
    _Documentation = None
T_cpuTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_cpuTime', T_cpuTime)
_module_typeBindings.T_cpuTime = T_cpuTime

# Atomic simple type: {odyssee/cocagne/CataProfileResultat}T_calls
class T_calls (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_calls')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 27, 1)
    _Documentation = None
T_calls._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_calls', T_calls)
_module_typeBindings.T_calls = T_calls

# Atomic simple type: {odyssee/cocagne/CataProfileResultat}T_fractionOfTotalTime
class T_fractionOfTotalTime (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfTotalTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 31, 1)
    _Documentation = None
T_fractionOfTotalTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_fractionOfTotalTime', T_fractionOfTotalTime)
_module_typeBindings.T_fractionOfTotalTime = T_fractionOfTotalTime

# Complex type {odyssee/cocagne/CataProfileResultat}T_fonction with content type ELEMENT_ONLY
class T_fonction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/CataProfileResultat}T_fonction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fonction')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 35, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/CataProfileResultat}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__odysseecocagneCataProfileResultat_T_fonction_odysseecocagneCataProfileResultatlabel', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 37, 3), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element {odyssee/cocagne/CataProfileResultat}cpuTime uses Python identifier cpuTime
    __cpuTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), 'cpuTime', '__odysseecocagneCataProfileResultat_T_fonction_odysseecocagneCataProfileResultatcpuTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 38, 3), )

    
    cpuTime = property(__cpuTime.value, __cpuTime.set, None, None)

    
    # Element {odyssee/cocagne/CataProfileResultat}calls uses Python identifier calls
    __calls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'calls'), 'calls', '__odysseecocagneCataProfileResultat_T_fonction_odysseecocagneCataProfileResultatcalls', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 39, 3), )

    
    calls = property(__calls.value, __calls.set, None, None)

    
    # Element {odyssee/cocagne/CataProfileResultat}fractionOfTotalTime uses Python identifier fractionOfTotalTime
    __fractionOfTotalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), 'fractionOfTotalTime', '__odysseecocagneCataProfileResultat_T_fonction_odysseecocagneCataProfileResultatfractionOfTotalTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 40, 3), )

    
    fractionOfTotalTime = property(__fractionOfTotalTime.value, __fractionOfTotalTime.set, None, None)

    _ElementMap.update({
        __label.name() : __label,
        __cpuTime.name() : __cpuTime,
        __calls.name() : __calls,
        __fractionOfTotalTime.name() : __fractionOfTotalTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_fonction = T_fonction
Namespace.addCategoryObject('typeBinding', 'T_fonction', T_fonction)


# Complex type {odyssee/cocagne/CataProfileResultat}T_MyProfileResultat with content type ELEMENT_ONLY
class T_MyProfileResultat (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/CataProfileResultat}T_MyProfileResultat with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_MyProfileResultat')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 43, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/CataProfileResultat}sha1Id uses Python identifier sha1Id
    __sha1Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1Id'), 'sha1Id', '__odysseecocagneCataProfileResultat_T_MyProfileResultat_odysseecocagneCataProfileResultatsha1Id', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 45, 3), )

    
    sha1Id = property(__sha1Id.value, __sha1Id.set, None, None)

    
    # Element {odyssee/cocagne/CataProfileResultat}cpuTotalTime uses Python identifier cpuTotalTime
    __cpuTotalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuTotalTime'), 'cpuTotalTime', '__odysseecocagneCataProfileResultat_T_MyProfileResultat_odysseecocagneCataProfileResultatcpuTotalTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 46, 3), )

    
    cpuTotalTime = property(__cpuTotalTime.value, __cpuTotalTime.set, None, None)

    
    # Element {odyssee/cocagne/CataProfileResultat}fonction uses Python identifier fonction
    __fonction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fonction'), 'fonction', '__odysseecocagneCataProfileResultat_T_MyProfileResultat_odysseecocagneCataProfileResultatfonction', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 47, 3), )

    
    fonction = property(__fonction.value, __fonction.set, None, None)

    _ElementMap.update({
        __sha1Id.name() : __sha1Id,
        __cpuTotalTime.name() : __cpuTotalTime,
        __fonction.name() : __fonction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_MyProfileResultat = T_MyProfileResultat
Namespace.addCategoryObject('typeBinding', 'T_MyProfileResultat', T_MyProfileResultat)


# Complex type {odyssee/cocagne/CataProfileResultat}T_CataProfileResultat with content type ELEMENT_ONLY
class T_CataProfileResultat (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/CataProfileResultat}T_CataProfileResultat with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_CataProfileResultat')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/CataProfileResultat}MyProfileResultat uses Python identifier MyProfileResultat
    __MyProfileResultat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MyProfileResultat'), 'MyProfileResultat', '__odysseecocagneCataProfileResultat_T_CataProfileResultat_odysseecocagneCataProfileResultatMyProfileResultat', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 53, 3), )

    
    MyProfileResultat = property(__MyProfileResultat.value, __MyProfileResultat.set, None, None)

    _ElementMap.update({
        __MyProfileResultat.name() : __MyProfileResultat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_CataProfileResultat = T_CataProfileResultat
Namespace.addCategoryObject('typeBinding', 'T_CataProfileResultat', T_CataProfileResultat)


CataProfileResultat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CataProfileResultat'), T_CataProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', CataProfileResultat.name().localName(), CataProfileResultat)



T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), T_label, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 37, 3)))

T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), T_cpuTime, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 38, 3)))

T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calls'), T_calls, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 39, 3)))

T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), T_fractionOfTotalTime, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 40, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 37, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 38, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'calls')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 39, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 40, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_fonction._Automaton = _BuildAutomaton()




T_MyProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1Id'), T_sha1Id, scope=T_MyProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 45, 3)))

T_MyProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuTotalTime'), T_cpuTotalTime, scope=T_MyProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 46, 3)))

T_MyProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fonction'), T_fonction, scope=T_MyProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 47, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 47, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1Id')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 45, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_MyProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuTotalTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 46, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(T_MyProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fonction')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 47, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_MyProfileResultat._Automaton = _BuildAutomaton_()




T_CataProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MyProfileResultat'), T_MyProfileResultat, scope=T_CataProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 53, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 52, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 53, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(T_CataProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MyProfileResultat')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataProfileResultat.xsd', 53, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
T_CataProfileResultat._Automaton = _BuildAutomaton_2()


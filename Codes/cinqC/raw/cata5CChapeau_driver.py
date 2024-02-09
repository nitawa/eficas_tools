# ./raw/cata5CChapeau_driver.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:060c125af1bd3520c12aa37a81f60e8b7844ea74
# Generated 2023-11-16 15:38:19.715223 by PyXB version 1.2.7.dev1 using Python 3.9.2.final.0
# Namespace odyssee/cocagne/Gui5C

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:5f6b8aa0-2120-4d9a-b08b-678025d0091f')

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
Namespace = pyxb.namespace.NamespaceForURI('odyssee/cocagne/Gui5C', create_if_missing=True)
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


# Atomic simple type: {odyssee/cocagne/Gui5C}AccasAssd
class AccasAssd (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccasAssd')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 7, 1)
    _Documentation = None
AccasAssd._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AccasAssd', AccasAssd)
_module_typeBindings.AccasAssd = AccasAssd

# Atomic simple type: {odyssee/cocagne/Gui5C}T_sha1
class T_sha1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 11, 1)
    _Documentation = None
T_sha1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1', T_sha1)
_module_typeBindings.T_sha1 = T_sha1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_testName
class T_testName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_testName')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 15, 1)
    _Documentation = None
T_testName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_testName', T_testName)
_module_typeBindings.T_testName = T_testName

# Atomic simple type: {odyssee/cocagne/Gui5C}T_version
class T_version (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_version')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 19, 1)
    _Documentation = None
T_version._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_version', T_version)
_module_typeBindings.T_version = T_version

# Atomic simple type: {odyssee/cocagne/Gui5C}T_date
class T_date (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_date')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 23, 1)
    _Documentation = None
T_date._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_date', T_date)
_module_typeBindings.T_date = T_date

# Atomic simple type: {odyssee/cocagne/Gui5C}T_CMakeBuildType
class T_CMakeBuildType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_CMakeBuildType')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 27, 1)
    _Documentation = None
T_CMakeBuildType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=T_CMakeBuildType)
T_CMakeBuildType.Release = T_CMakeBuildType._CF_enumeration.addEnumeration(unicode_value='Release', tag='Release')
T_CMakeBuildType.Debug = T_CMakeBuildType._CF_enumeration.addEnumeration(unicode_value='Debug', tag='Debug')
T_CMakeBuildType.RelWithDebInfo = T_CMakeBuildType._CF_enumeration.addEnumeration(unicode_value='RelWithDebInfo', tag='RelWithDebInfo')
T_CMakeBuildType._InitializeFacetMap(T_CMakeBuildType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'T_CMakeBuildType', T_CMakeBuildType)
_module_typeBindings.T_CMakeBuildType = T_CMakeBuildType

# Atomic simple type: {odyssee/cocagne/Gui5C}T_execution
class T_execution (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_execution')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 34, 1)
    _Documentation = None
T_execution._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=T_execution)
T_execution.par = T_execution._CF_enumeration.addEnumeration(unicode_value='par', tag='par')
T_execution.seq = T_execution._CF_enumeration.addEnumeration(unicode_value='seq', tag='seq')
T_execution._InitializeFacetMap(T_execution._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'T_execution', T_execution)
_module_typeBindings.T_execution = T_execution

# Atomic simple type: {odyssee/cocagne/Gui5C}T_procs
class T_procs (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_procs')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 40, 1)
    _Documentation = None
T_procs._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_procs', T_procs)
_module_typeBindings.T_procs = T_procs

# Atomic simple type: {odyssee/cocagne/Gui5C}T_host
class T_host (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_host')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 44, 1)
    _Documentation = None
T_host._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_host', T_host)
_module_typeBindings.T_host = T_host

# Atomic simple type: {odyssee/cocagne/Gui5C}T_OS
class T_OS (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_OS')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 48, 1)
    _Documentation = None
T_OS._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_OS', T_OS)
_module_typeBindings.T_OS = T_OS

# Atomic simple type: {odyssee/cocagne/Gui5C}T_totalCpuTime_NoUnit
class T_totalCpuTime_NoUnit (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_totalCpuTime_NoUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 52, 1)
    _Documentation = None
T_totalCpuTime_NoUnit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_totalCpuTime_NoUnit', T_totalCpuTime_NoUnit)
_module_typeBindings.T_totalCpuTime_NoUnit = T_totalCpuTime_NoUnit

# Atomic simple type: {odyssee/cocagne/Gui5C}T_label
class T_label (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_label')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 63, 1)
    _Documentation = None
T_label._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_label', T_label)
_module_typeBindings.T_label = T_label

# Atomic simple type: {odyssee/cocagne/Gui5C}T_cpuTime_NoUnit
class T_cpuTime_NoUnit (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTime_NoUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 67, 1)
    _Documentation = None
T_cpuTime_NoUnit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_cpuTime_NoUnit', T_cpuTime_NoUnit)
_module_typeBindings.T_cpuTime_NoUnit = T_cpuTime_NoUnit

# Atomic simple type: {odyssee/cocagne/Gui5C}T_fractionOfTotalTime
class T_fractionOfTotalTime (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfTotalTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 78, 1)
    _Documentation = None
T_fractionOfTotalTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_fractionOfTotalTime', T_fractionOfTotalTime)
_module_typeBindings.T_fractionOfTotalTime = T_fractionOfTotalTime

# Atomic simple type: {odyssee/cocagne/Gui5C}T_calls
class T_calls (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_calls')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 82, 1)
    _Documentation = None
T_calls._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_calls', T_calls)
_module_typeBindings.T_calls = T_calls

# Atomic simple type: {odyssee/cocagne/Gui5C}T_depth
class T_depth (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_depth')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 86, 1)
    _Documentation = None
T_depth._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_depth', T_depth)
_module_typeBindings.T_depth = T_depth

# Atomic simple type: {odyssee/cocagne/Gui5C}T_fractionOfCallerTime_NoUnit
class T_fractionOfCallerTime_NoUnit (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfCallerTime_NoUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 90, 1)
    _Documentation = None
T_fractionOfCallerTime_NoUnit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_fractionOfCallerTime_NoUnit', T_fractionOfCallerTime_NoUnit)
_module_typeBindings.T_fractionOfCallerTime_NoUnit = T_fractionOfCallerTime_NoUnit

# Atomic simple type: {odyssee/cocagne/Gui5C}T_testName_1
class T_testName_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_testName_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 132, 1)
    _Documentation = None
T_testName_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_testName_1', T_testName_1)
_module_typeBindings.T_testName_1 = T_testName_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_sha1_1
class T_sha1_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 136, 1)
    _Documentation = None
T_sha1_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1_1', T_sha1_1)
_module_typeBindings.T_sha1_1 = T_sha1_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_sha1Debut
class T_sha1Debut (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1Debut')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 140, 1)
    _Documentation = None
T_sha1Debut._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1Debut', T_sha1Debut)
_module_typeBindings.T_sha1Debut = T_sha1Debut

# Atomic simple type: {odyssee/cocagne/Gui5C}T_sha1Fin
class T_sha1Fin (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1Fin')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 144, 1)
    _Documentation = None
T_sha1Fin._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1Fin', T_sha1Fin)
_module_typeBindings.T_sha1Fin = T_sha1Fin

# Atomic simple type: {odyssee/cocagne/Gui5C}T_date_1
class T_date_1 (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_date_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 148, 1)
    _Documentation = None
T_date_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_date_1', T_date_1)
_module_typeBindings.T_date_1 = T_date_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_dateDebut
class T_dateDebut (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_dateDebut')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 152, 1)
    _Documentation = None
T_dateDebut._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_dateDebut', T_dateDebut)
_module_typeBindings.T_dateDebut = T_dateDebut

# Atomic simple type: {odyssee/cocagne/Gui5C}T_dateFin
class T_dateFin (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_dateFin')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 156, 1)
    _Documentation = None
T_dateFin._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_dateFin', T_dateFin)
_module_typeBindings.T_dateFin = T_dateFin

# Atomic simple type: {odyssee/cocagne/Gui5C}T_CMakeBuildType_1
class T_CMakeBuildType_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_CMakeBuildType_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 160, 1)
    _Documentation = None
T_CMakeBuildType_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_CMakeBuildType_1', T_CMakeBuildType_1)
_module_typeBindings.T_CMakeBuildType_1 = T_CMakeBuildType_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_execution_1
class T_execution_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_execution_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 164, 1)
    _Documentation = None
T_execution_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_execution_1', T_execution_1)
_module_typeBindings.T_execution_1 = T_execution_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_OS_1
class T_OS_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_OS_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 168, 1)
    _Documentation = None
T_OS_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_OS_1', T_OS_1)
_module_typeBindings.T_OS_1 = T_OS_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_procs_1
class T_procs_1 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_procs_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 172, 1)
    _Documentation = None
T_procs_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_procs_1', T_procs_1)
_module_typeBindings.T_procs_1 = T_procs_1

# Atomic simple type: {odyssee/cocagne/Gui5C}T_host_1
class T_host_1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_host_1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 176, 1)
    _Documentation = None
T_host_1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_host_1', T_host_1)
_module_typeBindings.T_host_1 = T_host_1

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 201, 5)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {odyssee/cocagne/Gui5C}T_sha1Id
class T_sha1Id (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1Id')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 214, 1)
    _Documentation = None
T_sha1Id._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1Id', T_sha1Id)
_module_typeBindings.T_sha1Id = T_sha1Id

# Atomic simple type: {odyssee/cocagne/Gui5C}T_cpuTotalTime
class T_cpuTotalTime (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTotalTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 218, 1)
    _Documentation = None
T_cpuTotalTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_cpuTotalTime', T_cpuTotalTime)
_module_typeBindings.T_cpuTotalTime = T_cpuTotalTime

# Atomic simple type: {odyssee/cocagne/Gui5C}PNEFdico
class PNEFdico (pyxb.binding.datatypes.string):

    """{'T_sha1': {'_sha1_MyJobPerformance': 'T_sha1', '_sha1_Selection': 'T_sha1_1'}, 'T_testName': {'_testName_MyJobPerformance': 'T_testName', '_testName_Selection': 'T_testName_1'}, 'T_date': {'_date_MyJobPerformance': 'T_date', '_date_Selection': 'T_date_1'}, 'T_CMakeBuildType': {'_CMakeBuildType_MyJobPerformance': 'T_CMakeBuildType', '_CMakeBuildType_Selection': 'T_CMakeBuildType_1'}, 'T_execution': {'_execution_MyJobPerformance': 'T_execution', '_execution_Selection': 'T_execution_1'}, 'T_procs': {'_procs_MyJobPerformance': 'T_procs', '_procs_Selection': 'T_procs_1'}, 'T_host': {'_host_MyJobPerformance': 'T_host', '_host_Selection': 'T_host_1'}, 'T_OS': {'_OS_MyJobPerformance': 'T_OS', '_OS_Selection': 'T_OS_1'}}
		"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PNEFdico')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 246, 1)
    _Documentation = "{'T_sha1': {'_sha1_MyJobPerformance': 'T_sha1', '_sha1_Selection': 'T_sha1_1'}, 'T_testName': {'_testName_MyJobPerformance': 'T_testName', '_testName_Selection': 'T_testName_1'}, 'T_date': {'_date_MyJobPerformance': 'T_date', '_date_Selection': 'T_date_1'}, 'T_CMakeBuildType': {'_CMakeBuildType_MyJobPerformance': 'T_CMakeBuildType', '_CMakeBuildType_Selection': 'T_CMakeBuildType_1'}, 'T_execution': {'_execution_MyJobPerformance': 'T_execution', '_execution_Selection': 'T_execution_1'}, 'T_procs': {'_procs_MyJobPerformance': 'T_procs', '_procs_Selection': 'T_procs_1'}, 'T_host': {'_host_MyJobPerformance': 'T_host', '_host_Selection': 'T_host_1'}, 'T_OS': {'_OS_MyJobPerformance': 'T_OS', '_OS_Selection': 'T_OS_1'}}\n\t\t"
PNEFdico._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PNEFdico', PNEFdico)
_module_typeBindings.PNEFdico = PNEFdico

# List simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_ (pyxb.binding.basis.STD_list):

    """Simple type that is a list of STD_ANON."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 199, 3)
    _Documentation = None

    _ItemType = STD_ANON
STD_ANON_._InitializeFacetMap()
_module_typeBindings.STD_ANON_ = STD_ANON_

# List simple type: {odyssee/cocagne/Gui5C}T_labels
# superclasses STD_ANON_
class T_labels (pyxb.binding.basis.STD_list):

    """Simple type that is a list of STD_ANON."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_labels')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 197, 1)
    _Documentation = None

    _ItemType = STD_ANON
T_labels._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_labels', T_labels)
_module_typeBindings.T_labels = T_labels

# Complex type {odyssee/cocagne/Gui5C}T_functionsJobStatistics with content type ELEMENT_ONLY
class T_functionsJobStatistics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_functionsJobStatistics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_functionsJobStatistics')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 101, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5Clabel', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 103, 3), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}cpuTime uses Python identifier cpuTime
    __cpuTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), 'cpuTime', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5CcpuTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 104, 3), )

    
    cpuTime = property(__cpuTime.value, __cpuTime.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}fractionOfTotalTime uses Python identifier fractionOfTotalTime
    __fractionOfTotalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), 'fractionOfTotalTime', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5CfractionOfTotalTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 105, 3), )

    
    fractionOfTotalTime = property(__fractionOfTotalTime.value, __fractionOfTotalTime.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}calls uses Python identifier calls
    __calls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'calls'), 'calls', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5Ccalls', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 106, 3), )

    
    calls = property(__calls.value, __calls.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}depth uses Python identifier depth
    __depth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'depth'), 'depth', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5Cdepth', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 107, 3), )

    
    depth = property(__depth.value, __depth.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}fractionOfCallerTime uses Python identifier fractionOfCallerTime
    __fractionOfCallerTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionOfCallerTime'), 'fractionOfCallerTime', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5CfractionOfCallerTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 108, 3), )

    
    fractionOfCallerTime = property(__fractionOfCallerTime.value, __fractionOfCallerTime.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}functionsJobStatistics uses Python identifier functionsJobStatistics
    __functionsJobStatistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), 'functionsJobStatistics', '__odysseecocagneGui5C_T_functionsJobStatistics_odysseecocagneGui5CfunctionsJobStatistics', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 109, 3), )

    
    functionsJobStatistics = property(__functionsJobStatistics.value, __functionsJobStatistics.set, None, None)

    _ElementMap.update({
        __label.name() : __label,
        __cpuTime.name() : __cpuTime,
        __fractionOfTotalTime.name() : __fractionOfTotalTime,
        __calls.name() : __calls,
        __depth.name() : __depth,
        __fractionOfCallerTime.name() : __fractionOfCallerTime,
        __functionsJobStatistics.name() : __functionsJobStatistics
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_functionsJobStatistics = T_functionsJobStatistics
Namespace.addCategoryObject('typeBinding', 'T_functionsJobStatistics', T_functionsJobStatistics)


# Complex type {odyssee/cocagne/Gui5C}T_JobStatistics with content type ELEMENT_ONLY
class T_JobStatistics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_JobStatistics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_JobStatistics')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 112, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}totalCpuTime uses Python identifier totalCpuTime
    __totalCpuTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalCpuTime'), 'totalCpuTime', '__odysseecocagneGui5C_T_JobStatistics_odysseecocagneGui5CtotalCpuTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 114, 3), )

    
    totalCpuTime = property(__totalCpuTime.value, __totalCpuTime.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}functionsJobStatistics uses Python identifier functionsJobStatistics
    __functionsJobStatistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), 'functionsJobStatistics', '__odysseecocagneGui5C_T_JobStatistics_odysseecocagneGui5CfunctionsJobStatistics', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 115, 3), )

    
    functionsJobStatistics = property(__functionsJobStatistics.value, __functionsJobStatistics.set, None, None)

    _ElementMap.update({
        __totalCpuTime.name() : __totalCpuTime,
        __functionsJobStatistics.name() : __functionsJobStatistics
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_JobStatistics = T_JobStatistics
Namespace.addCategoryObject('typeBinding', 'T_JobStatistics', T_JobStatistics)


# Complex type {odyssee/cocagne/Gui5C}T_MyJobPerformance with content type ELEMENT_ONLY
class T_MyJobPerformance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_MyJobPerformance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_MyJobPerformance')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 118, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}sha1 uses Python identifier sha1
    __sha1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1'), 'sha1', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5Csha1', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 120, 3), )

    
    sha1 = property(__sha1.value, __sha1.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}testName uses Python identifier testName
    __testName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'testName'), 'testName', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5CtestName', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 121, 3), )

    
    testName = property(__testName.value, __testName.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5Cversion', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 122, 3), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5Cdate', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 123, 3), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}CMakeBuildType uses Python identifier CMakeBuildType
    __CMakeBuildType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType'), 'CMakeBuildType', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5CCMakeBuildType', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 124, 3), )

    
    CMakeBuildType = property(__CMakeBuildType.value, __CMakeBuildType.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}execution uses Python identifier execution
    __execution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'execution'), 'execution', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5Cexecution', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 125, 3), )

    
    execution = property(__execution.value, __execution.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}procs uses Python identifier procs
    __procs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procs'), 'procs', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5Cprocs', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 126, 3), )

    
    procs = property(__procs.value, __procs.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}host uses Python identifier host
    __host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'host'), 'host', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5Chost', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 127, 3), )

    
    host = property(__host.value, __host.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}OS uses Python identifier OS
    __OS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OS'), 'OS', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5COS', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 128, 3), )

    
    OS = property(__OS.value, __OS.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}JobStatistics uses Python identifier JobStatistics
    __JobStatistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JobStatistics'), 'JobStatistics', '__odysseecocagneGui5C_T_MyJobPerformance_odysseecocagneGui5CJobStatistics', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 129, 3), )

    
    JobStatistics = property(__JobStatistics.value, __JobStatistics.set, None, None)

    _ElementMap.update({
        __sha1.name() : __sha1,
        __testName.name() : __testName,
        __version.name() : __version,
        __date.name() : __date,
        __CMakeBuildType.name() : __CMakeBuildType,
        __execution.name() : __execution,
        __procs.name() : __procs,
        __host.name() : __host,
        __OS.name() : __OS,
        __JobStatistics.name() : __JobStatistics
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_MyJobPerformance = T_MyJobPerformance
Namespace.addCategoryObject('typeBinding', 'T_MyJobPerformance', T_MyJobPerformance)


# Complex type {odyssee/cocagne/Gui5C}T_Selection with content type ELEMENT_ONLY
class T_Selection (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_Selection with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_Selection')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 180, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}testName uses Python identifier testName
    __testName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'testName'), 'testName', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5CtestName', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 182, 3), )

    
    testName = property(__testName.value, __testName.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}sha1 uses Python identifier sha1
    __sha1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1'), 'sha1', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Csha1', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 183, 3), )

    
    sha1 = property(__sha1.value, __sha1.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}sha1Debut uses Python identifier sha1Debut
    __sha1Debut = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1Debut'), 'sha1Debut', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Csha1Debut', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 184, 3), )

    
    sha1Debut = property(__sha1Debut.value, __sha1Debut.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}sha1Fin uses Python identifier sha1Fin
    __sha1Fin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1Fin'), 'sha1Fin', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Csha1Fin', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 185, 3), )

    
    sha1Fin = property(__sha1Fin.value, __sha1Fin.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Cdate', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 186, 3), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}dateDebut uses Python identifier dateDebut
    __dateDebut = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateDebut'), 'dateDebut', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5CdateDebut', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 187, 3), )

    
    dateDebut = property(__dateDebut.value, __dateDebut.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}dateFin uses Python identifier dateFin
    __dateFin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateFin'), 'dateFin', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5CdateFin', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 188, 3), )

    
    dateFin = property(__dateFin.value, __dateFin.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Cversion', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 189, 3), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}CMakeBuildType uses Python identifier CMakeBuildType
    __CMakeBuildType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType'), 'CMakeBuildType', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5CCMakeBuildType', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 190, 3), )

    
    CMakeBuildType = property(__CMakeBuildType.value, __CMakeBuildType.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}execution uses Python identifier execution
    __execution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'execution'), 'execution', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Cexecution', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 191, 3), )

    
    execution = property(__execution.value, __execution.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}OS uses Python identifier OS
    __OS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OS'), 'OS', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5COS', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 192, 3), )

    
    OS = property(__OS.value, __OS.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}procs uses Python identifier procs
    __procs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procs'), 'procs', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Cprocs', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 193, 3), )

    
    procs = property(__procs.value, __procs.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}host uses Python identifier host
    __host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'host'), 'host', '__odysseecocagneGui5C_T_Selection_odysseecocagneGui5Chost', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 194, 3), )

    
    host = property(__host.value, __host.set, None, None)

    _ElementMap.update({
        __testName.name() : __testName,
        __sha1.name() : __sha1,
        __sha1Debut.name() : __sha1Debut,
        __sha1Fin.name() : __sha1Fin,
        __date.name() : __date,
        __dateDebut.name() : __dateDebut,
        __dateFin.name() : __dateFin,
        __version.name() : __version,
        __CMakeBuildType.name() : __CMakeBuildType,
        __execution.name() : __execution,
        __OS.name() : __OS,
        __procs.name() : __procs,
        __host.name() : __host
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_Selection = T_Selection
Namespace.addCategoryObject('typeBinding', 'T_Selection', T_Selection)


# Complex type {odyssee/cocagne/Gui5C}T_PresentationLabels with content type ELEMENT_ONLY
class T_PresentationLabels (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_PresentationLabels with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_PresentationLabels')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 209, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}labels uses Python identifier labels
    __labels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'labels'), 'labels', '__odysseecocagneGui5C_T_PresentationLabels_odysseecocagneGui5Clabels', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 211, 3), )

    
    labels = property(__labels.value, __labels.set, None, None)

    _ElementMap.update({
        __labels.name() : __labels
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_PresentationLabels = T_PresentationLabels
Namespace.addCategoryObject('typeBinding', 'T_PresentationLabels', T_PresentationLabels)


# Complex type {odyssee/cocagne/Gui5C}T_fonction with content type ELEMENT_ONLY
class T_fonction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_fonction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fonction')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 222, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__odysseecocagneGui5C_T_fonction_odysseecocagneGui5Clabel', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 224, 3), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}cpuTime uses Python identifier cpuTime
    __cpuTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), 'cpuTime', '__odysseecocagneGui5C_T_fonction_odysseecocagneGui5CcpuTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 225, 3), )

    
    cpuTime = property(__cpuTime.value, __cpuTime.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}calls uses Python identifier calls
    __calls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'calls'), 'calls', '__odysseecocagneGui5C_T_fonction_odysseecocagneGui5Ccalls', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 226, 3), )

    
    calls = property(__calls.value, __calls.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}fractionOfTotalTime uses Python identifier fractionOfTotalTime
    __fractionOfTotalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), 'fractionOfTotalTime', '__odysseecocagneGui5C_T_fonction_odysseecocagneGui5CfractionOfTotalTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 227, 3), )

    
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


# Complex type {odyssee/cocagne/Gui5C}T_MyProfileResultat with content type ELEMENT_ONLY
class T_MyProfileResultat (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_MyProfileResultat with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_MyProfileResultat')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 230, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}sha1Id uses Python identifier sha1Id
    __sha1Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1Id'), 'sha1Id', '__odysseecocagneGui5C_T_MyProfileResultat_odysseecocagneGui5Csha1Id', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 232, 3), )

    
    sha1Id = property(__sha1Id.value, __sha1Id.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}cpuTotalTime uses Python identifier cpuTotalTime
    __cpuTotalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuTotalTime'), 'cpuTotalTime', '__odysseecocagneGui5C_T_MyProfileResultat_odysseecocagneGui5CcpuTotalTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 233, 3), )

    
    cpuTotalTime = property(__cpuTotalTime.value, __cpuTotalTime.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}fonction uses Python identifier fonction
    __fonction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fonction'), 'fonction', '__odysseecocagneGui5C_T_MyProfileResultat_odysseecocagneGui5Cfonction', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 234, 3), )

    
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


# Complex type {odyssee/cocagne/Gui5C}T_Gui5C with content type ELEMENT_ONLY
class T_Gui5C (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_Gui5C with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_Gui5C')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 238, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/Gui5C}MyJobPerformance uses Python identifier MyJobPerformance
    __MyJobPerformance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MyJobPerformance'), 'MyJobPerformance', '__odysseecocagneGui5C_T_Gui5C_odysseecocagneGui5CMyJobPerformance', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 240, 3), )

    
    MyJobPerformance = property(__MyJobPerformance.value, __MyJobPerformance.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}Selection uses Python identifier Selection
    __Selection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Selection'), 'Selection', '__odysseecocagneGui5C_T_Gui5C_odysseecocagneGui5CSelection', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 241, 3), )

    
    Selection = property(__Selection.value, __Selection.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}PresentationLabels uses Python identifier PresentationLabels
    __PresentationLabels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PresentationLabels'), 'PresentationLabels', '__odysseecocagneGui5C_T_Gui5C_odysseecocagneGui5CPresentationLabels', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 242, 3), )

    
    PresentationLabels = property(__PresentationLabels.value, __PresentationLabels.set, None, None)

    
    # Element {odyssee/cocagne/Gui5C}MyProfileResultat uses Python identifier MyProfileResultat
    __MyProfileResultat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MyProfileResultat'), 'MyProfileResultat', '__odysseecocagneGui5C_T_Gui5C_odysseecocagneGui5CMyProfileResultat', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 243, 3), )

    
    MyProfileResultat = property(__MyProfileResultat.value, __MyProfileResultat.set, None, None)

    _ElementMap.update({
        __MyJobPerformance.name() : __MyJobPerformance,
        __Selection.name() : __Selection,
        __PresentationLabels.name() : __PresentationLabels,
        __MyProfileResultat.name() : __MyProfileResultat
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_Gui5C = T_Gui5C
Namespace.addCategoryObject('typeBinding', 'T_Gui5C', T_Gui5C)


# Complex type {odyssee/cocagne/Gui5C}T_totalCpuTime with content type SIMPLE
class T_totalCpuTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_totalCpuTime with content type SIMPLE"""
    _TypeDefinition = T_totalCpuTime_NoUnit
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_totalCpuTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 56, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is T_totalCpuTime_NoUnit
    
    # Attribute unite_T_totalCpuTime uses Python identifier unite_T_totalCpuTime
    __unite_T_totalCpuTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unite_T_totalCpuTime'), 'unite_T_totalCpuTime', '__odysseecocagneGui5C_T_totalCpuTime_unite_T_totalCpuTime', pyxb.binding.datatypes.string, fixed=True, unicode_default='seconds')
    __unite_T_totalCpuTime._DeclarationLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 59, 3)
    __unite_T_totalCpuTime._UseLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 59, 3)
    
    unite_T_totalCpuTime = property(__unite_T_totalCpuTime.value, __unite_T_totalCpuTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unite_T_totalCpuTime.name() : __unite_T_totalCpuTime
    })
_module_typeBindings.T_totalCpuTime = T_totalCpuTime
Namespace.addCategoryObject('typeBinding', 'T_totalCpuTime', T_totalCpuTime)


# Complex type {odyssee/cocagne/Gui5C}T_cpuTime with content type SIMPLE
class T_cpuTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_cpuTime with content type SIMPLE"""
    _TypeDefinition = T_cpuTime_NoUnit
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 71, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is T_cpuTime_NoUnit
    
    # Attribute unite_T_cpuTime uses Python identifier unite_T_cpuTime
    __unite_T_cpuTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unite_T_cpuTime'), 'unite_T_cpuTime', '__odysseecocagneGui5C_T_cpuTime_unite_T_cpuTime', pyxb.binding.datatypes.string, fixed=True, unicode_default='seconds')
    __unite_T_cpuTime._DeclarationLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 74, 3)
    __unite_T_cpuTime._UseLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 74, 3)
    
    unite_T_cpuTime = property(__unite_T_cpuTime.value, __unite_T_cpuTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unite_T_cpuTime.name() : __unite_T_cpuTime
    })
_module_typeBindings.T_cpuTime = T_cpuTime
Namespace.addCategoryObject('typeBinding', 'T_cpuTime', T_cpuTime)


# Complex type {odyssee/cocagne/Gui5C}T_fractionOfCallerTime with content type SIMPLE
class T_fractionOfCallerTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/Gui5C}T_fractionOfCallerTime with content type SIMPLE"""
    _TypeDefinition = T_fractionOfCallerTime_NoUnit
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfCallerTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 94, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is T_fractionOfCallerTime_NoUnit
    
    # Attribute unite_T_fractionOfCallerTime uses Python identifier unite_T_fractionOfCallerTime
    __unite_T_fractionOfCallerTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unite_T_fractionOfCallerTime'), 'unite_T_fractionOfCallerTime', '__odysseecocagneGui5C_T_fractionOfCallerTime_unite_T_fractionOfCallerTime', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __unite_T_fractionOfCallerTime._DeclarationLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 97, 3)
    __unite_T_fractionOfCallerTime._UseLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 97, 3)
    
    unite_T_fractionOfCallerTime = property(__unite_T_fractionOfCallerTime.value, __unite_T_fractionOfCallerTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unite_T_fractionOfCallerTime.name() : __unite_T_fractionOfCallerTime
    })
_module_typeBindings.T_fractionOfCallerTime = T_fractionOfCallerTime
Namespace.addCategoryObject('typeBinding', 'T_fractionOfCallerTime', T_fractionOfCallerTime)


Gui5C = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Gui5C'), T_Gui5C, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 237, 1))
Namespace.addCategoryObject('elementBinding', Gui5C.name().localName(), Gui5C)



T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), T_label, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 103, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), T_cpuTime, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 104, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), T_fractionOfTotalTime, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 105, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calls'), T_calls, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 106, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'depth'), T_depth, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 107, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionOfCallerTime'), T_fractionOfCallerTime, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 108, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), T_functionsJobStatistics, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 109, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 109, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 103, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 104, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 105, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'calls')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 106, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'depth')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 107, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionOfCallerTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 108, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 109, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_functionsJobStatistics._Automaton = _BuildAutomaton()




T_JobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalCpuTime'), T_totalCpuTime, scope=T_JobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 114, 3)))

T_JobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), T_functionsJobStatistics, scope=T_JobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 115, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 115, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_JobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalCpuTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 114, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(T_JobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 115, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_JobStatistics._Automaton = _BuildAutomaton_()




T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1'), T_sha1, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 120, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'testName'), T_testName, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 121, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), T_version, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 122, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), T_date, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 123, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType'), T_CMakeBuildType, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 124, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'execution'), T_execution, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 125, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procs'), T_procs, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 126, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'host'), T_host, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 127, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OS'), T_OS, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 128, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JobStatistics'), T_JobStatistics, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 129, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 120, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'testName')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 121, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 122, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 123, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 124, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'execution')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 125, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procs')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 126, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'host')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 127, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OS')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 128, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JobStatistics')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 129, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_MyJobPerformance._Automaton = _BuildAutomaton_2()




T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'testName'), T_testName_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 182, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1'), T_sha1_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 183, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1Debut'), T_sha1Debut, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 184, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1Fin'), T_sha1Fin, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 185, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), T_date_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 186, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateDebut'), T_dateDebut, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 187, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateFin'), T_dateFin, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 188, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), T_version, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 189, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType'), T_CMakeBuildType_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 190, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'execution'), T_execution_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 191, 3), unicode_default='seq'))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OS'), T_OS_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 192, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procs'), T_procs_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 193, 3)))

T_Selection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'host'), T_host_1, scope=T_Selection, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 194, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'testName')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 182, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 183, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1Debut')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 184, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1Fin')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 185, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 186, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateDebut')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 187, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateFin')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 188, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 189, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 190, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'execution')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 191, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OS')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 192, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procs')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 193, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_Selection._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'host')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 194, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_Selection._Automaton = _BuildAutomaton_3()




T_PresentationLabels._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'labels'), T_labels, scope=T_PresentationLabels, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 211, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_PresentationLabels._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'labels')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 211, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
T_PresentationLabels._Automaton = _BuildAutomaton_4()




T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), T_label, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 224, 3)))

T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), T_cpuTime, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 225, 3)))

T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calls'), T_calls, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 226, 3)))

T_fonction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), T_fractionOfTotalTime, scope=T_fonction, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 227, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 224, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 225, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'calls')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 226, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_fonction._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 227, 3))
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
T_fonction._Automaton = _BuildAutomaton_5()




T_MyProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1Id'), T_sha1Id, scope=T_MyProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 232, 3)))

T_MyProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuTotalTime'), T_cpuTotalTime, scope=T_MyProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 233, 3)))

T_MyProfileResultat._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fonction'), T_fonction, scope=T_MyProfileResultat, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 234, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 234, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1Id')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 232, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_MyProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuTotalTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 233, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(T_MyProfileResultat._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fonction')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 234, 3))
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
T_MyProfileResultat._Automaton = _BuildAutomaton_6()




T_Gui5C._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MyJobPerformance'), T_MyJobPerformance, scope=T_Gui5C, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 240, 3)))

T_Gui5C._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Selection'), T_Selection, scope=T_Gui5C, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 241, 3)))

T_Gui5C._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PresentationLabels'), T_PresentationLabels, scope=T_Gui5C, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 242, 3)))

T_Gui5C._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MyProfileResultat'), T_MyProfileResultat, scope=T_Gui5C, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 243, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 239, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 240, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 241, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 242, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 243, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(T_Gui5C._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MyJobPerformance')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 240, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(T_Gui5C._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Selection')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 241, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(T_Gui5C._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PresentationLabels')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 242, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(T_Gui5C._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MyProfileResultat')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cata5CChapeau.xsd', 243, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
T_Gui5C._Automaton = _BuildAutomaton_7()


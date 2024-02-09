# ./raw/cataJobPerformance_driver.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f58fef81497c9138a771b0132ab752f5501fe9bf
# Generated 2023-11-14 10:03:35.475441 by PyXB version 1.2.7.dev1 using Python 3.9.2.final.0
# Namespace odyssee/cocagne/JobPerformance

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4917fc0a-0899-4caa-b59b-cc5e39778dfe')

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
Namespace = pyxb.namespace.NamespaceForURI('odyssee/cocagne/JobPerformance', create_if_missing=True)
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


# Atomic simple type: {odyssee/cocagne/JobPerformance}AccasAssd
class AccasAssd (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AccasAssd')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 7, 1)
    _Documentation = None
AccasAssd._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AccasAssd', AccasAssd)
_module_typeBindings.AccasAssd = AccasAssd

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_sha1
class T_sha1 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_sha1')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 11, 1)
    _Documentation = None
T_sha1._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_sha1', T_sha1)
_module_typeBindings.T_sha1 = T_sha1

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_testName
class T_testName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_testName')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 15, 1)
    _Documentation = None
T_testName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_testName', T_testName)
_module_typeBindings.T_testName = T_testName

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_version
class T_version (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_version')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 19, 1)
    _Documentation = None
T_version._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_version', T_version)
_module_typeBindings.T_version = T_version

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_date
class T_date (pyxb.binding.datatypes.date):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_date')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 23, 1)
    _Documentation = None
T_date._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_date', T_date)
_module_typeBindings.T_date = T_date

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_CMakeBuildType
class T_CMakeBuildType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_CMakeBuildType')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 27, 1)
    _Documentation = None
T_CMakeBuildType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=T_CMakeBuildType)
T_CMakeBuildType.Release = T_CMakeBuildType._CF_enumeration.addEnumeration(unicode_value='Release', tag='Release')
T_CMakeBuildType.Debug = T_CMakeBuildType._CF_enumeration.addEnumeration(unicode_value='Debug', tag='Debug')
T_CMakeBuildType.RelWithDebInfo = T_CMakeBuildType._CF_enumeration.addEnumeration(unicode_value='RelWithDebInfo', tag='RelWithDebInfo')
T_CMakeBuildType._InitializeFacetMap(T_CMakeBuildType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'T_CMakeBuildType', T_CMakeBuildType)
_module_typeBindings.T_CMakeBuildType = T_CMakeBuildType

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_execution
class T_execution (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_execution')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 34, 1)
    _Documentation = None
T_execution._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=T_execution)
T_execution.par = T_execution._CF_enumeration.addEnumeration(unicode_value='par', tag='par')
T_execution.seq = T_execution._CF_enumeration.addEnumeration(unicode_value='seq', tag='seq')
T_execution._InitializeFacetMap(T_execution._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'T_execution', T_execution)
_module_typeBindings.T_execution = T_execution

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_procs
class T_procs (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_procs')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 40, 1)
    _Documentation = None
T_procs._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_procs', T_procs)
_module_typeBindings.T_procs = T_procs

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_host
class T_host (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_host')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 44, 1)
    _Documentation = None
T_host._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_host', T_host)
_module_typeBindings.T_host = T_host

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_OS
class T_OS (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_OS')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 48, 1)
    _Documentation = None
T_OS._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_OS', T_OS)
_module_typeBindings.T_OS = T_OS

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_totalCpuTime_NoUnit
class T_totalCpuTime_NoUnit (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_totalCpuTime_NoUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 52, 1)
    _Documentation = None
T_totalCpuTime_NoUnit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_totalCpuTime_NoUnit', T_totalCpuTime_NoUnit)
_module_typeBindings.T_totalCpuTime_NoUnit = T_totalCpuTime_NoUnit

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_label
class T_label (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_label')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 63, 1)
    _Documentation = None
T_label._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_label', T_label)
_module_typeBindings.T_label = T_label

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_cpuTime_NoUnit
class T_cpuTime_NoUnit (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTime_NoUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 67, 1)
    _Documentation = None
T_cpuTime_NoUnit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_cpuTime_NoUnit', T_cpuTime_NoUnit)
_module_typeBindings.T_cpuTime_NoUnit = T_cpuTime_NoUnit

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_fractionOfTotalTime
class T_fractionOfTotalTime (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfTotalTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 78, 1)
    _Documentation = None
T_fractionOfTotalTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_fractionOfTotalTime', T_fractionOfTotalTime)
_module_typeBindings.T_fractionOfTotalTime = T_fractionOfTotalTime

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_calls
class T_calls (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_calls')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 82, 1)
    _Documentation = None
T_calls._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_calls', T_calls)
_module_typeBindings.T_calls = T_calls

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_depth
class T_depth (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_depth')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 86, 1)
    _Documentation = None
T_depth._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_depth', T_depth)
_module_typeBindings.T_depth = T_depth

# Atomic simple type: {odyssee/cocagne/JobPerformance}T_fractionOfCallerTime_NoUnit
class T_fractionOfCallerTime_NoUnit (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfCallerTime_NoUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 90, 1)
    _Documentation = None
T_fractionOfCallerTime_NoUnit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'T_fractionOfCallerTime_NoUnit', T_fractionOfCallerTime_NoUnit)
_module_typeBindings.T_fractionOfCallerTime_NoUnit = T_fractionOfCallerTime_NoUnit

# Complex type {odyssee/cocagne/JobPerformance}T_functionsJobStatistics with content type ELEMENT_ONLY
class T_functionsJobStatistics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_functionsJobStatistics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_functionsJobStatistics')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 101, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/JobPerformance}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'label'), 'label', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancelabel', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 103, 3), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}cpuTime uses Python identifier cpuTime
    __cpuTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), 'cpuTime', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancecpuTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 104, 3), )

    
    cpuTime = property(__cpuTime.value, __cpuTime.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}fractionOfTotalTime uses Python identifier fractionOfTotalTime
    __fractionOfTotalTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), 'fractionOfTotalTime', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancefractionOfTotalTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 105, 3), )

    
    fractionOfTotalTime = property(__fractionOfTotalTime.value, __fractionOfTotalTime.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}calls uses Python identifier calls
    __calls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'calls'), 'calls', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancecalls', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 106, 3), )

    
    calls = property(__calls.value, __calls.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}depth uses Python identifier depth
    __depth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'depth'), 'depth', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancedepth', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 107, 3), )

    
    depth = property(__depth.value, __depth.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}fractionOfCallerTime uses Python identifier fractionOfCallerTime
    __fractionOfCallerTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fractionOfCallerTime'), 'fractionOfCallerTime', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancefractionOfCallerTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 108, 3), )

    
    fractionOfCallerTime = property(__fractionOfCallerTime.value, __fractionOfCallerTime.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}functionsJobStatistics uses Python identifier functionsJobStatistics
    __functionsJobStatistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), 'functionsJobStatistics', '__odysseecocagneJobPerformance_T_functionsJobStatistics_odysseecocagneJobPerformancefunctionsJobStatistics', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 109, 3), )

    
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


# Complex type {odyssee/cocagne/JobPerformance}T_JobStatistics with content type ELEMENT_ONLY
class T_JobStatistics (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_JobStatistics with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_JobStatistics')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 112, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/JobPerformance}totalCpuTime uses Python identifier totalCpuTime
    __totalCpuTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totalCpuTime'), 'totalCpuTime', '__odysseecocagneJobPerformance_T_JobStatistics_odysseecocagneJobPerformancetotalCpuTime', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 114, 3), )

    
    totalCpuTime = property(__totalCpuTime.value, __totalCpuTime.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}functionsJobStatistics uses Python identifier functionsJobStatistics
    __functionsJobStatistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), 'functionsJobStatistics', '__odysseecocagneJobPerformance_T_JobStatistics_odysseecocagneJobPerformancefunctionsJobStatistics', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 115, 3), )

    
    functionsJobStatistics = property(__functionsJobStatistics.value, __functionsJobStatistics.set, None, None)

    _ElementMap.update({
        __totalCpuTime.name() : __totalCpuTime,
        __functionsJobStatistics.name() : __functionsJobStatistics
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_JobStatistics = T_JobStatistics
Namespace.addCategoryObject('typeBinding', 'T_JobStatistics', T_JobStatistics)


# Complex type {odyssee/cocagne/JobPerformance}T_MyJobPerformance with content type ELEMENT_ONLY
class T_MyJobPerformance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_MyJobPerformance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_MyJobPerformance')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 118, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/JobPerformance}sha1 uses Python identifier sha1
    __sha1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sha1'), 'sha1', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformancesha1', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 120, 3), )

    
    sha1 = property(__sha1.value, __sha1.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}testName uses Python identifier testName
    __testName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'testName'), 'testName', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformancetestName', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 121, 3), )

    
    testName = property(__testName.value, __testName.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'version'), 'version', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformanceversion', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 122, 3), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'date'), 'date', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformancedate', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 123, 3), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}CMakeBuildType uses Python identifier CMakeBuildType
    __CMakeBuildType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType'), 'CMakeBuildType', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformanceCMakeBuildType', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 124, 3), )

    
    CMakeBuildType = property(__CMakeBuildType.value, __CMakeBuildType.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}execution uses Python identifier execution
    __execution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'execution'), 'execution', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformanceexecution', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 125, 3), )

    
    execution = property(__execution.value, __execution.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}procs uses Python identifier procs
    __procs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procs'), 'procs', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformanceprocs', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 126, 3), )

    
    procs = property(__procs.value, __procs.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}host uses Python identifier host
    __host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'host'), 'host', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformancehost', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 127, 3), )

    
    host = property(__host.value, __host.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}OS uses Python identifier OS
    __OS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OS'), 'OS', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformanceOS', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 128, 3), )

    
    OS = property(__OS.value, __OS.set, None, None)

    
    # Element {odyssee/cocagne/JobPerformance}JobStatistics uses Python identifier JobStatistics
    __JobStatistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'JobStatistics'), 'JobStatistics', '__odysseecocagneJobPerformance_T_MyJobPerformance_odysseecocagneJobPerformanceJobStatistics', False, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 129, 3), )

    
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


# Complex type {odyssee/cocagne/JobPerformance}T_JobPerformance with content type ELEMENT_ONLY
class T_JobPerformance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_JobPerformance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_JobPerformance')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 133, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {odyssee/cocagne/JobPerformance}MyJobPerformance uses Python identifier MyJobPerformance
    __MyJobPerformance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MyJobPerformance'), 'MyJobPerformance', '__odysseecocagneJobPerformance_T_JobPerformance_odysseecocagneJobPerformanceMyJobPerformance', True, pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 135, 3), )

    
    MyJobPerformance = property(__MyJobPerformance.value, __MyJobPerformance.set, None, None)

    _ElementMap.update({
        __MyJobPerformance.name() : __MyJobPerformance
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.T_JobPerformance = T_JobPerformance
Namespace.addCategoryObject('typeBinding', 'T_JobPerformance', T_JobPerformance)


# Complex type {odyssee/cocagne/JobPerformance}T_totalCpuTime with content type SIMPLE
class T_totalCpuTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_totalCpuTime with content type SIMPLE"""
    _TypeDefinition = T_totalCpuTime_NoUnit
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_totalCpuTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 56, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is T_totalCpuTime_NoUnit
    
    # Attribute unite_T_totalCpuTime uses Python identifier unite_T_totalCpuTime
    __unite_T_totalCpuTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unite_T_totalCpuTime'), 'unite_T_totalCpuTime', '__odysseecocagneJobPerformance_T_totalCpuTime_unite_T_totalCpuTime', pyxb.binding.datatypes.string, fixed=True, unicode_default='seconds')
    __unite_T_totalCpuTime._DeclarationLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 59, 3)
    __unite_T_totalCpuTime._UseLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 59, 3)
    
    unite_T_totalCpuTime = property(__unite_T_totalCpuTime.value, __unite_T_totalCpuTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unite_T_totalCpuTime.name() : __unite_T_totalCpuTime
    })
_module_typeBindings.T_totalCpuTime = T_totalCpuTime
Namespace.addCategoryObject('typeBinding', 'T_totalCpuTime', T_totalCpuTime)


# Complex type {odyssee/cocagne/JobPerformance}T_cpuTime with content type SIMPLE
class T_cpuTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_cpuTime with content type SIMPLE"""
    _TypeDefinition = T_cpuTime_NoUnit
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_cpuTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 71, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is T_cpuTime_NoUnit
    
    # Attribute unite_T_cpuTime uses Python identifier unite_T_cpuTime
    __unite_T_cpuTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unite_T_cpuTime'), 'unite_T_cpuTime', '__odysseecocagneJobPerformance_T_cpuTime_unite_T_cpuTime', pyxb.binding.datatypes.string, fixed=True, unicode_default='seconds')
    __unite_T_cpuTime._DeclarationLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 74, 3)
    __unite_T_cpuTime._UseLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 74, 3)
    
    unite_T_cpuTime = property(__unite_T_cpuTime.value, __unite_T_cpuTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unite_T_cpuTime.name() : __unite_T_cpuTime
    })
_module_typeBindings.T_cpuTime = T_cpuTime
Namespace.addCategoryObject('typeBinding', 'T_cpuTime', T_cpuTime)


# Complex type {odyssee/cocagne/JobPerformance}T_fractionOfCallerTime with content type SIMPLE
class T_fractionOfCallerTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {odyssee/cocagne/JobPerformance}T_fractionOfCallerTime with content type SIMPLE"""
    _TypeDefinition = T_fractionOfCallerTime_NoUnit
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'T_fractionOfCallerTime')
    _XSDLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 94, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is T_fractionOfCallerTime_NoUnit
    
    # Attribute unite_T_fractionOfCallerTime uses Python identifier unite_T_fractionOfCallerTime
    __unite_T_fractionOfCallerTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'unite_T_fractionOfCallerTime'), 'unite_T_fractionOfCallerTime', '__odysseecocagneJobPerformance_T_fractionOfCallerTime_unite_T_fractionOfCallerTime', pyxb.binding.datatypes.string, fixed=True, unicode_default='percent')
    __unite_T_fractionOfCallerTime._DeclarationLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 97, 3)
    __unite_T_fractionOfCallerTime._UseLocation = pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 97, 3)
    
    unite_T_fractionOfCallerTime = property(__unite_T_fractionOfCallerTime.value, __unite_T_fractionOfCallerTime.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __unite_T_fractionOfCallerTime.name() : __unite_T_fractionOfCallerTime
    })
_module_typeBindings.T_fractionOfCallerTime = T_fractionOfCallerTime
Namespace.addCategoryObject('typeBinding', 'T_fractionOfCallerTime', T_fractionOfCallerTime)


JobPerformance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JobPerformance'), T_JobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 132, 1))
Namespace.addCategoryObject('elementBinding', JobPerformance.name().localName(), JobPerformance)



T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'label'), T_label, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 103, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cpuTime'), T_cpuTime, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 104, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime'), T_fractionOfTotalTime, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 105, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'calls'), T_calls, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 106, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'depth'), T_depth, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 107, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fractionOfCallerTime'), T_fractionOfCallerTime, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 108, 3)))

T_functionsJobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), T_functionsJobStatistics, scope=T_functionsJobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 109, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 109, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'label')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 103, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cpuTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 104, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionOfTotalTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 105, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'calls')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 106, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'depth')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 107, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fractionOfCallerTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 108, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(T_functionsJobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 109, 3))
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




T_JobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totalCpuTime'), T_totalCpuTime, scope=T_JobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 114, 3)))

T_JobStatistics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics'), T_functionsJobStatistics, scope=T_JobStatistics, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 115, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 115, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_JobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totalCpuTime')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 114, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(T_JobStatistics._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'functionsJobStatistics')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 115, 3))
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




T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sha1'), T_sha1, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 120, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'testName'), T_testName, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 121, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'version'), T_version, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 122, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'date'), T_date, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 123, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType'), T_CMakeBuildType, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 124, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'execution'), T_execution, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 125, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procs'), T_procs, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 126, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'host'), T_host, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 127, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OS'), T_OS, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 128, 3)))

T_MyJobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JobStatistics'), T_JobStatistics, scope=T_MyJobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 129, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sha1')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 120, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'testName')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 121, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'version')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 122, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'date')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 123, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CMakeBuildType')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 124, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'execution')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 125, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procs')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 126, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'host')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 127, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OS')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 128, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(T_MyJobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'JobStatistics')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 129, 3))
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




T_JobPerformance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MyJobPerformance'), T_MyJobPerformance, scope=T_JobPerformance, location=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 135, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 134, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 135, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(T_JobPerformance._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MyJobPerformance')), pyxb.utils.utility.Location('/home/A96028/QT5Dev/eficas5C/5C/cataJobPerformance.xsd', 135, 3))
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
T_JobPerformance._Automaton = _BuildAutomaton_3()


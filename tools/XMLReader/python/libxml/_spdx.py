# ./_spdx.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d94940d8678ebc14c5cf560c302f6e0c5fcd1cd6
# Generated 2017-08-30 12:29:09.744974 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Namespace http://spdx.org/rdf/terms# [xmlns:spdx]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0ccdd840-8d6e-11e7-9a6e-dc4a3e79b6da')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _rdf as _ImportedBinding__rdf

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://spdx.org/rdf/terms#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_rdf = pyxb.namespace.NamespaceForURI('http://www.w3.org/1999/02/22-rdf-syntax-ns#', create_if_missing=True)
_Namespace_rdf.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://spdx.org/rdf/terms#}Checksum with content type ELEMENT_ONLY
class Checksum (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://spdx.org/rdf/terms#}Checksum with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Checksum')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 11, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spdx.org/rdf/terms#}CheckSum uses Python identifier CheckSum
    __CheckSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), 'CheckSum', '__httpspdx_orgrdfterms_Checksum_httpspdx_orgrdftermsCheckSum', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 13, 3), )

    
    CheckSum = property(__CheckSum.value, __CheckSum.set, None, None)

    _ElementMap.update({
        __CheckSum.name() : __CheckSum
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Checksum = Checksum
Namespace.addCategoryObject('typeBinding', 'Checksum', Checksum)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://spdx.org/rdf/terms#}algorithm uses Python identifier algorithm
    __algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'algorithm'), 'algorithm', '__httpspdx_orgrdfterms_CTD_ANON_httpspdx_orgrdftermsalgorithm', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 17, 6), )

    
    algorithm = property(__algorithm.value, __algorithm.set, None, None)

    
    # Element {http://spdx.org/rdf/terms#}checksumValue uses Python identifier checksumValue
    __checksumValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'checksumValue'), 'checksumValue', '__httpspdx_orgrdfterms_CTD_ANON_httpspdx_orgrdftermschecksumValue', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 18, 6), )

    
    checksumValue = property(__checksumValue.value, __checksumValue.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpspdx_orgrdfterms_CTD_ANON_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 20, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __algorithm.name() : __algorithm,
        __checksumValue.name() : __checksumValue
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON = CTD_ANON


checksum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'checksum'), Checksum, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', checksum.name().localName(), checksum)



Checksum._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), CTD_ANON, scope=Checksum, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 13, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Checksum._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 13, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Checksum._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'algorithm'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 17, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'checksumValue'), pyxb.binding.datatypes.hexBinary, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 18, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'algorithm')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 17, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'checksumValue')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 18, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()


# ./_vcard.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e57b702b23b72519a53f2e354d0ce8470918cac2
# Generated 2017-08-30 12:29:09.745156 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Namespace http://www.w3.org/2006/vcard/ns# [xmlns:vcard]

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
import pyxb.binding.xml_
import pyxb.binding.datatypes
import _rdf as _ImportedBinding__rdf

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/2006/vcard/ns#', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_rdf = _ImportedBinding__rdf.Namespace
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


# Complex type {http://www.w3.org/2006/vcard/ns#}Organization with content type ELEMENT_ONLY
class Organization (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2006/vcard/ns#}Organization with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Organization')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 15, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2006/vcard/ns#}Organization uses Python identifier Organization
    __Organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organization'), 'Organization', '__httpwww_w3_org2006vcardns_Organization_httpwww_w3_org2006vcardnsOrganization', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 17, 3), )

    
    Organization = property(__Organization.value, __Organization.set, None, None)

    _ElementMap.update({
        __Organization.name() : __Organization
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Organization = Organization
Namespace.addCategoryObject('typeBinding', 'Organization', Organization)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 18, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2006/vcard/ns#}fn uses Python identifier fn
    __fn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fn'), 'fn', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org2006vcardnsfn', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 21, 6), )

    
    fn = property(__fn.value, __fn.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}organization-name uses Python identifier organization_name
    __organization_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'organization-name'), 'organization_name', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org2006vcardnsorganization_name', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 22, 6), )

    
    organization_name = property(__organization_name.value, __organization_name.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasEmail uses Python identifier hasEmail
    __hasEmail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasEmail'), 'hasEmail', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org2006vcardnshasEmail', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 24, 6), )

    
    hasEmail = property(__hasEmail.value, __hasEmail.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasURL uses Python identifier hasURL
    __hasURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasURL'), 'hasURL', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org2006vcardnshasURL', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 25, 6), )

    
    hasURL = property(__hasURL.value, __hasURL.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasTelephone uses Python identifier hasTelephone
    __hasTelephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasTelephone'), 'hasTelephone', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org2006vcardnshasTelephone', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 26, 6), )

    
    hasTelephone = property(__hasTelephone.value, __hasTelephone.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasAddress uses Python identifier hasAddress
    __hasAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasAddress'), 'hasAddress', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org2006vcardnshasAddress', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1), )

    
    hasAddress = property(__hasAddress.value, __hasAddress.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_org2006vcardns_CTD_ANON_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 28, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __fn.name() : __fn,
        __organization_name.name() : __organization_name,
        __hasEmail.name() : __hasEmail,
        __hasURL.name() : __hasURL,
        __hasTelephone.name() : __hasTelephone,
        __hasAddress.name() : __hasAddress
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.w3.org/2006/vcard/ns#}Address with content type ELEMENT_ONLY
class Address (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2006/vcard/ns#}Address with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Address')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 34, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2006/vcard/ns#}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_w3_org2006vcardns_Address_httpwww_w3_org2006vcardnsAddress', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 36, 3), )

    
    Address = property(__Address.value, __Address.set, None, None)

    _ElementMap.update({
        __Address.name() : __Address
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Address = Address
Namespace.addCategoryObject('typeBinding', 'Address', Address)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2006/vcard/ns#}street-address uses Python identifier street_address
    __street_address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'street-address'), 'street_address', '__httpwww_w3_org2006vcardns_CTD_ANON__httpwww_w3_org2006vcardnsstreet_address', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 40, 6), )

    
    street_address = property(__street_address.value, __street_address.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}locality uses Python identifier locality
    __locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locality'), 'locality', '__httpwww_w3_org2006vcardns_CTD_ANON__httpwww_w3_org2006vcardnslocality', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 41, 6), )

    
    locality = property(__locality.value, __locality.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}postal-code uses Python identifier postal_code
    __postal_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postal-code'), 'postal_code', '__httpwww_w3_org2006vcardns_CTD_ANON__httpwww_w3_org2006vcardnspostal_code', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 42, 6), )

    
    postal_code = property(__postal_code.value, __postal_code.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}country-name uses Python identifier country_name
    __country_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country-name'), 'country_name', '__httpwww_w3_org2006vcardns_CTD_ANON__httpwww_w3_org2006vcardnscountry_name', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 43, 6), )

    
    country_name = property(__country_name.value, __country_name.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_org2006vcardns_CTD_ANON__httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 45, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __street_address.name() : __street_address,
        __locality.name() : __locality,
        __postal_code.name() : __postal_code,
        __country_name.name() : __country_name
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.w3.org/2006/vcard/ns#}organization-name with content type SIMPLE
class organization_name_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2006/vcard/ns#}organization-name with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'organization-name')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 60, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2006vcardns_organization_name__httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 63, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.organization_name_ = organization_name_
Namespace.addCategoryObject('typeBinding', 'organization-name', organization_name_)


fn = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fn'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', fn.name().localName(), fn)

hasEmail = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasEmail'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 54, 1))
Namespace.addCategoryObject('elementBinding', hasEmail.name().localName(), hasEmail)

hasURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasURL'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 55, 1))
Namespace.addCategoryObject('elementBinding', hasURL.name().localName(), hasURL)

hasTelephone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasTelephone'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 56, 1))
Namespace.addCategoryObject('elementBinding', hasTelephone.name().localName(), hasTelephone)

hasLogo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasLogo'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 57, 1))
Namespace.addCategoryObject('elementBinding', hasLogo.name().localName(), hasLogo)

hasAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasAddress'), Address, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', hasAddress.name().localName(), hasAddress)

organization_name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organization-name'), organization_name_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 59, 1))
Namespace.addCategoryObject('elementBinding', organization_name.name().localName(), organization_name)



Organization._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organization'), CTD_ANON, scope=Organization, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 17, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Organization._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organization')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 17, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Organization._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fn'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 21, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'organization-name'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 22, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasEmail'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 24, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasURL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 25, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasTelephone'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 26, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasAddress'), Address, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 21, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 22, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 23, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 24, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 25, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 26, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fn')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'organization-name')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 22, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasAddress')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 23, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasEmail')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 24, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasURL')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 25, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasTelephone')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 26, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




Address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), CTD_ANON_, scope=Address, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 36, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Address._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street-address'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 40, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locality'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 41, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postal-code'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 42, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country-name'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 43, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'street-address')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 40, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locality')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 41, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postal-code')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 42, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country-name')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 43, 6))
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
CTD_ANON_._Automaton = _BuildAutomaton_3()


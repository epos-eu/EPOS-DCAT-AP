# ./_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:5dcb1364378c5447ae96566875e93ad355c0f590
# Generated 2017-08-30 12:29:09.746062 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Group contents:
# Namespace http://purl.org/dc/terms/ [xmlns:dct]
# Namespace http://www.w3.org/1999/02/22-rdf-syntax-ns# [xmlns:rdf]
# Namespace http://www.w3.org/2004/02/skos/core# [xmlns:skos]
# Namespace http://www.w3.org/ns/adms# [xmlns:adms]
# Namespace http://www.w3.org/ns/dcat# [xmlns:dcat]
# Namespace http://xmlns.com/foaf/0.1/ [xmlns:foaf]


from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.utils.utility
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
import _owl as _ImportedBinding__owl
import _schema as _ImportedBinding__schema
import _spdx as _ImportedBinding__spdx
import pyxb.binding.datatypes
import _vcard as _ImportedBinding__vcard
import pyxb.binding.xml_
import _locn as _ImportedBinding__locn

# NOTE: All namespace declarations are reserved within the binding
_Namespace_dct = pyxb.namespace.NamespaceForURI('http://purl.org/dc/terms/', create_if_missing=True)
_Namespace_dct.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_schema = pyxb.namespace.NamespaceForURI('http://schema.org/', create_if_missing=True)
_Namespace_schema.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_rdf = pyxb.namespace.NamespaceForURI('http://www.w3.org/1999/02/22-rdf-syntax-ns#', create_if_missing=True)
_Namespace_rdf.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_skos = pyxb.namespace.NamespaceForURI('http://www.w3.org/2004/02/skos/core#', create_if_missing=True)
_Namespace_skos.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_locn = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/locn#', create_if_missing=True)
_Namespace_locn.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dcat = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/dcat#', create_if_missing=True)
_Namespace_dcat.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_adms = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/adms#', create_if_missing=True)
_Namespace_adms.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_foaf = pyxb.namespace.NamespaceForURI('http://xmlns.com/foaf/0.1/', create_if_missing=True)
_Namespace_foaf.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_owl = pyxb.namespace.NamespaceForURI('http://www.w3.org/2002/07/owl#', create_if_missing=True)
_Namespace_owl.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_spdx = pyxb.namespace.NamespaceForURI('http://spdx.org/rdf/terms#', create_if_missing=True)
_Namespace_spdx.configureCategories(['typeBinding', 'elementBinding'])

# Complex type {http://purl.org/dc/terms/}LicenseDocument with content type ELEMENT_ONLY
class LicenseDocument (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}LicenseDocument with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'LicenseDocument')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 78, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}LicenseDocument uses Python identifier LicenseDocument
    __LicenseDocument = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'LicenseDocument'), 'LicenseDocument', '__httppurl_orgdcterms_LicenseDocument_httppurl_orgdctermsLicenseDocument', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 80, 3), )

    
    LicenseDocument = property(__LicenseDocument.value, __LicenseDocument.set, None, None)

    _ElementMap.update({
        __LicenseDocument.name() : __LicenseDocument
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LicenseDocument = LicenseDocument
_Namespace_dct.addCategoryObject('typeBinding', 'LicenseDocument', LicenseDocument)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 81, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httppurl_orgdcterms_CTD_ANON_httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://purl.org/dc/terms/}PeriodOfTime with content type ELEMENT_ONLY
class PeriodOfTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}PeriodOfTime with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'PeriodOfTime')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 92, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}PeriodOfTime uses Python identifier PeriodOfTime
    __PeriodOfTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'PeriodOfTime'), 'PeriodOfTime', '__httppurl_orgdcterms_PeriodOfTime_httppurl_orgdctermsPeriodOfTime', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 94, 3), )

    
    PeriodOfTime = property(__PeriodOfTime.value, __PeriodOfTime.set, None, None)

    _ElementMap.update({
        __PeriodOfTime.name() : __PeriodOfTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PeriodOfTime = PeriodOfTime
_Namespace_dct.addCategoryObject('typeBinding', 'PeriodOfTime', PeriodOfTime)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 95, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}startDate uses Python identifier startDate
    __startDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'startDate'), 'startDate', '__httppurl_orgdcterms_CTD_ANON__httpschema_orgstartDate', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 5, 1), )

    
    startDate = property(__startDate.value, __startDate.set, None, None)

    
    # Element {http://schema.org/}endDate uses Python identifier endDate
    __endDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'endDate'), 'endDate', '__httppurl_orgdcterms_CTD_ANON__httpschema_orgendDate', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 6, 1), )

    
    endDate = property(__endDate.value, __endDate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httppurl_orgdcterms_CTD_ANON__httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 101, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __startDate.name() : __startDate,
        __endDate.name() : __endDate
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://purl.org/dc/terms/}Location with content type ELEMENT_ONLY
class Location (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}Location with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'Location')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 107, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'Location'), 'Location', '__httppurl_orgdcterms_Location_httppurl_orgdctermsLocation', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 109, 3), )

    
    Location = property(__Location.value, __Location.set, None, None)

    _ElementMap.update({
        __Location.name() : __Location
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Location = Location
_Namespace_dct.addCategoryObject('typeBinding', 'Location', Location)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 110, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2004/02/skos/core#}prefLabel uses Python identifier prefLabel
    __prefLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel'), 'prefLabel', '__httppurl_orgdcterms_CTD_ANON_2_httpwww_w3_org200402skoscoreprefLabel', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 48, 1), )

    
    prefLabel = property(__prefLabel.value, __prefLabel.set, None, None)

    
    # Element {http://www.w3.org/ns/locn#}geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_locn, 'geometry'), 'geometry', '__httppurl_orgdcterms_CTD_ANON_2_httpwww_w3_orgnslocngeometry', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/locn.xsd', 13, 1), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httppurl_orgdcterms_CTD_ANON_2_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 116, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __prefLabel.name() : __prefLabel,
        __geometry.name() : __geometry
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://purl.org/dc/terms/}LinguisticSystem with content type ELEMENT_ONLY
class LinguisticSystem (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}LinguisticSystem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'LinguisticSystem')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 123, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}LinguisticSystem uses Python identifier LinguisticSystem
    __LinguisticSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'LinguisticSystem'), 'LinguisticSystem', '__httppurl_orgdcterms_LinguisticSystem_httppurl_orgdctermsLinguisticSystem', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 125, 3), )

    
    LinguisticSystem = property(__LinguisticSystem.value, __LinguisticSystem.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httppurl_orgdcterms_LinguisticSystem_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 128, 2)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __LinguisticSystem.name() : __LinguisticSystem
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.LinguisticSystem = LinguisticSystem
_Namespace_dct.addCategoryObject('typeBinding', 'LinguisticSystem', LinguisticSystem)


# Complex type {http://purl.org/dc/terms/}MediaTypeOrExtent with content type ELEMENT_ONLY
class MediaTypeOrExtent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}MediaTypeOrExtent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'MediaTypeOrExtent')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 132, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}MediaTypeOrExtent uses Python identifier MediaTypeOrExtent
    __MediaTypeOrExtent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'MediaTypeOrExtent'), 'MediaTypeOrExtent', '__httppurl_orgdcterms_MediaTypeOrExtent_httppurl_orgdctermsMediaTypeOrExtent', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 134, 3), )

    
    MediaTypeOrExtent = property(__MediaTypeOrExtent.value, __MediaTypeOrExtent.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httppurl_orgdcterms_MediaTypeOrExtent_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 137, 2)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __MediaTypeOrExtent.name() : __MediaTypeOrExtent
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.MediaTypeOrExtent = MediaTypeOrExtent
_Namespace_dct.addCategoryObject('typeBinding', 'MediaTypeOrExtent', MediaTypeOrExtent)


# Complex type {http://purl.org/dc/terms/}ProvenanceStatement with content type ELEMENT_ONLY
class ProvenanceStatement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}ProvenanceStatement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'ProvenanceStatement')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 141, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}ProvenanceStatement uses Python identifier ProvenanceStatement
    __ProvenanceStatement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'ProvenanceStatement'), 'ProvenanceStatement', '__httppurl_orgdcterms_ProvenanceStatement_httppurl_orgdctermsProvenanceStatement', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 143, 3), )

    
    ProvenanceStatement = property(__ProvenanceStatement.value, __ProvenanceStatement.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httppurl_orgdcterms_ProvenanceStatement_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 146, 2)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __ProvenanceStatement.name() : __ProvenanceStatement
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.ProvenanceStatement = ProvenanceStatement
_Namespace_dct.addCategoryObject('typeBinding', 'ProvenanceStatement', ProvenanceStatement)


# Complex type {http://purl.org/dc/terms/}RightsStatement with content type ELEMENT_ONLY
class RightsStatement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://purl.org/dc/terms/}RightsStatement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dct, 'RightsStatement')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 150, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}RightsStatement uses Python identifier RightsStatement
    __RightsStatement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'RightsStatement'), 'RightsStatement', '__httppurl_orgdcterms_RightsStatement_httppurl_orgdctermsRightsStatement', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 152, 3), )

    
    RightsStatement = property(__RightsStatement.value, __RightsStatement.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httppurl_orgdcterms_RightsStatement_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 155, 2)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __RightsStatement.name() : __RightsStatement
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.RightsStatement = RightsStatement
_Namespace_dct.addCategoryObject('typeBinding', 'RightsStatement', RightsStatement)


# Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}PlainLiteral with content type SIMPLE
class PlainLiteral (pyxb.binding.basis.complexTypeDefinition):
    """
The Resource Description Framework [RDF] is defined to have an extensible system of typed literals, based on XML Schema datatypes [XSD], and also to have plain literals. In the RDF specification, plain literals differ from typed literals in that plain literals have no datatype and can optionally have a language tag, indicating the natural language of the content.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rdf, 'PlainLiteral')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 12, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org19990222_rdf_syntax_ns_PlainLiteral_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 20, 4)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
_module_typeBindings.PlainLiteral = PlainLiteral
_Namespace_rdf.addCategoryObject('typeBinding', 'PlainLiteral', PlainLiteral)


# Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}TypedLiteral with content type SIMPLE
class TypedLiteral (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}TypedLiteral with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rdf, 'TypedLiteral')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'datatype'), 'datatype', '__httpwww_w3_org19990222_rdf_syntax_ns_TypedLiteral_httpwww_w3_org19990222_rdf_syntax_nsdatatype', pyxb.binding.datatypes.anyURI)
    __datatype._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 28, 4)
    __datatype._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 28, 4)
    
    datatype = property(__datatype.value, __datatype.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __datatype.name() : __datatype
    })
_module_typeBindings.TypedLiteral = TypedLiteral
_Namespace_rdf.addCategoryObject('typeBinding', 'TypedLiteral', TypedLiteral)


# Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}DateTimeLiteral with content type SIMPLE
class DateTimeLiteral (pyxb.binding.basis.complexTypeDefinition):
    """
			Date in 
      """
    _TypeDefinition = pyxb.binding.datatypes.dateTime
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rdf, 'DateTimeLiteral')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 33, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.dateTime
    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'datatype'), 'datatype', '__httpwww_w3_org19990222_rdf_syntax_ns_DateTimeLiteral_httpwww_w3_org19990222_rdf_syntax_nsdatatype', pyxb.binding.datatypes.anyURI, fixed=True, unicode_default='http://www.w3.org/2001/XMLSchema#dateTime')
    __datatype._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 41, 4)
    __datatype._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 41, 4)
    
    datatype = property(__datatype.value, __datatype.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __datatype.name() : __datatype
    })
_module_typeBindings.DateTimeLiteral = DateTimeLiteral
_Namespace_rdf.addCategoryObject('typeBinding', 'DateTimeLiteral', DateTimeLiteral)


# Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}Resource with content type EMPTY
class Resource (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}Resource with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rdf, 'Resource')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 46, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource uses Python identifier resource
    __resource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'resource'), 'resource', '__httpwww_w3_org19990222_rdf_syntax_ns_Resource_httpwww_w3_org19990222_rdf_syntax_nsresource', pyxb.binding.datatypes.anyURI)
    __resource._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 57, 1)
    __resource._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 47, 2)
    
    resource = property(__resource.value, __resource.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __resource.name() : __resource
    })
_module_typeBindings.Resource = Resource
_Namespace_rdf.addCategoryObject('typeBinding', 'Resource', Resource)


# Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}CatalogRoot with content type ELEMENT_ONLY
class CatalogRoot (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/1999/02/22-rdf-syntax-ns#}CatalogRoot with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_rdf, 'CatalogRoot')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 50, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/dcat#}Catalog uses Python identifier Catalog
    __Catalog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Catalog'), 'Catalog', '__httpwww_w3_org19990222_rdf_syntax_ns_CatalogRoot_httpwww_w3_orgnsdcatCatalog', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 38, 1), )

    
    Catalog = property(__Catalog.value, __Catalog.set, None, None)

    _ElementMap.update({
        __Catalog.name() : __Catalog
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CatalogRoot = CatalogRoot
_Namespace_rdf.addCategoryObject('typeBinding', 'CatalogRoot', CatalogRoot)


# Complex type {http://www.w3.org/2004/02/skos/core#}ConceptScheme with content type ELEMENT_ONLY
class ConceptScheme (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2004/02/skos/core#}ConceptScheme with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_skos, 'ConceptScheme')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 12, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2004/02/skos/core#}ConceptScheme uses Python identifier ConceptScheme
    __ConceptScheme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_skos, 'ConceptScheme'), 'ConceptScheme', '__httpwww_w3_org200402skoscore_ConceptScheme_httpwww_w3_org200402skoscoreConceptScheme', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 14, 3), )

    
    ConceptScheme = property(__ConceptScheme.value, __ConceptScheme.set, None, None)

    _ElementMap.update({
        __ConceptScheme.name() : __ConceptScheme
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ConceptScheme = ConceptScheme
_Namespace_skos.addCategoryObject('typeBinding', 'ConceptScheme', ConceptScheme)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 15, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_w3_org200402skoscore_CTD_ANON_httppurl_orgdctermstitle', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_org200402skoscore_CTD_ANON_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 21, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __title.name() : __title
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.w3.org/2004/02/skos/core#}Concept with content type ELEMENT_ONLY
class Concept (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2004/02/skos/core#}Concept with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_skos, 'Concept')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 28, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2004/02/skos/core#}Concept uses Python identifier Concept
    __Concept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_skos, 'Concept'), 'Concept', '__httpwww_w3_org200402skoscore_Concept_httpwww_w3_org200402skoscoreConcept', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 30, 3), )

    
    Concept = property(__Concept.value, __Concept.set, None, None)

    _ElementMap.update({
        __Concept.name() : __Concept
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Concept = Concept
_Namespace_skos.addCategoryObject('typeBinding', 'Concept', Concept)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 31, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2004/02/skos/core#}inScheme uses Python identifier inScheme
    __inScheme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_skos, 'inScheme'), 'inScheme', '__httpwww_w3_org200402skoscore_CTD_ANON__httpwww_w3_org200402skoscoreinScheme', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 35, 6), )

    
    inScheme = property(__inScheme.value, __inScheme.set, None, None)

    
    # Element {http://www.w3.org/2004/02/skos/core#}prefLabel uses Python identifier prefLabel
    __prefLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel'), 'prefLabel', '__httpwww_w3_org200402skoscore_CTD_ANON__httpwww_w3_org200402skoscoreprefLabel', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 48, 1), )

    
    prefLabel = property(__prefLabel.value, __prefLabel.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_org200402skoscore_CTD_ANON__httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 41, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __inScheme.name() : __inScheme,
        __prefLabel.name() : __prefLabel
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 36, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource uses Python identifier resource
    __resource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'resource'), 'resource', '__httpwww_w3_org200402skoscore_CTD_ANON_2_httpwww_w3_org19990222_rdf_syntax_nsresource', pyxb.binding.datatypes.anyURI)
    __resource._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 57, 1)
    __resource._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 37, 8)
    
    resource = property(__resource.value, __resource.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __resource.name() : __resource
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {http://www.w3.org/ns/adms#}Identifier with content type ELEMENT_ONLY
class Identifier (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/ns/adms#}Identifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_adms, 'Identifier')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 14, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/adms#}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'Identifier'), 'Identifier', '__httpwww_w3_orgnsadms_Identifier_httpwww_w3_orgnsadmsIdentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 16, 3), )

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    _ElementMap.update({
        __Identifier.name() : __Identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Identifier = Identifier
_Namespace_adms.addCategoryObject('typeBinding', 'Identifier', Identifier)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 17, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2004/02/skos/core#}notation uses Python identifier notation
    __notation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_skos, 'notation'), 'notation', '__httpwww_w3_orgnsadms_CTD_ANON_httpwww_w3_org200402skoscorenotation', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 47, 1), )

    
    notation = property(__notation.value, __notation.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_orgnsadms_CTD_ANON_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 22, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __notation.name() : __notation
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type {http://www.w3.org/ns/dcat#}Catalog with content type ELEMENT_ONLY
class Catalog_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/ns/dcat#}Catalog with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dcat, 'Catalog')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermsdescription', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}isPartOf uses Python identifier isPartOf
    __isPartOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'isPartOf'), 'isPartOf', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermsisPartOf', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 39, 1), )

    
    isPartOf = property(__isPartOf.value, __isPartOf.set, None, None)

    
    # Element {http://purl.org/dc/terms/}hasPart uses Python identifier hasPart
    __hasPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasPart'), 'hasPart', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermshasPart', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 40, 1), )

    
    hasPart = property(__hasPart.value, __hasPart.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermsspatial', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://purl.org/dc/terms/}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), 'rights', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermsrights', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://purl.org/dc/terms/}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), 'license', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermslicense', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {http://purl.org/dc/terms/}publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), 'publisher', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermspublisher', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1), )

    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_w3_orgnsdcat_Catalog__httppurl_orgdctermslanguage', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}dataset uses Python identifier dataset
    __dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'dataset'), 'dataset', '__httpwww_w3_orgnsdcat_Catalog__httpwww_w3_orgnsdcatdataset', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 45, 3), )

    
    dataset = property(__dataset.value, __dataset.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}homepage uses Python identifier homepage
    __homepage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'homepage'), 'homepage', '__httpwww_w3_orgnsdcat_Catalog__httpwww_w3_orgnsdcathomepage', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 47, 3), )

    
    homepage = property(__homepage.value, __homepage.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}themeTaxonomy uses Python identifier themeTaxonomy
    __themeTaxonomy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'themeTaxonomy'), 'themeTaxonomy', '__httpwww_w3_orgnsdcat_Catalog__httpwww_w3_orgnsdcatthemeTaxonomy', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 52, 3), )

    
    themeTaxonomy = property(__themeTaxonomy.value, __themeTaxonomy.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}record uses Python identifier record
    __record = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'record'), 'record', '__httpwww_w3_orgnsdcat_Catalog__httpwww_w3_orgnsdcatrecord', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 56, 3), )

    
    record = property(__record.value, __record.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_orgnsdcat_Catalog__httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 60, 2)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __issued.name() : __issued,
        __modified.name() : __modified,
        __isPartOf.name() : __isPartOf,
        __hasPart.name() : __hasPart,
        __spatial.name() : __spatial,
        __rights.name() : __rights,
        __license.name() : __license,
        __publisher.name() : __publisher,
        __language.name() : __language,
        __dataset.name() : __dataset,
        __homepage.name() : __homepage,
        __themeTaxonomy.name() : __themeTaxonomy,
        __record.name() : __record
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.Catalog_ = Catalog_
_Namespace_dcat.addCategoryObject('typeBinding', 'Catalog', Catalog_)


# Complex type {http://www.w3.org/ns/dcat#}CatalogRecord with content type ELEMENT_ONLY
class CatalogRecord (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/ns/dcat#}CatalogRecord with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dcat, 'CatalogRecord')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 63, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/dcat#}CatalogRecord uses Python identifier CatalogRecord
    __CatalogRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'CatalogRecord'), 'CatalogRecord', '__httpwww_w3_orgnsdcat_CatalogRecord_httpwww_w3_orgnsdcatCatalogRecord', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 65, 3), )

    
    CatalogRecord = property(__CatalogRecord.value, __CatalogRecord.set, None, None)

    _ElementMap.update({
        __CatalogRecord.name() : __CatalogRecord
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CatalogRecord = CatalogRecord
_Namespace_dcat.addCategoryObject('typeBinding', 'CatalogRecord', CatalogRecord)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 66, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermsdescription', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}conformsTo uses Python identifier conformsTo
    __conformsTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), 'conformsTo', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermsconformsTo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1), )

    
    conformsTo = property(__conformsTo.value, __conformsTo.set, None, None)

    
    # Element {http://purl.org/dc/terms/}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'source'), 'source', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermssource', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 59, 1), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_w3_orgnsdcat_CTD_ANON_httppurl_orgdctermslanguage', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'status'), 'status', '__httpwww_w3_orgnsdcat_CTD_ANON_httpwww_w3_orgnsadmsstatus', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 28, 1), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}primaryTopic uses Python identifier primaryTopic
    __primaryTopic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), 'primaryTopic', '__httpwww_w3_orgnsdcat_CTD_ANON_httpxmlns_comfoaf0_1primaryTopic', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 31, 1), )

    
    primaryTopic = property(__primaryTopic.value, __primaryTopic.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_orgnsdcat_CTD_ANON_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 81, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __issued.name() : __issued,
        __modified.name() : __modified,
        __conformsTo.name() : __conformsTo,
        __source.name() : __source,
        __language.name() : __language,
        __status.name() : __status,
        __primaryTopic.name() : __primaryTopic
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type {http://www.w3.org/ns/dcat#}Dataset with content type ELEMENT_ONLY
class Dataset (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/ns/dcat#}Dataset with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dcat, 'Dataset')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 87, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/dcat#}Dataset uses Python identifier Dataset
    __Dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Dataset'), 'Dataset', '__httpwww_w3_orgnsdcat_Dataset_httpwww_w3_orgnsdcatDataset', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 89, 3), )

    
    Dataset = property(__Dataset.value, __Dataset.set, None, None)

    _ElementMap.update({
        __Dataset.name() : __Dataset
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Dataset = Dataset
_Namespace_dcat.addCategoryObject('typeBinding', 'Dataset', Dataset)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 90, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsdescription', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}isVersionOf uses Python identifier isVersionOf
    __isVersionOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'isVersionOf'), 'isVersionOf', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsisVersionOf', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 33, 1), )

    
    isVersionOf = property(__isVersionOf.value, __isVersionOf.set, None, None)

    
    # Element {http://purl.org/dc/terms/}hasVersion uses Python identifier hasVersion
    __hasVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion'), 'hasVersion', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermshasVersion', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 34, 1), )

    
    hasVersion = property(__hasVersion.value, __hasVersion.set, None, None)

    
    # Element {http://purl.org/dc/terms/}relation uses Python identifier relation
    __relation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'relation'), 'relation', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsrelation', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 42, 1), )

    
    relation = property(__relation.value, __relation.set, None, None)

    
    # Element {http://purl.org/dc/terms/}conformsTo uses Python identifier conformsTo
    __conformsTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), 'conformsTo', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsconformsTo', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1), )

    
    conformsTo = property(__conformsTo.value, __conformsTo.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsspatial', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://purl.org/dc/terms/}temporal uses Python identifier temporal
    __temporal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), 'temporal', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermstemporal', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1), )

    
    temporal = property(__temporal.value, __temporal.set, None, None)

    
    # Element {http://purl.org/dc/terms/}accrualPeriodicity uses Python identifier accrualPeriodicity
    __accrualPeriodicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'accrualPeriodicity'), 'accrualPeriodicity', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsaccrualPeriodicity', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 51, 1), )

    
    accrualPeriodicity = property(__accrualPeriodicity.value, __accrualPeriodicity.set, None, None)

    
    # Element {http://purl.org/dc/terms/}provenance uses Python identifier provenance
    __provenance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance'), 'provenance', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsprovenance', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 55, 1), )

    
    provenance = property(__provenance.value, __provenance.set, None, None)

    
    # Element {http://purl.org/dc/terms/}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'source'), 'source', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermssource', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 59, 1), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://purl.org/dc/terms/}accessRights uses Python identifier accessRights
    __accessRights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), 'accessRights', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsaccessRights', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1), )

    
    accessRights = property(__accessRights.value, __accessRights.set, None, None)

    
    # Element {http://purl.org/dc/terms/}publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), 'publisher', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermspublisher', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1), )

    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_w3_orgnsdcat_CTD_ANON__httppurl_orgdctermslanguage', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://www.w3.org/2002/07/owl#}versionInfo uses Python identifier versionInfo
    __versionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo'), 'versionInfo', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_org200207owlversionInfo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/owl.xsd', 5, 1), )

    
    versionInfo = property(__versionInfo.value, __versionInfo.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}identifier uses Python identifier identifier_
    __identifier_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'identifier'), 'identifier_', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsadmsidentifier', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 29, 1), )

    
    identifier_ = property(__identifier_.value, __identifier_.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}sample uses Python identifier sample
    __sample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'sample'), 'sample', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsadmssample', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 30, 1), )

    
    sample = property(__sample.value, __sample.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}versionNotes uses Python identifier versionNotes
    __versionNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'versionNotes'), 'versionNotes', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsadmsversionNotes', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 31, 1), )

    
    versionNotes = property(__versionNotes.value, __versionNotes.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsdcatcontactPoint', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 97, 6), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), 'keyword', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsdcatkeyword', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 99, 6), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}theme uses Python identifier theme
    __theme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme'), 'theme', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsdcattheme', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 100, 6), )

    
    theme = property(__theme.value, __theme.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}landingPage uses Python identifier landingPage
    __landingPage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage'), 'landingPage', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsdcatlandingPage', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 107, 6), )

    
    landingPage = property(__landingPage.value, __landingPage.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}distribution uses Python identifier distribution
    __distribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'distribution'), 'distribution', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_orgnsdcatdistribution', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 118, 6), )

    
    distribution = property(__distribution.value, __distribution.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), 'page', '__httpwww_w3_orgnsdcat_CTD_ANON__httpxmlns_comfoaf0_1page', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1), )

    
    page = property(__page.value, __page.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_orgnsdcat_CTD_ANON__httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 121, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __issued.name() : __issued,
        __modified.name() : __modified,
        __isVersionOf.name() : __isVersionOf,
        __hasVersion.name() : __hasVersion,
        __relation.name() : __relation,
        __conformsTo.name() : __conformsTo,
        __spatial.name() : __spatial,
        __temporal.name() : __temporal,
        __accrualPeriodicity.name() : __accrualPeriodicity,
        __provenance.name() : __provenance,
        __source.name() : __source,
        __accessRights.name() : __accessRights,
        __publisher.name() : __publisher,
        __type.name() : __type,
        __identifier.name() : __identifier,
        __language.name() : __language,
        __versionInfo.name() : __versionInfo,
        __identifier_.name() : __identifier_,
        __sample.name() : __sample,
        __versionNotes.name() : __versionNotes,
        __contactPoint.name() : __contactPoint,
        __keyword.name() : __keyword,
        __theme.name() : __theme,
        __landingPage.name() : __landingPage,
        __distribution.name() : __distribution,
        __page.name() : __page
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type {http://www.w3.org/ns/dcat#}Distribution with content type ELEMENT_ONLY
class Distribution (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/ns/dcat#}Distribution with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dcat, 'Distribution')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 127, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/dcat#}Distribution uses Python identifier Distribution
    __Distribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Distribution'), 'Distribution', '__httpwww_w3_orgnsdcat_Distribution_httpwww_w3_orgnsdcatDistribution', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 129, 3), )

    
    Distribution = property(__Distribution.value, __Distribution.set, None, None)

    _ElementMap.update({
        __Distribution.name() : __Distribution
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Distribution = Distribution
_Namespace_dcat.addCategoryObject('typeBinding', 'Distribution', Distribution)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 130, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermsdescription', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), 'format', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermsformat', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1), )

    
    format = property(__format.value, __format.set, None, None)

    
    # Element {http://purl.org/dc/terms/}conformsTo uses Python identifier conformsTo
    __conformsTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), 'conformsTo', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermsconformsTo', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1), )

    
    conformsTo = property(__conformsTo.value, __conformsTo.set, None, None)

    
    # Element {http://purl.org/dc/terms/}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), 'rights', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermsrights', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://purl.org/dc/terms/}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), 'license', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermslicense', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httppurl_orgdctermslanguage', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://spdx.org/rdf/terms#}checksum uses Python identifier checksum
    __checksum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_spdx, 'checksum'), 'checksum', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpspdx_orgrdftermschecksum', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 26, 1), )

    
    checksum = property(__checksum.value, __checksum.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'status'), 'status', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpwww_w3_orgnsadmsstatus', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 28, 1), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}accessURL uses Python identifier accessURL
    __accessURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'accessURL'), 'accessURL', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpwww_w3_orgnsdcataccessURL', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 134, 6), )

    
    accessURL = property(__accessURL.value, __accessURL.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}downloadURL uses Python identifier downloadURL
    __downloadURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'downloadURL'), 'downloadURL', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpwww_w3_orgnsdcatdownloadURL', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 135, 6), )

    
    downloadURL = property(__downloadURL.value, __downloadURL.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}mediaType uses Python identifier mediaType
    __mediaType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'mediaType'), 'mediaType', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpwww_w3_orgnsdcatmediaType', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 139, 6), )

    
    mediaType = property(__mediaType.value, __mediaType.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}byteSize uses Python identifier byteSize
    __byteSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'byteSize'), 'byteSize', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpwww_w3_orgnsdcatbyteSize', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 143, 6), )

    
    byteSize = property(__byteSize.value, __byteSize.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), 'page', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpxmlns_comfoaf0_1page', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1), )

    
    page = property(__page.value, __page.set, None, None)

    
    # Attribute {http://www.w3.org/1999/02/22-rdf-syntax-ns#}about uses Python identifier about
    __about = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_rdf, 'about'), 'about', '__httpwww_w3_orgnsdcat_CTD_ANON_2_httpwww_w3_org19990222_rdf_syntax_nsabout', pyxb.binding.datatypes.anyURI)
    __about._DeclarationLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 56, 1)
    __about._UseLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 149, 5)
    
    about = property(__about.value, __about.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __issued.name() : __issued,
        __modified.name() : __modified,
        __format.name() : __format,
        __conformsTo.name() : __conformsTo,
        __rights.name() : __rights,
        __license.name() : __license,
        __language.name() : __language,
        __checksum.name() : __checksum,
        __status.name() : __status,
        __accessURL.name() : __accessURL,
        __downloadURL.name() : __downloadURL,
        __mediaType.name() : __mediaType,
        __byteSize.name() : __byteSize,
        __page.name() : __page
    })
    _AttributeMap.update({
        __about.name() : __about
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type {http://xmlns.com/foaf/0.1/}Document with content type ELEMENT_ONLY
class Document_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://xmlns.com/foaf/0.1/}Document with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_foaf, 'Document')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 14, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://xmlns.com/foaf/0.1/}primaryTopic uses Python identifier primaryTopic
    __primaryTopic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), 'primaryTopic', '__httpxmlns_comfoaf0_1_Document__httpxmlns_comfoaf0_1primaryTopic', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 16, 3), )

    
    primaryTopic = property(__primaryTopic.value, __primaryTopic.set, None, None)

    _ElementMap.update({
        __primaryTopic.name() : __primaryTopic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Document_ = Document_
_Namespace_foaf.addCategoryObject('typeBinding', 'Document', Document_)


# Complex type {http://xmlns.com/foaf/0.1/}Agent with content type ELEMENT_ONLY
class Agent_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://xmlns.com/foaf/0.1/}Agent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_foaf, 'Agent')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 22, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpxmlns_comfoaf0_1_Agent__httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'name'), 'name', '__httpxmlns_comfoaf0_1_Agent__httpxmlns_comfoaf0_1name', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 34, 1), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Agent_ = Agent_
_Namespace_foaf.addCategoryObject('typeBinding', 'Agent', Agent_)


extent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'extent'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 31, 1))
_Namespace_dct.addCategoryObject('elementBinding', extent.name().localName(), extent)

medium = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'medium'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 32, 1))
_Namespace_dct.addCategoryObject('elementBinding', medium.name().localName(), medium)

isVersionOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isVersionOf'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 33, 1))
_Namespace_dct.addCategoryObject('elementBinding', isVersionOf.name().localName(), isVersionOf)

hasVersion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 34, 1))
_Namespace_dct.addCategoryObject('elementBinding', hasVersion.name().localName(), hasVersion)

isReplacedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isReplacedBy'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 35, 1))
_Namespace_dct.addCategoryObject('elementBinding', isReplacedBy.name().localName(), isReplacedBy)

replaces = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'replaces'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 36, 1))
_Namespace_dct.addCategoryObject('elementBinding', replaces.name().localName(), replaces)

isRequiredBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isRequiredBy'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 37, 1))
_Namespace_dct.addCategoryObject('elementBinding', isRequiredBy.name().localName(), isRequiredBy)

requires = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'requires'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 38, 1))
_Namespace_dct.addCategoryObject('elementBinding', requires.name().localName(), requires)

isPartOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isPartOf'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 39, 1))
_Namespace_dct.addCategoryObject('elementBinding', isPartOf.name().localName(), isPartOf)

hasPart = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasPart'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 40, 1))
_Namespace_dct.addCategoryObject('elementBinding', hasPart.name().localName(), hasPart)

isReferencedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isReferencedBy'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 41, 1))
_Namespace_dct.addCategoryObject('elementBinding', isReferencedBy.name().localName(), isReferencedBy)

relation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'relation'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 42, 1))
_Namespace_dct.addCategoryObject('elementBinding', relation.name().localName(), relation)

references = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'references'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 43, 1))
_Namespace_dct.addCategoryObject('elementBinding', references.name().localName(), references)

isFormatOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isFormatOf'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 44, 1))
_Namespace_dct.addCategoryObject('elementBinding', isFormatOf.name().localName(), isFormatOf)

hasFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasFormat'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 45, 1))
_Namespace_dct.addCategoryObject('elementBinding', hasFormat.name().localName(), hasFormat)

conformsTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1))
_Namespace_dct.addCategoryObject('elementBinding', conformsTo.name().localName(), conformsTo)

audience = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'audience'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 49, 1))
_Namespace_dct.addCategoryObject('elementBinding', audience.name().localName(), audience)

accrualMethod = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accrualMethod'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 50, 1))
_Namespace_dct.addCategoryObject('elementBinding', accrualMethod.name().localName(), accrualMethod)

accrualPeriodicity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accrualPeriodicity'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 51, 1))
_Namespace_dct.addCategoryObject('elementBinding', accrualPeriodicity.name().localName(), accrualPeriodicity)

accrualPolicy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accrualPolicy'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 52, 1))
_Namespace_dct.addCategoryObject('elementBinding', accrualPolicy.name().localName(), accrualPolicy)

instructionalMethod = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'instructionalMethod'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 53, 1))
_Namespace_dct.addCategoryObject('elementBinding', instructionalMethod.name().localName(), instructionalMethod)

rightsHolder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'rightsHolder'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 58, 1))
_Namespace_dct.addCategoryObject('elementBinding', rightsHolder.name().localName(), rightsHolder)

source = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'source'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 59, 1))
_Namespace_dct.addCategoryObject('elementBinding', source.name().localName(), source)

mediator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'mediator'), pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 60, 1))
_Namespace_dct.addCategoryObject('elementBinding', mediator.name().localName(), mediator)

educationLevel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'educationLevel'), pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 61, 1))
_Namespace_dct.addCategoryObject('elementBinding', educationLevel.name().localName(), educationLevel)

bibliographicCitation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'bibliographicCitation'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 66, 1))
_Namespace_dct.addCategoryObject('elementBinding', bibliographicCitation.name().localName(), bibliographicCitation)

identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1))
_Namespace_dct.addCategoryObject('elementBinding', identifier.name().localName(), identifier)

comment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rdf, 'comment'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 60, 1))
_Namespace_rdf.addCategoryObject('elementBinding', comment.name().localName(), comment)

label = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rdf, 'label'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 61, 1))
_Namespace_rdf.addCategoryObject('elementBinding', label.name().localName(), label)

status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'status'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 28, 1))
_Namespace_adms.addCategoryObject('elementBinding', status.name().localName(), status)

contactPoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1))
_Namespace_dcat.addCategoryObject('elementBinding', contactPoint.name().localName(), contactPoint)

primaryTopic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 31, 1))
_Namespace_foaf.addCategoryObject('elementBinding', primaryTopic.name().localName(), primaryTopic)

mbox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'mbox'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 33, 1))
_Namespace_foaf.addCategoryObject('elementBinding', mbox.name().localName(), mbox)

alternative = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'alternative'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 16, 1))
_Namespace_dct.addCategoryObject('elementBinding', alternative.name().localName(), alternative)

title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1))
_Namespace_dct.addCategoryObject('elementBinding', title.name().localName(), title)

tableOfContents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'tableOfContents'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 18, 1))
_Namespace_dct.addCategoryObject('elementBinding', tableOfContents.name().localName(), tableOfContents)

abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 19, 1))
_Namespace_dct.addCategoryObject('elementBinding', abstract.name().localName(), abstract)

description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1))
_Namespace_dct.addCategoryObject('elementBinding', description.name().localName(), description)

created = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1))
_Namespace_dct.addCategoryObject('elementBinding', created.name().localName(), created)

valid = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'valid'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 22, 1))
_Namespace_dct.addCategoryObject('elementBinding', valid.name().localName(), valid)

available = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'available'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 23, 1))
_Namespace_dct.addCategoryObject('elementBinding', available.name().localName(), available)

issued = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1))
_Namespace_dct.addCategoryObject('elementBinding', issued.name().localName(), issued)

modified = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1))
_Namespace_dct.addCategoryObject('elementBinding', modified.name().localName(), modified)

dateAccepted = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'dateAccepted'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 26, 1))
_Namespace_dct.addCategoryObject('elementBinding', dateAccepted.name().localName(), dateAccepted)

dateCopyrighted = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'dateCopyrighted'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 27, 1))
_Namespace_dct.addCategoryObject('elementBinding', dateCopyrighted.name().localName(), dateCopyrighted)

dateSubmitted = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'dateSubmitted'), DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 28, 1))
_Namespace_dct.addCategoryObject('elementBinding', dateSubmitted.name().localName(), dateSubmitted)

format = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), MediaTypeOrExtent, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1))
_Namespace_dct.addCategoryObject('elementBinding', format.name().localName(), format)

spatial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), Location, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1))
_Namespace_dct.addCategoryObject('elementBinding', spatial.name().localName(), spatial)

temporal = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), PeriodOfTime, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1))
_Namespace_dct.addCategoryObject('elementBinding', temporal.name().localName(), temporal)

provenance = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance'), ProvenanceStatement, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 55, 1))
_Namespace_dct.addCategoryObject('elementBinding', provenance.name().localName(), provenance)

rights = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), RightsStatement, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1))
_Namespace_dct.addCategoryObject('elementBinding', rights.name().localName(), rights)

accessRights = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), RightsStatement, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1))
_Namespace_dct.addCategoryObject('elementBinding', accessRights.name().localName(), accessRights)

license = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1))
_Namespace_dct.addCategoryObject('elementBinding', license.name().localName(), license)

publisher = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), Agent_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1))
_Namespace_dct.addCategoryObject('elementBinding', publisher.name().localName(), publisher)

type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1))
_Namespace_dct.addCategoryObject('elementBinding', type.name().localName(), type)

language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), LinguisticSystem, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1))
_Namespace_dct.addCategoryObject('elementBinding', language.name().localName(), language)

subject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'subject'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 73, 1))
_Namespace_dct.addCategoryObject('elementBinding', subject.name().localName(), subject)

RDF = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rdf, 'RDF'), CatalogRoot, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 59, 1))
_Namespace_rdf.addCategoryObject('elementBinding', RDF.name().localName(), RDF)

notation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'notation'), TypedLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 47, 1))
_Namespace_skos.addCategoryObject('elementBinding', notation.name().localName(), notation)

prefLabel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 48, 1))
_Namespace_skos.addCategoryObject('elementBinding', prefLabel.name().localName(), prefLabel)

identifier_ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'identifier'), Identifier, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 29, 1))
_Namespace_adms.addCategoryObject('elementBinding', identifier_.name().localName(), identifier_)

sample = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'sample'), Distribution, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 30, 1))
_Namespace_adms.addCategoryObject('elementBinding', sample.name().localName(), sample)

versionNotes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'versionNotes'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 31, 1))
_Namespace_adms.addCategoryObject('elementBinding', versionNotes.name().localName(), versionNotes)

representationTechnique = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 33, 1))
_Namespace_adms.addCategoryObject('elementBinding', representationTechnique.name().localName(), representationTechnique)

theme = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 29, 1))
_Namespace_dcat.addCategoryObject('elementBinding', theme.name().localName(), theme)

keyword = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 31, 1))
_Namespace_dcat.addCategoryObject('elementBinding', keyword.name().localName(), keyword)

landingPage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage'), Document_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 32, 1))
_Namespace_dcat.addCategoryObject('elementBinding', landingPage.name().localName(), landingPage)

accessURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'accessURL'), Resource, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 33, 1))
_Namespace_dcat.addCategoryObject('elementBinding', accessURL.name().localName(), accessURL)

Catalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Catalog'), Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 38, 1))
_Namespace_dcat.addCategoryObject('elementBinding', Catalog.name().localName(), Catalog)

Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'Document'), Document_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 13, 1))
_Namespace_foaf.addCategoryObject('elementBinding', Document.name().localName(), Document)

Agent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'Agent'), Agent_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 21, 1))
_Namespace_foaf.addCategoryObject('elementBinding', Agent.name().localName(), Agent)

page = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), Document_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1))
_Namespace_foaf.addCategoryObject('elementBinding', page.name().localName(), page)

name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'name'), PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 34, 1))
_Namespace_foaf.addCategoryObject('elementBinding', name.name().localName(), name)



LicenseDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'LicenseDocument'), CTD_ANON, scope=LicenseDocument, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 80, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LicenseDocument._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'LicenseDocument')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 80, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LicenseDocument._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 84, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




PeriodOfTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'PeriodOfTime'), CTD_ANON_, scope=PeriodOfTime, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 94, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PeriodOfTime._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'PeriodOfTime')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 94, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PeriodOfTime._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'startDate'), DateTimeLiteral, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 5, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'endDate'), DateTimeLiteral, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 6, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 98, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 99, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'startDate')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 98, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'endDate')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 99, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'Location'), CTD_ANON_2, scope=Location, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 109, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 109, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'Location')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 109, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Location._Automaton = _BuildAutomaton_4()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel'), PlainLiteral, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 48, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_locn, 'geometry'), TypedLiteral, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/locn.xsd', 13, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 113, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 114, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_locn, 'geometry')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 113, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 114, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




LinguisticSystem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'LinguisticSystem'), pyxb.binding.datatypes.string, scope=LinguisticSystem, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 125, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 125, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LinguisticSystem._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'LinguisticSystem')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 125, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LinguisticSystem._Automaton = _BuildAutomaton_6()




MediaTypeOrExtent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'MediaTypeOrExtent'), pyxb.binding.datatypes.string, scope=MediaTypeOrExtent, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 134, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 134, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MediaTypeOrExtent._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'MediaTypeOrExtent')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 134, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MediaTypeOrExtent._Automaton = _BuildAutomaton_7()




ProvenanceStatement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'ProvenanceStatement'), pyxb.binding.datatypes.string, scope=ProvenanceStatement, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 143, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 143, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProvenanceStatement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'ProvenanceStatement')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 143, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProvenanceStatement._Automaton = _BuildAutomaton_8()




RightsStatement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'RightsStatement'), pyxb.binding.datatypes.string, scope=RightsStatement, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 152, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 152, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RightsStatement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'RightsStatement')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 152, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RightsStatement._Automaton = _BuildAutomaton_9()




CatalogRoot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Catalog'), Catalog_, scope=CatalogRoot, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 38, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CatalogRoot._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Catalog')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 52, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CatalogRoot._Automaton = _BuildAutomaton_10()




ConceptScheme._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'ConceptScheme'), CTD_ANON_3, scope=ConceptScheme, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 14, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConceptScheme._UseForTag(pyxb.namespace.ExpandedName(_Namespace_skos, 'ConceptScheme')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 14, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConceptScheme._Automaton = _BuildAutomaton_11()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), PlainLiteral, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_12()




Concept._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'Concept'), CTD_ANON_4, scope=Concept, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 30, 3)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Concept._UseForTag(pyxb.namespace.ExpandedName(_Namespace_skos, 'Concept')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 30, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Concept._Automaton = _BuildAutomaton_13()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'inScheme'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 35, 6)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel'), PlainLiteral, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 48, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 34, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 35, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_skos, 'prefLabel')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(_Namespace_skos, 'inScheme')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 35, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_14()




Identifier._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'Identifier'), CTD_ANON_6, scope=Identifier, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 16, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Identifier._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'Identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 16, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Identifier._Automaton = _BuildAutomaton_15()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_skos, 'notation'), TypedLiteral, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/skos.xsd', 47, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_skos, 'notation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_16()




Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), PlainLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), PlainLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), DateTimeLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), DateTimeLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isPartOf'), pyxb.binding.datatypes.anyURI, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 39, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasPart'), pyxb.binding.datatypes.anyURI, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 40, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), Location, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), RightsStatement, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), PlainLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), Agent_, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), LinguisticSystem, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'dataset'), Dataset, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 45, 3)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'homepage'), Document_, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 47, 3)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'themeTaxonomy'), ConceptScheme, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 52, 3)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'record'), CatalogRecord, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 56, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 47, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 48, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 49, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 50, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 51, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 52, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 54, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 55, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 56, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 57, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 58, 3))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 42, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 43, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 44, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'dataset')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 45, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'homepage')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 47, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'license')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 48, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 49, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 50, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 51, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'themeTaxonomy')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 52, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasPart')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 54, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'isPartOf')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 55, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'record')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 56, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 57, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 58, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Catalog_._Automaton = _BuildAutomaton_17()




CatalogRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'CatalogRecord'), CTD_ANON_7, scope=CatalogRecord, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 65, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CatalogRecord._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'CatalogRecord')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 65, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CatalogRecord._Automaton = _BuildAutomaton_18()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), PlainLiteral, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), PlainLiteral, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), DateTimeLiteral, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), DateTimeLiteral, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'source'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 59, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), LinguisticSystem, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'status'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 28, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 31, 1)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 72, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 73, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 74, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 76, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 79, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 69, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 70, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 72, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'status')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 73, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 74, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 76, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 77, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'source')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 78, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 79, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_19()




Dataset._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Dataset'), CTD_ANON_8, scope=Dataset, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 89, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Dataset._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Dataset')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 89, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Dataset._Automaton = _BuildAutomaton_20()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), PlainLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), PlainLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), DateTimeLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), DateTimeLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'isVersionOf'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 33, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 34, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'relation'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 42, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), Location, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), PeriodOfTime, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accrualPeriodicity'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 51, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance'), ProvenanceStatement, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 55, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'source'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 59, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), RightsStatement, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), Agent_, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), PlainLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), LinguisticSystem, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo'), PlainLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/owl.xsd', 5, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'identifier'), Identifier, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 29, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'sample'), Distribution, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 30, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'versionNotes'), PlainLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 31, 1)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), _ImportedBinding__vcard.Organization, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 97, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), PlainLiteral, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 99, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme'), Concept, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 100, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage'), Resource, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 107, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'distribution'), Distribution, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 118, 6)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), Document_, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 92, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 95, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 96, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 97, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 98, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 99, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 100, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 101, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 102, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 103, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 104, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 105, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 106, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 107, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 108, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 109, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 110, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 111, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 112, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 113, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 114, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 115, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 116, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 117, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 118, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 119, 6))
    counters.add(cc_25)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 92, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 93, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 94, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 95, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 96, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 97, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 98, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 99, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 100, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 101, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 102, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 103, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'accrualPeriodicity')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 104, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 105, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'isVersionOf')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 106, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 107, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 108, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 109, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 110, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'relation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 111, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'source')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 112, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 113, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 114, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 115, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 116, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'versionNotes')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 117, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'distribution')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 118, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'sample')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 119, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, True) ]))
    st_27._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_21()




Distribution._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Distribution'), CTD_ANON_9, scope=Distribution, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 129, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Distribution._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'Distribution')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 129, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Distribution._Automaton = _BuildAutomaton_22()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), PlainLiteral, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), PlainLiteral, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), DateTimeLiteral, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), DateTimeLiteral, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), MediaTypeOrExtent, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), RightsStatement, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), PlainLiteral, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), LinguisticSystem, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_spdx, 'checksum'), _ImportedBinding__spdx.Checksum, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/spdx.xsd', 26, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'status'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 28, 1)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'accessURL'), Resource, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 134, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'downloadURL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 135, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'mediaType'), Concept, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 139, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'byteSize'), pyxb.binding.datatypes.decimal, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 143, 6)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), Document_, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 132, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 133, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 136, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 137, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 138, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 139, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 140, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 141, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 142, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 143, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 144, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 145, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 146, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 147, 6))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 132, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 133, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'accessURL')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 134, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'downloadURL')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 135, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 136, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 137, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'format')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 138, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'mediaType')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 139, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 140, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'license')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 141, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 142, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'byteSize')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 143, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_spdx, 'checksum')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 144, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 145, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 146, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'status')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 147, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_23()




Document_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), pyxb.binding.datatypes.anyURI, scope=Document_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 16, 3)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Document_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 16, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Document_._Automaton = _BuildAutomaton_24()




Agent_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), PlainLiteral, scope=Agent_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

Agent_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'name'), PlainLiteral, scope=Agent_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 34, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 27, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Agent_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'name')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 25, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Agent_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 27, 3))
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
Agent_._Automaton = _BuildAutomaton_25()


mediator._setSubstitutionGroup(audience)

educationLevel._setSubstitutionGroup(audience)

# ./baseline.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:46b196d0e686e7109b81f0bb8e14faa7f15d8d4c
# Generated 2017-08-30 12:29:09.746325 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Namespace http://www.epos-ip.org/terms.html

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
import _owl as _ImportedBinding__owl
import _schema as _ImportedBinding__schema
import _dct as _ImportedBinding__dct
import pyxb.binding.datatypes
import _rdf as _ImportedBinding__rdf
import _vcard as _ImportedBinding__vcard
import _foaf as _ImportedBinding__foaf
import _cnt as _ImportedBinding__cnt
import _http as _ImportedBinding__http
import _adms as _ImportedBinding__adms
import _dcat as _ImportedBinding__dcat
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.epos-ip.org/terms.html', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dct = _ImportedBinding__dct.Namespace
_Namespace_dct.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_adms = _ImportedBinding__adms.Namespace
_Namespace_adms.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_dcat = _ImportedBinding__dcat.Namespace
_Namespace_dcat.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_rdf = _ImportedBinding__rdf.Namespace
_Namespace_rdf.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cnt = _ImportedBinding__cnt.Namespace
_Namespace_cnt.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_owl = _ImportedBinding__owl.Namespace
_Namespace_owl.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_foaf = _ImportedBinding__foaf.Namespace
_Namespace_foaf.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_schema = _ImportedBinding__schema.Namespace
_Namespace_schema.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_http = _ImportedBinding__http.Namespace
_Namespace_http.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_vcard = _ImportedBinding__vcard.Namespace
_Namespace_vcard.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://www.epos-ip.org/terms.html}Catalog with content type ELEMENT_ONLY
class Catalog_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Catalog with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Catalog')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 52, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.epos-ip.org/terms.html}Dataset uses Python identifier Dataset
    __Dataset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dataset'), 'Dataset', '__httpwww_epos_ip_orgterms_html_Catalog__httpwww_epos_ip_orgterms_htmlDataset', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 66, 1), )

    
    Dataset = property(__Dataset.value, __Dataset.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}CatalogRecord uses Python identifier CatalogRecord
    __CatalogRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CatalogRecord'), 'CatalogRecord', '__httpwww_epos_ip_orgterms_html_Catalog__httpwww_epos_ip_orgterms_htmlCatalogRecord', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 102, 1), )

    
    CatalogRecord = property(__CatalogRecord.value, __CatalogRecord.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_Catalog__httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_Catalog__httppurl_orgdctermsdescription', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), 'publisher', '__httpwww_epos_ip_orgterms_html_Catalog__httppurl_orgdctermspublisher', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1), )

    
    publisher = property(__publisher.value, __publisher.set, None, None)

    _ElementMap.update({
        __Dataset.name() : __Dataset,
        __CatalogRecord.name() : __CatalogRecord,
        __title.name() : __title,
        __description.name() : __description,
        __publisher.name() : __publisher
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Catalog_ = Catalog_
Namespace.addCategoryObject('typeBinding', 'Catalog', Catalog_)


# Complex type {http://www.epos-ip.org/terms.html}Dataset with content type ELEMENT_ONLY
class Dataset_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Dataset with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Dataset')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 67, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.epos-ip.org/terms.html}responsibleParty uses Python identifier responsibleParty
    __responsibleParty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty'), 'responsibleParty', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_epos_ip_orgterms_htmlresponsibleParty', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 34, 1), )

    
    responsibleParty = property(__responsibleParty.value, __responsibleParty.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}providedBy uses Python identifier providedBy
    __providedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'providedBy'), 'providedBy', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_epos_ip_orgterms_htmlprovidedBy', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 47, 1), )

    
    providedBy = property(__providedBy.value, __providedBy.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}distribution uses Python identifier distribution
    __distribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'distribution'), 'distribution', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_epos_ip_orgterms_htmldistribution', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 84, 3), )

    
    distribution = property(__distribution.value, __distribution.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'domain'), 'domain', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_epos_ip_orgterms_htmldomain', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 88, 3), )

    
    domain = property(__domain.value, __domain.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}subDomain uses Python identifier subDomain
    __subDomain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subDomain'), 'subDomain', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_epos_ip_orgterms_htmlsubDomain', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 89, 3), )

    
    subDomain = property(__subDomain.value, __subDomain.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}representationTechnique uses Python identifier representationTechnique
    __representationTechnique = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique'), 'representationTechnique', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_w3_orgnsadmsrepresentationTechnique', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 33, 1), )

    
    representationTechnique = property(__representationTechnique.value, __representationTechnique.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_w3_orgnsdcatcontactPoint', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), 'keyword', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_w3_orgnsdcatkeyword', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 31, 1), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}landingPage uses Python identifier landingPage
    __landingPage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage'), 'landingPage', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_w3_orgnsdcatlandingPage', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 32, 1), )

    
    landingPage = property(__landingPage.value, __landingPage.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsdescription', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}created uses Python identifier created
    __created = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), 'created', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermscreated', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1), )

    
    created = property(__created.value, __created.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}conformsTo uses Python identifier conformsTo
    __conformsTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), 'conformsTo', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsconformsTo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1), )

    
    conformsTo = property(__conformsTo.value, __conformsTo.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsspatial', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://purl.org/dc/terms/}temporal uses Python identifier temporal
    __temporal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), 'temporal', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermstemporal', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1), )

    
    temporal = property(__temporal.value, __temporal.set, None, None)

    
    # Element {http://purl.org/dc/terms/}provenance uses Python identifier provenance
    __provenance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance'), 'provenance', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsprovenance', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 55, 1), )

    
    provenance = property(__provenance.value, __provenance.set, None, None)

    
    # Element {http://purl.org/dc/terms/}accessRights uses Python identifier accessRights
    __accessRights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), 'accessRights', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsaccessRights', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1), )

    
    accessRights = property(__accessRights.value, __accessRights.set, None, None)

    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermslanguage', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://purl.org/dc/terms/}subject uses Python identifier subject
    __subject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'subject'), 'subject', '__httpwww_epos_ip_orgterms_html_Dataset__httppurl_orgdctermssubject', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 73, 1), )

    
    subject = property(__subject.value, __subject.set, None, None)

    
    # Element {http://www.w3.org/1999/02/22-rdf-syntax-ns#}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_rdf, 'comment'), 'comment', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_w3_org19990222_rdf_syntax_nscomment', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 60, 1), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {http://www.w3.org/2008/content#}characterEncoding uses Python identifier characterEncoding
    __characterEncoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cnt, 'characterEncoding'), 'characterEncoding', '__httpwww_epos_ip_orgterms_html_Dataset__httpwww_w3_org2008contentcharacterEncoding', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/cnt.xsd', 12, 1), )

    
    characterEncoding = property(__characterEncoding.value, __characterEncoding.set, None, None)

    _ElementMap.update({
        __responsibleParty.name() : __responsibleParty,
        __providedBy.name() : __providedBy,
        __distribution.name() : __distribution,
        __domain.name() : __domain,
        __subDomain.name() : __subDomain,
        __representationTechnique.name() : __representationTechnique,
        __contactPoint.name() : __contactPoint,
        __keyword.name() : __keyword,
        __landingPage.name() : __landingPage,
        __title.name() : __title,
        __description.name() : __description,
        __created.name() : __created,
        __issued.name() : __issued,
        __modified.name() : __modified,
        __conformsTo.name() : __conformsTo,
        __spatial.name() : __spatial,
        __temporal.name() : __temporal,
        __provenance.name() : __provenance,
        __accessRights.name() : __accessRights,
        __type.name() : __type,
        __identifier.name() : __identifier,
        __language.name() : __language,
        __subject.name() : __subject,
        __comment.name() : __comment,
        __characterEncoding.name() : __characterEncoding
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Dataset_ = Dataset_
Namespace.addCategoryObject('typeBinding', 'Dataset', Dataset_)


# Complex type {http://www.epos-ip.org/terms.html}CatalogRecord with content type ELEMENT_ONLY
class CatalogRecord_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}CatalogRecord with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CatalogRecord')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 103, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httpwww_w3_orgnsdcatcontactPoint', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httppurl_orgdctermstitle', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}created uses Python identifier created
    __created = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), 'created', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httppurl_orgdctermscreated', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1), )

    
    created = property(__created.value, __created.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httppurl_orgdctermslanguage', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://www.w3.org/2002/07/owl#}versionInfo uses Python identifier versionInfo
    __versionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo'), 'versionInfo', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httpwww_w3_org200207owlversionInfo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/owl.xsd', 5, 1), )

    
    versionInfo = property(__versionInfo.value, __versionInfo.set, None, None)

    
    # Element {http://www.w3.org/2008/content#}characterEncoding uses Python identifier characterEncoding
    __characterEncoding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_cnt, 'characterEncoding'), 'characterEncoding', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httpwww_w3_org2008contentcharacterEncoding', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/cnt.xsd', 12, 1), )

    
    characterEncoding = property(__characterEncoding.value, __characterEncoding.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}primaryTopic uses Python identifier primaryTopic
    __primaryTopic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), 'primaryTopic', '__httpwww_epos_ip_orgterms_html_CatalogRecord__httpxmlns_comfoaf0_1primaryTopic', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 31, 1), )

    
    primaryTopic = property(__primaryTopic.value, __primaryTopic.set, None, None)

    _ElementMap.update({
        __contactPoint.name() : __contactPoint,
        __title.name() : __title,
        __created.name() : __created,
        __modified.name() : __modified,
        __identifier.name() : __identifier,
        __language.name() : __language,
        __versionInfo.name() : __versionInfo,
        __characterEncoding.name() : __characterEncoding,
        __primaryTopic.name() : __primaryTopic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CatalogRecord_ = CatalogRecord_
Namespace.addCategoryObject('typeBinding', 'CatalogRecord', CatalogRecord_)


# Complex type {http://www.epos-ip.org/terms.html}WebService with content type ELEMENT_ONLY
class WebService_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}WebService with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WebService')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 122, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}documentation uses Python identifier documentation
    __documentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'documentation'), 'documentation', '__httpwww_epos_ip_orgterms_html_WebService__httpschema_orgdocumentation', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 22, 1), )

    
    documentation = property(__documentation.value, __documentation.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publisher'), 'publisher', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_epos_ip_orgterms_htmlpublisher', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 42, 1), )

    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'domain'), 'domain', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_epos_ip_orgterms_htmldomain', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 138, 3), )

    
    domain = property(__domain.value, __domain.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}subDomain uses Python identifier subDomain
    __subDomain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subDomain'), 'subDomain', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_epos_ip_orgterms_htmlsubDomain', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 139, 3), )

    
    subDomain = property(__subDomain.value, __subDomain.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}operation uses Python identifier operation
    __operation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'operation'), 'operation', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_epos_ip_orgterms_htmloperation', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 141, 3), )

    
    operation = property(__operation.value, __operation.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_epos_ip_orgterms_htmlparameter', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 143, 3), )

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Element {http://www.w3.org/ns/adms#}representationTechnique uses Python identifier representationTechnique
    __representationTechnique = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique'), 'representationTechnique', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_w3_orgnsadmsrepresentationTechnique', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 33, 1), )

    
    representationTechnique = property(__representationTechnique.value, __representationTechnique.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_w3_orgnsdcatcontactPoint', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), 'keyword', '__httpwww_epos_ip_orgterms_html_WebService__httpwww_w3_orgnsdcatkeyword', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 31, 1), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermstitle', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsdescription', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}created uses Python identifier created
    __created = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), 'created', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermscreated', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1), )

    
    created = property(__created.value, __created.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}modified uses Python identifier modified
    __modified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), 'modified', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsmodified', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1), )

    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Element {http://purl.org/dc/terms/}format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), 'format', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsformat', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1), )

    
    format = property(__format.value, __format.set, None, None)

    
    # Element {http://purl.org/dc/terms/}hasVersion uses Python identifier hasVersion
    __hasVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion'), 'hasVersion', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermshasVersion', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 34, 1), )

    
    hasVersion = property(__hasVersion.value, __hasVersion.set, None, None)

    
    # Element {http://purl.org/dc/terms/}conformsTo uses Python identifier conformsTo
    __conformsTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), 'conformsTo', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsconformsTo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1), )

    
    conformsTo = property(__conformsTo.value, __conformsTo.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsspatial', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://purl.org/dc/terms/}temporal uses Python identifier temporal
    __temporal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), 'temporal', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermstemporal', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1), )

    
    temporal = property(__temporal.value, __temporal.set, None, None)

    
    # Element {http://purl.org/dc/terms/}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), 'rights', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsrights', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1), )

    
    rights = property(__rights.value, __rights.set, None, None)

    
    # Element {http://purl.org/dc/terms/}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), 'license', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermslicense', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_WebService__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), 'page', '__httpwww_epos_ip_orgterms_html_WebService__httpxmlns_comfoaf0_1page', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1), )

    
    page = property(__page.value, __page.set, None, None)

    _ElementMap.update({
        __documentation.name() : __documentation,
        __publisher.name() : __publisher,
        __domain.name() : __domain,
        __subDomain.name() : __subDomain,
        __operation.name() : __operation,
        __parameter.name() : __parameter,
        __representationTechnique.name() : __representationTechnique,
        __contactPoint.name() : __contactPoint,
        __keyword.name() : __keyword,
        __title.name() : __title,
        __description.name() : __description,
        __created.name() : __created,
        __issued.name() : __issued,
        __modified.name() : __modified,
        __format.name() : __format,
        __hasVersion.name() : __hasVersion,
        __conformsTo.name() : __conformsTo,
        __spatial.name() : __spatial,
        __temporal.name() : __temporal,
        __rights.name() : __rights,
        __license.name() : __license,
        __identifier.name() : __identifier,
        __page.name() : __page
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.WebService_ = WebService_
Namespace.addCategoryObject('typeBinding', 'WebService', WebService_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 144, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}minValue uses Python identifier minValue
    __minValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'minValue'), 'minValue', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httpschema_orgminValue', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 20, 1), )

    
    minValue = property(__minValue.value, __minValue.set, None, None)

    
    # Element {http://schema.org/}maxValue uses Python identifier maxValue
    __maxValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'maxValue'), 'maxValue', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httpschema_orgmaxValue', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 21, 1), )

    
    maxValue = property(__maxValue.value, __maxValue.set, None, None)

    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.w3.org/1999/02/22-rdf-syntax-ns#}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_rdf, 'label'), 'label', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httpwww_w3_org19990222_rdf_syntax_nslabel', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 61, 1), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element {http://www.w3.org/2002/07/owl#}versionInfo uses Python identifier versionInfo
    __versionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo'), 'versionInfo', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httpwww_w3_org200207owlversionInfo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/owl.xsd', 5, 1), )

    
    versionInfo = property(__versionInfo.value, __versionInfo.set, None, None)

    
    # Element {http://www.w3.org/2006/http#}paramName uses Python identifier paramName
    __paramName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_http, 'paramName'), 'paramName', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httpwww_w3_org2006httpparamName', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/http.xsd', 12, 1), )

    
    paramName = property(__paramName.value, __paramName.set, None, None)

    
    # Element {http://www.w3.org/2006/http#}paramValue uses Python identifier paramValue
    __paramValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_http, 'paramValue'), 'paramValue', '__httpwww_epos_ip_orgterms_html_CTD_ANON_httpwww_w3_org2006httpparamValue', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/http.xsd', 13, 1), )

    
    paramValue = property(__paramValue.value, __paramValue.set, None, None)

    _ElementMap.update({
        __minValue.name() : __minValue,
        __maxValue.name() : __maxValue,
        __type.name() : __type,
        __label.name() : __label,
        __versionInfo.name() : __versionInfo,
        __paramName.name() : __paramName,
        __paramValue.name() : __paramValue
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.epos-ip.org/terms.html}Publication with content type ELEMENT_ONLY
class Publication_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Publication with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Publication')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 168, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}issueNumber uses Python identifier issueNumber
    __issueNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'issueNumber'), 'issueNumber', '__httpwww_epos_ip_orgterms_html_Publication__httpschema_orgissueNumber', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 8, 1), )

    
    issueNumber = property(__issueNumber.value, __issueNumber.set, None, None)

    
    # Element {http://schema.org/}volumeNumber uses Python identifier volumeNumber
    __volumeNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'volumeNumber'), 'volumeNumber', '__httpwww_epos_ip_orgterms_html_Publication__httpschema_orgvolumeNumber', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 9, 1), )

    
    volumeNumber = property(__volumeNumber.value, __volumeNumber.set, None, None)

    
    # Element {http://schema.org/}numberOfPages uses Python identifier numberOfPages
    __numberOfPages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'numberOfPages'), 'numberOfPages', '__httpwww_epos_ip_orgterms_html_Publication__httpschema_orgnumberOfPages', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 10, 1), )

    
    numberOfPages = property(__numberOfPages.value, __numberOfPages.set, None, None)

    
    # Element {http://schema.org/}issn uses Python identifier issn
    __issn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'issn'), 'issn', '__httpwww_epos_ip_orgterms_html_Publication__httpschema_orgissn', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 11, 1), )

    
    issn = property(__issn.value, __issn.set, None, None)

    
    # Element {http://schema.org/}keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'keywords'), 'keywords', '__httpwww_epos_ip_orgterms_html_Publication__httpschema_orgkeywords', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 12, 1), )

    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}authors uses Python identifier authors
    __authors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authors'), 'authors', '__httpwww_epos_ip_orgterms_html_Publication__httpwww_epos_ip_orgterms_htmlauthors', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 41, 1), )

    
    authors = property(__authors.value, __authors.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publisher'), 'publisher', '__httpwww_epos_ip_orgterms_html_Publication__httpwww_epos_ip_orgterms_htmlpublisher', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 42, 1), )

    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}contributors uses Python identifier contributors
    __contributors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contributors'), 'contributors', '__httpwww_epos_ip_orgterms_html_Publication__httpwww_epos_ip_orgterms_htmlcontributors', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 43, 1), )

    
    contributors = property(__contributors.value, __contributors.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_Publication__httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}abstract uses Python identifier abstract
    __abstract = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract'), 'abstract', '__httpwww_epos_ip_orgterms_html_Publication__httppurl_orgdctermsabstract', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 19, 1), )

    
    abstract = property(__abstract.value, __abstract.set, None, None)

    
    # Element {http://purl.org/dc/terms/}issued uses Python identifier issued
    __issued = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), 'issued', '__httpwww_epos_ip_orgterms_html_Publication__httppurl_orgdctermsissued', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1), )

    
    issued = property(__issued.value, __issued.set, None, None)

    
    # Element {http://purl.org/dc/terms/}format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), 'format', '__httpwww_epos_ip_orgterms_html_Publication__httppurl_orgdctermsformat', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1), )

    
    format = property(__format.value, __format.set, None, None)

    
    # Element {http://purl.org/dc/terms/}accessRights uses Python identifier accessRights
    __accessRights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), 'accessRights', '__httpwww_epos_ip_orgterms_html_Publication__httppurl_orgdctermsaccessRights', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1), )

    
    accessRights = property(__accessRights.value, __accessRights.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Publication__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __issueNumber.name() : __issueNumber,
        __volumeNumber.name() : __volumeNumber,
        __numberOfPages.name() : __numberOfPages,
        __issn.name() : __issn,
        __keywords.name() : __keywords,
        __authors.name() : __authors,
        __publisher.name() : __publisher,
        __contributors.name() : __contributors,
        __title.name() : __title,
        __abstract.name() : __abstract,
        __issued.name() : __issued,
        __format.name() : __format,
        __accessRights.name() : __accessRights,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Publication_ = Publication_
Namespace.addCategoryObject('typeBinding', 'Publication', Publication_)


# Complex type {http://www.epos-ip.org/terms.html}Equipment with content type ELEMENT_ONLY
class Equipment_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Equipment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Equipment')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 190, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}serialNumber uses Python identifier serialNumber
    __serialNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'serialNumber'), 'serialNumber', '__httpwww_epos_ip_orgterms_html_Equipment__httpschema_orgserialNumber', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 13, 1), )

    
    serialNumber = property(__serialNumber.value, __serialNumber.set, None, None)

    
    # Element {http://schema.org/}numberOfItems uses Python identifier numberOfItems
    __numberOfItems = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'numberOfItems'), 'numberOfItems', '__httpwww_epos_ip_orgterms_html_Equipment__httpschema_orgnumberOfItems', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 14, 1), )

    
    numberOfItems = property(__numberOfItems.value, __numberOfItems.set, None, None)

    
    # Element {http://schema.org/}manufacturer uses Python identifier manufacturer
    __manufacturer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'manufacturer'), 'manufacturer', '__httpwww_epos_ip_orgterms_html_Equipment__httpschema_orgmanufacturer', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 15, 1), )

    
    manufacturer = property(__manufacturer.value, __manufacturer.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}isPartOf uses Python identifier isPartOf
    __isPartOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isPartOf'), 'isPartOf', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlisPartOf', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 39, 1), )

    
    isPartOf = property(__isPartOf.value, __isPartOf.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'owner'), 'owner', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlowner', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 45, 1), )

    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}relatedTo uses Python identifier relatedTo
    __relatedTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedTo'), 'relatedTo', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlrelatedTo', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 46, 1), )

    
    relatedTo = property(__relatedTo.value, __relatedTo.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orientation'), 'orientation', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlorientation', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 205, 3), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}dynamicRange uses Python identifier dynamicRange
    __dynamicRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dynamicRange'), 'dynamicRange', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmldynamicRange', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 206, 3), )

    
    dynamicRange = property(__dynamicRange.value, __dynamicRange.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}resolution uses Python identifier resolution
    __resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'resolution'), 'resolution', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlresolution', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 214, 3), )

    
    resolution = property(__resolution.value, __resolution.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}samplePeriod uses Python identifier samplePeriod
    __samplePeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'samplePeriod'), 'samplePeriod', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlsamplePeriod', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 215, 3), )

    
    samplePeriod = property(__samplePeriod.value, __samplePeriod.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_epos_ip_orgterms_htmlfilter', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 223, 3), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_epos_ip_orgterms_html_Equipment__httpwww_w3_orgnsdcatcontactPoint', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_Equipment__httppurl_orgdctermstitle', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_Equipment__httppurl_orgdctermsdescription', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_epos_ip_orgterms_html_Equipment__httppurl_orgdctermsspatial', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://purl.org/dc/terms/}temporal uses Python identifier temporal
    __temporal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), 'temporal', '__httpwww_epos_ip_orgterms_html_Equipment__httppurl_orgdctermstemporal', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1), )

    
    temporal = property(__temporal.value, __temporal.set, None, None)

    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpwww_epos_ip_orgterms_html_Equipment__httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Equipment__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __serialNumber.name() : __serialNumber,
        __numberOfItems.name() : __numberOfItems,
        __manufacturer.name() : __manufacturer,
        __isPartOf.name() : __isPartOf,
        __owner.name() : __owner,
        __relatedTo.name() : __relatedTo,
        __orientation.name() : __orientation,
        __dynamicRange.name() : __dynamicRange,
        __resolution.name() : __resolution,
        __samplePeriod.name() : __samplePeriod,
        __filter.name() : __filter,
        __contactPoint.name() : __contactPoint,
        __title.name() : __title,
        __description.name() : __description,
        __spatial.name() : __spatial,
        __temporal.name() : __temporal,
        __type.name() : __type,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Equipment_ = Equipment_
Namespace.addCategoryObject('typeBinding', 'Equipment', Equipment_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 207, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}unitText uses Python identifier unitText
    __unitText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'unitText'), 'unitText', '__httpwww_epos_ip_orgterms_html_CTD_ANON__httpschema_orgunitText', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 16, 1), )

    
    unitText = property(__unitText.value, __unitText.set, None, None)

    
    # Element {http://schema.org/}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'value'), 'value_', '__httpwww_epos_ip_orgterms_html_CTD_ANON__httpschema_orgvalue', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 17, 1), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __unitText.name() : __unitText,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 216, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}unitText uses Python identifier unitText
    __unitText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'unitText'), 'unitText', '__httpwww_epos_ip_orgterms_html_CTD_ANON_2_httpschema_orgunitText', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 16, 1), )

    
    unitText = property(__unitText.value, __unitText.set, None, None)

    
    # Element {http://schema.org/}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'value'), 'value_', '__httpwww_epos_ip_orgterms_html_CTD_ANON_2_httpschema_orgvalue', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 17, 1), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __unitText.name() : __unitText,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.epos-ip.org/terms.html}Facility with content type ELEMENT_ONLY
class Facility_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Facility with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Facility')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 230, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.epos-ip.org/terms.html}facilityManager uses Python identifier facilityManager
    __facilityManager = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facilityManager'), 'facilityManager', '__httpwww_epos_ip_orgterms_html_Facility__httpwww_epos_ip_orgterms_htmlfacilityManager', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 44, 1), )

    
    facilityManager = property(__facilityManager.value, __facilityManager.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'owner'), 'owner', '__httpwww_epos_ip_orgterms_html_Facility__httpwww_epos_ip_orgterms_htmlowner', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 45, 1), )

    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}theme uses Python identifier theme
    __theme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme'), 'theme', '__httpwww_epos_ip_orgterms_html_Facility__httpwww_w3_orgnsdcattheme', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 29, 1), )

    
    theme = property(__theme.value, __theme.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_epos_ip_orgterms_html_Facility__httpwww_w3_orgnsdcatcontactPoint', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_Facility__httppurl_orgdctermstitle', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_Facility__httppurl_orgdctermsdescription', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpwww_epos_ip_orgterms_html_Facility__httppurl_orgdctermstype', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Facility__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasAddress uses Python identifier hasAddress
    __hasAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress'), 'hasAddress', '__httpwww_epos_ip_orgterms_html_Facility__httpwww_w3_org2006vcardnshasAddress', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1), )

    
    hasAddress = property(__hasAddress.value, __hasAddress.set, None, None)

    
    # Element {http://xmlns.com/foaf/0.1/}page uses Python identifier page
    __page = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), 'page', '__httpwww_epos_ip_orgterms_html_Facility__httpxmlns_comfoaf0_1page', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1), )

    
    page = property(__page.value, __page.set, None, None)

    _ElementMap.update({
        __facilityManager.name() : __facilityManager,
        __owner.name() : __owner,
        __theme.name() : __theme,
        __contactPoint.name() : __contactPoint,
        __title.name() : __title,
        __description.name() : __description,
        __type.name() : __type,
        __identifier.name() : __identifier,
        __hasAddress.name() : __hasAddress,
        __page.name() : __page
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Facility_ = Facility_
Namespace.addCategoryObject('typeBinding', 'Facility', Facility_)


# Complex type {http://www.epos-ip.org/terms.html}Project with content type ELEMENT_ONLY
class Project_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Project with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Project')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 248, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://purl.org/dc/terms/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), 'title', '__httpwww_epos_ip_orgterms_html_Project__httppurl_orgdctermstitle', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_Project__httppurl_orgdctermsdescription', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Project__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Project_ = Project_
Namespace.addCategoryObject('typeBinding', 'Project', Project_)


# Complex type {http://www.epos-ip.org/terms.html}Organisation with content type ELEMENT_ONLY
class Organisation_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Organisation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Organisation')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 260, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.epos-ip.org/terms.html}legalContact uses Python identifier legalContact
    __legalContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalContact'), 'legalContact', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_epos_ip_orgterms_htmllegalContact', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 36, 1), )

    
    legalContact = property(__legalContact.value, __legalContact.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}financialContact uses Python identifier financialContact
    __financialContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'financialContact'), 'financialContact', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_epos_ip_orgterms_htmlfinancialContact', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 37, 1), )

    
    financialContact = property(__financialContact.value, __financialContact.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}scientificContact uses Python identifier scientificContact
    __scientificContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scientificContact'), 'scientificContact', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_epos_ip_orgterms_htmlscientificContact', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 38, 1), )

    
    scientificContact = property(__scientificContact.value, __scientificContact.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}isPartOf uses Python identifier isPartOf
    __isPartOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isPartOf'), 'isPartOf', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_epos_ip_orgterms_htmlisPartOf', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 39, 1), )

    
    isPartOf = property(__isPartOf.value, __isPartOf.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}associatedProjects uses Python identifier associatedProjects
    __associatedProjects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'associatedProjects'), 'associatedProjects', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_epos_ip_orgterms_htmlassociatedProjects', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 40, 1), )

    
    associatedProjects = property(__associatedProjects.value, __associatedProjects.set, None, None)

    
    # Element {http://purl.org/dc/terms/}spatial uses Python identifier spatial
    __spatial = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), 'spatial', '__httpwww_epos_ip_orgterms_html_Organisation__httppurl_orgdctermsspatial', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1), )

    
    spatial = property(__spatial.value, __spatial.set, None, None)

    
    # Element {http://purl.org/dc/terms/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), 'type', '__httpwww_epos_ip_orgterms_html_Organisation__httppurl_orgdctermstype', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Organisation__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasAddress uses Python identifier hasAddress
    __hasAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress'), 'hasAddress', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnshasAddress', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1), )

    
    hasAddress = property(__hasAddress.value, __hasAddress.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}fn uses Python identifier fn
    __fn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'fn'), 'fn', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnsfn', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 53, 1), )

    
    fn = property(__fn.value, __fn.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasEmail uses Python identifier hasEmail
    __hasEmail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasEmail'), 'hasEmail', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnshasEmail', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 54, 1), )

    
    hasEmail = property(__hasEmail.value, __hasEmail.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasURL uses Python identifier hasURL
    __hasURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasURL'), 'hasURL', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnshasURL', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 55, 1), )

    
    hasURL = property(__hasURL.value, __hasURL.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasTelephone uses Python identifier hasTelephone
    __hasTelephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasTelephone'), 'hasTelephone', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnshasTelephone', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 56, 1), )

    
    hasTelephone = property(__hasTelephone.value, __hasTelephone.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasLogo uses Python identifier hasLogo
    __hasLogo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasLogo'), 'hasLogo', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnshasLogo', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 57, 1), )

    
    hasLogo = property(__hasLogo.value, __hasLogo.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}organization-name uses Python identifier organization_name
    __organization_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'organization-name'), 'organization_name', '__httpwww_epos_ip_orgterms_html_Organisation__httpwww_w3_org2006vcardnsorganization_name', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 59, 1), )

    
    organization_name = property(__organization_name.value, __organization_name.set, None, None)

    _ElementMap.update({
        __legalContact.name() : __legalContact,
        __financialContact.name() : __financialContact,
        __scientificContact.name() : __scientificContact,
        __isPartOf.name() : __isPartOf,
        __associatedProjects.name() : __associatedProjects,
        __spatial.name() : __spatial,
        __type.name() : __type,
        __identifier.name() : __identifier,
        __hasAddress.name() : __hasAddress,
        __fn.name() : __fn,
        __hasEmail.name() : __hasEmail,
        __hasURL.name() : __hasURL,
        __hasTelephone.name() : __hasTelephone,
        __hasLogo.name() : __hasLogo,
        __organization_name.name() : __organization_name
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Organisation_ = Organisation_
Namespace.addCategoryObject('typeBinding', 'Organisation', Organisation_)


# Complex type {http://www.epos-ip.org/terms.html}Person with content type ELEMENT_ONLY
class Person_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Person with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Person')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 285, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}qualifications uses Python identifier qualifications
    __qualifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'qualifications'), 'qualifications', '__httpwww_epos_ip_orgterms_html_Person__httpschema_orgqualifications', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 7, 1), )

    
    qualifications = property(__qualifications.value, __qualifications.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}affiliation uses Python identifier affiliation
    __affiliation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'affiliation'), 'affiliation', '__httpwww_epos_ip_orgterms_html_Person__httpwww_epos_ip_orgterms_htmlaffiliation', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 35, 1), )

    
    affiliation = property(__affiliation.value, __affiliation.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Person__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://purl.org/dc/terms/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), 'language', '__httpwww_epos_ip_orgterms_html_Person__httppurl_orgdctermslanguage', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasAddress uses Python identifier hasAddress
    __hasAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress'), 'hasAddress', '__httpwww_epos_ip_orgterms_html_Person__httpwww_w3_org2006vcardnshasAddress', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1), )

    
    hasAddress = property(__hasAddress.value, __hasAddress.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}fn uses Python identifier fn
    __fn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'fn'), 'fn', '__httpwww_epos_ip_orgterms_html_Person__httpwww_w3_org2006vcardnsfn', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 53, 1), )

    
    fn = property(__fn.value, __fn.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasEmail uses Python identifier hasEmail
    __hasEmail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasEmail'), 'hasEmail', '__httpwww_epos_ip_orgterms_html_Person__httpwww_w3_org2006vcardnshasEmail', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 54, 1), )

    
    hasEmail = property(__hasEmail.value, __hasEmail.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasURL uses Python identifier hasURL
    __hasURL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasURL'), 'hasURL', '__httpwww_epos_ip_orgterms_html_Person__httpwww_w3_org2006vcardnshasURL', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 55, 1), )

    
    hasURL = property(__hasURL.value, __hasURL.set, None, None)

    
    # Element {http://www.w3.org/2006/vcard/ns#}hasTelephone uses Python identifier hasTelephone
    __hasTelephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasTelephone'), 'hasTelephone', '__httpwww_epos_ip_orgterms_html_Person__httpwww_w3_org2006vcardnshasTelephone', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 56, 1), )

    
    hasTelephone = property(__hasTelephone.value, __hasTelephone.set, None, None)

    _ElementMap.update({
        __qualifications.name() : __qualifications,
        __affiliation.name() : __affiliation,
        __identifier.name() : __identifier,
        __language.name() : __language,
        __hasAddress.name() : __hasAddress,
        __fn.name() : __fn,
        __hasEmail.name() : __hasEmail,
        __hasURL.name() : __hasURL,
        __hasTelephone.name() : __hasTelephone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Person_ = Person_
Namespace.addCategoryObject('typeBinding', 'Person', Person_)


# Complex type {http://www.epos-ip.org/terms.html}Service with content type ELEMENT_ONLY
class Service_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Service with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Service')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 305, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schema.org/}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'name'), 'name', '__httpwww_epos_ip_orgterms_html_Service__httpschema_orgname', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 18, 1), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://schema.org/}serviceType uses Python identifier serviceType
    __serviceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_schema, 'serviceType'), 'serviceType', '__httpwww_epos_ip_orgterms_html_Service__httpschema_orgserviceType', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 19, 1), )

    
    serviceType = property(__serviceType.value, __serviceType.set, None, None)

    
    # Element {http://www.w3.org/ns/dcat#}contactPoint uses Python identifier contactPoint
    __contactPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), 'contactPoint', '__httpwww_epos_ip_orgterms_html_Service__httpwww_w3_orgnsdcatcontactPoint', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1), )

    
    contactPoint = property(__contactPoint.value, __contactPoint.set, None, None)

    
    # Element {http://purl.org/dc/terms/}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), 'description', '__httpwww_epos_ip_orgterms_html_Service__httppurl_orgdctermsdescription', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://purl.org/dc/terms/}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), 'license', '__httpwww_epos_ip_orgterms_html_Service__httppurl_orgdctermslicense', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1), )

    
    license = property(__license.value, __license.set, None, None)

    
    # Element {http://purl.org/dc/terms/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), 'identifier', '__httpwww_epos_ip_orgterms_html_Service__httppurl_orgdctermsidentifier', False, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __serviceType.name() : __serviceType,
        __contactPoint.name() : __contactPoint,
        __description.name() : __description,
        __license.name() : __license,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Service_ = Service_
Namespace.addCategoryObject('typeBinding', 'Service', Service_)


# Complex type {http://www.epos-ip.org/terms.html}Epos with content type ELEMENT_ONLY
class Epos_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.epos-ip.org/terms.html}Epos with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Epos')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 355, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.epos-ip.org/terms.html}Catalog uses Python identifier Catalog
    __Catalog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Catalog'), 'Catalog', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlCatalog', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 51, 1), )

    
    Catalog = property(__Catalog.value, __Catalog.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}WebService uses Python identifier WebService
    __WebService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WebService'), 'WebService', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlWebService', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 121, 1), )

    
    WebService = property(__WebService.value, __WebService.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Publication uses Python identifier Publication
    __Publication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Publication'), 'Publication', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlPublication', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 167, 1), )

    
    Publication = property(__Publication.value, __Publication.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Equipment uses Python identifier Equipment
    __Equipment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Equipment'), 'Equipment', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlEquipment', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 189, 1), )

    
    Equipment = property(__Equipment.value, __Equipment.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Facility uses Python identifier Facility
    __Facility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Facility'), 'Facility', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlFacility', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 229, 1), )

    
    Facility = property(__Facility.value, __Facility.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Project uses Python identifier Project
    __Project = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Project'), 'Project', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlProject', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 247, 1), )

    
    Project = property(__Project.value, __Project.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Organisation uses Python identifier Organisation
    __Organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), 'Organisation', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlOrganisation', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 259, 1), )

    
    Organisation = property(__Organisation.value, __Organisation.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Person uses Python identifier Person
    __Person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Person'), 'Person', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlPerson', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 284, 1), )

    
    Person = property(__Person.value, __Person.set, None, None)

    
    # Element {http://www.epos-ip.org/terms.html}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Service'), 'Service', '__httpwww_epos_ip_orgterms_html_Epos__httpwww_epos_ip_orgterms_htmlService', True, pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 304, 1), )

    
    Service = property(__Service.value, __Service.set, None, None)

    _ElementMap.update({
        __Catalog.name() : __Catalog,
        __WebService.name() : __WebService,
        __Publication.name() : __Publication,
        __Equipment.name() : __Equipment,
        __Facility.name() : __Facility,
        __Project.name() : __Project,
        __Organisation.name() : __Organisation,
        __Person.name() : __Person,
        __Service.name() : __Service
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Epos_ = Epos_
Namespace.addCategoryObject('typeBinding', 'Epos', Epos_)


responsibleParty = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 34, 1))
Namespace.addCategoryObject('elementBinding', responsibleParty.name().localName(), responsibleParty)

affiliation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'affiliation'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 35, 1))
Namespace.addCategoryObject('elementBinding', affiliation.name().localName(), affiliation)

legalContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalContact'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', legalContact.name().localName(), legalContact)

financialContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'financialContact'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 37, 1))
Namespace.addCategoryObject('elementBinding', financialContact.name().localName(), financialContact)

scientificContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scientificContact'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', scientificContact.name().localName(), scientificContact)

isPartOf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isPartOf'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', isPartOf.name().localName(), isPartOf)

associatedProjects = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'associatedProjects'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', associatedProjects.name().localName(), associatedProjects)

authors = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authors'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', authors.name().localName(), authors)

publisher = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publisher'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 42, 1))
Namespace.addCategoryObject('elementBinding', publisher.name().localName(), publisher)

contributors = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contributors'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 43, 1))
Namespace.addCategoryObject('elementBinding', contributors.name().localName(), contributors)

facilityManager = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facilityManager'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', facilityManager.name().localName(), facilityManager)

owner = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 45, 1))
Namespace.addCategoryObject('elementBinding', owner.name().localName(), owner)

relatedTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedTo'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 46, 1))
Namespace.addCategoryObject('elementBinding', relatedTo.name().localName(), relatedTo)

providedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'providedBy'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 47, 1))
Namespace.addCategoryObject('elementBinding', providedBy.name().localName(), providedBy)

Catalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Catalog'), Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', Catalog.name().localName(), Catalog)

Dataset = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dataset'), Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 66, 1))
Namespace.addCategoryObject('elementBinding', Dataset.name().localName(), Dataset)

CatalogRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CatalogRecord'), CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 102, 1))
Namespace.addCategoryObject('elementBinding', CatalogRecord.name().localName(), CatalogRecord)

WebService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WebService'), WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 121, 1))
Namespace.addCategoryObject('elementBinding', WebService.name().localName(), WebService)

Publication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Publication'), Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 167, 1))
Namespace.addCategoryObject('elementBinding', Publication.name().localName(), Publication)

Equipment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Equipment'), Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 189, 1))
Namespace.addCategoryObject('elementBinding', Equipment.name().localName(), Equipment)

Facility = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Facility'), Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 229, 1))
Namespace.addCategoryObject('elementBinding', Facility.name().localName(), Facility)

Project = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Project'), Project_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 247, 1))
Namespace.addCategoryObject('elementBinding', Project.name().localName(), Project)

Organisation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 259, 1))
Namespace.addCategoryObject('elementBinding', Organisation.name().localName(), Organisation)

Person = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 284, 1))
Namespace.addCategoryObject('elementBinding', Person.name().localName(), Person)

Service = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Service'), Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 304, 1))
Namespace.addCategoryObject('elementBinding', Service.name().localName(), Service)

Epos = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Epos'), Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 354, 1))
Namespace.addCategoryObject('elementBinding', Epos.name().localName(), Epos)



Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dataset'), Dataset_, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 66, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CatalogRecord'), CatalogRecord_, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 102, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Catalog_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher'), _ImportedBinding__nsgroup.Agent_, scope=Catalog_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 67, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'publisher')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dataset')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 60, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Catalog_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CatalogRecord')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 61, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Catalog_._Automaton = _BuildAutomaton()




Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty'), pyxb.binding.datatypes.anyURI, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 34, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'providedBy'), pyxb.binding.datatypes.anyURI, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 47, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'distribution'), _ImportedBinding__nsgroup.Distribution, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 84, 3)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'domain'), pyxb.binding.datatypes.string, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 88, 3)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subDomain'), pyxb.binding.datatypes.string, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 89, 3)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 33, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 31, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage'), _ImportedBinding__nsgroup.Document_, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 32, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.binding.datatypes.anyURI, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), _ImportedBinding__nsgroup.Location, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), _ImportedBinding__nsgroup.PeriodOfTime, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance'), _ImportedBinding__nsgroup.ProvenanceStatement, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 55, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), _ImportedBinding__nsgroup.RightsStatement, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), _ImportedBinding__nsgroup.LinguisticSystem, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'subject'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 73, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rdf, 'comment'), pyxb.binding.datatypes.string, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 60, 1)))

Dataset_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cnt, 'characterEncoding'), _ImportedBinding__nsgroup.PlainLiteral, scope=Dataset_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/cnt.xsd', 12, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 78, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 79, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 80, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 81, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 82, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 83, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 95, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 96, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 97, 3))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 70, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 71, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 72, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 73, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 74, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 75, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'provenance')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 76, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 77, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 78, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 79, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 80, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'landingPage')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 81, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 82, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 83, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'distribution')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 84, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'domain')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 88, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subDomain')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 89, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'created')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 90, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'subject')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 91, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cnt, 'characterEncoding')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 92, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 93, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responsibleParty')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 94, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_rdf, 'comment')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 95, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 96, 3))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Dataset_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'providedBy')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 97, 3))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    transitions = []
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
    transitions.append(fac.Transition(st_2, [
         ]))
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
    transitions.append(fac.Transition(st_5, [
         ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_24._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Dataset_._Automaton = _BuildAutomaton_()




CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), _ImportedBinding__nsgroup.LinguisticSystem, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo'), _ImportedBinding__nsgroup.PlainLiteral, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/owl.xsd', 5, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cnt, 'characterEncoding'), _ImportedBinding__nsgroup.PlainLiteral, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/cnt.xsd', 12, 1)))

CatalogRecord_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic'), pyxb.binding.datatypes.anyURI, scope=CatalogRecord_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 31, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 109, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 113, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'primaryTopic')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 106, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 107, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 108, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 109, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 112, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 113, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cnt, 'characterEncoding')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 114, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 115, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CatalogRecord_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'created')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 116, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CatalogRecord_._Automaton = _BuildAutomaton_2()




WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'documentation'), pyxb.binding.datatypes.anyURI, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 22, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publisher'), pyxb.binding.datatypes.anyURI, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 42, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'domain'), pyxb.binding.datatypes.string, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 138, 3)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subDomain'), pyxb.binding.datatypes.string, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 139, 3)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'operation'), pyxb.binding.datatypes.string, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 141, 3)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), CTD_ANON, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 143, 3)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique'), _ImportedBinding__nsgroup.PlainLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/adms.xsd', 33, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword'), _ImportedBinding__nsgroup.PlainLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 31, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'created'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 21, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 25, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), _ImportedBinding__nsgroup.MediaTypeOrExtent, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion'), pyxb.binding.datatypes.anyURI, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 34, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo'), pyxb.binding.datatypes.anyURI, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 46, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), _ImportedBinding__nsgroup.Location, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), _ImportedBinding__nsgroup.PeriodOfTime, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights'), _ImportedBinding__nsgroup.RightsStatement, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 57, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), _ImportedBinding__nsgroup.PlainLiteral, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

WebService_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), _ImportedBinding__nsgroup.Document_, scope=WebService_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 129, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 132, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 133, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 140, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 142, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 143, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 156, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 159, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 160, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 161, 3))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 125, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 126, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 127, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'modified')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 128, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'license')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 129, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 130, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'format')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 131, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'rights')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 132, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'conformsTo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 133, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 136, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'created')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 137, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'domain')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 138, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subDomain')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 139, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'keyword')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 140, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'operation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 141, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'hasVersion')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 142, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 143, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'documentation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 156, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 157, 3))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publisher')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 158, 3))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 159, 3))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_adms, 'representationTechnique')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 160, 3))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WebService_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 161, 3))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WebService_._Automaton = _BuildAutomaton_3()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'minValue'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 20, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'maxValue'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 21, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rdf, 'label'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/rdf.xsd', 61, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/owl.xsd', 5, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_http, 'paramName'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/http.xsd', 12, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_http, 'paramValue'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/http.xsd', 13, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 149, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 150, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 151, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 152, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_http, 'paramName')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 146, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_rdf, 'label')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 147, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 148, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_http, 'paramValue')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 149, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'minValue')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 150, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'maxValue')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 151, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_owl, 'versionInfo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 152, 6))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_4()




Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'issueNumber'), _ImportedBinding__nsgroup.PlainLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 8, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'volumeNumber'), _ImportedBinding__nsgroup.PlainLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 9, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'numberOfPages'), pyxb.binding.datatypes.integer, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 10, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'issn'), _ImportedBinding__nsgroup.PlainLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 11, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'keywords'), _ImportedBinding__nsgroup.PlainLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 12, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authors'), pyxb.binding.datatypes.anyURI, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 41, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publisher'), pyxb.binding.datatypes.anyURI, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 42, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contributors'), pyxb.binding.datatypes.anyURI, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 43, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract'), _ImportedBinding__nsgroup.PlainLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 19, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued'), _ImportedBinding__nsgroup.DateTimeLiteral, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 24, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'format'), _ImportedBinding__nsgroup.MediaTypeOrExtent, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 30, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights'), _ImportedBinding__nsgroup.RightsStatement, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 63, 1)))

Publication_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Publication_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 175, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 177, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 178, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 179, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 180, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 181, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 182, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 183, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 184, 3))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 171, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 172, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authors')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 173, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publisher')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 174, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'abstract')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 175, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'issued')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 176, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'issn')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 177, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'issueNumber')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 178, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'volumeNumber')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 179, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'numberOfPages')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 180, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'keywords')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 181, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contributors')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 182, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'accessRights')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 183, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Publication_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'format')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 184, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Publication_._Automaton = _BuildAutomaton_5()




Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'serialNumber'), _ImportedBinding__nsgroup.PlainLiteral, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 13, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'numberOfItems'), pyxb.binding.datatypes.integer, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 14, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'manufacturer'), _ImportedBinding__nsgroup.PlainLiteral, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 15, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isPartOf'), pyxb.binding.datatypes.anyURI, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 39, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), pyxb.binding.datatypes.anyURI, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 45, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedTo'), pyxb.binding.datatypes.anyURI, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 46, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.string, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 205, 3)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dynamicRange'), CTD_ANON_, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 206, 3)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'resolution'), pyxb.binding.datatypes.double, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 214, 3)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'samplePeriod'), CTD_ANON_2, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 215, 3)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), pyxb.binding.datatypes.string, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 223, 3)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), _ImportedBinding__nsgroup.Location, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal'), _ImportedBinding__nsgroup.PeriodOfTime, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 48, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), _ImportedBinding__nsgroup.PlainLiteral, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

Equipment_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Equipment_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 194, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 204, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 205, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 206, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 214, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 215, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 223, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 224, 3))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 193, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'serialNumber')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 194, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 195, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'numberOfItems')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 196, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'manufacturer')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 197, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 198, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 199, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedTo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 200, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isPartOf')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 201, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 202, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 203, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'temporal')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 204, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orientation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 205, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dynamicRange')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 206, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'resolution')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 214, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'samplePeriod')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 215, 3))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 223, 3))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Equipment_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 224, 3))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Equipment_._Automaton = _BuildAutomaton_6()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'unitText'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 16, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'value'), pyxb.binding.datatypes.double, scope=CTD_ANON_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 17, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'unitText')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 209, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'value')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 210, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_7()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'unitText'), _ImportedBinding__nsgroup.PlainLiteral, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 16, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'value'), pyxb.binding.datatypes.double, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 17, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'unitText')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 218, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'value')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 219, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_8()




Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facilityManager'), pyxb.binding.datatypes.anyURI, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 44, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), pyxb.binding.datatypes.anyURI, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 45, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme'), _ImportedBinding__nsgroup.PlainLiteral, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 29, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), _ImportedBinding__nsgroup.PlainLiteral, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress'), _ImportedBinding__vcard.Address, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1)))

Facility_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page'), _ImportedBinding__nsgroup.Document_, scope=Facility_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/foaf.xsd', 32, 1)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 241, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 242, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 233, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 234, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 235, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 236, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 237, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 238, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facilityManager')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 239, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 240, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_foaf, 'page')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 241, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Facility_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'theme')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 242, 3))
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Facility_._Automaton = _BuildAutomaton_9()




Project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'title'), _ImportedBinding__nsgroup.PlainLiteral, scope=Project_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 17, 1)))

Project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=Project_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Project_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Project_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 252, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 251, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'title')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 252, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Project_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 253, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Project_._Automaton = _BuildAutomaton_10()




Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalContact'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 36, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'financialContact'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 37, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scientificContact'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 38, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isPartOf'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 39, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'associatedProjects'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 40, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial'), _ImportedBinding__nsgroup.Location, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 47, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'type'), _ImportedBinding__nsgroup.PlainLiteral, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 69, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress'), _ImportedBinding__vcard.Address, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'fn'), pyxb.binding.datatypes.string, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 53, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasEmail'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 54, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasURL'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 55, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasTelephone'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 56, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasLogo'), pyxb.binding.datatypes.anyURI, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 57, 1)))

Organisation_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'organization-name'), _ImportedBinding__vcard.organization_name_, scope=Organisation_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 59, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 264, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 266, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 267, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 268, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 269, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 274, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 278, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 279, 3))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'fn')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 263, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'organization-name')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 264, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 265, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasEmail')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 266, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasURL')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 267, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasTelephone')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 268, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasLogo')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 269, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 272, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scientificContact')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 273, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'spatial')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 274, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'type')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 275, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalContact')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 276, 3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'financialContact')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 277, 3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isPartOf')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 278, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Organisation_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'associatedProjects')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 279, 3))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
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
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Organisation_._Automaton = _BuildAutomaton_11()




Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'qualifications'), _ImportedBinding__nsgroup.PlainLiteral, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 7, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'affiliation'), pyxb.binding.datatypes.anyURI, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 35, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'language'), _ImportedBinding__nsgroup.LinguisticSystem, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 72, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress'), _ImportedBinding__vcard.Address, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 51, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'fn'), pyxb.binding.datatypes.string, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 53, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasEmail'), pyxb.binding.datatypes.anyURI, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 54, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasURL'), pyxb.binding.datatypes.anyURI, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 55, 1)))

Person_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasTelephone'), pyxb.binding.datatypes.anyURI, scope=Person_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/vcard.xsd', 56, 1)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 289, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 290, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 291, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 297, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 298, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'fn')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 288, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasAddress')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 289, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasEmail')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 290, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasTelephone')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 291, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 294, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'affiliation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 295, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'language')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 296, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'qualifications')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 297, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Person_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_vcard, 'hasURL')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 298, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Person_._Automaton = _BuildAutomaton_12()




Service_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'name'), _ImportedBinding__nsgroup.PlainLiteral, scope=Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 18, 1)))

Service_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_schema, 'serviceType'), _ImportedBinding__nsgroup.PlainLiteral, scope=Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 19, 1)))

Service_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint'), pyxb.binding.datatypes.anyURI, scope=Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcat.xsd', 30, 1)))

Service_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'description'), _ImportedBinding__nsgroup.PlainLiteral, scope=Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 20, 1)))

Service_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'license'), _ImportedBinding__nsgroup.PlainLiteral, scope=Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 65, 1)))

Service_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier'), pyxb.binding.datatypes.anyURI, scope=Service_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/dcterms.xsd', 70, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Service_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'identifier')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 308, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Service_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'name')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 309, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Service_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_schema, 'serviceType')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 310, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Service_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'description')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 311, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Service_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dct, 'license')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 313, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Service_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dcat, 'contactPoint')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 314, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Service_._Automaton = _BuildAutomaton_13()




Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Catalog'), Catalog_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 51, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WebService'), WebService_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 121, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Publication'), Publication_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 167, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Equipment'), Equipment_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 189, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Facility'), Facility_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 229, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Project'), Project_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 247, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organisation'), Organisation_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 259, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Person'), Person_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 284, 1)))

Epos_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Service'), Service_, scope=Epos_, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 304, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 357, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 358, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 359, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 360, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 361, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 362, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 363, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 364, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 365, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Catalog')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 357, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Person')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 358, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organisation')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 359, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Project')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 360, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WebService')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 361, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Publication')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 362, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Service')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 363, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Equipment')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 364, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Epos_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Facility')), pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/EPOS-DCAT-AP.xsd', 365, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Epos_._Automaton = _BuildAutomaton_14()


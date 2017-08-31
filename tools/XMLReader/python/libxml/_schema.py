# ./_schema.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bc1ff65348276a56c5ecd66c11cb769389d29ae5
# Generated 2017-08-30 12:29:09.746810 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Namespace http://schema.org/ [xmlns:schema]

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
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://schema.org/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


numberOfPages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numberOfPages'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', numberOfPages.name().localName(), numberOfPages)

numberOfItems = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'numberOfItems'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', numberOfItems.name().localName(), numberOfItems)

value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.double, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', value.name().localName(), value)

documentation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentation'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 22, 1))
Namespace.addCategoryObject('elementBinding', documentation.name().localName(), documentation)

if __name__ == '__main__':
    startDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startDate'), _ImportedBinding__nsgroup.DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 5, 1))
    Namespace.addCategoryObject('elementBinding', startDate.name().localName(), startDate)
    
    endDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endDate'), _ImportedBinding__nsgroup.DateTimeLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 6, 1))
    Namespace.addCategoryObject('elementBinding', endDate.name().localName(), endDate)
    
    qualifications = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'qualifications'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 7, 1))
    Namespace.addCategoryObject('elementBinding', qualifications.name().localName(), qualifications)
    
    issueNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'issueNumber'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 8, 1))
    Namespace.addCategoryObject('elementBinding', issueNumber.name().localName(), issueNumber)
    
    volumeNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'volumeNumber'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 9, 1))
    Namespace.addCategoryObject('elementBinding', volumeNumber.name().localName(), volumeNumber)
    
    issn = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'issn'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 11, 1))
    Namespace.addCategoryObject('elementBinding', issn.name().localName(), issn)
    
    keywords = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keywords'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 12, 1))
    Namespace.addCategoryObject('elementBinding', keywords.name().localName(), keywords)
    
    serialNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serialNumber'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 13, 1))
    Namespace.addCategoryObject('elementBinding', serialNumber.name().localName(), serialNumber)
    
    manufacturer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'manufacturer'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 15, 1))
    Namespace.addCategoryObject('elementBinding', manufacturer.name().localName(), manufacturer)
    
    unitText = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unitText'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 16, 1))
    Namespace.addCategoryObject('elementBinding', unitText.name().localName(), unitText)
    
    name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 18, 1))
    Namespace.addCategoryObject('elementBinding', name.name().localName(), name)
    
    serviceType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serviceType'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 19, 1))
    Namespace.addCategoryObject('elementBinding', serviceType.name().localName(), serviceType)
    
    minValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'minValue'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 20, 1))
    Namespace.addCategoryObject('elementBinding', minValue.name().localName(), minValue)
    
    maxValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxValue'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/schema.org.xsd', 21, 1))
    Namespace.addCategoryObject('elementBinding', maxValue.name().localName(), maxValue)

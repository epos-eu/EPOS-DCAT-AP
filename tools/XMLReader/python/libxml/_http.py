# ./_http.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1caa642e48a05b407e63a48eb65131303b43cb3f
# Generated 2017-08-30 12:29:09.746570 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Namespace http://www.w3.org/2006/http# [xmlns:http]

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
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/2006/http#', create_if_missing=True)
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


paramName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paramName'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/http.xsd', 12, 1))
Namespace.addCategoryObject('elementBinding', paramName.name().localName(), paramName)

paramValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paramValue'), _ImportedBinding__nsgroup.PlainLiteral, location=pyxb.utils.utility.Location('https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/master/schemas/http.xsd', 13, 1))
Namespace.addCategoryObject('elementBinding', paramValue.name().localName(), paramValue)

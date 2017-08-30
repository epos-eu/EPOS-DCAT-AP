# ./_dct.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:62e52a6e1b0d23522982e9c2905e5cb67ad01951
# Generated 2017-08-30 12:29:09.745561 by PyXB version 1.2.5 using Python 2.7.13.final.0
# Namespace http://purl.org/dc/terms/ [xmlns:dct]

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
Namespace = pyxb.namespace.NamespaceForURI('http://purl.org/dc/terms/', create_if_missing=True)
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

from _nsgroup import extent # {http://purl.org/dc/terms/}extent
from _nsgroup import medium # {http://purl.org/dc/terms/}medium
from _nsgroup import isVersionOf # {http://purl.org/dc/terms/}isVersionOf
from _nsgroup import hasVersion # {http://purl.org/dc/terms/}hasVersion
from _nsgroup import isReplacedBy # {http://purl.org/dc/terms/}isReplacedBy
from _nsgroup import replaces # {http://purl.org/dc/terms/}replaces
from _nsgroup import isRequiredBy # {http://purl.org/dc/terms/}isRequiredBy
from _nsgroup import requires # {http://purl.org/dc/terms/}requires
from _nsgroup import isPartOf # {http://purl.org/dc/terms/}isPartOf
from _nsgroup import hasPart # {http://purl.org/dc/terms/}hasPart
from _nsgroup import isReferencedBy # {http://purl.org/dc/terms/}isReferencedBy
from _nsgroup import relation # {http://purl.org/dc/terms/}relation
from _nsgroup import references # {http://purl.org/dc/terms/}references
from _nsgroup import isFormatOf # {http://purl.org/dc/terms/}isFormatOf
from _nsgroup import hasFormat # {http://purl.org/dc/terms/}hasFormat
from _nsgroup import conformsTo # {http://purl.org/dc/terms/}conformsTo
from _nsgroup import audience # {http://purl.org/dc/terms/}audience
from _nsgroup import accrualMethod # {http://purl.org/dc/terms/}accrualMethod
from _nsgroup import accrualPeriodicity # {http://purl.org/dc/terms/}accrualPeriodicity
from _nsgroup import accrualPolicy # {http://purl.org/dc/terms/}accrualPolicy
from _nsgroup import instructionalMethod # {http://purl.org/dc/terms/}instructionalMethod
from _nsgroup import rightsHolder # {http://purl.org/dc/terms/}rightsHolder
from _nsgroup import source # {http://purl.org/dc/terms/}source
from _nsgroup import mediator # {http://purl.org/dc/terms/}mediator
from _nsgroup import educationLevel # {http://purl.org/dc/terms/}educationLevel
from _nsgroup import bibliographicCitation # {http://purl.org/dc/terms/}bibliographicCitation
from _nsgroup import identifier # {http://purl.org/dc/terms/}identifier
from _nsgroup import alternative # {http://purl.org/dc/terms/}alternative
from _nsgroup import title # {http://purl.org/dc/terms/}title
from _nsgroup import tableOfContents # {http://purl.org/dc/terms/}tableOfContents
from _nsgroup import abstract # {http://purl.org/dc/terms/}abstract
from _nsgroup import description # {http://purl.org/dc/terms/}description
from _nsgroup import created # {http://purl.org/dc/terms/}created
from _nsgroup import valid # {http://purl.org/dc/terms/}valid
from _nsgroup import available # {http://purl.org/dc/terms/}available
from _nsgroup import issued # {http://purl.org/dc/terms/}issued
from _nsgroup import modified # {http://purl.org/dc/terms/}modified
from _nsgroup import dateAccepted # {http://purl.org/dc/terms/}dateAccepted
from _nsgroup import dateCopyrighted # {http://purl.org/dc/terms/}dateCopyrighted
from _nsgroup import dateSubmitted # {http://purl.org/dc/terms/}dateSubmitted
from _nsgroup import format # {http://purl.org/dc/terms/}format
from _nsgroup import spatial # {http://purl.org/dc/terms/}spatial
from _nsgroup import temporal # {http://purl.org/dc/terms/}temporal
from _nsgroup import provenance # {http://purl.org/dc/terms/}provenance
from _nsgroup import rights # {http://purl.org/dc/terms/}rights
from _nsgroup import accessRights # {http://purl.org/dc/terms/}accessRights
from _nsgroup import license # {http://purl.org/dc/terms/}license
from _nsgroup import publisher # {http://purl.org/dc/terms/}publisher
from _nsgroup import type # {http://purl.org/dc/terms/}type
from _nsgroup import language # {http://purl.org/dc/terms/}language
from _nsgroup import subject # {http://purl.org/dc/terms/}subject
from _nsgroup import LicenseDocument # {http://purl.org/dc/terms/}LicenseDocument
from _nsgroup import CTD_ANON # None
from _nsgroup import PeriodOfTime # {http://purl.org/dc/terms/}PeriodOfTime
from _nsgroup import CTD_ANON_ # None
from _nsgroup import Location # {http://purl.org/dc/terms/}Location
from _nsgroup import CTD_ANON_2 # None
from _nsgroup import LinguisticSystem # {http://purl.org/dc/terms/}LinguisticSystem
from _nsgroup import MediaTypeOrExtent # {http://purl.org/dc/terms/}MediaTypeOrExtent
from _nsgroup import ProvenanceStatement # {http://purl.org/dc/terms/}ProvenanceStatement
from _nsgroup import RightsStatement # {http://purl.org/dc/terms/}RightsStatement

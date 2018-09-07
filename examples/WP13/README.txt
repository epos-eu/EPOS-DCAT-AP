Status of WP13 EPOS-DCAT-AP RDF/TTL metadata, at 06/09/2018
-----------------------------------------------------------

WP 13 is providing 10 web services from 8 DDSS elements:

- WP13-DDSS-001 - INTERMAGNET observatory data web service
- WP13-DDSS-001 - WDC Geomagnetism World Data Centre web service
- WP13-DDSS-002 - IMAGE variometer network web service
- WP13-DDSS-003 - WDC global survey data
- WP13-DDSS-006 - ISGI Geomagnetic Indices web service
- WP13-DDSS-007 - ISGI Geomagentic Events web service
- WP13-DDSS-008 - IMAGE electrojet indices web service
- WP13-DDSS-009 - IMAGE substorm events
- WP13-DDSS-012 - WMM World Magnetic Model web service
- WP13-DDSS-012 - IGRF Internal Geomagnetic Reference Field model web service
  
Status of metadata:

- WP13-DDSS-001 - INTERMAGNET:  Validated
- WP13-DDSS-001 - WDC:          Validated
- WP13-DDSS-002 - IMAGE:        Validated
- WP13-DDSS-003 - Survey data:  Validated
- WP13-DDSS-006 - ISGI:         Updated
- WP13-DDSS-007 - ISGI:         Updated
- WP13-DDSS-008 - IMAGE:        Old version of metadata
- WP13-DDSS-009 - IMAGE subst   Not created yet
- WP13-DDSS-012 - WMM:          Old version of metadata
- WP13-DDSS-012 - IGRF:         Updated
 

Understanding SHACL / Turtle
----------------------------

EPOS metadata is described using SHACL. It can be verified using this tool:

http://shacl.org/playground/

Which requires a 'Shape Graph' (definition) of the EPOS metadata schema:

https://raw.githubusercontent.com/epos-eu/EPOS-DCAT-AP/EPOS-DCAT-AP-shapes/eposdcat-ap_shapes.ttl

Paste this into the left-hand pane, the paste the file to be validated into
the right-hand pane.

A good tutorial on Turtle (used to represent RDF) is here:

https://www.w3.org/TR/turtle/

To summarise:
- '.' is used to terminate a triple / list of triples
- ',' separates objects in a list of objects (common subject and predicate)
- ';' separates predicate-objects in a list of predicates and objects (common subject)
- The token 'a' in the predicate position represents the IRI http://www.w3.org/1999/02/22-rdf-syntax-ns#type 
- Relative and absolute IRIs are written surrounded by '<>'
- How prefixes work:
    To write http://www.perceive.net/schemas/relationship/enemyOf using a prefixed name:
    Define a prefix label for the vocabulary IRI http://www.perceive.net/schemas/relationship/ 
    as somePrefix. Then write somePrefix:enemyOf which is equivalent to writing 
    <http://www.perceive.net/schemas/relationship/enemyOf>, Example:
      @prefix somePrefix: <http://www.perceive.net/schemas/relationship/> .
      <http://example.org/#green-goblin> somePrefix:enemyOf <http://example.org/#spiderman> .
- '""' or "''" is used to surround literals
  - A literal may be followed by '@' and a language tag
  - A literal may be followed by '^^' and a data type IRI (absolute, relative or prefixed)
    - default data type is xsd:string
- '_:' introduces a blank node - characters following are the node's label
- '[]' encloses a blank node with a predicate-object list
- '()' encloses a collection / list of zero elements. Can only be used in subject or object



Status of WP13 EPOS-DCAT-AP RDF/TTL metadata, at 10/05/2018
-----------------------------------------------------------

WP 13 is providing 8 web services from 6 priority DDSS elements:

- WP13-DDSS-001 - INTERMAGNET observatory data web service
- WP13-DDSS-001 - WDC Geomagnetism World Data Centre web service
- WP13-DDSS-002 - IMAGE variometer network web service
- WP13-DDSS-006 - ISGI Geomagnetic Indices web service
- WP13-DDSS-007 - ISGI Geomagentic Events web service
- WP13-DDSS-008 - IMAGE electrojet indices web service
- WP13-DDSS-013 - WMM World Magnetic Model web service
- WP13-DDSS-013 - IGRF Internal Geomagnetic Reference Field model web service
  
Status of metadata RDF/TTL:

- WP13-DDSS-001 - INTERMAGNET: Updated to access new WP13 proxy server
                               Avoids problems with digest authentication
- WP13-DDSS-001 - WDC: Converted from previously unvalidated XML file
                       Updated to use hydra template - allows use of 
                       RESTful parameter types
- WP13-DDSS-002 - IMAGE: Converted from previously validated XML file
- WP13-DDSS-006 - ISGI: Converted from previously unvalidated XML file
                        Updated to access new WP13 proxy server
                        Gets around 'hidden parameter' problem while
                        we investigate AAAI
- WP13-DDSS-007 - ISGI: Converted from previously unvalidated XML file
                        Updated to access new WP13 proxy server
                        Gets around 'hidden parameter' problem while
                        we investigate AAAI
- WP13-DDSS-008 - IMAGE: Converted from previously validated XML file
- WP13-DDSS-013 - WMM: Converted from previously validated XML file
- WP13-DDSS-013 - IGRF: Converted from previously validated XML file
 
A number of other noncritical issues were also raised that affect the
effectiveness and ease with which WP13 web services can be called:
- issue #177 (parameter values constrained by other web services)
- issue #178 (parameter min/max values for dates)
- issue #179 (parameter default value)
- issue #181 (data type - clarification of terminology sought)
- issue #182 (link from DDSS data set to trustworthy repository status)

  
Useful links
------------

Link to EPOS metadata editor:
    http://epos.cineca.it/apache/mde/public/index.php
    
Link to SHACL validation website:
    http://shacl.org/playground/
  
Hydra metadata description:
    http://www.hydra-cg.com/spec/latest/core/
    
Templates in Hydra conform to RFC 6570 (I think):
    https://tools.ietf.org/html/rfc6570

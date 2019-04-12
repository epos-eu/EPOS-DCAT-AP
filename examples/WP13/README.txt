Status of WP13 EPOS-DCAT-AP RDF/TTL metadata, at 27/03/2019
-----------------------------------------------------------

Summary of work done to WP13 metadata:

1. Mail from Rossana Paciello, 15/01/2019
  1.1 Add metadata for web services with more than one payload
2. Mail from Rossana Paciello, 12/03/2019
  2.1 Add temporal information for DDSS discovery
  2.2 Add temporal information for DDSS query
  2.3 Add spatial information for DDSS discovery
  2.4 Add spatial metadata for DDSS query
  2.5 Check metadata quality for key attributes
3. Add new web services
  3.1 Add web service for out-of-cycle WMM release

  
### 1.1 Add metadata for web services with more than one payload ###

- insert the format as parameter of web service;
- have only one the description of hydra:Operation. 
- add multiple occurrences of hydra:returns in hydra:Operation.

For example:

```
<https://www.epos-eu.org/epos-dcat-ap/GeoElectroMagnetism/WP13-DDSS-001/INTERMAGNET/Operation> a hydra:Operation;
    hydra:method "GET"^^xsd:string;
    hydra:returns "text/xml";
         hydra:returns "application/json";
         hydra:returns "...";
    hydra:property[ a hydra:IriTemplate;
        hydra:template "http://geomag.bgs.ac.uk/EPOS/WP13/intermagnet/?Request=GetData&{&observatoryIagaCode, SamplesPerDay, dataStartDate, dataDuration, publicationState, recordTermination, traceList, format}"^^xsd:string;
            hydra:mapping[ a hydra:IriTemplateMapping;
                hydra:variable "format"^^xsd:string;
                rdfs:label "output format";
                rdfs:range "xsd:string" ;
                schema:defaultValue "XML";
                hydra:required "true"^^xsd:boolean;
                http:paramValue "XML";
                http:paramValue "JSON";
                ...
            ];
...
```

==> All WP13 entries updated to include multiple hydra:returns entries where appropriate.

There's still a problem that:

1. There's no way to recognise which hydra:mapping attribute controls the payload 
   format for the web service. There needs to be a semantic label attached to the
   (single) hydra:mapping attribute that controls the payload format.
   
2. There's no way to link the http:paramValues in the payload format description to
   the hydra:returns attributes, so at present the GUI won't know what type of return
   it will get for any particular format value. This is complicated because:
   - There's no direct mapping between names in the hydra:mapping 'format' attribute
     and mime types in the hydra:returns attribute
   - There may be a many-to-one relationship between hydra:mapping 'format' and
     hydra:returns, for example where the format allows choice between a number
     of different plain text formats (all of which would have a Mime type of text/plain).
   - Not all payloads have a Mime type registered yet (e.g. Coverage JSON).


### 2.1 Add temporal information for DDSS discovery ###

Dataset and WebService entities must contain schema:startDate and schema:endDate 
attributes, though schema:endDate may be omitted if collection of the data is 
ongoing. The date format to be used for these elements is “YYYY-MM-DDThh:mm:ssZ”.

==> All WP13 metadata already contains these entries, though two incorrect entries
    were found and corrected (missing end date for DDSS-012 WMM and DDSS-012 IGRF).


### 2.2 Add temporal information for DDSS query ###

Operation entities must have schema:startDate / schema:endDate and 
schema:valuePattern attributes added to IRITemplateMapping attributes
to give semantic information on how to fill out start / end dates when
querying a web service, e.g.:

```
hydra:mapping[ a hydra:IriTemplateMapping; 
        hydra:variable "epoch_start"; 
        hydra:property "schema:startDate"; 
        schema:valuePattern "YYYY-MM-DD"; 
        ... ];
```

The valuePattern may be one of: YYYY-MM-DD, YYYYMMDD, YYYY.yyy
(other patterns may be used, but these are sufficient for WP13).

==> All WP13 metadata already contains these entries


### 2.3 Add spatial information for DDSS discovery ###

Dataset and WebService entities must contain spatial bounding boxes in the form
of a closed polygon, with coordinates in long lat, long lat, ... order. The default 
reference is WGS84, EG:

```
dct:spatial [ a dct:Location; 
    locn:geometry "POLYGON(180.0 -90.0, -180.0 -90.0, -180.0 90.0, 180.0 90.0, 180.0 -90.0)"^^gsp:wktLiteral ;
]; 
```

==> All WP13 already contains these entries. Entries were checked for valid bounding boxes.


### 2.4 Add spatial metadata for DDSS query ###

Operation entities must have epos:southernmostLatitude, epos:northernmostLatitude,
epos:easternmostLongitude, and epos:westernmostLongitude attributes where the web 
service allows setting of a bounding box for the query.

A note in the guidance says that entities without these attributes will be excluded from 
EPOS search, though they will be included in a later version (before the end of EPOS-IP).

==> Some WP13 web services specify a point rather than a box. These have been encoded 
    by putting south/north and east/west attributes in the same web service parameter. 
    THIS MAY NOT BE CORRECT.
    
| WP13 DDSS number  | Spatial encoding for DDSS query |
|-------------------|---------------------------------|
| 001 - INTERMAGNET | N/A                             |
| 001 - WDC:        | N/A                             |
| 002 - IMAGE:      | N/A                             |
| 003 - Survey data | Bounding box "approach A"       |
| 006 - ISGI:       | N/A                             |
| 007 - ISGI:       | N/A                             |
| 008 - IMAGE:      | N/A                             |
| 009 - IMAGE subst | N/A                             |
| 012 - WMM:        | LAT/LONG point                  |
| 012 - IGRF:       | LAT/LONG point                  |


### 2.5 Check metadata quality for key attributes ###

Check for the following entities and attributes:

Dataset entity
- dct:title “It contains a name given to the Dataset”;
- dct:description “It contains a free-text description of the Dataset”;
- adms:identifier “It contains the DDSS-ID according to the master table”;
- dct:spatial “It refers to a geographical area covered by the Dataset”;
- dct:temporal “It refers to a temporal period that the Dataset covers”;
- dcat:keyword “It contains the keywords used to describe the Dataset”;

Distribution entity
- dct:title “It contains a name given to the Distribution”;
- dct:description “It contains a free-text account of the Distribution”;
- dct:license “It refers to the license under which the Distribution is made available”;

WebService entity
- schema:name “It contains a name given to the Web Service”;
- schema:description “It contains a free-text description of the Web Service”;
- schema:keywords “It contains the keywords used to describe the Web Service”;
- dct:spatial “It refers to a geographical area covered by the Web Service”;
- dct:temporal “It refers to a temporal period that the Web Service covers”;

Operation entity
- rdfs:label “It contains a short string used to describe the meaning of the parameter”;
- hydra:returns “It is used to specify the output format of the Operation. The possible 
  values are listed here: https://www.iana.org/assignments/media-types/media-types.xhtml”;

==> A number of small updates made
  
  
### Add web service for out-of-cycle WMM release ###

Update dataset description
Update webservice description
Update Operation to allow access to both WMM 2015 and WMM 2015 v2


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
- WP13-DDSS-006 - ISGI:         Validated
- WP13-DDSS-007 - ISGI:         Validated
- WP13-DDSS-008 - IMAGE:        Validated
- WP13-DDSS-009 - IMAGE subst:  Validated
- WP13-DDSS-012 - WMM:          Validated
- WP13-DDSS-012 - IGRF:         Validated
 

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
- WP13-DDSS-012 - WMM World Magnetic Model web service
- WP13-DDSS-012 - IGRF Internal Geomagnetic Reference Field model web service
  
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
- WP13-DDSS-012 - WMM: Converted from previously validated XML file
- WP13-DDSS-012 - IGRF: Converted from previously validated XML file
 
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

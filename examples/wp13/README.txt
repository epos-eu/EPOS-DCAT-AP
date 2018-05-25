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
                         Waiting resolution of issue #158 (RESTful parameter types)
                         This seems possible with a Hydra:template and I've tried to implement a solution.
  - WP13-DDSS-002 - IMAGE: Converted from previously validated XML file
  - WP13-DDSS-006 - ISGI: Converted from previously unvalidated XML file
                          Waiting resolution of issue #215 (Hidden web service parameters)
  - WP13-DDSS-007 - ISGI: Converted from previously unvalidated XML file
                          Waiting resolution of issue #215 (Hidden web service parameters)
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
  
Hydra metadata description:
    http://www.hydra-cg.com/spec/latest/core/
    
Templates in Hydra conform to RFC 6570 (I think):
    https://tools.ietf.org/html/rfc6570
from rdflib import Namespace, URIRef, Graph
from rdflib.namespace import RDF, FOAF

data = Namespace("http://www.example.org#")

# create the RDF graph
g = Graph()

# create namespaces
ns_adms = Namespace('http://www.w3.org/ns/adms#')
ns_rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ns_epos = Namespace('https://www.epos-eu.org/epos-dcat-ap#')
ns_dc = Namespace('http://purl.org/dc/elements/1.1/')
ns_dct = Namespace('http://purl.org/dc/terms/')
ns_vcard = Namespace('http://www.w3.org/2006/vcard/ns#')
ns_hydra = Namespace('http://www.w3.org/ns/hydra/core#')
ns_xsd = Namespace('http://www.w3.org/2001/XMLSchema#')
ns_schema = Namespace('http://schema.org/')
ns_dcat = Namespace('http://www.w3.org/ns/dcat#')
ns_cnt = Namespace('http://www.w3.org/2011/content#')
ns_locn = Namespace('http://www.w3.org/ns/locn#')
ns_skos = Namespace('http://www.w3.org/2004/02/skos/core#')
ns_rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
ns_http = Namespace('http://www.w3.org/2006/http#')
ns_owl = Namespace('http://www.w3.org/2002/07/owl#')
ns_gsp = Namespace('http://www.opengis.net/ont/geosparql#')

# bind namespaces to the graph with prefixes
g.bind ('adms', ns_adms)
g.bind ('rdf', ns_rdf)
g.bind ('epos', ns_epos)
g.bind ('dc', ns_dc)
g.bind ('dct', ns_dct)
g.bind ('vcard', ns_vcard)
g.bind ('hydra', ns_hydra)
g.bind ('xsd', ns_xsd)
g.bind ('schema', ns_schema)
g.bind ('dcat', ns_dcat)
g.bind ('cnt', ns_cnt)
g.bind ('locn', ns_locn)
g.bind ('skos', ns_skos)
g.bind ('rdfs', ns_rdfs)
g.bind ('http', ns_http)
g.bind ('owl', ns_owl)
g.bind ('gsp', ns_gsp)

g.add( (URIRef(data.Alice), RDF.type , FOAF.person) )
g.add( (URIRef(data.Bob), RDF.type , FOAF.person) )
g.add( (URIRef(data.Alice), FOAF.knows, URIRef(data.Bob)) )

g.serialize(destination='output.ttl', format='turtle')


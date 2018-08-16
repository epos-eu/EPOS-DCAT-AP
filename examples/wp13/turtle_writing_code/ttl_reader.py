from rdflib import Namespace, URIRef, Graph
import ttl_utils as ttl

g = ttl.read_ttl ('../EPOS-DCAT-AP_WP13_DDSS-001_INTERMAGNET.ttl')

g2 = ttl.search_triples (g, 'mailto:smf@bgs.ac.uk')
ttl.dump_graph (g2)

g3 = ttl.search_triples (g, 'http://orcid.org/0000-0002-7677-5158')
ttl.dump_graph (g3)

g_final = g2 + g3
ttl.dump_graph (g_final)

ttl.write_ttl(g, 'output.ttl')



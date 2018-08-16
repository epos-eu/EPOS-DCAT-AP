from rdflib import Namespace, URIRef, Graph

def read_ttl (filename):
    graph = Graph()
    graph.parse(location=filename, format='n3')
    return graph

def write_ttl (graph, filename):
    graph.serialize(destination=filename, format='turtle')

def copy_namespaces (graph1, graph2):
    for ns_prefix, ns_uri in graph1.namespaces():
    #for namespace in graph1.namespaces():
        graph2.bind (ns_prefix, ns_uri)

def search_triples (graph, search_term):
    new_g = Graph()
    copy_namespaces (graph, new_g)
    for s, p, o in graph:
        if (str(s) == search_term) or (str(o) == search_term):
            new_g.add ((s, p, o))
    return new_g

def dump_graph (graph):
    print("--- printing raw triples: " + str(len(graph)) + " ---")
    for s, p, o in graph:
        print((s, p, o))

def dump_namespaces (graph):
    print ("--- printing namespaces ---")
    print (list (graph.namespaces()))

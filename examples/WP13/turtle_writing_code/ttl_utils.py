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

def search_triples (graph, search_term, new_graph=None):
    print ("Search: " + search_term)
    if new_graph is None:
        new_graph = Graph()
        copy_namespaces (graph, new_graph)
    # iterate over the the triples in the graph
    for s, p, o in graph:
        triple = (s, p, o)
        # is the search term the subject of the triple?
        if str(s) == search_term:
            # yes - have we seen this triple before?
            if not triple in new_graph:
                # no - recursively search for triples containing the object
                print ("Found triple by subject: " + str(s) + ", " + str(p) + ", " + str(o))
                new_graph.add (triple)
                #search_triples(graph, str(o), new_graph)
        # is the search term the object of the triple?
        elif str(o) == search_term:
            # yes - have we seen this triple before?
            if not triple in new_graph:
                # no - recursively search for triples containing the subject
                print("Found triple by object: " + str(s) + ", " + str(p) + ", " + str(o))
                new_graph.add (triple)
                search_triples (graph, str(s), new_graph)
    return new_graph

def dump_graph (graph):
    print("--- printing raw triples: " + str(len(graph)) + " ---")
    for s, p, o in graph:
        print((s, p, o))

def dump_namespaces (graph):
    print ("--- printing namespaces ---")
    print (list (graph.namespaces()))

from pathlib import Path
from rdflib import Namespace, Graph
from rdflib.namespace import RDFS
from rdflib.term import BNode, URIRef
from requests.exceptions import RequestException

import logging
import re
import requests
import sys
import tempfile
import zipfile

# Set up basic logging to stdout
logging.basicConfig(level=logging.INFO)

# Namespaces that are not currently defined in rdflib
HYDRA = Namespace('http://www.w3.org/ns/hydra/core#')
SCHEMA = Namespace('http://schema.org/')


# Local Exceptions
class BNodeException(Exception):
    def __init__(self, bnode):
        self.message = f"Final element of triple must be a BNode, it's {type(bnode)}"

class TemplateException(Exception):
    def __init__(self):
        self.message = "There must be just one template"

class DefaultValueException(Exception):
    def __init__(self, parameter):
        self.message = f"Required parameter {parameter} must have a default value"


# A subclass of rdflib's Graph that allows basic subgraphing.
class SubgraphableGraph(Graph):

    # Create a subgraph from a triple by recursing
    # through the subgraph using the BNodes.
    # This assumes there are no cycles in the graph!
    def sub_graph(self, triple):
        bnode = triple[2]
        if type(bnode) != BNode:
            raise BNodeException(bnode)

        children = self.triples((bnode, None, None))
        g = Graph()
     
        for child in children:
            g.add(child)
            if type(child[2]) == BNode:
                g = g + self.sub_graph(child)

        return g


class Operation:
    def __init__(self, g):
        """
        Attributes intialised in __init__()
            base_url    a string extracted from hydra.template
            parameters  set of strings extracted from hydra.template
            variables   set of strings extracted from hydra.variables
            defaults    dictionary of required parameters and default values
        """
        self.path_params = None
        self._parse_template(g)
        self._parse_parameters(g)

    def _parse_template(self, g):
        # Extract url and parameters from template string 
        template = list(g.triples((None, HYDRA.template, None)))
        if len(template) != 1:
            raise TemplateException(template)
        logging.debug(template[0][2])

        # Split into URL and query parameters and then tidy up the parameters 
        # This doesn't deal with '} ?' which might be possible?
        url_parts = template[0][2].split('{?')
        # It's possible the optional parameters are introduced by & not ?
        if len(url_parts) == 1:
            url_parts = template[0][2].split('{&')
        self.base_url = url_parts[0]
        self.parameters = set([])
        if len(url_parts) > 1:
            for p in url_parts[1].rstrip('}').split(','):
                self.parameters.add(p.strip())

        # Are there any parameters embedded in the URL?
        # If so extract them and add them to the other parameters
        if '{' in self.base_url:
            self.path_params = set(re.findall(r'\{.*?\}', self.base_url))
            logging.debug("Path parameters: " + str(self.path_params))
            for p in self.path_params:
                self.parameters.add(p.lstrip('{').rstrip('}').strip())

        logging.debug("Template parameters: " + str(self.parameters))

    def _parse_parameters(self, g):
        # Extract parameters from RDF, then required parameters and defaults values
        self.defaults = {}
        self.variables = set([])
        for var in g.triples((None, HYDRA.variable, None)):
            self.variables.add(str(var[2]))
            try:
                required = list(g.triples((var[0], HYDRA.required, None)))[0][2]
                default = list(g.triples((var[0], SCHEMA.defaultValue, None)))[0][2]
                self.defaults[str(var[2])] = str(default)
            except IndexError:
                if required:
                    raise DefaultValueException(str(var[2]))
                # If not required simply don't add to the defaults

        logging.debug("HYDRA parameters: " + str(self.variables))
        logging.debug("Default parameters: " + str(self.defaults))

        # These two sets should be identical
        if self.variables != self.parameters:
            logging.warn("Variable and parameter lists differ")

    def _create_base_url(self):
        url = self.base_url
        # If there are any path parameters replace with the default
        # values and remove them from defaul
        if self.path_params:
            for p in self.path_params:
                param = p.lstrip('{').rstrip('}').strip()
                value = self.defaults[param]
                url = url.replace(p, value)
                self.defaults.pop(param)

        return url

    def get(self):
        url = self._create_base_url()

        logging.debug("Base URL: " + url)
        logging.debug("parameters: " + str(self.defaults))

        rsp = requests.get(url, params=self.defaults)

        logging.info("URL: " + rsp.url)
        logging.info("Status: " + str(rsp.status_code))

        rsp.raise_for_status()

        logging.info("Content type: " + rsp.headers['Content-Type'])

        if rsp.headers['Content-Type'] == "application/octet-stream":
            # For WP13 this is a zip file so log contained files
            logging.info("Binary data")
            with tempfile.TemporaryFile() as f:
                f.write(rsp.content)
                z = zipfile.ZipFile(f)
                logging.info("Zipped files: " + str(z.namelist()))
        # Text file of some sort, log a summary
        else:
            if len(rsp.text) <= 1200:
                logging.info("Text:\n" + rsp.text)
            else:
                logging.info("Text:\n" + rsp.text[:500] + "...\n...\n..." + rsp.text[-500:])


def test_operation(filename):
    logging.info(f"\nProcessing: {filename}")
    logging.info("-"*50)
    graph = SubgraphableGraph()
    graph.parse(location=filename, format='n3')
    operations =  graph.triples((None, HYDRA.property, None))

    ographs = []
    for o in operations:
        # The root of an operation must be:
        #     (URIRef, HYDRA.property, BNode)
        if type(o[0]) != URIRef or type(o[2]) != BNode:
            continue
        # Generate a subgraph (tree) for each operation
        g = Graph()
        g.add(o)
        try:
            g = g + graph.sub_graph(o)
        except BNodeException as bne:
            logging.error(bne.message)
            logging.error("Unable to proceed with this file")
            return
        ographs.append(g)

    for o in ographs:
        try:
            op = Operation(o)
        except (TemplateException, DefaultValueException) as e:
            logging.error(e.message)
            logging.error("Unable to proceed with this file")
            return

        try:
            op.get()
        except RequestException as e:
            logging.error(e)


if __name__ == "__main__":
    p = Path(sys.argv[1])
    if p.is_file():
        test_operation(str(p))
    elif p.is_dir():
        for f in p.glob('*.ttl'):
            test_operation(str(f))
            logging.info("="*50)

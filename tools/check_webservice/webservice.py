import argparse
import logging
import re
import requests
import sys
import tempfile
import zipfile

from pathlib import Path
from rdflib import Namespace, Graph
from rdflib.namespace import RDFS
from rdflib.term import BNode, URIRef
from requests.exceptions import RequestException


# Set up basic logging to stdout
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

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


class ParameterException(Exception):
    def __init__(self, url):
        self.message = f"For {url} variable and parameter lists differ"


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
    def __init__(self, graph, level):
        """
        Attributes intialised in __init__()
            base_url    a string extracted from hydra.template
            parameters  set of strings extracted from hydra.template
            variables   set of strings extracted from hydra.variables
            defaults    dictionary of required parameters and default values
        """
        self.path_params = None
        self.level = level
        self.graph = graph

    def parse_template(self):
        # Extract url and parameters from template string
        template = list(self.graph.triples((None, HYDRA.template, None)))
        if len(template) != 1:
            raise TemplateException(template)
        logging.debug(template[0][2])

        # Split into URL and query parameters and then tidy up the parameters
        # This doesn't deal with '} ?' which might be possible?
        url_parts = template[0][2].split('{?')
        # It's possible the optional parameters are introduced by & not?
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

    def parse_parameters(self):
        # Extract parameters from RDF, then required parameters and defaults values
        self.defaults = {}
        self.variables = set([])
        for var in self.graph.triples((None, HYDRA.variable, None)):
            self.variables.add(str(var[2]))
            try:
                required = list(
                    self.graph.triples((var[0], HYDRA.required, None)))[0][2]
                default = list(
                    self.graph.triples((var[0], SCHEMA.defaultValue, None)))[0][2]
                self.defaults[str(var[2])] = str(default)
            except IndexError:
                if required:
                    raise DefaultValueException(str(var[2]))
                # If not required simply don't add to the defaults

        logging.debug("HYDRA parameters: " + str(self.variables))
        logging.debug("Default parameters: " + str(self.defaults))

        # These two sets should be identical
        if self.variables != self.parameters:
            raise ParameterException(self.base_url)

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

        rsp = requests.get(url, params=self.defaults, stream=True)
        rsp.raise_for_status()

        if self.level > 0:
            print("URL: " + rsp.url)
            print("Status: " + str(rsp.status_code))

        if self.level > 1:
            print("Content type: " + rsp.headers['Content-Type'])
            try:
                print("Content length: " + rsp.headers['Content-Length'])
            except KeyError as ke:
                print("Content length: not provided")

        if self.level > 2:
            if rsp.headers['Content-Type'] == "application/octet-stream":
                # For WP13 this is a zip file so log contained files
                print("Binary data")
                with tempfile.TemporaryFile() as f:
                    for chunk in rsp.iter_content(chunk_size=8192):
                        f.write(chunk)
                    f.flush()
                    try:
                        z = zipfile.ZipFile(f)
                        print("Zipped files: " + str(z.namelist()))
                    except zipfile.BadZipFile as bzf:
                        logging.error(bzf)

            # Text file of some sort, log a summary
            else:
                first = True
                for chunk in rsp.iter_content(chunk_size=1024):
                    if first:
                        print("Head:\n" + chunk.decode("utf-8")[:500])
                        first = False
                if chunk:
                    print("Tail:\n" + chunk.decode("utf-8")[-500:])


def test_operation(filename, level):
    if level > 0:
        print("="*80)
        print(f"Processing: {filename}")

    graph = SubgraphableGraph()
    graph.parse(location=filename, format='n3')
    operations = list(graph.triples((None, HYDRA.property, None)))

    found = False
    for o in operations:
        # The root of an operation must be:
        #     (URIRef, HYDRA.property, BNode)
        if type(o[0]) != URIRef or type(o[2]) != BNode:
            continue

        if level > 0:
            print("-"*80)

        # Generate a subgraph (tree) for each operation
        g = Graph()
        g.add(o)
        try:
            g = g + graph.sub_graph(o)
            op = Operation(g, level)
            found = True
            op.parse_template()
            op.parse_parameters()
            op.get()
        except BNodeException as bne:
            logging.error(bne.message)
        except ParameterException as pe:
            logging.warn(pe.message)
        except (TemplateException, DefaultValueException) as e:
            logging.error(e.message)
        except RequestException as e:
            logging.error(e)

    if not found:
        logging.warn("No operations found in this file")

    if level > 0:
        print("="*80 + "\n")


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("target", help="file or folder to be processed")
parser.add_argument("--level", type=int, choices=[0, 1, 2, 3], default=1,
                    help=("output level (default: %(default)s)\n"
                          "  0 - suppress output, report errors and warnings\n"
                          "  1 - echo urls and response status\n"
                          "  2 - plus other response headers\n"
                          "  3 - plus attempt to show head and tail of content\n"
                          "      or list files in compressed content."))

args = parser.parse_args()
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    p = Path(args.target)
    if p.is_file():
        test_operation(str(p), args.level)
    elif p.is_dir():
        for f in p.glob('*.ttl'):
            test_operation(str(f), args.level)

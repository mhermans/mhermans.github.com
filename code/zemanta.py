import urllib, sys, getopt
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET # needs 2.5 XXX check for seperate elementtree install
import RDF, simplejson

from pprint import pprint            
# Basic api wrapper for the Zemanta API
# Needs simplejson and Redland RDF libraries 

def summary(rdfxmlResponseData):

    formats = { 'json' : 'http://www.w3.org/2001/sw/DataAccess/json-sparql/',
                'xml' : 'http://www.w3.org/2005/sparql-results#'
                }

    sparqlString = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX z:   <http://s.zemanta.com/ns#>
        PREFIX c: <http://s.opencalais.com/1/pred/>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
                                                           
        SELECT ?thing ?anchor ?link
                                                           
        WHERE {
                ?thing  rdf:type z:Recognition;
                        z:anchor ?anchor;
                        z:object ?object
                ?object owl:sameAs ?link
                                                           
            }
        ORDER BY ?anchor
        """

    q = RDF.SPARQLQuery(querystring=sparqlString)
    
    m = RDF.Model()
    p = RDF.Parser()
    base = RDF.Uri("http://base.com")
    p.parse_string_into_model(m, rdfxmlResponseData, base)
    
    syntax = "xml" #'json' also possible

    sparqlResult = q.execute(m).to_string(formats[syntax]) 
    tree = ET.ElementTree(ET.fromstring(sparqlResult))
    r = {}
    for x in tree.findall('//{http://www.w3.org/2005/sparql-results#}result'):
        anchor = x.find('./{http://www.w3.org/2005/sparql-results#}binding/{http://www.w3.org/2005/sparql-results#}literal').text
        uris = x.findall('./{http://www.w3.org/2005/sparql-results#}binding/{http://www.w3.org/2005/sparql-results#}uri')
        uri = uris[0].text
        link = uris[1].text
        if anchor not in r:
            #print "#####", r.keys(), anchor, "not in r"
            r[anchor] = {"anchor": anchor, "uri": uri, "links": []}
        else:
            r[anchor]["links"].append(link)

    return r








class ZemantaAPI:
    def __init__(self, apiKey, returnMethod="zemanta.suggest_markup"):
        self.apiKey = apiKey
        self.returnMethod = returnMethod

    def extractEntities(self, data, outputFormat="turtle"):
        """XXX"""
        if outputFormat == "rdfxml":
            return self.queryAPI(data, returnFormat="rdfxml")

        elif outputFormat  in ("turtle", "ntriples"):
            #import RDF
            response = self.queryAPI(data, returnFormat="rdfxml")

            m = RDF.Model()
            p = RDF.Parser()
            s = RDF.Serializer(outputFormat)
            base = RDF.Uri("http://base.com")
            p.parse_string_into_model(m, response["data"], base)
            return s.serialize_model_to_string(m)
            
        elif outputFormat == "json":
            response = self.queryAPI(data, returnFormat="json")
            print response, len(response)
            return simplejson.loads(response["data"])

        else:
            raise ValueError("Ouputformat not recoginzed/supported") 

    def queryAPI(self, data, returnFormat="rdfxml", summary=True):
        """XXX"""

        gateway = 'http://api.zemanta.com/services/rest/0.0/'
        args = {    'method': self.returnMethod,
                    'api_key': self.apiKey,
                    'text': data,
                    'return_categories': 'dmoz',
                    'format': returnFormat}            
        args_enc = urllib.urlencode(args)

        responseData = urllib.urlopen(gateway, args_enc).read() # XXX errorhandling?
        
        response = {}
        response["data"] = responseData

        if returnFormat == "rdfxml" and summary:
            response["summary"] = self.summary(responseData)
        
        else: response["summary"] = "Summary only implemented for rdfxml return format"

        return response


















































class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
       
        filename = args[0]
        f = open(filename, 'r')
        txt = f.read()
        f.close()

        myapikey = 'hup76nfffvzfkhscxbngzvsq' #Invalid; request@http://developer.zemanta.com/apps/register
        zApi = ZemantaAPI(myapikey)
        result = zApi.extractEntities(txt, "rdfxml")
        print len(result["summary"]), "entities exctracted by Zemanta:\n"
        pprint(result["summary"])
        #print result["data"]
        result = zApi.extractEntities(txt, "json")
        pprint


    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())

import urllib, sys, getopt
import RDF, simplejson
# Basic api wrapper for the Zemanta API
# Lazy loading of simplejson and/or Redland RDF libraries 
# if needed for serializing

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
            p.parse_string_into_model(m, response, base)
            return s.serialize_model_to_string(m)
            
        elif outputFormat == "json":
            #import simplejson
            #from pprint import pprint            
            pass
            #output = simplejson.loads(raw_output)
            #pprint(output)

        else:
            raise ValueError("Ouputformat not recoginzed/supported") 

    def queryAPI(self, data, returnFormat="rdfxml", summary=True):
        """XXX"""

        gateway = 'http://api.zemanta.com/services/rest/0.0/'
        args = {'method': self.returnMethod,
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

    def summary(self, responseData):
        #def query(self, sparql, syntax='xml'):
        #"Executes a sparql-query on the result-graph. Results of the query can be serialized in 'json' or 'xml'-format"

        formats = { 'json' : 'http://www.w3.org/2001/sw/DataAccess/json-sparql/',
                    'xml' : 'http://www.w3.org/2005/sparql-results#'
                    }

        sparqlString = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX z:   <http://s.zemanta.com/ns#>
            PREFIX c: <http://s.opencalais.com/1/pred/>
                                                               
            SELECT ?anchor
                                                               
            WHERE {
                    ?thing rdf:type z:Recognition
                    ?thing z:anchor ?anchor
                                                               
                }
            """

        q = RDF.SPARQLQuery(querystring=sparqlString)
        
        m = RDF.Model()
        p = RDF.Parser()
        base = RDF.Uri("http://base.com")
        p.parse_string_into_model(m, responseData, base)
        
        syntax = "xml" #'json' also possible

        sparqlResult = q.execute(m).to_string(formats[syntax]) 
        print sparqlResult
        #xml = self.query(q, syntax='xml')
        #tree = ET.ElementTree(ET.fromstring(self.query(q)))
        #for x in tree.findall('//{http://www.w3.org/2005/sparql-results#}result'):
        #name = x.find('./{http://www.w3.org/2005/sparql-results#}binding/{http://www.w3.org/2005/sparql-results#}literal').text
        #type = x.find('./{http://www.w3.org/2005/sparql-results#}binding/{http://www.w3.org/2005/sparql-results#}uri').text
        #print ''.join([name, ' (', type.split("/")[-1], ')']) 
        return "Summary..."

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

        myapikey = 'up76nfffvzfkhscxbngzvsq' #Invalid; request@http://developer.zemanta.com/apps/register
        zApi = ZemantaAPI(myapikey)
        print zApi.extractEntities(txt, "rdfxml")["data"] 

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())

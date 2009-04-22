#!/usr/bin/env python
import urllib, sys, getopt
# A basic API-wrapper for the Zemanta API
# Lazy loading of simplejson and Redland RDF libraries, depending on serialization

APIKEY = 'up76nfffvzfkhscxbngzvsq' #Invalid; request @http://developer.zemanta.com/apps/register

class ZemantaAPI:
    def __init__(self, apiKey, returnMethod="zemanta.suggest_markup"):
        self.apiKey = apiKey
        self.returnMethod = returnMethod

    def extractEntities(self, data, outputFormat="rdfxml"):
        """XXX"""
        if outputFormat == "rdfxml":
            return self.queryAPI(data, returnFormat="rdfxml")

        elif outputFormat  in ("turtle", "ntriples"):
            import RDF # lazy loauding of librdf XXX switch to rdflib?
            response = self.queryAPI(data, returnFormat="rdfxml")

            m = RDF.Model()
            p = RDF.Parser()
            s = RDF.Serializer(outputFormat)
            base = RDF.Uri("http://base.com") #XXX appropriate base-URI?
            p.parse_string_into_model(m, response, base)
            return s.serialize_model_to_string(m)
            
        elif outputFormat == "json":
            import simplejson
            response = self.queryAPI(data, returnFormat="json")
            return simplejson.loads(response)

        else:
            raise ValueError("Ouputformat not recognized/supported")

    def queryAPI(self, data, returnFormat="rdfxml"):
        """XXX"""

        gateway = 'http://api.zemanta.com/services/rest/0.0/'
        args = {    'method': self.returnMethod,
                    'api_key': self.apiKey,
                    'text': data,
                    'return_categories': 'dmoz',
                    'format': returnFormat}            
        args_enc = urllib.urlencode(args)
        responseData = urllib.urlopen(gateway, args_enc).read() # XXX errorhandling?
        
        return responseData

    def summary(self, rdfData):
        """Basic summary of the results return by Zemanta."""

        import RDF
        m = RDF.Model()
        p = RDF.Parser()
        base = RDF.Uri("http://base.com") #XXX Base-URI?
        try:
            p.parse_string_into_model(m, rdfData, base)
        except RDF.RedlandError:
            p = RDF.Parser("turtle")
            try:
                p.parse_string_into_model(m, rdfData, base)
            except RDF.RedlandError:
                p = RDF.Parser("ntriples")
                try:
                    p.parse_string_into_model(m, rdfData, base)
                except RDF.RedLandError:
                    raise e

        ZEM = RDF.NS('http://s.zemanta.com/ns#')
        RDFNS = RDF.NS('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        OWL = RDF.NS('http://www.w3.org/2002/07/owl#')

        st = RDF.Statement(None, RDFNS.type, ZEM.Recognition)
        recognitions  = m.find_statements(st) #Returns a RDF.Stream =>  len()?
        i = 0
        print "Entities extracted&linked:"
        print "-"*26
        for r in recognitions:
            i = i+1
            s = r.subject
            objectLink = m.get_target(s, ZEM.object)

            print m.get_target(s, ZEM.anchor), s
            for link in m.get_targets(objectLink, OWL.sameAs):
                print "\tlink", link

        print '=> Zemanta found', i , 'entities.'


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ht", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
        
        for o, a in opts:
            if o == "-t":
                import doctest
                doctest.testfile("doctest.txt", globs={"key":APIKEY}) # pass dict with api-key to doctest
            elif o in ("-h", "--help"):
                print "..."
        if len(opts) == 0 and len(argv[1:]) == 1:
            filename = args[0]
            f = open(filename, 'r')
            txt = f.read()
            f.close()
                
            myapikey = APIKEY 
            zApi = ZemantaAPI(myapikey)
            result = zApi.extractEntities(txt, "ntriples")
            zApi.summary(result)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())

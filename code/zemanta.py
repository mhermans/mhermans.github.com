import urllib, sys, getopt
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
            import RDF
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

    def queryAPI(self, data, returnFormat="rdfxml"):
        """XXX"""

        gateway = 'http://api.zemanta.com/services/rest/0.0/'
        args = {'method': self.returnMethod,
        'api_key': self.apiKey,
        'text': data,
        'return_categories': 'dmoz',
        'format': returnFormat}            
        args_enc = urllib.urlencode(args)

        responseData = urllib.urlopen(gateway, args_enc).read() # XXX errorhandling?

        return responseData

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
        print zApi.extractEntities(txt, "rdfxml") 

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())

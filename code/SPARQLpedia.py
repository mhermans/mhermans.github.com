#!/usr/bin/env python
# SPARQLpedia API documentation: http://sparqlpedia.org/api.html
# it is labled a "REST-based protocol", but GET & POST are equivalent...
import urllib

class SPARQLpediaAPI:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.endpoint = "http://sparqlpedia.org:8080/tbl/server/tbl/servlet"

    def add(self, query):
        pass

    def delete(self, query):
        pass

    def find(self, searchValues):
        submitter = searchValues
        namespace = None
        nodes = None
        args =  {   "action"    : "sparqlmotion",
                    "id"        : "findQueries",
                    #"namespace" : namespace,
                    #"nodes"     : nodes,
                    "submitter" : submitter
                }
        argsEnc = urllib.urlencode(args)
        responseData = urllib.urlopen(self.endpoint, argsEnc).read() # XXX errorhandling?
        return responseData

class Query:
    def __init__(self):
        pass
api = SPARQLpediaAPI("mhermans", "passwd")
print api.find("Holger Knublauch")

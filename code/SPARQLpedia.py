#!/usr/bin/env python
# SPARQLpedia API documentation: http://sparqlpedia.org/api.html
# it is labled a "REST-based protocol", but GET & POST are equivalent...


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
        pass

class Query:
    def __init__(self):
        pass


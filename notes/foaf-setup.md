Foaf-profile recipe
====================

Four requirements:

* Stable, cool uri
* Dereferencable
* Not only rdf, but a html-version for humans/browsers when dereferencing
* and this without registering/commiting to a domain of my own.

Solution: a purl (permanent url), with Apache-content negotiation.

To coin a purl you register at purl.org, pick a stable refering url, pick a (variabele) url to which it should resolve and click submit. I chose "http://purl.org/net/mhermans-foaf", which refers to http://pinosa.studentenweb.org/webruimte/public/foaf" (webspace I have access to). This is not a permanent space (gone when I graduate), but this is no problem: I can switch hosts and update the location where my purl refers to.

The last url does not corresponds to a file in my webspace named "foaf". Instead I use Apache Rewrite-statements in an .htaccess-file to redirect agents dereferencing "http://purl.org/net/mhermans-foaf" a second time. This time the redirection depends on the content-type requested. If the agent arriving on "http://pinosa.studentenweb.org/webruimte/public/foaf" wants html, that is, he used an "Accept: text/html"-header, he is likely a human using a standard browser. If he requests rdf ("Accept: application/rdf+xml"), it is probabily a crawler or a semantic web-aware  browser like Tabulator. And we try to give both their choice.

This is achieved by the following snippet in a .htaccess-file:

    Rewrite
    Balala
    Bbbqsq

The "foaf.html" and "foaf.rdf" *do* exist, and are (finaly) sent to the agent who issued the request.

Question: Following "http://purl.org/net/mhermans-foaf" gives me a file. Does that URI refer to the file, or the person decribed in the file? To make usefull statements (especially statements like "I made this file") Resolving this ambiguity Now, For instance, I want to assert *I* fragment-identifiers ("#mh") do traverse all these redirections. So let's say I want to make assertions about my significant other (using her URI) and she's not interested in a foaf-document of her own.

The html-document provides a human readable version. This can be a complete "About me"-page, but for me it just needs to say "this is a page about me" so that persons following my purl get something less confusing then a blob of RDF/XML. One helpfull addition is providing a link from the html-page to the rdf-data. If a semantic web-aware browser/crawler encounters the url "http://pinosa.studentenweb.org/webruimte/public/foaf.html", it can follow its nose and still get to the rdf-data. Providing this link is straitforward. inside the <head>-section of the html-page "<link rel="meta" type="application/rdf+xml" title="FOAF" href="foaf.rdf" />" http://xmlns.com/foaf/spec/#sec-autodesc For a related mechanism, see HTTP Link header http://esw.w3.org/topic/LinkHeader

Practical tips (that worked for me):

For humans the turtle syntax is much more readable en editable than RDF/XML. The community standard appears to be serializing and publishing your profile in RDF/XML though. Tools that come with the redland libraries <link> for instance provide convenient roundtripping between syntaxes (see below for an example).

Use an foaf-generator <link>, or start from an existing foaf-profile:
    
    #!/usr/bin/bash
    $curl http://example-foaf-file-of-someone/foaf.rdf > foaf.rdf
    $rapper -i rdfxml -o turtle > foaf.ttl
    $vim foaf.ttl #modify all the properties, delete irrelevant ones.
    $rapper -i turtle -o rdfxml-abbrev > foaf.rdf

Test it in Tabulator <link>, Disco http://www4.wiwiss.fu-berlin.de/rdf_browser/



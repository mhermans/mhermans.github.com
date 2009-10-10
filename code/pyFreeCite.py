#!/usr/bin/python
import urllib,urllib2
#from xml.etree import ElementTree as ET
#import libxslt, libxml2
from lxml import etree
from  StringIO import StringIO

url = 'http://freecite.library.brown.edu/citations/create'
citations = ['Eliason, S.R., 1993. Maximum Likelihood Estimation. Sage, Newbury Park, CA.','Bryk, A.S, Raudenbush, S.W., 1992. Hierarchical Linear Models. Sage, Newbury Park, CA.', 'Hox, J.J., Maas, C.J.M., 2001. The accuracy of multilevel structural equation modeling with pseudobalanced groups and small samples. Structural Equation Modeling 8, 157-174.']

#data = urllib.urlencode(parameters) # This does not work: different keys expected; and FreeCite expects the same key.

param = []
for citation in citations:
    param.append('='.join(["citation[]", urllib.quote_plus(citation)]))
data = '&'.join(param)

headers = { 
    'Accept' : 'text/xml',
    'User-Agent' : 'pyFreeCite 0.1'
}
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request) # This request is sent in HTTP POST
#page = response.read(200000)
xml = etree.fromstring(response.read(20000))
data = xml.findall('citation')

#print(75*'-')
#for c in data:
#    print(etree.tostring(c))
#    print(75*'-')
#
#print(75*'=')

f = StringIO('''\
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:dc="http://purl.org/dc/"
    xmlns:bibo="http://purl.org/bibo/"
    xmlns:foaf="http://purl.org/foaf/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:str="http://exslt.org/strings"
    xmlns:exslt="http://exslt.org/common">

    <xsl:template match="/">
        <rdf:RDF>


        <xsl:for-each select="//citation">
            <bibo:Document>
                <xsl:if test="journal">
                    <dc:journal><xsl:value-of select="journal" /></dc:journal>
                </xsl:if>
                <xsl:if test="title">
                    <dc:title><xsl:value-of select="title" /></dc:title>
                </xsl:if>
                <xsl:if test="year">
                    <dc:published><xsl:value-of select="year" /></dc:published>
                </xsl:if>
                <xsl:if test="volume">
                    <bibo:volume><xsl:value-of select="volume" /></bibo:volume>
                </xsl:if>
                <xsl:if test="pages">
                    <xsl:variable name="pages" select="str:tokenize(pages,'-')"/>
                        <bibo:startpage>
                            <xsl:value-of select="$pages[1]"/>
                        </bibo:startpage>
                        <bibo:endpage>
                            <xsl:value-of select="$pages[2]"/>
                        </bibo:endpage>
                </xsl:if>

                <xsl:variable name="authornum" select = "count(authors/author)" />
                
                <xsl:if test="authors/author"><xsl:choose>
                    <!-- No Seq for single author? -->
                    <xsl:when test="$authornum = 1" >
                        <!--bibo:authorList-->
                        <bibo:contributor rdf:parseType="Resource">
                            <!--rdf:Seq-->
                                <xsl:for-each select="authors/author">
                                    <!--foaf:Agent-->
                                        <foaf:name><xsl:value-of select="." /></foaf:name>
                                    <!--/foaf:Agent-->
                                </xsl:for-each>
                            <!--/rdf:Seq-->
                        <!--/bibo:authorList-->
                        </bibo:contributor>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:for-each select="authors/author">
                            <xsl:variable name="auname" select = "." />
                            <bibo:contributor rdf:parseType="Resource">
<foaf:name><xsl:value-of select="." /></foaf:name>
                            </bibo:contributor>    
                        </xsl:for-each>
                    </xsl:otherwise>
                </xsl:choose></xsl:if>

            </bibo:Document>
        </xsl:for-each>
        </rdf:RDF>
    </xsl:template>
</xsl:stylesheet>''')
xslt_doc = etree.parse(f)
transform = etree.XSLT(xslt_doc)
result_tree = transform(xml)
print(etree.tostring(result_tree, pretty_print=True))
#print(75*'=')
#for c in data:
#    print(etree.tostring(c, pretty_print=True))

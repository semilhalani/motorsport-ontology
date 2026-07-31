import rdflib
from rdflib.graph import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, XML
from rdflib.plugins.stores.memory import Memory
 
# Configuring the end-point and constructing query.
# Notice the various SPARQL constructs we are making use of:
#
#   * PREFIX to bind prefixes in our query
#   * CONSTRUCT to build new individuals from our query
#   * OPTIONAL to indicate that some fields may not exist and that's OK
# 
#
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
    PREFIX ma: <http://www.semanticweb.org/samael/ontologies/2022/4/Car#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    PREFIX dbpprop: <http://dbpedia.org/property/>
      
    CONSTRUCT {
        ?motors rdf:type ma:Motorsport .
        ?motors ma:isServiceOf ?service .
        ?service rdf:type ma:Service .
        ?motors ma:isOccupationOf ?occupation .
        ?occupation rdf:type ma:Occupation .
        ?motors ma:isCategoryOf ?category .
        ?category rdf:type ma:Category .
        ?motors ma:isPurposeOf ?purpose .
        ?purpose rdf:type ma:Purpose .
        ?motors ma:isKnownFor ?knownFor .
        ?knownFor rdf:type ma:KnownFor .
        ?motors ma:isIndustryOf ?industry .
        ?industry rdf:type ma:Industry .
        ?motors ma:isGenreOf ?genre .
        ?genre rdf:type ma:Genre .
        ?motors ma:isEventsOf ?events .
        ?events rdf:type ma:Events .
        ?motors ma:hasUnion ?union .
        ?union rdf:type ma:Union .

        ?motors ma:region ?region .
        ?motors ma:first ?first .
        ?motors ma:firstlabel ?firstlabel .
        ?motors ma:name ?name .
        ?motors ma:olympic ?olympic .
    }
    WHERE{
        ?motors rdf:type dbpedia-owl:Activity .
        OPTIONAL {?motors ^dbo:service ?service} .
        OPTIONAL {?motors ^dbo:occupation ?occupation} .
        OPTIONAL {?motors ^dbp:category ?category} .
        OPTIONAL {?motors ^dbp:purpose ?purpose} .
        OPTIONAL {?motors ^dbo:knownFor ?knownFor} .
        OPTIONAL {?motors ^dbo:industry ?industry} .
        OPTIONAL {?motors ^dbo:genre ?genre} .
        OPTIONAL {?motors ^dbp:events ?events} .
        OPTIONAL {?motors ^dbp:events ?union} .

        OPTIONAL {?motors dbpedia-owl:region ?region} .
        OPTIONAL {?motors dbpedia-owl:first ?first} .
        OPTIONAL {?motors dbpedia-owl:firstlabel ?firstlabel} .
        OPTIONAL {?motors dbpedia-owl:name ?name} .
        OPTIONAL {?motors dbpedia-owl:olympic ?olympic} .
    } """
    
    
sparql.setQuery(construct_query)
sparql.setReturnFormat(XML)

# maeating the RDF store and graph
# We're telling the rdflib library to maeate a new graph and store it in memory (so, temporarily).
memory_store = Memory()
graph_id = URIRef("http://www.semanticweb.org/samael/ontologies/2022/4/Car#")
g = Graph(store = memory_store, identifier = graph_id)

# SPARQL queries can take some time to run, especially if the query is particularly
# large and you're grabbing very many items. 
#
# While experimenting we used the LIMIT construct in SPARQL to take
# only a couple of items, as in this way we can experiment with things without waiting
# ages for a query to complete.
print("  I might take some time, bear with  me...")

# merging results and saving the store
# running the query will return a valid RDFlib graph.
g = sparql.query().convert()

# We can parse files as valid RDFlib graphs too. When we do both of these things, they will be merged together.
g.parse("car.owl")

# You can open this file in protege and compare it to the existing `car.owl`
# ontology to see what we did. You could also open this in a text editor and have
# a poke around that way.
g.serialize("car_basic.owl", "xml")

print("  ...All done!")
print("")

import rdflib
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, XML
from rdflib.plugins.stores.memory import Memory
 
# configuring the end-point and constructing query
# the given construct query will add the data to the existing individuals 
# it will rather add new individual movies to the graph with the data from linkedmdb
# this is not an ideal solution but works fine with the Sparql query in the query_bonus.py.
# If you open the full_example.owl in Protege you will find out that the individuals 
# 1236,1237,1238,1239 are the movie data from linkedmdb.
sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
construct_query="""
     PREFIX ma: <http://www.semanticweb.org/samael/ontologies/2022/4/Car#>
     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
     PREFIX motor: <http://data.linkedmdb.org/resource/motorsport/>
     PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
     PREFIX dc: <http://purl.org/dc/terms/>
     prefix owl: <http://www.w3.org/2002/07/owl#>
      
      CONSTRUCT {
      ?motors rdf:type ma:Motorsport .
      ?motors ma:service ?service .
      ?motors ma:genre ?genre .
      ?genre owl:sameAs <https://dbpedia.org/page/Auto_Motor_und_Sport> .
      ?motors ma:region ?region
      }
       WHERE{
       ?motors rdf:type motor:motors .
       ?motors dc:genre ?genre .
       ?motors motor:service ?service .
       ?genre motor:genre "Auto Motor und Sport" .
       ?motors motor:region ?region .
       ?region rdfs:label ?region
       }"""

sparql.setQuery(construct_query)
sparql.setReturnFormat(XML)

# creating the RDF store and graph
memory_store = Memory()
graph_id = URIRef('http://www.semanticweb.org/samael/ontologies/2022/4/Car#')
g = Graph(store = memory_store, identifier = graph_id)

if False: 
    print("  I might take some time, bear with  me...")

    # merging results and saving the store 
    g = sparql.query().convert()
    g.parse("mcar_basic.owl")
    # the graph will be saved as movie_full.owl. You can open the file with Protege to inspect it.
    g.serialize("mcar_full.owl", "xml")

    print("  ...All done!")

else:
    # If you find a SPARQL endpoint that you want to use but it appears to be
    # down or otherwise nonfunctional, you can try to see if you can find a dump
    # of the ontology.
    #
    # For example, there is a full dump of the linkedmdb data available here:
    #   https://www.cs.toronto.edu/~oktie/linkedmdb/
    #
    # It's not included in this example because its 500mb and that's a bit too
    # much to be distributing on qmplus. We already know how to parse files into
    # a graph using RDFlib and we also know that we can write SPARQL queries against
    # those graphs.
    #
    # Knowing both of those things, you might realise that there's nothing stopping
    # you from downloading the dump from linkedmdb and trying to alter this example
    # to work against the local dump instead of the Web SPARQL endpoint.
    #
    # This is something you could do for your own coursework, as well. What is
    # important is you demonstrate that you can pull data from two sources
    # using SPARQL queries. Whether those queries run against a Web-based service
    # or an offline local file is not relevant.
    #
    # If you decide to experiment with this example script, don't forget to change
    # line 45 from `if False:` to `if True:` so the code will actually run. If
    # you did it right you won't see the message below printed in your console.
    print("  The endpoint used in this example 'http://data.linkedmdb.org/sparql'")
    print("  has been down for some time (years). You can't run the query, then,")
    print("  but you can still inspect the code and get an idea of what you might")
    print("  do yourself.")

print("")

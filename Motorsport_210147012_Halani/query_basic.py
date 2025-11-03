import rdflib

# This simple query grabs all motorsport cars with it's genre and service and sorts it out according to the genre.
query = """
PREFIX ma: <http://www.semanticweb.org/samael/ontologies/2022/4/Car#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
SELECT DISTINCT ?genre ?service
WHERE 
    {
        ?motors rdf:type ma:Motorsport .
        ?motors ma:isGenreOf ?genre .
        ?genre rdf:type ma:Genre .
        ?motors ma:isServiceOf ?service .
        ?service rdf:type ma:Service .
    } GROUP BY ?genre """


# Create an empty RDF graph and then parse our generated ontology into it.
g = rdflib.Graph()
g.parse("car_basic.owl", "xml")

print("graph has %s statements.\n" % len(g))

# formatting strings used in Python to nicely format a table and print the respective data.
print ("Genre", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "\t", "Service")
for x, y in g.query(query):
    print (x,"\t", "\t","\t", y)

print("")
print("  Try editing the code to run this query against 'car.owl' instead.")
print("  Notice how the query runs and a few results are returned. When")
print("  your ontology it can be handy to define a few individuals so you can")
print("  test your queries and perform some sanity checks. That way you can focus")
print("  your attention on writing the proper queries to populate the rest of")
print("  your ontology now you know what your individuals should look like.")
print("")

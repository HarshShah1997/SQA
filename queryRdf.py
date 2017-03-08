import rdflib

g = rdflib.Graph()

g.parse("myfile.rdf")
queryString = '''
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX quepy: <http://www.machinalis.com/quepy#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX yago: <http://dbpedia.org/class/yago/>
PREFIX fred: <http://www.ontologydesignpatterns.org/ont/fred/domain.owl#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>

SELECT DISTINCT ?x3 WHERE {
  ?x0 fred:runtimeOf ?x1.
  ?x1 rdf:type ?x2.
  ?x2 owl:equivalentClass dbr:Pulp_Fiction.
  ?x0 dul:hasDataValue ?x3.
}
'''

qres = g.query(queryString)

for row in qres:
    print(row)

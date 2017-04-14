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
PREFIX quant: <http://www.ontologydesignpatterns.org/ont/fred/quantifiers.owl#>

SELECT DISTINCT ?x1 WHERE {
  ?x0 rdf:type fred:BestPerformance.
  ?x0 fred:winOf ?x1.
  ?x0 fred:in ?x2.
  ?x2 rdf:type fred:60mHurdle.
  ?x2 quant:hasQuantifier quant:60m.
}
'''

qres = g.query(queryString)

for row in qres:
    print(row)

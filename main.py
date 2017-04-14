from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request
import quepy

app = Flask(__name__)
dbpedia = quepy.install("dbpedia")

@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        query = request.form['question']
        result = get_query(query)
    else:
        result = []
    return render_template("home.html", result=result)

def get_query(question):
    target, query, metadata = dbpedia.get_query(question)
    print(target)
    print(query)
    print(metadata)
    return query

def run_query(query):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)
    return results['results']['bindings']

    #for result in results["results"]["bindings"]:
    #print(result["label"]["value"])

if __name__ == '__main__':
    app.run(debug=True)

from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        query = request.form['query']
        result = run_query(query)
    else:
        result = []
    return render_template("home.html", result=result)

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

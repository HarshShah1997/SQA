from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, render_template, request
import quepy

app = Flask(__name__)
dbpedia = quepy.install("dbpedia")

@app.route("/", methods=["GET"])
def root():
    return render_template("home.html")

@app.route("/_generateQuery", methods=["POST"])
def generateQuery():
    if request.method == "POST":
        question = request.form['question']
        query = get_query(question)
        return str(query)

@app.route("/_executeQuery", methods=["POST"])
def executeQuery():
    if request.method == "POST":
        query = request.form['query']
        result = run_query(query)
        processed = process(result)
        return processed

def process(result):
    ans = ''
    for col in result:
        for key in col:
            ans += col[key]['value'] + '\n'
    return ans

def get_query(question):
    target, query, metadata = dbpedia.get_query(question)
    return query

def run_query(query):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results['results']['bindings']

    #for result in results["results"]["bindings"]:
    #print(result["label"]["value"])

if __name__ == '__main__':
    app.run(debug=True)

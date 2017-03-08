import fredlib
sentence = "The runtime of Pulp Fiction is 184 minutes." #write here your sentence
filename = "myfile.rdf" #a file for storing the Fred’s rdf graph
g = fredlib.getFredGraph(fredlib.preprocessText(sentence),filename)

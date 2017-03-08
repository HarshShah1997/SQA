import txt2rdf
import rdflib.extras.cmdlineutils as cmd
import rdflib.tools.rdf2dot as rdf2dot
import sys
import rdflib

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('PangoCairo', '1.0')

import xdot
from gi.repository import Gtk

def main():
    sentence = sys.stdin.read()
    if sentence.strip() == "":
        sentence = "Valentina gave Aldo a book by Charlie Mingus."

    generate(sentence)

def generate(sentence):

    filename = "myfile.rdf"
    g = txt2rdf.getFredGraph(txt2rdf.preprocessText(sentence),filename)

    g = rdflib.Graph()
    g.parse("myfile.rdf")

    output_file = open("myfile.dot", "w")
    rdf2dot.rdf2dot(g, output_file)
    output_file.close()

    window = xdot.DotWindow()
    window.open_file("myfile.dot")
    window.connect('delete-event', Gtk.main_quit)
    Gtk.main()

if __name__ == '__main__':
    main()


import fredlib
import rdflib.extras.cmdlineutils as cmd
import rdflib.tools.rdf2dot as rdf2dot
import sys
import rdflib

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('PangoCairo', '1.0')

import xdot
from gi.repository import Gtk

sentence = "The runtime of Pulp Fiction is 184 minutes." 
filename = "myfile.rdf"
g = fredlib.getFredGraph(fredlib.preprocessText(sentence),filename)

g = rdflib.Graph()
g.parse("myfile.rdf")

output_file = open("myfile.dot", "w")
rdf2dot.rdf2dot(g, output_file)
output_file.close()

window = xdot.DotWindow()
window.open_file("myfile.dot")
window.connect('delete-event', Gtk.main_quit)
Gtk.main()


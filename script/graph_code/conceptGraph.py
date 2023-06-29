from rdflib import *
from rdflib import OWL, RDF, RDFS

# maybe we can add concepts descriptions

conceptGraph = Graph()

namespace = "http://www.semanticweb.org/ghiot/ontologies/2023/5/chthuluConcepts"
chco = Namespace(namespace)
conceptGraph.bind(chco, "chco")

# INDIVIDUALS

BecomingWith = URIRef(namespace+"/BecomingWith")
GoVisit = URIRef(namespace+"/GoVisit")
Inheritance  = URIRef(namespace+"/Inheritance")
Ongoingness = URIRef(namespace+"/Ongoingness")
PlayingSF = URIRef(namespace+"/PlayingSF")
Politeness = URIRef(namespace+"/Politeness")
RenderCapable = URIRef(namespace+"/RenderCapable")
ResponseAbility = URIRef(namespace+"/ResponseAbility")
Storytelling = URIRef(namespace+"/Storytelling")
ThinkFrom = URIRef(namespace+"/ThinkFrom")
ThinkWith = URIRef(namespace+"/ThinkWith")

# CLASSES
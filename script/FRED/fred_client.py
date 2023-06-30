from fredclient import FREDClient, FREDParameters, FREDDefaults
from rdflib import Graph, Namespace

# fredclient
key = "227e3c3c-d1e6-3fe6-8c26-a9552ec901db";
fred_uri = "http://wit.istc.cnr.it/stlab-tools/fred"

def parse_paragraph(sentence):

    fredclient = FREDClient(fred_uri, key=key)
    fredparams = FREDParameters(semantic_subgraph=False)
    g = fredclient.execute_request(sentence, fredparams)

    # changing namespaces for readabilty
    
    role = Namespace("http://www.ontologydesignpatterns.org/ont/vn/abox/role/")
    sem = Namespace("http://ontologydesignpatterns.org/cp/owl/semiotics.owl#") #create a Namespace with the Namespace constructor method
    schema = Namespace("http://www.w3.org/2006/03/wn/wn30/schema/")
    earmark = Namespace("http://www.essepuntato.it/2008/12/earmark#")
    quant = Namespace("http://www.ontologydesignpatterns.org/ont/fred/quantifiers.owl#")
    dul = Namespace("http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#")
    pos = Namespace("http://www.ontologydesignpatterns.org/ont/fred/pos.owl#")
    fred = Namespace("http://www.ontologydesignpatterns.org/ont/fred/")
    boxer  = Namespace("http://www.ontologydesignpatterns.org/ont/boxer/boxer.owl#")
    boxing = Namespace("http://www.ontologydesignpatterns.org/ont/boxer/boxing.owl#")


    g.bind("role", role)
    g.bind("sem", sem)
    g.bind("schema", schema)
    g.bind("earmark", earmark)
    g.bind("quant", quant)
    g.bind("dul", dul)
    g.bind("pos", pos)
    g.bind("fred", fred)
    g.bind("boxer", boxer)
    g.bind("boxing", boxing)

    return g




# print(g.serialize(format="turtle"))

'''def parse_text(text):
    # split text in paragraphs
    paragraphs = []
    for paragraph in paragraphs:
        parse_paragraph(paragraph)'''

print(parse_paragraph('''She is a philosopher and a scientist who is allergic to denunciation and 
hungry for discovery, needy for what must be known and built together, 
with and for earthly beings, living, dead, and yet to come.'''))

# see what classes come out and align with tailored ontology
# join each paragraph graph together ANZI no I have to make a graph that organizes the superstructure of the book and for every paragraph points to its graph





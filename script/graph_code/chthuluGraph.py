from rdflib import *
from json import load
import pandas as pd

chthuluGraph = Graph()

#PREFIXES definition
chthulu = Namespace("http://www.semanticweb.org/ghiot/ontologies/2023/5/chthulucene") # for all ontology classes and properties
chthuluGraph.bind(chthulu, "chthulu")

rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#") #for type
chthuluGraph.bind(rdf, "rdf")

owl = Namespace("http://www.w3.org/2002/07/owl#") #for defining what is a Class and what is a Property etc..
chthuluGraph.bind(owl, "owl")

rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#") #for defining subClassOf
chthuluGraph.bind(rdfs, "rdfs")
#for dereferencing?
dbr = Namespace("http://dbpedia.org/resource/") 
dbo = Namespace("http://dbpedia.org/ontology/")
chthuluGraph.bind(dbr, "dbr")
chthuluGraph.bind(dbo, "dbo")

# dictionary of words to identify frames
framesLU = {"Collaborative_thinking" : ["thinks-with", "attunement"], 
            "Perception_active" : ["listened"], 
            "Coming_to_believe" : ["learned"], 
            "Studying" : ["studies"], 
            "Coming_up_with" : ["theorizes", "theory", "proposes"], 
            "Mental_stimulus_stimulus_focus" : ["interested in"], 
            "Cause_expansion" : ["enlarges", "dilates", "expands", "adds"], 
            "Being_in_category" : ["practice"], 
            "People_by_vocation" : ["who", "scientist"], 
            "Needing" : ["needy"]}
# dictionary of words to identify concepts
conceptsLU = {"ThinkWith": ["thinks-with", "kind of thinking", "built together"], 
              "GoVisit": ["going visiting"], 
              "RenderCapable" :["render each other capable"], 
              "Worlding" : ["worlding"], 
              "Ongoingness" : ["yet to come"]}
# list of vocations
vocation = ["artist", "designer", "philosopher", "scientist", "ornithologist", "ethologist", "scientist"]

# loading BookNLP outputs
# tokens
tokens = pd.read_csv("script\BookNLP\ch_7\ch_7.tokens", delimiter="\t")
entities = pd.read_csv("script\BookNLP\ch_7\ch_7.entities", delimiter="\t")

# load jsons to parse as intermediate step for creating graph:
with open("AgentiveEntities.json", "r", encoding="utf-8") as f:
  AgEntJson = load(f)

with open("Frames.json", "r", encoding="utf-8") as j:
  FramesJson = load(j)

#functions

def build_sentence(sentence_number):
    tokens = tokens.query(f"sentence_ID == {sentence_number}")
    sentence = list(tokens["word"])
    print(sentence)
    sentence = "".join(sentence)
    print(sentence)
    return sentence

def find_frame(sentence):
    frames = []
    for key, value in framesLU.items():
      for word in value:
         if word in sentence:
            frames.append(key)
    return frames

def find_concept(sentence):
    concepts = []
    for key, value in conceptsLU.items():
      for word in value:
         if word in sentence:
            concepts.append(key)
    return concepts



# triples for concepts





#print(chthuluGraph.serialize(format="ttl"))



























#use rdfs for subclassof etc

# 1 What are good practices to make kin?
cq1 = '''
PREFIX ns1: <http://www.semanticweb.org/ghiot/ontologies/2023/2/Chthulucene/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?subject 
WHERE {
  ?subject rdfs:subClassOf owl:ActivityConcept .
}
'''

cq2 = '''
PREFIX ns1: <http://www.semanticweb.org/ghiot/ontologies/2023/2/Chthulucene/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?obj ?superclass
WHERE {
  ?subj owl:someValuesFrom ?obj;
        rdf:type owl:Restriction .
    ?obj rdfs:subClassOf ?superclass .
 
}
'''


'''
resultCQ1 = chthuluGraph.query(cq1)
for el in resultCQ1:
  print(el)'''

'''resultCQ2 = chthuluGraph.query(cq2)
for el in resultCQ2:
    print(el)'''
from rdflib import *
from rdflib import RDF, RDFS, OWL
from json import load
import pandas as pd
import pprint


# =============================== PREFIXES definition ================================ #

# for all ontology classes and properties
global rdf #for type
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
#chthuluGraph.bind(rdf, "rdf")

global owlns 
owlns = "http://www.w3.org/2002/07/owl#"
owl = Namespace(owlns) #for defining what is a Class and what is a Property etc..
# chthuluGraph.bind(owl, "owl")

rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#") #for defining subClassOf
#chthuluGraph.bind(rdfs, "rdfs")

#for dereferencing?
'''dbr = Namespace("http://dbpedia.org/resource/") 
dbo = Namespace("http://dbpedia.org/ontology/")
chthuluGraph.bind(dbr, "dbr")
chthuluGraph.bind(dbo, "dbo")'''

# ========================== RESOURCES =========================== #

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

# loading BookNLP outputs and aligned first paragraph
# tokens
tokens = pd.read_csv("script\BookNLP\ch_7\ch_7.tokens", delimiter="\t")
alignment = pd.read_csv("script/graph_code/alignment.csv")

# ========================== FUNCTIONS =========================== #


# construct a sentence from BookNLP tokens
def build_sentence(sentence_number, tokens): 
    tokens = tokens.query(f"sentence_ID == {sentence_number}")
    sentence = list(tokens["word"])
    sentence = " ".join(sentence)
    #sentence = sentence.replace(" ,", ","). replace(" .", ".").replace(" :", ":").replace(" ;", ";")
    if "-" in sentence:
        sentence = sentence.replace(" - ", "-")
    return sentence


# checks if a Frame is evoked in a sentence
def find_frame(sentence): 
    frames = []
    for key, value in framesLU.items():
      for word in value:
         if word in sentence:
            frames.append(key)
    return frames


 # checks if a concept is evoked in a sentence
def find_concept(sentence, frame_inst, chthuluGraph ):
    concepts = []
    for key, value in conceptsLU.items():
        for word in value:
            if word in sentence:
                concepts.append(key)
    for concept in concepts:
        instance = URIRef(chthuluns+concept+"_1")
        # create triples to align with concepts ontology
        triple = (instance, URIRef(owlns+"sameAs"), URIRef(chthuluConcns+f"{concept}"))
        print(triple)
        # triple for chthuluGraph
        class_triple = (instance, RDF.type, URIRef(chthuluns+f"{concept}"))
        print(class_triple)
        evokedBy = (instance, URIRef(chthuluns+"isEvokedBy"), frame_inst)
        print(evokedBy)
        evokes = (frame_inst, URIRef(chthuluns+"evokes"), instance)
        print(evokes)
        #add triples
        chthuluGraph.add(triple)    
        chthuluGraph.add(class_triple)    
        chthuluGraph.add(evokedBy)
        chthuluGraph.add(evokes)        

    return chthuluGraph


# takes all triples describing classes hierarchy and object properties from the ontology RDF
def get_ontology_info(chthuluGraph): 
    
    chthuluOnt = Graph()
    chthuluOnt.parse("ontologies\Chthulucene7.ttl", format="ttl")
    chthulu = Namespace(chthuluns)
    chthuluOnt.bind(chthulu, "chthulu")
    print(str(len(chthuluOnt))+"==\n")

    #iterates over triples that have a specific property
    classes = chthuluOnt.triples((None, RDF.type, OWL.Class)) 
    hierarchy = chthuluOnt.triples((None, RDFS.subClassOf, None))
    objects = chthuluOnt.triples((None, RDF.type, OWL.ObjectProperty))

    for s, p, o in objects:
        all_obj_info = chthuluOnt.triples((s, None, None))
        for s, p, o in all_obj_info:
            chthuluGraph.add((s, p, o))

    for s, p, o in classes:
        chthuluGraph.add((s, p, o))
    
    for s, p, o in hierarchy:
        if isinstance(o, BNode) == False:
            chthuluGraph.add((s, p, o))

    #print(chthuluGraph.serialize(format="ttl"))      
    print(str(len(chthuluGraph))+"==\n")
    return chthuluGraph


# takes all triples fro concepts ontology rdf and adds them to main rdf
def get_concepts_info(chthuluGraph):
    conceptOnt = Graph()
    conceptOnt.parse("ontologies\ChthuluConcepts7.ttl", format="ttl")
    global chthuluConcns 
    chthuluConcns = "http://www.semanticweb.org/ghiot/ontologies/2023/5/chthuluConcepts#"
    global chco 
    chco = Namespace(chthuluConcns)
    conceptOnt.bind(chco, "chco")

    all_info = conceptOnt.triples((None, None, None))
    print(str(len(conceptOnt))+"==\n")
   
    for s, p, o in all_info:
       chthuluGraph.add((s, p, o))

    #print(chthuluGraph.serialize(format="ttl")) 
    print(str(len(chthuluGraph))+"==\n")
    return chthuluGraph


def find_superclass(subclass, chthuluGraph):
    concept_var = False

    triples = chthuluGraph.triples


# ================================= MAIN ========================== #

def main(tokens, alignment):
    i = 0

    chthuluGraph = Graph()
    global chthuluns 
    chthuluns = "http://www.semanticweb.org/ghiot/ontologies/2023/5/chthulucene#"
    global chthulu 
    chthulu = Namespace(chthuluns)
    chthuluGraph.bind(chthulu, "chthulu")


    chthuluGraph = get_ontology_info(chthuluGraph)
    print(str(len(chthuluGraph))+"\n=================================================")
    chthuluGraph = get_concepts_info(chthuluGraph)
    print(str(len(chthuluGraph)))

    


    # while loop to parse only the first paragraph, namely 9 sentences
    while i <= 9:
        sentence = build_sentence(i, tokens)
        print(sentence)

        # create Frame triples
        frames = find_frame(sentence)
        for frame in frames:
            info = alignment.query(f"F_LABEL == '{frame}'")

            for idx, row in info.iterrows():
                if row["FE_INSTANCE"].casefold() not in sentence.casefold():
                    info = info.drop(idx)
                    filtered_info = info

            for idx, row in filtered_info.iterrows():   
                # create individual and class type triple
                frame_instance = URIRef(chthuluns+frame+"_"+str(row["Token_ID_within_document"]))
                frame_type = (frame_instance, RDF.type, URIRef(chthuluns+f"{frame}"))
                chthuluGraph.add(frame_type)

                role_instance = URIRef(chthuluns+str(row["ROLE"])+"_"+str(row["Token_ID_within_document"]))
                role_type = (role_instance, RDF.type, URIRef(chthuluns+str(row["ROLE"])))
                chthuluGraph.add(role_type)

                if row["ENT_TYPE"] != "None":
                    arg_instance = URIRef(chthuluns+str(row["FE_INSTANCE"])+"_"+str(row["Token_ID_within_document"]))
                    arg_class = URIRef(chthuluns+str(row["ENT_TYPE"]))
                    arg_type = (arg_instance, RDF.type, arg_class)
                    chthuluGraph.add(arg_type)
                    
                # create involvesRole relation
                involvesRole = (frame_instance, URIRef(chthuluns+"involvesRole"), role_instance)
                print(involvesRole)
                chthuluGraph.add(involvesRole)
                print(chthuluGraph.serialize(format="ttl"))

                concept_var, graph = find_superclass(arg_class, chthuluGraph)

       

       
        i += 1
   



if __name__ == '__main__':
    main(tokens, alignment)


























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
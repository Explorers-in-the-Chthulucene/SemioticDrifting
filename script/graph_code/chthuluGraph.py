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
conceptsLU = {"ThinkWith": ["thinks-with", "thinks with", "thinking", "theory", "built together"], 
              "GoVisit": ["going visiting"], 
              "RenderCapable" :["capable", "competencies"], 
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
    return set(frames)


 # checks if a concept is evoked in a sentence
def find_concept(sentence, frame_inst, chthuluGraph):
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
        class_triple = (instance, RDF.type, URIRef(chthuluns+f"Concept"))
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

        print("\nthis is the length of chthulugraph after adding concept_type, concept_alignment, evokes, isEvokedBy IN FIND_CONCEPT FUNC\n")
        print(str(len(chthuluGraph))+"\n===============================================\n")
    return chthuluGraph


# takes all triples describing classes hierarchy and object properties from the ontology RDF
def get_ontology_info(chthuluGraph): 
    
    chthuluOnt = Graph()
    chthuluOnt.parse("ontologies\Chthulucene7.ttl", format="ttl")
    chthulu = Namespace(chthuluns)
    chthuluOnt.bind(chthulu, "chthulu")

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

    for triple in conceptOnt:
        chthuluGraph.add(triple)
    print("this is the length of conceptOnt\n")
    print(str(len(conceptOnt))+"\n========================================\n")
   
    #print(chthuluGraph.serialize(format="ttl")) 
    print("this is the length of chthuluGraph with concept statements before being returned\n")
    print(str(len(chthuluGraph))+"\n===============================================\n")
    return chthuluGraph


def find_superclass(subclass, instance, role_instance, chthuluGraph):
    temp = False
    # check if it's a concept and doesn't have a superclass
    currentclass = subclass.split("#")
    print(currentclass)

    if currentclass[1] == "Concept":
        temp = True
        conceptRole = (instance, URIRef(chthuluns+"conceptRole"), role_instance)
        print(conceptRole)
        chthuluGraph.add(conceptRole)
    
    else:     
        for s, p, o in chthuluGraph.triples((subclass, RDFS.subClassOf, None)):
            superclass = o.split("#")
            superclass = superclass[1]

            # create hasRole relation
            print(superclass)
            if superclass == "HumanProp" or superclass == "HumanComm" or superclass == "Animal" or superclass == "AgentiveEntity":
                agentiveRole = (instance, URIRef(chthuluns+"agentiveRole"), role_instance)
                print(agentiveRole)
                chthuluGraph.add(agentiveRole)
            
            if superclass == "Descriptor":
                descriptorRole = (instance, URIRef(chthuluns+"descriptorRole"), role_instance)
                print(descriptorRole)
                chthuluGraph.add(descriptorRole)
            
            if superclass == "Place":
                locationRole = (instance, URIRef(chthuluns+"locationRole"), role_instance)
                print(locationRole)
                chthuluGraph.add(locationRole)

    print("\n\n this is the length of chthuluGraph, adding one hasRole statement\n")
    print(str(len(chthuluGraph))+"\n===============================================\n")
    return temp, chthuluGraph


# ================================= MAIN ========================== #

def main(tokens, alignment):
    i = 5

    chthuluGraph = Graph()
    global chthuluns 
    chthuluns = "http://www.semanticweb.org/ghiot/ontologies/2023/5/chthulucene#"
    global chthulu 
    chthulu = Namespace(chthuluns)
    chthuluGraph.bind(chthulu, "chthulu")

    print("this is chthuluGraph len at the start\n")
    print(str(len(chthuluGraph))+"\n=================================================\n")

    chthuluGraph = get_ontology_info(chthuluGraph)
    print("this is chthuluGraph after importing triples from ontology\n")
    print(str(len(chthuluGraph))+"\n=================================================\n")
    chthuluGraph = get_concepts_info(chthuluGraph)
    print("this is chthuluGraph after importing the concepts RDF\n")
    print(str(len(chthuluGraph))+"\n====================================\n")


    # while loop to parse only the first paragraph, namely 9 sentences
    while i <= 9:
        sentence = build_sentence(i, tokens)
        print(sentence)

        # create Frame triples
        frames = find_frame(sentence)
        for frame in frames:
            concept_var = False
            info = alignment.query(f"F_LABEL == '{frame}'")

            for idx, row in info.iterrows():
                if row["FE_INSTANCE"].casefold() not in sentence.casefold():
                    info = info.drop(idx)
                    filtered_info = info

            filtered_info = info
            for idx, row in filtered_info.iterrows():   
                # FOR EACH ROW
                # create individual and class type triple
                frame_instance = URIRef(chthuluns+frame+"_"+str(row["Token_ID_within_document"]))
                frame_type = (frame_instance, RDF.type, URIRef(chthuluns+f"{frame}"))
                chthuluGraph.add(frame_type)

                role_instance = URIRef(chthuluns+str(row["ROLE"])+"_"+str(row["Token_ID_within_document"]))
                role_type = (role_instance, RDF.type, URIRef(chthuluns+str(row["ROLE"])))
                chthuluGraph.add(role_type)

                  # create involvesRole relation
                involvesRole = (frame_instance, URIRef(chthuluns+"involvesRole"), role_instance)
                chthuluGraph.add(involvesRole)
                #print(chthuluGraph.serialize(format="ttl"))

                if row["ENT_TYPE"] != "None":
                    arg_instance = URIRef(chthuluns+str(row["FE_INSTANCE"])+"_"+str(row["Token_ID_within_document"]))
                    arg_class = URIRef(chthuluns+str(row["ENT_TYPE"]))
                    arg_type = (arg_instance, RDF.type, arg_class)
                    chthuluGraph.add(arg_type)
                    
                    print("\n======================\nthis is the length of chthuluGraph, after adding frame_type, arg_type, role_type and involvesRole\n")
                    print(str(len(chthuluGraph))+"\n===============================================\n")

                    print("we are looking for the superclass of this class:\n")
                    print(arg_class+"\n")
                    print("this class is the type of the current row's instance which is\n")
                    print(arg_instance)

                    temp, chthuluGraph = find_superclass(arg_class, arg_instance, role_instance, chthuluGraph)
                    if temp == True:
                        concept_var = True
                       
                    # create concept relations 
                    if concept_var == True and arg_class[-3:] == "ept":
                      
                        # create triples to align with concepts ontology
                        for key, value in conceptsLU.items():
                            for word in value:
                                if word == row["FE_INSTANCE"]:
                                    print(key)
                                    conc_sameas = (arg_instance, URIRef(owlns+"sameAs"), URIRef(chthuluConcns+key))
                                    print(conc_sameas)
                        
                        # triple for chthuluGraph                    
                        evokedBy = (arg_instance, URIRef(chthuluns+"isEvokedBy"), frame_instance)
                        print(evokedBy)
                        evokes = (frame_instance, URIRef(chthuluns+"evokes"), arg_instance)
                        print(evokes)
                        #add triples
                        chthuluGraph.add(conc_sameas)     
                        chthuluGraph.add(evokedBy)
                        chthuluGraph.add(evokes)    
                    
                        print("\nthis is the length of chthulugraph after adding concept_alignment, evokes, isEvokedBy\n")
                        print(print(str(len(chthuluGraph))+"\n===============================================\n"))


            # after iterating on rows see if, even without having a role, the frame evokes a concept
            if concept_var == False: 
                
                chthuluGraph = find_concept(sentence, frame_instance, chthuluGraph)
                print("\nthis is the length of chthulugraph after adding concept_alignment, evokes, isEvokedBy IN FIND_CONCEPT FUNC\n")
                print(print(str(len(chthuluGraph))+"\n===============================================\n"))
                    
        i += 1

    return chthuluGraph.serialize(destination="script\graph_code\cthuluGraph.ttl")



if __name__ == '__main__':
    main(tokens, alignment)


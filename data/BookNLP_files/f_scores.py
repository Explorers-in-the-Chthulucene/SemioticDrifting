# file for tools accuracy evaluation (f-scores)
# this file contains lists of entities to be recognized
named_chars =  []
per = ["Vinciane Despret", "singing blackbird", "Thelma Rowell", "Soay sheep", "Hannah Arendt", "Miss Manners", "Amotz Zahavi", "Arabian babblers", "Jocelyne Porcher", "Isabelle Stengers", "Virginia Woolf", "Beatriz da Costa"  ]
# oddper = [{"Curiosity": "Curiosity always leads its practitioners a bit too far off the path, and that way lie stories."}]
general = ["birds", "scientists", "observers", "a polite inquirer", "humans", "critters", "apparatuses", "farmers", "breeders", "pigs", "cows", "animals", "women", "camels", "father", "sons", "old man", "the heirs", "beasts", "anyone listening", "anyone attuned", "storyteller", "people", "racing pigeons, also called carrier pigeons", "fanciers", "collegues", "Matali Crasset", "colombophiles", "visitors", "avian voyageurs"]
gpe = ["Cerisy", "Southern California", "Baghdad", "Damascus", "New Yorl", "Berlin", "France", "Iran", "California", "Caudry"]
loc = ["Negev desert", "southern Israeli desert" "a world of propositions not available before", "nonindustrial French farms", "Western worlds", "village", "the mortal world", "markets", "places of travel and labour", "Worlds-at-stake", "Gobi desert", "chateau", "public spaces", "innovative pigeon lofts", "leisure park", "ecological park", "farmland", "nature reserve"]
org = ["The Beauvois association of carier pigeon fanciers"]

concepts = [{"haraway" : ["vocation", "going visiting", "thinking-with", "rendering-capable", "worlding", "live and die", "multispecies flourishing", "fabulate", "response-ability", "earth-bound", "make a fuss", "cat's cradle", "ongoingness", "string figure games", "companion species", "past, present, yet to come (so far)", "they stay with the trouble", "speculative fabulation" ]}, {"Despret": ["the virtue of politeness", "anthropo-zoo-genesis", "make a fuss", "thinking from a heritage = loyalty", "start from", "inherit"]}, {"Arendt" : ["going-visiting", "make a fuss"]}, {"Birds and scientists": ["becoming-with", "create narratives"]} ]

# Viniciane Despret is a philosopher and a scinetist
# Thelma Rowell is an ethologist
# Israeli ornithologist Amotz Zahavi

{"going visiting" : ["Visiting is not an easy practice; it demands the ability to find others actively interesting, even or especially others most people already claim to know all too completely, to ask questions that one's interlocutors truly find interesting, to cultivate the wild virtue of curiosity, to retune one's ability to sense and respond—and to do all this politely!",
                     "Visiting is a subject- and object-making dance, and the choreographer is a trickster",
                     "Visiting might be risky, but it is definitely not boring."],
 "politeness" :  "Despret's sort of politeness does the energetic work of holding open the possibility that surprises are in store, that something interesting is about to happen, but only if one cultivates the virtue of letting those one visits intra-actively shape what occurs.",
 "thinking" : "what thinking can possibly mean in the civilization in which we find ourselves",
"situated stories" : " it draws deeply from another virtue that is sometimes confused with loyalty, namely, “thinking from” a heritage. She is tuned to the obligations that inhere in starting from situated histories, situated stories. She retells the parable of the twelve camels in order to tease out what it means to 'start from,' that is, to 'remain obligated with respect to that from which we speak, think, or act. It means to let ourselves learn from the event and to create from it.'",
"inherit" : "an act 'which demands thought and commitment. An act that calls for our transformation by the very deed of inheriting'",
"ongoingness": "that is, nurturing, or inventing, or discovering, or somehow cobbling together ways for living and dying well with each other in the tissues of an earth whose very habitability is threatened"}


# this is a draft on ways different concepts might be related

causality = ["leads to", "provoke", "reasons of",   ]
hyponomy = ["is a",]
hyperonomy = [""]

# ways different agents can be related

encounters = ["provocation", "mutual observation", "rendering each-other capable", "becoming-with", "working-with", ]

# this is a draft of different practices connected to agents:

dict = [("Desprets", "go visiting", "asking questions", "politeness", "curiosity", "observation", "narration", "literal collaborations"), ("Zahavi", "asking questions", "experiments with", "look at the world with"), ("Arabian blabbers", "altruism", "dancing"), ("breeders", "live and die")]

# Women Who Make a Fuss: The Unfaithful Daughters of Virginia Woolf
# Three Guineas
# parable of the twelve camels
# PigeonBlog

# art-technology-environmental-activist
# art-design-activist practices

# Matali Crasset's Capsule (objects belong to someone, or are created to someone through an activity)

# artist and industrial designer, philosopher and scientist, Zahavi?, 
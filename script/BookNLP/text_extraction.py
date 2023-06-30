# for accuracy evaluation (f-scores)
# lists of entities to be recognized
per = ["Vinciane Despret", "singing blackbird", "Thelma Rowell", "Soay sheep", "Hannah Arendt", "Miss Manners", "Amotz Zahavi", "Arabian babblers", "Jocelyne Porcher", "Isabelle Stengers", "Virginia Woolf", "Beatriz da Costa"  ]
per_general = ["birds", "scientists", "observers", "a polite inquirer", "humans", "critters", "apparatuses", "farmers", "breeders", "pigs", "cows", "animals", "women", "camels", "father", "sons", "old man", "the heirs", "beasts", "anyone listening", "anyone attuned", "storyteller", "people", "racing pigeons, also called carrier pigeons", "fanciers", "collegues", "Matali Crasset", "colombophiles", "visitors", "avian voyageurs"]
gpe = ["Cerisy", "Southern California", "Baghdad", "Damascus", "New Yorl", "Berlin", "France", "Iran", "California", "Caudry"]
loc = ["Negev desert", "southern Israeli desert" "a world of propositions not available before", "nonindustrial French farms", "Western worlds", "village", "the mortal world", "markets", "places of travel and labour", "Worlds-at-stake", "Gobi desert", "chateau", "public spaces", "innovative pigeon lofts", "leisure park", "ecological park", "farmland", "nature reserve"]
org = ["The Beauvois association of carier pigeon fanciers"]

# add coref Giusy

# lexical units for recognizing concepts and frames (!only first paragraph)
FramesLU = {"Collaborative_thinking" : ["thinks-with", "attunement"], "Perception_active" : ["listened"], "Coming_to_believe" : ["learned"], "Studying" : ["studies"], "Coming_up_with" : ["theorizes", "theory", "proposes"], "Mental_stimulus_stimulus_focus" : ["interested in"], "Cause_expansion" : ["enlarges", "dilates", "expands", "adds"], "Being_in_category" : ["practice"], "People_by_vocation" : ["who", "scientist"], "Needing" : ["needy"]}
RolesInFrames = ["Thinker_1_in_Collaborative_thinking", 
                    "Thinker_1_in_Collaborative_thinking", 
                    "Manner_in_Collaborative_thinking", 
                    "Perceiver_agentive_in_Perception_active", 
                    "Phenomenon_in_Perception_active","Location_in_Perception_active", 
                    "Cognizer_in_Coming_to_believe", "Content_in_Coming_to_believe",
                    "Evidence_in_Coming_to_believe",
                    "Student_in_Studying",
                    "Subject_in_Studying",
                    "Manner_in_Studying",
                    "Cognizer_in_Coming_up_with",
                    "Idea_in_Coming_up_with",
                    "Experiencer_in_Mental_stimulus_stimulus_focus",
                    "Stimulus_in_Mental_stimulus_stimulus_focus",
                    "Manner_in_Mental_stimulus_stimulus_focus",
                    "Agent_in_Cause_expansion",
                    "Cause_in_Cause_expansion",
                    "Item_in_Cause_expansion",
                    "Purpose_in_Cause_expansion",
                    "Category_in_Being_in_category",
                    "Item_in_Being_in_category",
                    "Person_in_People_by_vocation",
                    "Persistent_characteristic_in_People_by_vocation",
                    "Cognizer_in_Needing",
                    "Requirement_in_Needing",
                    "Consequences_in_Needing"]

conceptsLU = {"ThinkWith": ["thinks-with", "kind of thinking", "built together"], "GoVisit": ["going visiting"], "RenderCapable" :["render each other capable"], "Worlding" : ["worlding"], "Ongoingness" : ["yet to come"]}

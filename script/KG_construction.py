from rdflib import Graph, Namespace
import pandas as pd

entities = pd.read_csv("script\BookNLP\ch_7\ch_7.entities", delimiter="\t")
tokens = pd.read_csv("script\BookNLP\ch_7\ch_7.tokens", delimiter="\t")

sub_frame = tokens.query("sentence_ID == 4")

def find_coref(token_id, entities):
    possible_matches = entities.query(f"start_token = {token_id}") #starts looking for tokens skipping all rows BUT IT'S WRONG 
    #devo cercare row in cui start token  == token_id, se non si trova cerco
    # def closest(lst, K):     
    #return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

    for idx, row in possible_matches.iterrows():
        tokens_in_ent = list(range(row["start_token"], row["end_token"]+1))
        if token_id in tokens_in_ent:
            return row["COREF"]
        if row["start_token"] > token_id:
            return None

#print(find_coref(73, entities))

for idx, row in sub_frame.iterrows():
    token_id = row["token_ID_within_document"]
    find_coref(token_id, entities)


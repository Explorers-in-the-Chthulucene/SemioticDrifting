import pandas as pd
import pprint
import os

cwd = os.getcwd()
print(cwd)

df = pd.read_csv("distant_reading/ChthuluceneDR/Chthulucene.tokens", delimiter="\t")
pprint(df)
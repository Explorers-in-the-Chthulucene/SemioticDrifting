from pprint import pprint
#import nltk
#nltk.download('framenet_v17')
from nltk.corpus import framenet as fn
from nltk.corpus.reader.framenet import PrettyList
from operator import itemgetter

#f = fn.frame(200)
f = fn.frames(r'Coming_to_believe')
#id_list = PrettyList(sorted(fn.lus(r'help'), key=itemgetter('ID')))
#for item
id_list = PrettyList(sorted(f, key=itemgetter('ID')))

for id in id_list:
    print(id)
'''print(f.name)
print(f.definition)
print(len(f.lexUnit))
pprint(sorted([x for x in f.FE]))
pprint(f.frameRelations)'''


# x.sort(key=itemgetter('ID'))



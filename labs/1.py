from operator import itemgetter
import json
import nltk
from pprint import pprint
with open('tweets.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

# print(data[0])
counts = {}
for i in range(0, len(data)):
    a = dict(data[i])
    words = nltk.word_tokenize(a['text'])
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
sor = dict((sorted(counts.items(), key=itemgetter(1), reverse=True))[:10])
# print (sor)
for item, key in sor.items():
    print(item, "\t", key)
# pprint(sor)

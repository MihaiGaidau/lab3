from operator import itemgetter
import json
import nltk
from pprint import pprint

cuvint = input("give the begin word: ")

with open('tweets.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

# print(data[0])
counts = {}
for i in range(0, len(data)):
    a = dict(data[i])
    words = nltk.word_tokenize(a['text'])
    for i in range(0, len(words) - 1):
        if words[i] == cuvint:
            word = words[i + 1]
            if word not in counts:
                counts[word] = 0
            counts[word] += 1
sor = dict((sorted(counts.items(), key=itemgetter(1), reverse=True))[:3])

pprint(sor)

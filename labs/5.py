from operator import itemgetter
import json
import nltk
from pprint import pprint

cuvint = input("give the begin off the word: ")

with open('tweets.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

# print(data[0])
counts = {}
for i in range(0, len(data)):
    a = dict(data[i])
    words = nltk.word_tokenize(a['text'])
    for word in words:
        if len(word) >= len(cuvint) and word[:len(cuvint)] == cuvint:
            if word not in counts:
                counts[word] = 0
            counts[word] += 1
sor = dict((sorted(counts.items(), key=itemgetter(1), reverse=True))[:3])

pprint(sor)

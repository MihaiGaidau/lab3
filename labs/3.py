from operator import itemgetter
import json
import nltk
from pprint import pprint
import time
# from dateutil import parser
import timestring
with open('tweets.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

cuvint = input("give a word: ")
counts = {}

for i in range(0, len(data)):
    a = dict(data[i])
    words = nltk.word_tokenize(a['text'])
    if len(str(timestring.Date(a["created_at"]).month)) == 2:
        fdate = str(timestring.Date(a["created_at"]).year) + str(timestring.Date(a["created_at"]).month)
    else:
        fdate = str(timestring.Date(a["created_at"]).year) + '0' + str(timestring.Date(a["created_at"]).month)
    for word in words:
        if word == cuvint:
            if fdate not in counts:
                counts[fdate] = 0
            counts[fdate] += 1
counts = dict((sorted(counts.items(), key=itemgetter(0), reverse=False)))
pprint(counts)
# sor = dict((sorted(counts.items(), key=itemgetter(1), reverse=True))[:10])
# print ((sorted(counts.values(), reverse=True))[:10])
# pprint(sor)

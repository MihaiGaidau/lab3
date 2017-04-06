import json
import nltk
from pprint import pprint
from operator import itemgetter
with open('tweets.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

counts = {}
likes = {}
retweets = {}
was = {}
for i in range(0, len(data)):
    a = dict(data[i])
    words = []
    for word, pos in nltk.pos_tag(nltk.word_tokenize(a['text'])):
        if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
            words.append(word)
    for item, key in was.items():
        was[item] = 0
    for word in words:
        if word not in counts:
            counts[word] = 0
            was[word] = 0
        counts[word] += 1
        if was[word] == 0:
            was[word] = 1
            if word not in likes:
                likes[word] = 0
            if word not in retweets:
                retweets[word] = 0
            likes[word] += int(a["likes"])
            retweets[word] += int(a["retweets"])

# pprint(likes["program"])
# print(retweets["program"])
# pprint(counts)
for name, nr in counts.items():
    counts[name] = round(counts[name] * (1.4 + retweets[name]) * (1.2 + likes[name]), 3)

# pprint(counts)
counts = dict((sorted(counts.items(), key=itemgetter(1), reverse=True))[:10])
# pprint(sorted(counts.values(), reverse=True
pprint(counts)

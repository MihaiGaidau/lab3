# nStr = '000123000123123'
# print(nStr.count('123'))
from operator import itemgetter
import nltk
sentence = "let's play the banana ass zebra zebra zebra zebra game for three times, football, youtube banana banana gama game"
words = sentence.split()
counts = {}
words = []
for word, pos in nltk.pos_tag(nltk.word_tokenize(sentence)):
    if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
        words.append(word)
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

# print(counts)
print (sorted(counts.values(), reverse=True))[:10]
sor = sorted(counts, key=counts.get, reverse=True)
sor = sorted(counts.items(), key=itemgetter(1), reverse=True)
print(sor)


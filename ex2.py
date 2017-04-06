import json
from pprint import pprint
with open('tweets.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

# pprint(data)
# print(data)
print(len(data))
a = dict(data[0])
print(a['text'])

# sentence = "hai acasa mai vasile mai acum vasile"
# words = sentence.split()
# counts = {}
# for word in words:
#     if word not in counts:
#         counts[word] = 0
#     counts[word] += 1

# print(counts)

# json_data = open("tweets.json").read()
# data = json.loads(json_data)
# print(data)

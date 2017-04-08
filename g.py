import nltk
import json
from pprint import pprint
from operator import itemgetter
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
import numpy as np
with open('tweets.json',encoding='utf-8') as data_file:
  dictionary = json.loads(data_file.read())
enter_word = input("Give the word:")
new_dictionary={}
for i in range(0,len(dictionary)):
    input_one = dict(dictionary[i])
    d = int((str(input_one['created_at'])[:7]).replace("-", ""))
    m = input_one['text']
    n = nltk.word_tokenize(m)
    for word in n:
        if word == enter_word:
            if d not in new_dictionary:
                new_dictionary[d] = 0
            new_dictionary[d] += 1
pprint(new_dictionary)


datas = []
nr =[]
for item, key in new_dictionary.items():
    datas.append(str(item))
# print(datas)
datas = sorted(datas)
# print(datas)
timp = []
for i in range(0, len(datas)):
    nr.append(new_dictionary[int(datas[i])])
    datas[i] = str(datas[i])
    # timp.append(time.strptime(datas[i], "%Y%m"))

# pprint(timp)
# print(datas)
# print(nr)
# plt.bar(datas, nr, color="blue")
y_pos = np.arange(len(datas))

plt.bar(y_pos, nr, align='center', alpha=0.5)
# plt.plot(datas, nr)
plt.xticks(y_pos, datas)
plt.ylabel('Usage')
plt.xlabel('data')
plt.title('the use ')

plt.show()

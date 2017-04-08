from operator import itemgetter
import json
import nltk
from pprint import pprint
import time
# from dateutil import parser
import timestring
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
import numpy as np
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

plotly.tools.set_credentials_file(username='MihaiGaidau', api_key='gXPsYKcMRKHFpGWNnq2w')
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

# y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
# N = len(y)
# x = range(N)
width = 1
datas = []
nr =[]
for item, key in counts.items():
    datas.append(str(item))
    nr.append(key)

datas = sorted(datas)
timp = []
for i in range(0,len(datas)):
    nr[i] = counts[datas[i]]
    datas[i] = str(datas[i])
    # timp.append(time.strptime(datas[i], "%Y%m"))

# pprint(timp)
print(datas)
print(nr)
# plt.bar(datas, nr, color="blue")
y_pos = np.arange(len(datas))

plt.bar(y_pos, nr, align='center', alpha=0.5)
# plt.plot(datas, nr)
plt.xticks(y_pos, datas)
plt.ylabel('Usage')
plt.title('the use of "love"')

plt.show()
# fig = plt.gcf()
# plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')
# sor = dict((sorted(counts.items(), key=itemgetter(1), reverse=True))[:10])
# print ((sorted(counts.values(), reverse=True))[:10])
# pprint(sor)

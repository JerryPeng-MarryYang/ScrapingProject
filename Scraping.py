from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import ssl
import re
import csv
import requests
import time
import random
ssl._create_default_https_context = ssl._create_unverified_context
def SavePicture(MovieName):
    params ={'q':MovieName,'cat':'1002'}
    r = requests.post('https://www.douban.com/search', data = params)
    bs = BeautifulSoup(r.text, 'html.parser')
    list = bs.findAll('img', {'src':re.compile('.*.jpg')})
    list = list[:1]
    for line in list:
        if '/' in MovieName:
            MovieName = MovieName.replace('/','_')
        urlretrieve(line['src'], r'./img/%s.jpg'%MovieName)
        print(line)
        print("................"+MovieName + "  图片已经下载...................")

def OpenFile(FileName, start, end):
    csvFile = open(FileName, 'r')
    r = csv.reader(csvFile)
    l = list(r)[start:end]
    return l

mov = OpenFile('movies.csv', 1, 9125)
x = 0
for line in mov:
    x += 1
    print(line)
    SavePicture(line[1])
    time.sleep(random.uniform(0, 2))
    if x == 50:
        x = 0
        time.sleep(random.uniform(30, 50))

print('...............图片下载完成..........................')


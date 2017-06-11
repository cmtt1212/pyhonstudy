#-*- coding:utf-8 -*-
import re
import requests
from Tools.scripts.treesync import raw_input

word = raw_input("What do you want to have: ")
s_word = str(word)
url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&lm=-1&v=flip';

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)

i=0


for miao in pic_url:
    print(miao)
    try:
        pic= requests.get(miao,timeout=5)
    except requests.exceptions.ConnectionError:
        print('ConnectionErr')
        continue
    string = 'C:\\Users\\Tony\\Desktop\\pic\\'+str(i)+'.jpg'
    picFile = open(string,'wb')
    picFile.write(pic.content)
    picFile.close()
    i += 1


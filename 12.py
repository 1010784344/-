#coding=utf-8
import urllib
import requests
from bs4 import BeautifulSoup



if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/4888149054'

    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text)
    ee = soup.select('.BDE_Image')
    cc = []
    for dd in ee:
        cc.append(dd['src'])
    print cc

    t= 1
    for image in cc:
        urllib.urlretrieve(image,"C:\Users\Administrator\Desktop\jpg\%s.jpg"%t)
        t = t + 1
#coding=utf-8
import urllib
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'https://bbs.hupu.com/5752143.html'

    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text)
    ee = soup.select('img')
    cc = []
    for dd in ee:
        cc.append(dd['src'])
    print cc
    print len(cc)
    t = 1

    for image in cc:
        urllib.urlretrieve(image, "C:\Users\Administrator\Desktop\jpg\hupu\%s.jpg" % t)
        t = t + 1
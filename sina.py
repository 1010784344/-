#coding=utf-8
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    # 获取数据
    url = 'http://news.sina.com.cn/china/'
    res = requests.get(url)
    res.encoding = 'utf-8'
    res = res.text

    # 处理数据
    soup = BeautifulSoup(res)
    # print soup.select('.news-item')
    for news in  soup.select('.news-item'):
        # 一边判断一边查看很有必要，之前就遇到过一个问题，明明有很多图片却只爬了两张图片，应该是有空的情况存在
        # 没有添加判断
        if len(news.select('h2'))>0:
            h2 = news.select('h2')[0].text
            href = news.select('a')[0]['href']
            time = news.select('.time')[0].text
            print time,h2,href
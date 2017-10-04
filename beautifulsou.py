#coding=utf-8

import requests


if __name__ == '__main__':
    sin_url = 'http://news.sina.com.cn/china/'
    sin = requests.get(sin_url)
    sin.encoding = 'utf-8'
    print sin.text
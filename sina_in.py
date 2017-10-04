#coding=utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import re
import json
reload(sys)
sys.setdefaultencoding('utf-8')

def get_commt(url):
    id = re.search('doc-i(.+).shtml', url)
    url_id = id.group(1)

    # js的链接是有动过手脚的，为了通用，把最后的js的变量给删了（两次获取到的数据源是一样的），以下是原链接
    # 每个js链接只是中间部分的id和最后的js变量不一样，其他都一样
    # http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fymenmt6585922&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1506520036646_27398114
    js = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-%s&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'%url_id
    res = requests.get(js)
    res.encoding = 'utf-8'
    comm = res.text.lstrip('var data=')
    com = json.loads(comm)
    return com['result']['count']['total']

def get_detail(url):
    result = {}
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text)

    title = soup.select('#artibodyTitle')[0]

    result['title'] = title.text

    Time = soup.select('.time-source')[0].contents[0].strip()
    # 将字符串的日期解成datetime格式
    tt = datetime.strptime(Time,u'%Y年%m月%d日%H:%M')
    # 将datetime格式转化为我们自己规定的字符串
    result['Time'] = tt.strftime(u'%Y-%m-%d')

    result['sour'] = soup.select('.time-source span a')[0].text

    # result['article'] = ' '.join([tt.text.strip() for tt in soup.select('#artibody p')[:-1]])
    try:
        result['edit'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：')

    except:
        result['edit'] = ''
    result['comment'] = get_commt(url)

    return result

if __name__ == '__main__':
    # 获取数据
    url = 'http://news.sina.com.cn/o/2017-10-02/doc-ifymmiwm3811180.shtml'

    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text)

    #获取文章内容拼接
    # red = get_detail(url)
    #
    # for key in red:
    #     print key, red[key]


    # 获取新闻评论数封装
    # get_commt(url)



    # 获取新闻id
    # news = 'http://news.sina.com.cn/o/2017-09-24/doc-ifymenmt6585922.shtml'
    # news_id = news.split('/')[-1].lstrip('doc-i').rstrip('.shtml')
    # print news_id
    # 正则获取新闻id
    # news = 'http://news.sina.com.cn/o/2017-09-24/doc-ifymenmt6585922.shtml'
    # id = re.search('doc-i(.+).shtml',news)
    # print id.group(1)





    # 获取评论，因为是js的，所以如下获取不到：mem = soup.select('#commentCount1M')流程是先在network的xhr
    # 里找寻，没有的话去js里看，地毯式搜索找到评论对应的js插件，在preview和Response都可以看到，preview更容易观察
    # url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=' \
    #       'comos-fymenmt6585922&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=' \
    #       'loader_1506437239229_94757987'
    # res = requests.get(url)
    # res.encoding = 'utf-8'
    # comm = res.text.lstrip('var loader_1506437239229_94757987=')
    # # print comm
    #
    # com = json.loads(comm)
    # print com['result']['count']['total']


    # # 获取编辑
    # edit = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    # print edit

    # # 获取内文
    # aa = ' '.join([tt.text.strip() for tt in soup.select('#artibody p')[:-1]])
    # print aa


    # # 获取来源
    # sour = soup.select('.time-source span a')[0].text
    # print sour



    # # 获取时间
    # Time = soup.select('.time-source')[0].contents[0].strip()
    #
    # # 将字符串的日期解成datetime格式
    # tt = datetime.strptime(Time,u'%Y年%m月%d日%H:%M')
    # print tt
    # # 将datetime格式转化为我们自己规定的字符串
    # ss = tt.strftime(u'%Y-%m-%d')
    # print ss


    # 获取标题
    title = soup.select('#artibodyTitle')[0]
    print title.text










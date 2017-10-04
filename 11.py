#-*- coding:utf-8 -*-
import urllib

# print dirprin
# print help(urllib.urlopen)
# url = 'http://dormousehole.readthedocs.io/en/latest/installation.html#installation'
url = 'http://news.sina.com.cn/c/nd/2017-10-02/doc-ifymmiwm3810841.shtml'
html =  urllib.urlopen(url)
# print html.read()
# print dir(html)
# 获取头部信息
# print html.info()
# 获取状态码
print html.getcode()
# 关闭文件
# html.close()
#网页抓取，下载网页
urllib.urlretrieve(url,'C:\Users\Administrator\Desktop\hh.html')

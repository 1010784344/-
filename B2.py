#coding=utf-8

from bs4 import BeautifulSoup

if __name__ == '__main__':

    aa = '''<html>

<body> 

<p>
<a class = '456' href="/index.html">本文本</a> 是一个指向本网站中的一个页面的链接。</p>

<p><a id = '123' href="http://www.microsoft.com/">本文本</a> 是一个指向万维网上的页面的链接。</p>

</body>
</html>
'''
    soup = BeautifulSoup(aa)
    bb = soup.select('a')[0]
    # bb= soup.select('a')[0]['href']
    print type(bb)
    # for key in bb:
    #     print bb[key]
#coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import time

def crawl_detail(id):

    url = 'https://www.lagou.com/jobs/%s.html'%id
    headers = {
        'Host':'www.lagou.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

    }

    res = requests.get(url,headers= headers)
    res.encoding = 'utf-8'


    soup = BeautifulSoup(res.text)
    soup = soup.select('.job_bt')
    soup = soup[0].text

    return soup

def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'

    head = {
        'Host': 'www.lagou.com', 'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
        'User-Agent': 'Mozil la/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        , 'X-Anit-Forge-Code': '0', 'X-Anit-Forge-Token': 'None', 'X-Requested-With': 'XMLHttpRequest',
        'Cookie':'user_trace_token=20170607071833-75d0c1fb-4b0e-11e7-b2cb-525400f775ce; LGUID=20170607071833-75d0c8b5-4b0e-11e7-b2cb-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEF44D3395E7772BD7FF07EEBA0C2FC3105; PRE_UTM=m_cf_cpt_360_pc; PRE_HOST=www.so.com; PRE_SITE=http%3A%2F%2Fwww.so.com%2Flink%3Fm%3DaUx27bmvZzK3gxE6xSw4uTRxfI3jN6xdRDvvke1O8yPv6d2MclQTyzOUxpxZwEqjAaEuqvkmtDmWwu4fKYlUX%252F7CKyddTaNyDVwUIsO6Rj%252F4FT5m%252B62WbDEvnF5l0nnImi8HHcQ%253D%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_360_pc; TG-TRACK-CODE=index_search; _gid=GA1.2.61666233.1507338492; _ga=GA1.2.241137602.1496791526; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507111331,1507185209,1507338492,1507420013; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1507420043; LGSID=20171008074101-fa46221f-abb8-11e7-bff2-525400f775ce; LGRID=20171008074132-0c66ec08-abb9-11e7-bff2-525400f775ce; SEARCH_ID=dcb327b0af5b45819329d7496e95545d'

    }
    # form = {
    #     'first':'true',
    #     'pn':'1',
    #     'kd':'python'
    # }
    #
    # res = requests.get(url,headers = head ,data=form)
    # res.encoding = 'utf-8'
    # # 将获取到的直接转换成字典
    # result = res.json()
    #
    # print result
    # fin_result = json.dumps(result['content']['positionResult']['result'])
    #
    # with open('lagou.json','w') as fp:
    #     fp.write(fin_result.encode('utf-8'))

    fin_result = []
    # 循环获取每一页的数据
    for x in range(1, 3):
        form = {
            'first': 'true',
            'pn': str(x),
            'kd': 'python'
        }
        res = requests.get(url, headers=head, data=form)
        res.encoding = 'utf-8'

        # 将获取到的直接转换成字典

        result = res.json()


        page_result = result['content']['positionResult']['result']



    #获取职位详情的操作
    #     for position in page_result:
    #         pos_dic = {
    #             'positionName': position['positionName'],
    #             'workYear': position['workYear'],
    #             'salary': position['salary'],
    #             'district': position['district'],
    #             'companyFullName': position['companyFullName']
    #
    #         }
    #         pos_id = position['positionId']
    #         pos_dic['pos_detail'] = crawl_detail(pos_id)
    #
    #
    #         fin_result.append(pos_dic)
    #         time.sleep(3)
    # fin_result = json.dumps(fin_result)
    #
    # with open('lagou.json', 'w') as fp:
    #     fp.write(fin_result.encode('utf-8'))


        fin_result.extend(page_result)
        time.sleep(3)
    fin_result = json.dumps(fin_result)

    with open('lagou.json', 'w') as fp:
        fp.write(fin_result.encode('utf-8'))


if __name__ == '__main__':
    # id = '2966647'
    #
    # bb = crawl_detail(id)

    main()
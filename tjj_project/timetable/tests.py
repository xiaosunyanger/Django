from django.test import TestCase

# Create your tests here.
from bs4 import BeautifulSoup
import requests

url = 'http://www.zfjw.xupt.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N253508'
headers = {
    'Cookie': 'JSESSIONID=206ADCBE5711CAC78865ED17E38456CB',
    'Host': 'www.zfjw.xupt.edu.cn',
    'Referer': 'http://www.zfjw.xupt.edu.cn/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N253508&layout=default&su=03163126',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
# res = requests.post(url, data={ 'xnm': 2019,'xqm': 12}, headers=headers).json()
# print(res)
# 学年： xnm 学期： xqm 第一学期是3 第二学期是12
xn_list = [2017, 2018, 2019]
xq_list = [3, 12]
for xn in xn_list:
    for xq in xq_list:
        data = {
            'xnm': xn,
            'xqm': xq
        }
        res = requests.post(url, data=data, headers=headers).json()
        if xn == 2019 and xq == 12:
            kb_list = res['sjkList']
            for kb in kb_list:
                d = {
                    'year': res['xsxx']['XNMC'],
                    'semester': res['xsxx']['XQMMC'],
                    'course_title': kb['kcmc'],
                    'weeks': kb['qsjsz'],
                    'campus': '',
                    'place_class': '',
                    'teacher': kb['xm'],
                    'teaching_class': '',
                    'assessment_method': '',
                    'course_hours': '',
                    'week_hours': '',
                    'total_hours': '',
                    'credit': '',
                }
                print(d)
        else:
            kb_list = res['kbList']
            for kb in kb_list:
                d = {
                    'year': res['xsxx']['XNMC'],
                    'semester': res['xsxx']['XQMMC'],
                    'course_title': kb['kcmc'],
                    'weeks': kb['zcd'],
                    'campus': kb['xqmc'],
                    'place_class': kb['cdmc'],
                    'teacher': kb['xm'],
                    'teaching_class': kb['jxbmc'],
                    'assessment_method': kb['khfsmc'],
                    'course_hours': kb['kcxszc'],
                    'week_hours': kb['zhxs'],
                    'total_hours': kb['zxs'],
                    'credit': kb['xf'],
                }
                print(d)

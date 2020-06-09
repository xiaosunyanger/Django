# coding: utf-8
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from news.models import News
import requests
headers = {
            'Referer': 'http://www.xiyou.edu.cn/xwzx/xyyw/493.htm',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
parser = 'html.parser'
news_map = {
    '西邮要闻': 'http://www.xiyou.edu.cn/xwzx/xyyw.htm',  # 共494页
    '综合新闻': 'http://www.xiyou.edu.cn/xwzx/zhxw.htm',  # 共318页
    '媒体关注': 'http://www.xiyou.edu.cn/xwzx/mtgz.htm'  # 共191页
}
page_map = {
    '西邮要闻': 495,  # 共494页
    '综合新闻': 319,  # 共318页
    '媒体关注': 192  # 共191页
}
# 获取前100页新闻
s = 'http://www.xiyou.edu.cn/info'


class Command(BaseCommand):
    def handle(self, *args, **options):
        for k, v in news_map.items():
            for num in range(page_map[k], page_map[k] - 100, -1):
                try:
                    if num < page_map[k]:
                        v = news_map[k].replace('.htm', '/{}.htm'.format(num))
                    res = requests.get(v, headers=headers)
                    res.encoding = 'utf-8'
                    soup = BeautifulSoup(res.text, parser)
                    title_lis = soup.find_all('a', class_='c44380')
                    date_lis = soup.find_all('span', class_='c44380_date')
                    for i in range(len(title_lis)):
                        try:
                            news_url = title_lis[i]['href']
                            if '..' in title_lis[i]['href']:
                                news_url = s + title_lis[i]['href'].split('info')[1]
                            data = {
                                'news_title': title_lis[i]['title'],
                                'news_type': k,
                                'news_time': date_lis[i].get_text().strip(),
                                'news_content': '',
                                'news_url': news_url
                            }
                            print(k, date_lis[i].get_text().strip(), title_lis[i]['title'], news_url)
                            News.objects.create(**data)
                        except Exception as e:
                            continue
                except Exception as e:
                    continue


import requests
import re
from bs4 import BeautifulSoup



class GetNews:

    def get_html(self, index_url):
        r = requests.get(index_url)
        r.encoding = 'UTF-8'
        return r.text

    def get_page_url(self, html):
        news_list = []
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'}

        for news in re.compile(r'.*?<a(.*?)</a>.*?').findall(html):
            # print(news)

            # 新闻标题，链接
            for result in re.compile(r'href=\'(.*?).html\'.*?title=\'(.*?)\'').findall(news):
                title = result[1]
                url = 'http://www.cidp.edu.cn' + result[0] + '.html'
                try:
                    print('get:', title, url)
                    page_info = requests.get(url, headers=header)
                except requests.exceptions:
                    continue
                page_info.encoding = 'UTF-8'
                page_content, pub_time = GetNews().get_news_content(url=url)
                news_list.append({'url': url, 'title': title, 'page_content': page_content, 'pub_time': pub_time})

        return news_list

    def get_news_content(self, url):
        page = requests.get(url)
        page.encoding = 'UTF-8'
        html = page.text
        public_time = re.compile(r'.*?<meta name="PubDate" content="(.*?)">').findall(page.text)
        soup = BeautifulSoup(html, 'lxml')
        page_list = []
        for p in soup.find_all('p'):
            str = ''
            # print(p)
            # 拿到 a 标签里的图片链接
            for a in p.find_all('a'):
                pic_url = 'http://www.cidp.edu.cn' + a['href']
                page_list.append({'pic': pic_url})
                continue

            # 段落文字
            page_content = str.join(p.stripped_strings)
            page_list.append({'content': page_content})

        return page_list[:-4], public_time


    def save_news(self, news_list):
        for news in news_list:
            print(news)

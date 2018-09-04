from django.test import TestCase
from tools.searchNews import GetNews
# from news.models import News

# Create your tests here.

s = GetNews()

html = s.get_html(index_url='http://www.cidp.edu.cn/col/col52/index.html?pageNum=1&uid=17343')
news = s.get_page_url(html)

print(news)
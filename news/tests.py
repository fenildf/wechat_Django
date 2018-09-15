from django.test import TestCase
from tools.searchNews import GetNews
from tools.IdriverManage import Search
# from news.models import News

# Create your tests here.

g = GetNews('http://www.fzxy.edu.cn/col/col52/index.html?uid=17343&pageNum=2')
html = g.get_html()
g.get_page(html)
from django.test import TestCase
from tools.searchNews import GetNews
from tools.IdriverManage import Search
# from news.models import News
from search import models

# Create your tests here.

g = GetNews()
html = g.get_page_content('www.cidp.edu.cn/art/2018/9/13/art_52_89878.html')
g.get_page(html)

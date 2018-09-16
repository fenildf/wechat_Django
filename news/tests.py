from django.test import TestCase
from tools.searchNews import GetNews
from tools.IdriverManage import Search
# from news.models import News

# Create your tests here.

g = GetNews()
g.get_page_content('http://www.cidp.edu.cn/art/2018/6/11/art_52_87573.html')

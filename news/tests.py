from django.test import TestCase
from tools.searchNews import GetNews
from tools.IdriverManage import Search
# from news.models import News

# Create your tests here.

d = Search()
# d.time_table('165041131', '19981202')
d.term_grade('165041131', '19981202')

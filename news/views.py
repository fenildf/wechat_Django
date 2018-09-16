from django.shortcuts import render
from django.http import HttpResponse
from tools.searchNews import GetNews
import json
# Create your views here.

g = GetNews()


def content(request):
    print(request.GET['content'])
    url = request.GET['content']
    news_content = g.get_page_content(url)

    return HttpResponse(json.dumps({
        'news_content': news_content
    }))

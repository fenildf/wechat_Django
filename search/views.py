from django.shortcuts import render
from django.http import HttpResponse
from tools.webcontent import get_grade, open_page, get_grade_result, get_timetable_result, get_timetable
import json
import time


# Create your views here.

def index(request):
    # data = json.loads(request.body.decode('utf-8'))
    # sid = data.get('sid')
    # pwd = data.get('sid')
    # print(sid, pwd)
    return HttpResponse('Django test')


def grade(request):
    listData1 = []
    listData2 = []
    data = []
    body = json.loads(request.body.decode('utf-8'))
    sid = body.get('sid')
    pwd = body.get('pwd')
    print(sid,pwd)

    try:
        try:
            html = get_grade(open_page(sid, pwd))
            data = get_grade_result(html)
        except:
            return 'e'
    except:
        return HttpResponse(
            json.dumps({
                'statusCode': 300
            })
        )

    if len(data) == 2:
        listData1 = data[0]
        listData2 = data[1]
    elif len(data) == 1:
        listData1 = data[0]
    else:
        listData1 = []
        listData2 = []

    print(sid, pwd)
    print(listData1,listData2)

    return HttpResponse(json.dumps({
        'list1': listData1,
        'list2': listData2,
    }))


def calendar(request, sid, pwd):
    pass


def time_table(request):
    # try:
    body = json.loads(request.body.decode('utf-8'))
    sid = body.get('sid')
    pwd = body.get('pwd')
    print(sid,pwd)
    html = get_timetable(open_page(sid, pwd))
    term, data = get_timetable_result(html)
    # except:
    #     return HttpResponse(
    #         json.dumps({
    #             'statusCode': 300
    #         })
    #     )

    print(data)

    return HttpResponse(
        json.dumps({
            'term': term,
            'data': data
        })
    )

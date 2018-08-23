from django.shortcuts import render
from django.http import HttpResponse
from tools.webcontent import get_grade, open_page, get_grade_result, get_timetable_result, get_timetable
import json
import time


# Create your views here.


def grade(request, sid, pwd):
    listData1 = []
    listData2 = []
    data = []

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
    print(listData1)
    print(listData2)

    print(sid, pwd)
    time.sleep(5)

    return HttpResponse(json.dumps({
        'list1': listData1,
        'list2': listData2,
    }))


def calendar(request, sid, pwd):
    pass


def time_table(request, sid, pwd):
    try:
        html = get_timetable(open_page(sid, pwd))
        data = get_timetable_result(html)
    except:
        return HttpResponse(
            json.dumps({
                'statusCode': 300
            })
        )

    print(sid, pwd)

    return HttpResponse(
        json.dumps({
            'data': data
        })
    )

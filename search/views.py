from django.shortcuts import render
from django.http import HttpResponse
from tools.webcontent import Driver
from selenium.common import exceptions
import json
import time


# Create your views here.

def index(request):
    # data = json.loads(request.body.decode('utf-8'))
    # sid = data.get('sid')
    # pwd = data.get('sid')
    # print(sid, pwd)
    return HttpResponse('Django test Welcome')


def grade(request):
    listData1 = []
    listData2 = []
    try:
        body = json.loads(request.body.decode('utf-8'))
        sid = body.get('sid')
        pwd = body.get('pwd')
        d = Driver(sid, pwd)
        try:
            d.open_page()
            html = d.get_grade()
            data = d.get_grade_result(html)
            if len(data) != 2:
                listData1 = data[0]
                listData2 = data[1]
            elif len(data) == 1:
                listData1 = data[0]
            print(listData1, listData2)
            return HttpResponse(json.dumps({
                'list1': listData1,
                'list2': listData2,
            }))
        except exceptions.UnexpectedAlertPresentException:
            print('学号或密码错误')
            return HttpResponse(
                json.dumps({
                    'statusCode': 300
                })
            )
        except TypeError:
            print('获取成绩失败')
            return HttpResponse(
                json.dumps({
                    'statusCode': 500,
                    'info': '获取成绩失败，请稍后重试'
                })
            )
        except exceptions.WebDriverException:
            print('selenium error')
            return HttpResponse(
                json.dumps({
                    'statusCode': 500,
                    'info': '服务器出现了问题'
                })
            )
        finally:
            print('销毁')
            d.driver.quit()
    except exceptions.WebDriverException:
        print('selenium error')
        return HttpResponse(
            json.dumps({
                'statusCode': 500,
                'info': '服务器出现了问题'
            })
        )


def calendar(request, sid, pwd):
    pass


def time_table(request):
    body = json.loads(request.body.decode('utf-8'))
    sid = body.get('sid')
    pwd = body.get('pwd')
    term = []
    result = []
    print(sid, pwd, 'timetable')
    d = Driver(sid, pwd)
    try:
        try:
            d.open_page()
            html = d.get_timetable()
            result = d.get_timetable_result(html)
            print(result)
            return HttpResponse(
                json.dumps({
                    'term': term,
                    'data': result
                }))
        except exceptions.UnexpectedAlertPresentException:
            print('学号或密码错误')
            return HttpResponse(
                json.dumps({
                    'statusCode': 300,
                }))
        except TypeError:
            print('获取成绩失败, type error')
            return HttpResponse(
                json.dumps({
                    'statusCode': 500,
                    'info': '获取成绩失败，请稍后重试'
                }))
        except exceptions.WebDriverException:
            print('selenium error2, dean problem')
            return HttpResponse(
                json.dumps({
                    'statusCode': 500,
                    'info': '服务器出现了问题'
                }))
        finally:
            print('销毁进程')
            d.driver.quit()
    except exceptions.WebDriverException:
        print('selenium error1, network problem')
        return HttpResponse(
            json.dumps({
                'statusCode': 500,
                'info': '服务器出现了问题'
            }))
    finally:
        print('销毁进程')
        d.driver.quit()

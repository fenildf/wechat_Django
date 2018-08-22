from django.shortcuts import render
from django.http import HttpResponse
from tools.webcontent import getcontent
import json
import time

# Create your views here.


def grade(request, sid, pwd):
        listData1 = []
        listData2 = []
        data = [[{'code': '150347', 'name': '操作系统', 'property_name': '必修', 'number': '08', 'credit': '4', 'mark_value': '93', 'GPA': '4.3', 'ranking': '1 / 50'}, {'code': '150698', 'name': '大学英语Ⅲ', 'property_name': '必修', 'number': '30', 'credit': '2', 'mark_value': '69', 'GPA': '1.9', 'ranking': '29 / 50'}, {'code': '950001', 'name': '高等数学学位考试（理工类）', 'property_name': '专任选', 'number': '100', 'credit': '0', 'mark_value': '0', 'GPA': '0', 'ranking': '-'}, {'code': '150459', 'name': '经济学原理', 'property_name': '必修', 'number': '01', 'credit': '3', 'mark_value': '78', 'GPA': '2.8', 'ranking': '40 / 96'}, {'code': '150459', 'name': '经济学原理', 'property_name': '必修', 'number': '01', 'credit': '3', 'mark_value': '78', 'GPA': '2.8', 'ranking': '40 / 96'}, {'code': '150007', 'name': '毛泽东思想和中国特色社会主义理论体系概论', 'property_name': '必修', 'number': '01', 'credit': '4', 'mark_value': '81', 'GPA': '3.1', 'ranking': '52 / 96'},{'code': '150375', 'name': '数据库原理', 'property_name': '必修', 'number': '01', 'credit': '4', 'mark_value': '83', 'GPA': '3.3', 'ranking': '18 / 51'}, {'code': '150691', 'name': '线性代数', 'property_name': '必修', 'number': '07', 'credit': '2', 'mark_value': '73', 'GPA': '2.3', 'ranking': '64 / 97'}, {'code': '150010', 'name': '形势与政策（3）', 'property_name': '必修', 'number': '12', 'credit': '0', 'mark_value': '优秀', 'GPA': '4.5', 'ranking': '1 / 96'}, {'code': '150002', 'name': '职业生涯与发展规划', 'property_name': '必修', 'number': '16', 'credit': '2', 'mark_value': '良好', 'GPA': '3.5', 'ranking': '29 / 96'}, {'code': '450009', 'name': '中国古建筑欣赏与设计', 'property_name': '公选', 'number': '01', 'credit': '2', 'mark_value': '60', 'GPA': '1', 'ranking': '99 / 119'}, {'code': '951038', 'name': '足球(秋)', 'property_name': '必修', 'number': '01', 'credit': '1', 'mark_value': '88', 'GPA': '3.8', 'ranking': '8 / 19'}]]
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
        # return HttpResponse(status=404)












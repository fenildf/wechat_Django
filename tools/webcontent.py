from selenium import webdriver
import random
import time
import re


def start_driver():
    # 启动 Firefox , 可优化
    t = time.time()
    options = webdriver.FirefoxOptions()
    options.set_headless()
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(firefox_options=options)
    print('driver', time.time() - t)
    return driver


def open_page(id, pwd):
    driver = start_driver()
    t = time.time()
    driver.get('http://jwauth.cidp.edu.cn/Login.aspx')
    name = driver.find_element_by_name('TextBoxUserName')
    password = driver.find_element_by_name('TextBoxPassword')
    name.clear()
    password.clear()
    name.send_keys(id)
    password.send_keys(pwd)
    print('login', time.time() - t)
    try:
        driver.find_element_by_name('ButtonLogin').click()
        jw_url = "http://jwauth.cidp.edu.cn/NoMasterJumpPage.aspx?URL=JWGL"
        driver.get(jw_url)
        print('openpage', time.time() - t)
    except:
        return 0
    return driver


def get_grade(driver):
    t = time.time()
    mark_url = 'http://jw.cidp.edu.cn/Teacher/MarkManagement/StudentAverageMarkSearchFZ.aspx'
    driver.get(mark_url)
    print('openpage', time.time() - t)
    # 显性等待，(driver, 超时时长， 调用频率， 异常忽略)
    # WebDriverWait(driver, 15, 0.5).until(EC.frame_to_be_available_and_switch_to_it('year1'))

    grade_html = driver.find_element_by_id('DivCon2').get_attribute('innerHTML')

    print('find', time.time() - t)
    # driver.find_element_by_id('year1').click()
    # HTML = driver.find_element_by_id('DivCon2')
    driver.close()
    return grade_html


def get_timetable(driver):
    t = time.time()
    table_url = 'http://jw.cidp.edu.cn/Student/CourseTimetable/MyCourseTimeTable.aspx'
    driver.get(table_url)
    time.sleep(3)
    term = driver.find_element_by_id('lblSemester').get_attribute('innerHTML')
    iframe = driver.find_element_by_id('iframeTimeTable')
    driver.switch_to_frame(iframe)
    table_html = driver.find_element_by_id('tableMain').get_attribute('innerHTML')
    print('find', time.time() - t)
    driver.close()
    return term+table_html


def get_grade_result(html):
    result = re.compile(r'.*?([\u4e00-\u9fa5]+).*?<tr><td(.*?)</tbody></table>.*?', re.S).findall(html)

    term = []
    for terms in result:
        lists = []
        mark = re.compile(r'.*?">(.*?)</td>.*?', re.S).findall(terms[1])
        # lists.append(term)
        l = [i for i in mark]
        for list in [l[i:i + 9] for i in range(0, len(l), 9)]:
            dict = {}
            dict['code'] = list[0]
            dict['name'] = list[1]
            dict['property_name'] = list[2]
            dict['number'] = list[3]
            dict['credit'] = list[4]
            dict['mark_value'] = list[5]
            dict['GPA'] = list[6]
            dict['ranking'] = list[7]
            lists.append(dict)
        term.append(lists)
    return term


def get_timetable_result(html):
    result = re.compile(r'.*?<tr>(.*?)</tr>.*?', re.S).findall(html)
    term = re.compile(r'(.*?)学期', re.S).findall(html)[0] + '学期'
    list = []
    class_list = []
    class_set = []
    n = [1, 3, 6, 8, 11]
    m = 0

    # 留下有用行
    for i in result:
        if (m in n):
            list.append(i)
        m += 1

    # 匹配每行中的有课部分
    for index in list:
        class_name = re.compile(r'.*?rowspan="(.*?)">.*?').findall(index)
        class_set.append(class_name)

        for content in list:
            data = re.compile(r'.*?<td rowspan="2">(.*?)</td>', re.S).findall(content)
            a = 0
            for i in data:
                dict = {}
                a += 1
                cname = re.compile(r'class="spLUName">《(.*?)》</span>').findall(i)
                week = re.compile(r'class="spWeekInfo">(.*?)</span>').findall(i)
                room = re.compile(r'class="spClassroom">(.*?)</span>').findall(i)
                teacher = re.compile(r'class="spTeacherName">(.*?)</span>').findall(i)
                building = re.compile(r'class="spBuilding">(.*?)</span>').findall(i)
                method = re.compile(r'class="spDelymethodName.*?>(.*?)</span>').findall(i)

                dict['class_name'] = cname[0]
                dict['class_room'] = room[0]
                dict['week_info'] = week[0]
                dict['teacher'] = teacher[0]
                dict['building'] = building[0]
                dict['method'] = method[0]
                dict['color'] = random.randint(0, 12)

                if (len(cname) == 2):
                    dict['class_room2'] = room[1]
                    dict['building2'] = building[1]
                    dict['week_info2'] = week[1]
                class_list.append(dict)

    n = 0
    week = []

    # 遍历分布的二维数组，将其与课程对应
    for a in class_set:
        classes = []
        for i in a:

            # 2 为有课位置，将其代替成数据，1 放入空 dict
            if (i == '2'):
                class_dict = class_list[n]
                n += 1
            else:
                class_dict = {}
            classes.append(class_dict)

        # 分布的数组变成了一周的数据
        week.append(classes)

    c = 0
    search_result = []

    # 用7个 list 来装七天的数据， 将按时间分布的信息转置成按星期分布
    for i in range(7):
        m = []
        for a in week:
            m.append(a[c])
        search_result.append(m)
        c += 1

    return term, search_result

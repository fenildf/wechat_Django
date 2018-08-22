from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re


def start_driver():
    # 启动 Firefox , 可优化
    options = webdriver.FirefoxOptions()
    options.set_headless()
    options.add_argument('--disable-gpu')

    driver = webdriver.Firefox(firefox_options=options, )
    return driver


def getcontent(id, pwd):
    t = time.time()

    # 启动浏览器
    driver = start_driver()

    print('diver')
    print(time.time() - t)

    print('open page')
    try:
        driver.get('http://jwauth.cidp.edu.cn/Login.aspx')
        name = driver.find_element_by_name('TextBoxUserName')
        password = driver.find_element_by_name('TextBoxPassword')
        name.clear()
        password.clear()
        name.send_keys(id)
        password.send_keys(pwd)
        print(time.time() - t)
        driver.find_element_by_name('ButtonLogin').click()
    except:
        return

    print('click')
    print(time.time() - t)

    jwurl = "http://jwauth.cidp.edu.cn/NoMasterJumpPage.aspx?URL=JWGL"
    markurl = 'http://jw.cidp.edu.cn/Teacher/MarkManagement/StudentAverageMarkSearchFZ.aspx'

    driver.get(jwurl)

    # driver.wait.until(EC.presence_of_all_elements_located((By.ID, 'divSpeedWay')))

    driver.get(markurl)


    # 显性等待，(driver, 超时时长， 调用频率， 异常忽略)
    # WebDriverWait(driver, 15, 0.5).until(EC.frame_to_be_available_and_switch_to_it('year1'))

    # driver.find_element_by_id('year1').click()
    html = driver.find_element_by_id('DivCon2').get_attribute('innerHTML')

    # HTML = driver.find_element_by_id('DivCon2').text

    # driver.find_element_by_id('year1').click()
    # HTML = driver.find_element_by_id('DivCon2')
    driver.close()

    result = re.compile(r'.*?([\u4e00-\u9fa5]+).*?<tr><td(.*?)</tbody></table>.*?', re.S).findall(html)

    term = []
    for terms in result:
        lists = []
        mark = re.compile(r'.*?">(.*?)</td>.*?', re.S).findall(terms[1])
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

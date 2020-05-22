from gevent import monkey
monkey.patch_all()

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import  WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

import pkg_resources.py2_warn
import random
import csv
import  requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import gevent
from gevent.queue import Queue

urlQ= Queue()
ua = UserAgent()

pro = 0
len_= 30
infoFlow = {}

def get_cookie():
    url = 'http://www.pigai.org/'
    self_user = '16733208014'
    self_psw = '16733208014'

    options = ChromeOptions()
    options.add_argument('--headless')
    api = Chrome(options=options)

    # login
    api.get(url)
    WebDriverWait(api, 30).until(EC.presence_of_all_elements_located)
    user = api.find_element_by_id('username').send_keys(self_user)
    bak = api.find_element_by_id('lg_logo').click()
    psw = api.find_element_by_id('password').send_keys(self_psw)
    login_btn = api.find_element_by_id('ulogin').click()
    cookies_api = api.get_cookies()

    # 获取cookie
    cookies = {
        'Cookie':'',
    }
    cookie_dir = ';'.join\
    ([item['name'] + '=' + item['value'] for item in cookies_api])

    cookies['Cookie'] = cookie_dir

    api.quit()
    return cookies

def get_title(cookies):
    global  pro
    while not urlQ.empty():
        target = urlQ.get_nowait()

        headers = {'user-agent' : ua.random}
        res = requests.get(target, headers=headers, cookies=cookies)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, 'html.parser')
        try:
            title = soup.find('div', attrs={'id':'timu'}).text.strip()
            intro = soup.find('div', attrs={'id':'request_y'}).text.strip()

            infoFlow.update(
                {
                    intro:title
                }
            )
            now_len_ = len(list(infoFlow.keys()))
            print('[{}] {}'.format(now_len_,intro))
            if now_len_ % 5 == 0 :
                draw()
            if now_len_ >= len_:
                break
        except Exception as e:
            pass

def draw():
    with open('批改网作文题.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Intro'])

        intro = list(infoFlow.keys())
        title = list(infoFlow.values())

        for i in range(len(title)):
            writer.writerow([title[i], intro[i]])

def bbr():
    global  len_

    #构写url，入队
    code_pool = [random.randint(1798298, 1798498) for _ in range(100) ]
    for code in code_pool :
        url = 'http://www.pigai.org/?c=v2&a=write&rid={}'.format(code)
        print(url)
        urlQ.put_nowait(url)

    #获取cookie
    cookie = get_cookie()

    #开启协程
    task_list = []
    for x in range(20):
        task = gevent.spawn(get_title,cookie)
        task_list.append(task)

    gevent.joinall(task_list)


if __name__ == "__main__":

    bbr()

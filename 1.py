from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue
import  requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import gevent
import csv

urlQ= Queue()
ua = UserAgent()

pro = 0
len_= 0
infoFlow = {}
def get_title():
    global  pro
    while not urlQ.empty():
        target = urlQ.get_nowait()

        headers = {'user-agent' : ua.random}
        cookies = {
        'Cookie':'old=2012; isPrize=0; Hm_lvt_3f46f9c09663bf0ac2abdeeb95c7e516=1589846083,1589849260,1589854460,1590029410; PHPSESSID=nhei5jco0e0e1cjjmpke6gvs97; JK_GCNT=0; _fromCode=230707; Hm_lpvt_3f46f9c09663bf0ac2abdeeb95c7e516=1590032772; _JUKU_USER=%7B%22i%22%3A%2223353756%22%2C%22u%22%3A%22N5ec34f8898eed%22%2C%22u2%22%3A%22yaogon%22%2C%22k%22%3A%22f1fee0f64787c0da831084a8ca3b3e95%22%2C%22img%22%3A%22%22%2C%22ts%22%3A2%2C%22s%22%3A%22%5Cu9102%5Cu5dde%5Cu5927%5Cu5b66%22%2C%22iv%22%3A1%2C%22st%22%3A%227%22%2C%22no%22%3A%222410874531%22%2C%22cl%22%3A%22%5Cu521d%5Cu4e09%5Cuff081%5Cuff09%5Cu73ed%22%7D'
        }

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

        except Exception as e:
            pass
        finally:
            pro += 1
            print(' {} / {}'.format(pro, len_))
            if pro % 10 == 0 :
                draw()

def draw():
    with open('1.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Intro'])

        intro = list(infoFlow.keys())
        title = list(infoFlow.values())

        for i in range(len(title)):
            writer.writerow([title[i], intro[i]])



def bbr():
    global  len_
    bat = [1780493, 1798498]
    for code in range(bat[0], bat[-1]) :
        url = 'http://www.pigai.org/?c=v2&a=write&rid={}'.format(code)
        print(url)
        urlQ.put_nowait(url)

    len_ = bat[-1] - bat[0] + 1

    task_list = []
    for x in range(300):
        task = gevent.spawn(get_title)
        task_list.append(task)

    gevent.joinall(task_list)


def check_contain_chinese(check_str):
    if isinstance(check_str, str):
        index = [i for i, check in enumerate(check_str) if u'\u4e00' <= check <= u'\u9fff']
        return  index

if __name__ == "__main__":
    # bbr()
    text = 'Made in China 中国制造 123'
    idx = check_contain_chinese(text)
    Chinese = text[idx[0] : idx[-1] + 1]
    print(Chinese)
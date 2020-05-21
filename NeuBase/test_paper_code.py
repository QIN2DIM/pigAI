import requests
from bs4 import  BeautifulSoup
from fake_useragent import UserAgent
import random

ua = UserAgent()
code_set = []
with open('temp_code.txt','w',encoding='utf-8')as f:
    for i in range(20):
        code_set.append(random.randint(1800000, 1899999))

    code_set = set(code_set)
    for i in code_set:
        f.write(str(i))
        f.write('\n')



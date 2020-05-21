#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random
from NeuBase import readJSON

data = readJSON.read_json(".\\NeuBase\\data.json")
fam_said = data["famous"] # a 代表前面垫话，b代表后面垫话
forward_said = data["before"] # 在名人名言前面弄点废话
fora_said = data['after']  # 在名人名言后面弄点废话
content = data['bosh'] # 代表文章主要废话来源

xx = "学生会退会"

review_dun = 2

def DataClean(lst):
    global review_dun
    pool = list(lst) * review_dun
    while True:
        random.shuffle(pool)
        for var in pool:
            yield var

next_content = DataClean(content)
next_fam_said = DataClean(fam_said)

def ComeOn_fam_said():
    global next_fam_said
    xx = next(next_fam_said)
    xx = xx.replace(  "a", random.choice(forward_said))
    xx = xx.replace(  "b", random.choice(fora_said))
    return xx

def OtherContent():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

def generator(key):
    xx = str(key)
    for x in xx:
        tmp = str()
        while len(tmp) < 6000 :
            child_content = random.randint(0,100)
            if child_content < 5:
                tmp += OtherContent()
            elif child_content < 20 :
                tmp += ComeOn_fam_said()
            else:
                tmp += next(next_content)
        tmp = tmp.replace("x",xx)
        return tmp

def punc_tor():
    key = input('输入关键词')
    for _ in key :
        tmp = str()
        while len(tmp) < 6000 :
            child_content = random.randint(0, 100)
            if child_content < 5 :
                tmp += OtherContent()
            elif child_content < 20 :
                tmp += ComeOn_fam_said()
            else :
                tmp += next(next_content)
        tmp = tmp.replace("x", key)
        print(tmp)

# punc_tor()

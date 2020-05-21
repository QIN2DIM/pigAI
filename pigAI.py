from NeuBase.generator import generator
from NeuBase.open_task import BullshitGO
from NeuBase.get_title_keywords import get_word
from NeuBase.zh2en import caiyun_tranlate, google_tranlate
import re

# print('初始化')
bsg = BullshitGO()

# print('登录')
bsg.login_and_turn()

# print('获取作文题目')
bsg.get_title()

# print('获取题目摘要')
key = get_word()

print('根据摘要生成文本')
bullshit = generator(key)

print('预处理生成式')
# great_paper_zh = re.split(r'[\s?:,.，。？！；]', bullshit)
# great_paper_en = tranlate(bullshit, 'auto2en')
great_paper_en = google_tranlate(bullshit, [100, 500])

# print('存储作文语料')
bsg.get_paper(great_paper_en)

print('》》》正在填充作文内容')
bsg.rush_text()

# print('击毙弹窗')
bsg.select_self_class_verifyWarning()

print('作文提交成功')
bsg.submit()

# print('进程结束')
bsg.over_quit()


from NeuBase.generator import generator
from NeuBase.open_task import BullshitGO
from NeuBase.get_title_keywords import get_cn_word
from NeuBase.zh2en import cain_translate, google_translate

# print('初始化')
bsg = BullshitGO()

# print('登录')
bsg.login_and_turn()

# print('获取作文题目')
bsg.get_title()

# print('获取题目摘要')
key = get_cn_word()

print('>>> 根据摘要生成文本\n')
bullshit = generator(key)

print('>>> 预处理生成式\n')
great_paper_en = google_translate(bullshit, [400, 1000])

# print('存储作文语料')
bsg.get_paper(great_paper_en)

print('>>> 正在填充作文内容\n')
bsg.rush_text()

# print('击毙弹窗')
bsg.select_self_class_verifyWarning()

print('>>> 作文提交成功\n')
bsg.submit()


# print('进程结束')
bsg.over_quit()

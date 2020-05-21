# pigAI

## pigAI.py

主程序，通过运行此文件启动进程

## pgweb_config.ini [配置文件]

- 默认参数(无特殊需求请勿修改)

```ini
url =  批改网官网 http://www.pigai.org/ 
content = 作文内容[文本路径] 
title = 作文题目[文本路径] 
```

- 自定义参数

```ini
user = 账号,已储备开发者账号  
password = 密码,已储备开发者账号  
paper_code = 作文号  
class = 班级（需与提交时的选项文本一致，否则会出现不可预估的错误)  
```

## 使用说明

1. **此脚本基于Python3 + Selenium + Chrome**
   - 自动化测试并未使用PO模式构写应用层，如果客官没有能力改动原码的话可以试试[Chrome](https://www.google.cn/chrome/)
   - 如果浏览器没有配置ChromeDriver，[点此配置](https://localprod.pandateacher.com/python-manuscript/crawler-html/chromedriver/ChromeDriver.html) 

## 必要声明

###### - 我在测试版本中引用了[BullshitGenerator](https://github.com/menzi11/BullshitGenerator)文章生成脚本，这个脚本非常nice，开箱即用非常有趣~

1. 此项目仍处于测试阶段，属于**娱乐项目**，暂未上传与NLP上游应用有关功能模块，使用的方法仍是原始粗暴的随机匹配。
2. 众所周知批改网的评分系统本就比较智障，即使文章本身狗屁不通，即使全是单句，即使完全跑题，只要句子本身语法没多大问题，分数一般不会太低。
3. **严禁使用此脚本参与任何批改网官办写作活动！**(百万同题之类的)
4. 谨慎用于个人利益相关的作文测试！  此项目暂时处于测试阶段，生成的文本狗屁不通，存在明显的句法依存问题，如果翻车了……那就上船吧233~

最后，本人刚入门学习NLP，我会不定时运用最新学习成果更新版本[确信]。

# pigAI

[TOC]

## 1.快速上手

### [1]配置脚本环境

- #### 此脚本基于**Python3 + Selenium + Chrome**

  - 自动化测试并未使用PO模式构写应用层，如果客官没有能力改动原码的话可以试试[Chrome](https://www.google.cn/chrome/)
  - 如果浏览器没有配置ChromeDriver，[点此配置](https://localprod.pandateacher.com/python-manuscript/crawler-html/chromedriver/ChromeDriver.html) 

### [2]设置登录信息

- #### **pgweb_config.ini**

  - 默认参数(无特殊需求请勿修改)

  ```ini
  url = http://www.pigai.org/ 			#官网网站
  content = .\\NeuBase\\TrashTalk.txt		#正文文本路径
  title = .\\NeuBase\\title.txt			#作文标题路径
  ```

  - 自定义参数

  ```ini
  user = 账号,已储备开发者账号  
  password = 密码,已储备开发者账号  
  paper_code = 作文号  
  class = 班级（需与提交时的选项文本一致，否则会出现不可预估的错误)  
  ```


### [3]模块介绍

- #### **pigAI.py**

  - 功能简介：主程序，通过运行此文件启动脚本

- **抓取作文号.py**

  - 功能简介：爬虫携带开发者账号登录批改网，抓取小批量样本。
  - 输出路径：当前目录下生成*\\批改网作文题.csv* 
  - 数据结构： [Title, Introduction]

- **open_task.py**

  - 功能简介：批改网爬虫主题，采用自动化测试方法。
  - 补充说明：包含登录，切换作答页面，获取要求信息，输入文本，去除弹窗，提交答案几个简易流程。

- **zh2en.py**

  - 功能简介：Google zh2en API， 采用自动化测试方法。
  - 补充说明：因为测试版本是由bullshitGenerator生成中文句式，所以需要将中文翻译成英文 。后期将为脚本装配NLP相关自言语言处理模型直接书写英文，跳过“翻译”的步骤。

- **generator.py**

  - 功能简介：bullshitGenerator本体
  - 补充说明：将中文变量改为英文...

- **get_title_keywords.py**

  - 功能简介：暂用[Jiagu自然语言处理工具](https://github.com/ownthink/Jiagu)完成文章关键词提取工作。**[**致谢**]**
  - 补充说明：由于此模块与本脚本未来发展方向有所偏差，我在NLP版本中已弃用此模块(采用了更高效的方法生成句式)

## 2.脚本声明

**我在测试版本中引用了[BullshitGenerator](https://github.com/menzi11/BullshitGenerator)文章生成脚本，这个脚本非常nice，开箱即用非常有趣~**

1. 此项目仍处于测试阶段，属于**娱乐项目**，暂未上传与NLP上游应用有关功能模块，使用的方法仍是原始粗暴的随机匹配。
2. 众所周知批改网的评分系统本就比较智障，即使文章本身狗屁不通，即使全是单句，即使完全跑题，只要句子本身语法没多大问题，分数一般不会太低。
3. **严禁使用此脚本参与任何批改网官办写作活动！**(百万同题之类的)
4. 谨慎用于个人利益相关的作文测试！  此项目暂时处于测试阶段，生成的文本狗屁不通，存在明显的句法依存问题，如果翻车了……那就上船吧233~

最后，本人刚入门学习NLP，我会不定时运用最新学习成果更新版本[确信]。



# pigAI

## pigAI.py
主程序，通过运行此文件启动进程

## pgweb_config.ini **[配置文件]**
`**默认参数(无特殊需求请勿修改**)`  
**[url]** = 批改网官网 http://www.pigai.org/ 
**[content]** = 作文内容[文本路径]  
**[title]** = 作文题目[文本路径]  
`**自定义参数**`  
**[user]** = 账号,已储备开发者账号  
**[password]** = 密码,已储备开发者账号  
**[paper_code]** = 作文号  
**[class]** = 班级（需与提交时的选项文本一致，否则会出现不可预估的错误)  

## 使用说明
- **此脚本运行环境基于Python3 + Selenium + Chrome.
1.自动化测试并未使用PO模式构写应用层..所以客官没有能力改动原码的话可以试试使用Chrome浏览器orz   
2.如果浏览器为配置WebDriver.点此跳转  
- https://localprod.pandateacher.com/python-manuscript/crawler-html/chromedriver/ChromeDriver.html

## 声明
 **在测试版本中,引用了[menzi11]BullshitGenerator文章生成脚本**  
- github ：https://github.com/menzi11/BullshitGenerator

1. 此项目仍处于测试阶段，属于娱乐项目，暂未上传NLP上游应用功能模块（调教中...）。  
2. 本人刚入门学习NLP，我会不定时运用最新学习成果更新版本[确信]。  
3. 众所周知批改网的评分系统本就比较智障，即使文章本身狗屁不通，即使全是单句，即使完全跑题，只要句子语法没大问题，分数一般不会太低。  
4. 不要使用此脚本参与任何批改网官办活动（百万同题之类的)，此项目暂时处于测试阶段，生成的文本狗屁不通，存在明显的句法依存问题(*/ω＼*)   
5. **谨慎用于个人利益切实相关的作文测试！**  
  

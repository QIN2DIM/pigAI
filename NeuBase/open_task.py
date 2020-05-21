from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException,TimeoutException
import  selenium.webdriver.support.expected_conditions as EC
import time
from configparser import ConfigParser
import easygui

config = ConfigParser()
config.read('pgweb_config.ini', encoding='utf-8')

class BullshitGO(object):
    def __init__(self):
        # 初始化账号信息
        config = ConfigParser()
        config.read('pgweb_config.ini', encoding='utf-8')

        self.url = config['MAIN']['url']
        self.self_user = config['MAIN']['user']
        self.self_psw = config['MAIN']['password']
        self.self_cls = config['MAIN']['class']
        self.paper_code = config['MAIN']['paper_code']
        self.cont_PATH = config['MAIN']['contents']
        with open(self.cont_PATH, 'r')as f :
            self.paper_contents = f.read()  # 正文

        self.api = self.setChromeOptions()

    @staticmethod
    def setChromeOptions():
        # setting your chrome
        options = ChromeOptions()
        api = Chrome(options=options)
        return api

    def login_and_turn(self):
        # open task flow
        self.api.get(self.url)

        # login
        WebDriverWait(self.api, 30).until(EC.presence_of_all_elements_located)
        user = self.api.find_element_by_id('username').send_keys(self.self_user)
        bak = self.api.find_element_by_id('lg_logo').click()
        psw = self.api.find_element_by_id('password').send_keys(self.self_psw)
        login_btn = self.api.find_element_by_id('ulogin').click()

        # turn to self paper task
        WebDriverWait(self.api, 5).until(EC.presence_of_all_elements_located)
        self.api.find_element_by_name('rid').clear()
        paper_input = self.api.find_element_by_name('rid').send_keys(self.paper_code)
        paper_btn = self.api.find_element_by_xpath("//button[@class='sf_bt']").click()

    def get_title(self):
        title_PATH = config['MAIN']['title']
        try:
            paper_title = self.api.find_element_by_xpath("//div[@id='timu']").text
        except NoSuchElementException :
            paper_title = self.api.find_element_by_xpath("//div[@id='request_y']").text

        with open(title_PATH, 'w', encoding='utf-8')as f:
            f.write(paper_title)
            key = paper_title.split(']')[-1].split('】')[-1]
            print(paper_title)

    def get_paper(self,paper):
        with open(self.cont_PATH, 'w', encoding='utf-8')as f:
            f.write(paper)

    def rush_text(self) :
        # input your trash talk ~orz~
        time.sleep(0.2)
        content = self.api.find_element_by_id('contents')
        content.clear()
        content.send_keys(self.paper_contents)

    def select_self_class_verifyWarning(self):
        # select self class
        try:
            class_menu = self.api.find_element_by_id('stu_class').click()
            choice_self_class = WebDriverWait(self.api,1.2).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//select[@id='stu_class']//option[contains(@value,'{}')]".format(self.self_cls)
                ))).click()
        except (NoSuchElementException, WebDriverException) :
            pass

        # verify_warning
        try:
            check_ = WebDriverWait(self.api,2).until(
            EC.presence_of_element_located((
            By.XPATH,"//div[@id='icibaWinBotton']//input[@value='关闭']"
            ))).click()
        except (NoSuchElementException, WebDriverException, TimeoutException):
            pass

    def submit(self):
        #submit paper task
        time.sleep(1)
        submit = self.api.find_element_by_id('dafen').click()

    def over_quit(self):
        #quit
        while True:
            try:
                check_warning = self.api.find_element_by_xpath("//div[@id='icibaWinCont']").text
                # easygui.msgbox('若提交动作无响应,可手动操作')
                if '重复' in check_warning:
                    easygui.msgbox(check_warning)
                    self.api.find_element_by_xpath("//div[@id='icibaWinBotton']//input").click()
                    self.api.quit()
                    break
                if check_warning != '':
                    continue
                else:
                    time.sleep(1)
                    self_score = self.api.find_element_by_xpath("//span[@class='circles-integer']").text
                    easygui.msgbox('作文提交成功, 垃圾话得分:{}'.format(self_score))
                    self.api.quit()
                    break
            except (NoSuchElementException, WebDriverException):
                pass


if __name__ == '__main__':
    pass

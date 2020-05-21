def caiyun_tranlate(source, direction) :
    import requests
    import json

    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers, and it should be replaced by your token
    token = "3975l6lr5pcbvidl6jl2"

    payload = {
        "source" : source,
        "trans_type" : direction,
        "request_id" : "demo",
        "detect" : True,
    }

    headers = {
        'content-type' : "application/json",
        'x-authorization' : "token " + token,
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return response.text
    # return json.loads(response.text)['target']

def google_tranlate(source=None, direction=None):
    """

    :param source: str
    :param direction:
    :return:
    """
    from selenium.webdriver import Chrome
    from selenium.webdriver import ChromeOptions
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException, TimeoutException,WebDriverException
    import selenium.webdriver.support.expected_conditions as EC
    import re
    import time
    import pyperclip
    import random

    # 数据预处理
    if isinstance(source, str):
        source = re.split(r'[。]', source)[:-1]

    # 定义非零边界
    if not direction:
        Threshold = direction[-1]
    else:
        Threshold = 300

    #初始化浏览器
    options = ChromeOptions()
    options.add_argument('--headless')
    api = Chrome(options=options)

    api.get('https://translate.google.cn/#view=home&op=translate&sl=zh-CN&tl=en')
    WebDriverWait(api,10).until(EC.presence_of_all_elements_located)

    #逐句翻译
    len_ = 0
    content_ = ''
    for sent in source:
        tran_board = api.find_element_by_id('source')
        tran_board.clear()
        tran_board.send_keys(sent)

        #copy
        time.sleep(1)
        try:
            tran2en = api.find_element_by_xpath("//span[@class='tlid-translation translation']").text
            tran_text = tran2en + '.'

            content_ += tran_text
            len_ += len(tran_text)

            if len_ >= Threshold * 0.7514:
                return content_

        except (NoSuchElementException, TimeoutException, WebDriverException):
            pass

    #over quit
    api.quit()

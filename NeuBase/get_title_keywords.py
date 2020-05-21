import jiagu
from configparser import ConfigParser
import random


def get_word():
    config = ConfigParser()
    config.read('pgweb_config.ini', encoding='utf-8')

    title_PATH = config['MAIN']['title']

    with open(title_PATH, 'r', encoding='utf-8')as f:
        title = f.read()

    keys = jiagu.keywords(title)
    keys = [key for key in keys if key != '']
    key = random.choice(keys)

    return key

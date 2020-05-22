
def get_cn_word(PATH = False):
    import jieba
    from configparser import ConfigParser
    import random

    config = ConfigParser()
    config.read('pgweb_config.ini', encoding='utf-8')
    try:
        title_PATH = config['MAIN']['title']
    except KeyError:
        title_PATH = 'title.txt'
    with open(title_PATH, 'r', encoding='utf-8')as f:
        title = f.read()

    keys = jieba.cut(title)
    keys = [key for key in keys if key != ' 'and key.isalpha()]

    print(keys)
    key = random.choice(keys)

    return key

if __name__ == '__main__':
    text = 'good night boy~'
    import jiagu
    from  stanfordcorenlp.corenlp import  StanfordCoreNLP

    sfnlp = StanfordCoreNLP(r'E:\Alkaid\Lib\site-packages\stanfordcorenlp\corenlp.py')
    out = sfnlp.pos_tag(text)

    print(out)
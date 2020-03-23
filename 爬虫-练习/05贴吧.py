# http://tieba.baidu.com/p/3522395718
# 跟帖用户名，跟帖内容，跟帖时间
from lxml import etree
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import json
import os


if os.path.exists('贴吧.txt'):
    os.remove('贴吧.txt')


def get_one_page(url):
    try:
        response = requests.post(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求页面出错')
        return None


def parser_one_page(html):
    select = etree.HTML(html)
    data = select.xpath('//*[@id="j_p_postlist"]/div')
    for items in data:
        dic = {}
        user = items.xpath('./div[2]/ul/li[3]/a/text()')
        user = ''.join(user)
        content = items.xpath('./div[3]/div[1]//text()')[-3]
        content = ''.join(content).replace(' ', '')
        time = items.xpath('./@data-field')[0]
        dicc = json.loads(time)
        time = dicc['content']['date']
        dic['用户名'] = user
        dic['发帖内容'] = content
        dic['发帖时间'] = time

        with open('贴吧.txt', 'a+', encoding='utf-8') as f:
            f.write(dic['用户名']+'\n')
            f.write(dic['发帖内容']+'\n')
            f.write(dic['发帖时间']+'\n')
            f.write('*'*80+'\n')


def main(page):
    url = 'http://tieba.baidu.com/p/3522395718?pn=' + str(page)
    html = get_one_page(url)
    parser_one_page(html)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1, 2)])






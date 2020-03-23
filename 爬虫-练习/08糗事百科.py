
from multiprocessing import Pool
from lxml import etree
import requests
import json


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text


def parser_one_page(html):
    select = etree.HTML(html)
    items = select.xpath('//*[contains(@id,"qiushi_tag_")]')
    list = []
    for item in items:
        dic = {}
        user = item.xpath('./div[1]/a[2]/h2/text()')
        user = ''.join(user).replace('\n', '')
        content = item.xpath('./a[1]/div/span/text()')
        content = ''.join(content).replace('\n', '').replace('\t', '')
        happy = item.xpath('./div[2]/span[1]/i/text()')
        happy = ''.join(happy)
        dic['用户名'] = user
        dic['内容'] = content
        dic['好笑数'] = happy
        list.append(dic)
    return list


def write_to_page(data):
        with open('糗事百科08.txt', mode='w', encoding='utf-8') as f:
            for dic in data:
                f.write(json.dumps(dic, ensure_ascii=False) + '\n')
            print('完成')


def main(page):
    url = 'https://www.qiushibaike.com/text/page/' + str(page) + '/'
    html = get_one_page(url)
    data = parser_one_page(html)
    write_to_page(data)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1, 2)])

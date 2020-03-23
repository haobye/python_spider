
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
    for item in items:
        user = item.xpath('./div[1]/a[2]/h2/text()')
        user = ''.join(user).replace('\n', '')
        content = item.xpath('./a[1]/div/span/text()')
        content = ''.join(content).replace('\n', '').replace('\t', '')
        happy = item.xpath('./div[2]/span[1]/i/text()')
        happy = ''.join(happy)
        yield {
            '用户名': user,
            '内容': content,
            '点赞数': happy
        }


def write_to_page(one):
        with open('糗事百科09.txt', mode='a+', encoding='utf-8') as f:
            f.write(json.dumps(one, ensure_ascii=False) + '\n')


def main(page):
    url = 'https://www.qiushibaike.com/text/page/' + str(page) + '/'
    html = get_one_page(url)
    data = parser_one_page(html)
    for one in list(data):
        write_to_page(one)
        print(one)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1, 2)])

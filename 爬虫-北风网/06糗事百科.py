import requests
import json
import os
from multiprocessing import Pool
from lxml import etree


if os.path.exists('糗事百科.txt'):
    os.remove('糗事百科.txt')


def get_one_page(url):
    headers = {
        'Referer': 'https://www.qiushibaike.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    return html


def parse_alone(html):
    select = etree.HTML(html)
    items = select.xpath('//*[contains(@id,"qiushi_tag")]')
    for item in items:
        all_url = []
        name = item.xpath('./div[1]/a[2]/h2/text()')
        name = ''.join(name).replace('\n', '')
        content_key = item.xpath('./a[1]/@href')
        content_key = ''.join(content_key)
        content_url = 'https://www.qiushibaike.com' + str(content_key)
        all_url.append(content_url)
        for url in all_url:
            html = requests.get(url).text
            select = etree.HTML(html)
            content = select.xpath('//*[@id="single-next-link"]/div/text()')
            content = ''.join(content)
        zan = item.xpath('./div[2]/span[1]/i/text()')
        zan = ''.join(zan)
        yield {
            '用户名': name,
            '发帖内容': content,
            '点赞': zan
        }


def save_data(content):
    with open('糗事百科.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(page):
    url = 'https://www.qiushibaike.com/text/page/' + str(page) + '/'
    print('正在写入第{}页···'.format(page))
    html = get_one_page(url)
    items = parse_alone(html)
    for item in list(items):
        save_data(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(1, 11)])

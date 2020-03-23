import os
import requests
import json
import re
from multiprocessing import Pool
from lxml import etree


if os.path.exists('豆瓣电影.txt'):
    os.remove('豆瓣电影.txt')


def get_one_page(url):
    headers = {
        'Referer': 'https://movie.douban.com/explore',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    return response


def get_one_page_url(response):
    data = json.loads(response.text).get('subjects')
    url = []
    for item in data:
        one_url = item['url']
        url.append(one_url)
    return url


def get_all_data(url):
    headers = {
        'Referer': 'https://movie.douban.com/explore',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    data = []
    for url in url:
        response = requests.get(url, headers=headers)
        html = response.text
        select = etree.HTML(html)
        dic = {}
        name = select.xpath('//*[@id="content"]/h1/span[1]/text()')
        name = ''.join(name)
        daoyan = select.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
        daoyan = ''.join(daoyan)
        bianju = select.xpath('//*[@id="info"]/span[2]/span[2]//text()')
        bianju = ''.join(bianju)
        zhuyan = select.xpath('//*[@id="info"]/span[3]//text()')[4:]
        zhuyan = ''.join(zhuyan)
        shangying = re.findall(r'<span property="v:initialReleaseDate".*?>(.*?)</span>', html)
        shangying = ''.join(shangying)
        time = re.findall(r'<span property="v:runtime".*?>(.*?)</span>', html)
        time = ''.join(time)
        dic['name'] = name
        dic['daoyan'] = daoyan
        dic['bianju'] = bianju
        dic['zhuyan'] = zhuyan
        dic['shangying'] = shangying
        dic['time'] = time
        data.append(dic)
    return data


def save_data(data):
    with open('豆瓣电影.txt', 'a', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(page)
    response = get_one_page(url)
    url = get_one_page_url(response)
    data = get_all_data(url)
    save_data(data)


if __name__ == '__main__':
    # main()
    pool = Pool()
    pool.map(main, [page*10 for page in range(11) if page % 2 == 0])

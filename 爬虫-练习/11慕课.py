import requests
from lxml import etree
import re
import os
from multiprocessing import Pool


if os.path.exists('慕课finally.txt'):
    os.remove('慕课finally.txt')


def get_one_page(url):
    headers = {
        'Host': 'coding.imooc.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    return html


def parse_one_page(html):
    html = etree.HTML(html)
    items = html.xpath('/html/body/div[5]/div[2]/div[1]/div')
    data = []
    for item in items:
        dic = {}
        name = item.xpath('./a/div/div/div[2]/p[1]/text()')
        name = ''.join(name)
        dengji = item.xpath('./a/div/div/div[2]/div[1]/div[1]/span[1]/text()')
        dengji = ''.join(dengji)
        person = item.xpath('./a/div/div/div[2]/div[1]/div[1]/span[2]/text()')
        person = ''.join(person)
        old_score = item.xpath('./a/div/div/div[2]/div[1]/div[1]/span[3]/text()')
        new_score = ''.join(old_score)
        score = re.findall(r"评价：(.*?)分", new_score)
        score = ''.join(score)
        title = item.xpath('./a/div/div/div[2]/p[2]/text()')
        title = ''.join(title)
        money = item.xpath('./a/div/div[2]/div[2]/div[2]/div[1]/span[1]/text()')
        money = ''.join(money)
        if money == '':
            money = item.xpath('./a/div/div/div[2]/div[2]/div[1]/div[1]/text()')
            money = ''.join(money)
        # print(money)
        dic['name'] = name
        dic['dengji'] = dengji
        dic['person'] = person
        dic['score'] = score
        dic['title'] = title
        dic['money'] = money
        data.append(dic)
    return data


def save_one_page(page, data):
    with open('慕课finally.txt', 'a', encoding='utf-8') as f:
        print('正在写入第{}页···'.format(page))
        num = 0
        for items in data:
            num += 1
            f.write('第{}页第{}个课程'.format(page, num) + '\n')
            f.write('课程名称：' + items['name'] + '\n')
            f.write('课程等级：' + items['dengji'] + '\n')
            f.write('参与人数：' + items['person'] + '\n')
            f.write('课程评分：' + items['score'] + '\n')
            f.write('课程简介：' + items['title'] + '\n')
            f.write('课程价格：' + items['money'] + '\n')
            f.write('**' * 40 + '\n')


def main(page):
    url = 'https://coding.imooc.com/?sort=0&unlearn=0&page=' + str(page)
    html = get_one_page(url)
    data = parse_one_page(html)
    save_one_page(page, data)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [page for page in range(1, 6)])

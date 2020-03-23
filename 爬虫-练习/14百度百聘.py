# 应该需要重写了，所有print都无用

import requests
import json
import re
from lxml import etree


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response


def get_one_page_all_url(response):
    html = response.text
    select = etree.HTML(html)
    data = select.xpath('//*[@id="cktarget"]/div')
    all_url = []
    for items in data:
        item = items.xpath('./@data-click')[0]
        item = json.loads(item)
        url = item['url']
        all_url.append(url)
        print(url)
    return all_url


def get_every_data(all_url):
    headers = {
        'Referer': 'https://zhaopin.baidu.com/quanzhi?city=%E5%90%88%E8%82%A5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for url in all_url:
        url = url[30:]
        url = re.sub('://', '%3A%2F%2F', url)
        url = re.sub('/', '%2F', url)
        url = 'https://zhaopin.baidu.com/szzw?' + url + '&query=&city=%E5%90%88%E8%82%A5&is_promise=1&is_direct=1&vip_sign=&asp_ad_job='
        print(url)
        response = requests.get(url, headers=headers)
        html = response.text
        data = etree.HTML(html)
        dic = {}
        name = data.xpath('//*[@id="main"]/div[1]/h4/text()')
        name = ''.join(name)
        money = data.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/span[1]/text()')
        money = ''.join(money)
        require = data.xpath('//*[@id="main"]/div[1]/div[3]/text()')
        require = ''.join(require)
        num = data.xpath('//*[@id="main"]/div[1]/div[3]/span/text()')
        num = ''.join(num)
        num = re.findall(r'招聘人数：(.*?)人', num)
        num = ''.join(num)
        good = data.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[2]/p//text()')
        good = ''.join(good)
        time = data.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/p[3]/text()')
        time = ''.join(time)
        # time = re.findall(r"有效日期：(.*?)", time)
        address = data.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[3]/p[5]/text()')
        address = ''.join(address)
        # address = re.findall(r"工作地点：(.*?)", address)
        ask = data.xpath('//*[@id="main"]/div[3]/div[1]/div[1]/div[4]/div//text()')
        ask = ''.join(ask)
        dic['name'] = name
        dic['money'] = money
        dic['require'] = require
        dic['num'] = num
        dic['good'] = good
        dic['time'] = time
        dic['address'] = address
        dic['ask'] = ask
        print(dic)


def main():
    url = 'https://zhaopin.baidu.com/api/qzasync?query=&city=%25E5%258C%2597%25E4%25BA%25AC&is_adq=1&pcmod=1&token=%3D%3DwlSr9pUyNqbp1mWqZmTumnV62ZIiYashpbZ6mmUWJm&pn=200&rn=10'
    response = get_one_page(url)
    url = get_one_page_all_url(response)
    get_every_data(url)


if __name__ == '__main__':
    main()
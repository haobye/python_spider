# 只写入首页url
import requests
import json
import os
from lxml import etree

if os.path.exists('拉钩网-首页.txt'):
    os.remove('拉钩网-首页.txt')


def get_home_page(headers):
    url = 'https://www.lagou.com/'
    response = requests.get(url, headers=headers)
    data = etree.HTML(response.text)
    name = data.xpath('//*[@id="sidebar"]/div/div/div[2]/dl/dd/a/text()')
    company = data.xpath('//*[@id="sidebar"]/div/div/div[2]/dl/dd/a/@href')
    for i in range(len(company)):
        dic = {
            'name': name[i],
            'url': company[i],
        }
        with open('拉钩网-首页.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    headers = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    get_home_page(headers)


if __name__ == '__main__':
    main()

# 未完成

import requests
import re
from urllib.parse import quote
from lxml import etree

session = requests.session()


def get_main_page(url):
    headers = {
        'Referer': 'https://www.zhaopin.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
    }
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def get_job_cat_list(html):
    select = etree.HTML(html)
    data = select.xpath('//*[@id="root"]/div[2]/div[2]/div[1]//text()')
    all_url = []
    for key in data:
        key = quote(key)
        new_url = 'https://sou.zhaopin.com/?jl=489&kw=' + key + '&kt=3'
        all_url.append(new_url)
    return all_url


def parse_all_job(all_url):
    # for url in all_url:
    html = session.get(url=all_url[5], headers={
        'Host': 'sou.zhaopin.com',
        'Referer': 'https://www.zhaopin.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
    })
    print(all_url[5])
    print(html.text)
    # 从这里进不去 各个类别职位 的网页，失败


def main():
    url = 'https://www.zhaopin.com'
    html = get_main_page(url)
    all_url = get_job_cat_list(html)
    parse_all_job(all_url)


if __name__ == '__main__':
    main()

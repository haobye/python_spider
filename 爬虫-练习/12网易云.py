# 歌单列表url已得到，没有获取具体每首歌的url-----失败
# 成功案例：‘year2019month02’-->‘爬虫练习’-->‘02网易云’

import requests
import json
import re
from lxml import etree
from bs4 import BeautifulSoup


def get_main_page(url):
    headers = {
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response


def get_all_cat_url(response):
    html = response.text
    select = etree.HTML(html)
    all_url = []
    all_end_url = select.xpath('//*[@id="m-pl-container"]/li/div/a/@href')
    for end_url in all_end_url:
        start_url = 'https://music.163.com/#'
        url = start_url + end_url
        all_url.append(url)
    return all_url


def get_song_url(all_url):
    for url in all_url:
        headers = {
            'Referer': 'https://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        # data = {
        #     'params': '8sBCsLAKZaaV4yPLR7b5C8DMVle3ZcQDSBm2PYZx5uufEz3G1yYe3c+WvnBWBna7ZqOlVk7kvD5wnpe4IbuJtcJrUR7DuIm9Vc+4Qf6n0zZ9n3H4/O60WREZbCB8wc/4',
        #     'encSecKey': '3a2d84a533a0b7860fe0217166b3089e29ac04ca9f3d26bee029f10fbb3c702a097811dcb6d34d8851613971a19f4018bce03dd46bd82116d2b01da701d2b707ca2a6806c387b4c646315ca6d283e554490101d9a2cedf46fd1e15e2102dd609cc3e3f3efb9e91b01a33f976eeede21e1dd53b728263b1a587078f33d0a47f74'
        # }
        response = requests.post(url, headers=headers)
        select = etree.HTML(response.text)
        data = select.xpath('//*[@id="auto-id-TM8gUt04TpVDyUss"]/table/tbody/tr/@id')
        print(data)


def main():
    url = 'https://music.163.com/discover/playlist'
    response = get_main_page(url)
    cat_url = get_all_cat_url(response)
    get_song_url(cat_url)


if __name__ == '__main__':
    main()
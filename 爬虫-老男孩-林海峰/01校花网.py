# 提高下载效率，写入线程池(怎么使用)
from concurrent.futures import ThreadPoolExecutor

import requests
import re

p = ThreadPoolExecutor(30)


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_all_url(html):
    urls = re.findall(r'class="items".*?href="(.*?)"', html, re.S)
    return urls


def get_all_mp4(urls):
    # for url in urls:
    url = urls[19]
    html = requests.get(url).text
    data = re.findall(r'id="media".*?src="(.*?)"', html, re.S)
    return data[0]


def save_mp4(data):
    content = requests.get(url=data)
    with open('E:\爬虫系统学习\林海锋-老男孩\day1\lianxi.mp4', 'wb') as f:
        print('开始下载')
        f.write(content.content)
        print('下载完成')


def main():
    url = 'http://www.xiaohuar.com/v/'
    html = get_one_page(url)
    urls = get_all_url(html)
    movie = get_all_mp4(urls)
    save_mp4(movie)


if __name__ == '__main__':
    main()



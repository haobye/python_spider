# 得到大串url，继续解析精简
# 又得不到那一大串了
# 网页不稳定，时隐时现


import requests
import json
import re
from bs4 import BeautifulSoup


def get_key_page(url):
    headers = {
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    params = {
        'aid': '24',
        'offset': '0',
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,
        'from': 'gallery',
        'pd': ''
    }
    response = requests.get(url, headers=headers, params=params)
    return response


def get_cat_url(response):
    all_url = []
    for i in range(18):
        try:
            data = json.loads(response.text).get('data')[i]
            url = data['article_url']
        except:
            url = json.loads(response.text).get('share_url')
        all_url.append(url)
    return all_url


def get_all_photo_url(all_url):
    for url in all_url:
        try:
            id = url[25:-1]
            headers = {
                'referer': url,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
            params = {
                'group_id': id,
                'item_id': id,
                'offset': '0',
                'count': '5',
            }
            response = requests.get(url, headers=headers, params=params)
            html = response.text
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.select('title')[0].get_text()
            rule = re.compile(r'gallery: JSON.parse\("{(.*?)}"\)', re.S)
            url = re.findall(rule, html)
            print(title)
            print(url)
        except:
            print('解析详情页出错')


def save_photo(url):
    pass


def main():
    url = 'https://www.toutiao.com/api/search/content/'
    response = get_key_page(url)
    all_url = get_cat_url(response)
    url = get_all_photo_url(all_url)
    save_photo(url)


if __name__ == '__main__':
    main()


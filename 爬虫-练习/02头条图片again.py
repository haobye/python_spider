import re
import requests
import json
from requests.exceptions import RequestException
from urllib.parse import urlencode


def get_one_page(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1
    }
    try:
        url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求页出错了')
        return None


def parse_one_page(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def main():
    html = get_one_page(0, '街拍')
    # print(html)
    for item in parse_one_page(html):
        print(item)


if __name__ == '__main__':
    main()



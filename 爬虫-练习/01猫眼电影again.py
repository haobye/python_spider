import re
import requests
import json
import os
from requests.exceptions import RequestException
from multiprocessing import Pool


if os.path.exists('猫眼.txt'):
    os.remove('猫眼.txt')


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None


def parse_one_page(html):
    rule = r'<dd>.*?board.*?">(.*?)</i>.*?<p class="name"><a.*?data-val="{.*?}">(.*?)</a></p>.*?p class=".*?">(.*?)</p>\n<p class=".*?">上映时间：(.*?)</.*?div class=".*?".*?p class=".*?"><i class=".*?">(.*?)</i><i class=".*?">(.*?)</i></p>'
    patter = re.compile(rule, re.S)
    content = re.findall(patter, html)
    for item in content:
        yield{
            'num':item[0],
            'name':item[1],
            'star':item[2].strip(),
            'time':item[3],
            'pg':item[4] + item[5]
        }


def write_to_page(content):
    with open('猫眼.txt', mode='a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for content in parse_one_page(html):
        write_to_page(content)
        # print(content)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i*10 for i in range(0, 10)])
import re
import requests
import json
from requests.exceptions import RequestException
from multiprocessing import Pool


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    rule = r'<dd>.*?board.*?">(.*?)</i>.*?<p class="name"><a.*?data-val="{.*?}">(.*?)</a></p>.*?p class=".*?">(.*?)</p>\n<p class=".*?">上映时间：(.*?)</.*?div class=".*?".*?p class=".*?"><i class=".*?">(.*?)</i><i class=".*?">(.*?)</i></p>'
    patter = re.compile(rule, re.S)
    items = re.findall(patter, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'star': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('猫眼分析.txt', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])

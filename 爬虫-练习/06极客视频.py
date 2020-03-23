import re
import os
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
from bs4 import BeautifulSoup


if os.path.exists('极客分析.txt'):
    os.remove('极客分析.txt')


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求页出错')
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    cont = soup.find_all('li').__str__()
    cont = cont.replace('\n', '').replace('\t', '').replace('\t\t', '').replace('\t\t\t\t\t\t\t', '')
    # print(cont)
    rule = r'<div class=".*?"><h2 class=".*?"><a href=".*?" jktag=".*?" target="_blank">(.*?)</a></h2><p style=".*?">(.*?)</p><div class=".*?"><div class=".*?"><dl><dd class=".*?"><i class=".*?"></i><em>(.*?)</em></dd><dd class=".*?"><i class=".*?"></i><em>(.*?)</em></dd></dl><em class=".*?">(.*?)人学习</em></div>'
    pattern = re.compile(rule, re.S)
    need = re.findall(pattern, cont)
    for items in need:
        yield {
            '课程名称':items[0],
            '课程介绍':items[1],
            '课程时间':items[2],
            '课程等级':items[3],
            '参与人数':items[4]
        }


def write_to_file(content):
    with open('极客分析.txt', mode='a', encoding='utf-8') as f:
        f.write(content)

def main(page):
    url = 'https://www.jikexueyuan.com/course/?pageNum=' + str(page)
    html = get_one_page(url)
    for i in parse_one_page(html):
        print(i)
        write_to_file(str(i)+os.linesep)


if __name__ == '__main__':
    # pool = Pool()
    # pool.map(main, [i for i in range(1,11)])
    for page in range(1,2):
        main(page)



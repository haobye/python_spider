# 这个是把所有的电影都解析完成后，再统一写入，没有06那样解析一部写入一部好

import requests
import json
import re
from bs4 import BeautifulSoup


def get_home_page(url):
    headers = {
        'Host': 'dianying.2345.com',
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response


def get_details_url(response):
    lst = []
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.select('a.aPlayBtn')
    for items in data:
        item = items.attrs['href']
        url = 'http:' + item
        lst.append(url)
    return lst


def into_details_page(lst):
    info = []
    headers = {
        'Host': 'dianying.2345.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for url in lst:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.select('div.tit h1')[0].get_text()
        print('正在解析电影', name)
        score = soup.select('p.pTxt')[0].get_text()
        score = re.findall(r'(.*?)分加入收藏', score)
        score = ''.join(score)
        zhuyan = soup.select('ul.txtList li')[0].get_text()
        zhuyan = ''.join(zhuyan).replace('\n', ',')[5:]
        daoyan = soup.select('ul.txtList li.li_4')[0].get_text()
        daoyan = ''.join(daoyan).replace('\n', '')[3:]
        leix = soup.select('ul.txtList li')[2].get_text()
        leix = ''.join(leix).replace('\n', ',')[5:]
        time = soup.select('ul.txtList li')[4].get_text()
        time = ''.join(time).replace('\n', '')[3:][:-2]
        try:
            jianjie = soup.select('ul.txtList li span.sAll')[0].get_text()
        except:
            jianjie = None
        dic = {
            'name': name,
            'score': score,
            'zhuyan': zhuyan,
            'daoyan': daoyan,
            'leix': leix,
            'time': time,
            'jianjie': jianjie
        }
        info.append(dic)
    return info


def save_data(info):
    for dic in info:
        with open('林正英电影05.txt', 'a', encoding='utf-8') as f:
            print('正在写入电影>>>', dic['name'])
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    url = 'https://dianying.2345.com/mingxing/269-3/'
    response = get_home_page(url)
    lst = get_details_url(response)
    info = into_details_page(lst)
    save_data(info)


if __name__ == '__main__':
    main()

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
    headers = {
        'Host': 'dianying.2345.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for url in lst:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.select('div.tit h1')[0].get_text()
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
        language = soup.select('ul.txtList li')[7].get_text()
        language = ''.join(language).replace('\n', '')[3:]
        jianjie = soup.select('span.sAll')[0].get_text()
        dic = {
            'name': name,
            'score': score,
            'zhuyan': zhuyan,
            'daoyan': daoyan,
            'leix': leix,
            'time': time,
            'language': language,
            'jianjie': jianjie
        }
        save_data(name, dic)


def save_data(name, dic):
    with open('林正英06.txt', 'a', encoding='utf-8') as f:
        print('正在写入电影{}'.format(name))
        f.writelines(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    url = 'https://dianying.2345.com/mingxing/269-3/'
    response = get_home_page(url)
    lst = get_details_url(response)
    into_details_page(lst)


if __name__ == '__main__':
    main()

import requests
import re
import json
from lxml import etree


def get_movie_url():
    url = 'https://dianying.2345.com/mingxing/269-3/'
    headers = {
        'Host': 'dianying.2345.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    data = etree.HTML(html)
    items = data.xpath('/html/body/div[2]/div[2]/div[1]/ul/li')
    # print(items)
    lst = []
    for item in items:
        end_url = item.xpath('./div[1]/a/@href')[0]
        info_url = 'https:' + end_url
        lst.append(info_url)
    return lst


def parse_movie(lst):
    for url in lst:
        response = requests.get(url)
        data = etree.HTML(response.text)
        name = data.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/h1/text()')[0]
        score = data.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/p/em/text()')[0]
        score = re.findall(r'(.*?)分', score)[0]
        leix = data.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[3]//text()')
        leix = ''.join(leix).replace('\n', ',').replace(' ', '')[5:]
        time = data.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[5]/em[2]/text()')
        time = ''.join(time)
        if time.endswith('分钟'):
            time = re.findall(r'(.*?)分钟', time)[0]
        else:
            time = data.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li[4]/em[2]/text()')[0]
            time = re.findall(r'(.*?)分钟', time)[0]
        try:
            jianjie = data.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[10]/p/span[2]/text()')
        except:
            jianjie = data.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li[7]/p/span[2]/text()')
        jianjie = ''.join(jianjie)
        dic = {
            'name':name,
            'score': score,
            'leix': leix,
            'time': time,
            'jianjie': jianjie,
        }
        save_data(dic)


def save_data(dic):
    with open('林正英-xpath.txt', 'a', encoding='utf-8') as f:
        print('正在写入电影', dic['name'])
        f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    lst = get_movie_url()
    parse_movie(lst)


if __name__ == '__main__':
    main()

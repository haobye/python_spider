import requests
import json
import re
from lxml import etree


def get_city_url(url, headers):
    response = requests.get(url, headers=headers)
    data = etree.HTML(response.text)
    lst = []
    items = data.xpath('//*[@id="main"]/div[4]/ul/li/div[2]/div/a/@href')
    for item in items:
        con_url = 'http:' + item
        lst.append(con_url)
    return lst


def get_city_num(lst, headers):
    for con_url in lst:
        response = requests.get(con_url, headers=headers)
        data = etree.HTML(response.text)
        items = data.xpath('/html/head/script[2]/text()')[0]
        id = re.findall(r" 'cityId': '(.*?)'", items, re.S)[0]
        chname = re.findall(r" 'cityCName': '(.*?)'", items, re.S)[0]
        enname = re.findall(r" 'cityEnName': '(.*?)'", items, re.S)[0]
        dic = {
            'chname': chname,
            'id': id,
            'enname': enname,
            'url': con_url,
        }
        with open('大众点评地区ID信息.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')
            print(dic)


def main():
    url = 'http://www.dianping.com/citylist'
    headers = {
        'Host': 'www.dianping.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    lst = get_city_url(url, headers)
    get_city_num(lst, headers)


if __name__ == '__main__':
    main()

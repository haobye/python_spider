import requests
import json
from lxml import etree


def get_one_page(page):
    url = 'https://www.kuaidaili.com/free/inha/' + str(page) + '/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = etree.HTML(response.text)
    items = data.xpath('//*[@id="list"]/table/tbody/tr')
    lst = []
    for item in items:
        ip = item.xpath('./td[1]/text()')[0]
        port = item.xpath('./td[2]/text()')[0]
        http = 'http://' + ip + ':' + port
        proxies = {'http': http}
        lst.append(proxies)
    return lst


def try_validation(lst):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url = 'http://www.baidu.com/'
    for proxies in lst:
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            state = response.status_code
            if state == 200:
                save_effective(proxies)
                print('加入代理池>>>', proxies)
        except:
            print('失效', proxies)


def save_effective(proxies):
    with open('代理池.txt', 'a') as f:
        f.write(json.dumps(proxies, ensure_ascii=False) + '\n')


def main():
    for page in range(5):
        lst = get_one_page(page)
        try_validation(lst)


if __name__ == '__main__':
    main()

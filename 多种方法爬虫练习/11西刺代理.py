import requests
import json
from lxml import etree


def get_home_page(page):
    url = 'https://www.xicidaili.com/nn/' + str(page)
    headers = {
        'Host': 'www.xicidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print('正在解析西刺代理第{}页内容···'.format(page))
    data = etree.HTML(response.text)
    leix = data.xpath('//*[@id="ip_list"]/tr/td[6]/text()')
    http = data.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
    port = data.xpath('//*[@id="ip_list"]/tr/td[3]/text()')
    for i in range(len(leix)):
        dic = {
            leix[i]: leix[i] + '://' + http[i] + ':' + port[i]
        }
        search_proxies(dic)


def search_proxies(dic):
    url = 'https://www.baidu.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    respones = requests.get(url, headers=headers, proxies=dic, timeout=10)
    if respones.status_code == 200:
        print('     加入代理池>>>', dic)
        with open('代理池.txt', 'a') as f:
            f.write(json.dumps(dic) + '\n')


def main():
    for page in range(1, 3):
        get_home_page(page)


if __name__ == '__main__':
    main()
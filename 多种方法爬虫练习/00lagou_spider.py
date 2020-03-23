import requests
import json
import os
from lxml import etree

if os.path.exists('lagouwang.txt'):
    os.remove('lagouwang.txt')


def get_ip():
    url = 'http://www.zhuhaizhuochi.cn/Tools/proxyIP.ashx?OrderNumber=71e5cbfa913eee46e089accebeafd556&poolIndex=49233&cache=1&qty=1'
    req = requests.get(url)
    ip = req.content.decode('utf-8', 'ignore')
    return ip


def get_home_page(name_url):
    headers = {
        'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    name_url = json.loads(name_url)
    # print(name_url)
    start_url = name_url['url']
    name = name_url['name']
    flog = 0
    for page in range(1, 2):
        print('正在写入关于{}的第{}页信息···'.format(name, page))
        ip = get_ip()
        print(ip)
        proxies = {'http': ip}
        end_url = str(page) + '/?filterOption=' + str(page)
        find_url = start_url + end_url
        response = requests.get(url=find_url, headers=headers, proxies=proxies)
        html = response.text
        data = etree.HTML(html)
        items = data.xpath('//*[@id="s_position_list"]/ul/li')
        for item in items:
            name = item.xpath('./div[1]/div[1]/div[1]/a//text()')
            # //*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a
            name = ''.join(name).replace('\n', '').replace(' ', '')
            money = item.xpath('./div[1]/div[1]/div[2]/div//text()')
            money = ''.join(money).replace('\n', '').replace(' ', '').replace('经验', '/')
            tag = item.xpath('./div[2]/div[1]//text()')
            tag = ''.join(tag).replace('\n', '、').replace(' ', '')
            company = item.xpath('./div[1]/div[2]/div[1]/a/text()')
            company = ''.join(company)
            info = item.xpath('./div[1]/div[2]/div[2]/text()')
            info = ''.join(info).replace('\n', '').replace(' ', '')
            word = item.xpath('./div[2]/div[2]/text()')
            word = ''.join(word)
            print(name+money+tag+company+info+word)
            with open('lagouwang.txt', 'a', encoding='utf-8')as f:
                f.write(name+money+tag+company+info+word+'\n')


def main():
    with open('拉钩网-首页.txt', 'r', encoding='utf-8') as f:
        lst_name_url = f.readlines()
        for name_url in lst_name_url:
            get_home_page(name_url)


if __name__ == '__main__':
    main()






import requests
import re
import json
import os
from lxml import etree

if os.path.exists('起点.txt'):
    os.remove('起点.txt')


def get_home_page(url):
    headers = {
        'Host': 'www.qidian.com',
        'Referer': 'https://www.qidian.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    return None


def get_all_url(response):
    html = response.text
    select = etree.HTML(html)
    url = select.xpath('/html/body/div[2]/div[5]/div[2]/div[2]/div/ul/li/div[2]/h4/a/@href')
    return url


def go_in_content(home_url, list_url):
    for url in list_url:
        new_url = 'https:' + url
        headers = {
            'Host': 'book.qidian.com',
            'Referer': home_url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }
        response = requests.get(url=new_url, headers=headers)
        parser_page(response)


def parser_page(response):
    try:
        html = response.text
    except:
        html = response.content.decode('utf-8')
    data = etree.HTML(html)
    name = data.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/h1/em/text()')
    name = ''.join(name)
    user = data.xpath('/html/body/div[2]/div[6]/div[1]/div[2]/h1/span/a/text()')
    user = ''.join(user)
    introduce = data.xpath('/html/body/div[2]/div[6]/div[4]/div[1]/div[1]/div[1]/p//text()')
    introduce = ''.join(introduce).replace('\r', '').replace(' ', '').replace('\u3000', '')
    count = data.xpath('//*[@id="j_catalogPage"]/i/span/text()')
    count = ''.join(count)
    count = re.findall(r'\((.*?)章\)', count)
    count = ''.join(count)
    if count == '': count = '无信息'
    #     count = data.xpath('/html/body/div[2]/div[6]/div[4]/div[1]/div[1]/div[2]/ul/li[3]/div/p[1]/a/text()')
    #     count = ''.join(count)
    #     count = re.findall(r'第(.*?)章', count)
    #     count = ''.join(count)
    # with open('起点.csv', 'a', encoding='utf-8') as f:
    #     f.write(name + ',' + user + ',' + count + ',' + introduce + '\n')
    dic = {
        'name': name,
        'user': user,
        'count': count,
        'introduce': introduce,
    }
    with open('起点.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    for i in range(1, 2):
        url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=' + str(i)
        print('正在写入第{}页'.format(i))
        response = get_home_page(url)
        list_url = get_all_url(response)
        go_in_content(url, list_url)


if __name__ == '__main__':
    main()

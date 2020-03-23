import requests
from lxml import etree


def get_content_page(key, page):
    print('     -----第{}页-----'.format(page))
    url = 'http://weixin.sogou.com/weixin?'
    headers = {
        'Host': 'weixin.sogou.com',
        'Referer': 'http://weixin.sogou.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    params = {
        'type': '2',    # 文章
        'query': key,
        'ie': 'utf8',
        's_from': 'input',
        '_sug_': 'y',
        '_sug_type_': '',
        'w': '01019900',
        'page': page
    }
    # # 代理池不够稳定,不使用
    # with open('代理池-维护后.txt', 'r') as f:
    #     dic = f.readlines()
    #     proxies = random.choice(dic)
    #     proxies = json.loads(proxies)
    #     print(proxies)
    response = requests.get(url, headers=headers, params=params)
    data = etree.HTML(response.text)
    items = data.xpath('//*[@id="main"]/div[5]/ul/li')
    for item in items:
        info_url = item.xpath('./div[1]/a/@href')
        info_url = ''.join(info_url)
        # print(info_url)
        save_info(info_url)


def save_info(url):
    response = requests.get(url)
    select = etree.HTML(response.text)
    name = select.xpath('//*[@id="activity-name"]/text()')
    name = ''.join(name).replace('\n', '').replace(' ', '').replace('|', '-')
    data = select.xpath('//*[@id="js_content"]//text()')
    data = ''.join(data).replace('\n', '').replace(' ', '')
    with open('E:\python爬虫\微信文章\\' + name + '.txt', 'w', encoding='utf-8') as f:
        f.write(data)
        print(name, '写入完成...')


def main():
    key = input("请输入关键字>>>")
    for page in range(1, 3):
        get_content_page(key, page)


if __name__ == '__main__':
    main()

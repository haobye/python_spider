import requests
import os
from lxml import etree


if os.path.exists('博客园again.txt'):
    os.remove('博客园again.txt')


def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    select = etree.HTML(html)
    items = select.xpath('//*[@id="post_list"]/div')
    all_list = []
    for item in items:
        list = []
        con_url = item.xpath('./div/h3/a/@href')[0]
        html2 = requests.get(con_url).content.decode('utf-8')
        select2 = etree.HTML(html2)
        title = select2.xpath('//*[@id="cb_post_title_url"]/text()')
        content = select2.xpath('//*[@id="cnblogs_post_body"]//text()')
        content = ''.join(content).replace('\n', '').replace('\r', '')
        list.append(title)
        list.append(content)
        all_list.append(list)
    return all_list


def save_one_page(page, url, data):
    with open('博客园again.txt', 'a+', encoding='utf-8') as f:
        a = 0
        f.write('URL：%s' % url + '\n')
        for i in data:
            a += 1
            f.write('第%s页第%s个帖子' % (page, a) + '\n')
            print('第%s页第%s个帖子' % (page, a) + '\n')
            f.write(str(i[0]) + '\n')
            f.write(str(i[1]) + '\n' + '\n')
            if a == 20:
                a = 0
# 使用format，在{}里面放入初始值


def main():
    for page in range(1, 11):
        url = 'https://www.cnblogs.com/#p' + str(page)
        html = get_one_page(url)
        data = parse_one_page(html)
        save_one_page(page, url, data)


if __name__ == '__main__':
    main()


import requests
from lxml import etree
import re
from multiprocessing import Pool


def get_one_pge(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text


dic = {}


def parser_one_page(url):
    html = get_one_pge(url)
    data = etree.HTML(html)
    items = data.xpath('//*[@id="_j_search_result_left"]/div/div/ul/li')
    for item in items:
        name = item.xpath('./div/div[2]/h3/a//text()')
        name = ''.join(name)

        address = item.xpath('./div/div[2]/ul/li[1]/a/text()')
        address = ''.join(address)

        zan = item.xpath('./div/div[2]/ul/li[2]/a/text()')[0]
        zan = re.findall(r'点评\((.*?)\)', zan)
        zan = ''.join(zan)

        say = item.xpath('./div/div[2]/ul/li[3]/a/text()')[0]
        say = re.findall(r'游记\((.*?)\)', say)
        say = ''.join(say)

        dic['景点'] = name
        dic['地址'] = address
        dic['点赞数量'] = zan
        dic['评论数量'] = say
        print(dic)


if __name__ == '__main__':
    city = input('请输入需要查询的城市>>>')
    print('正在查询中，请稍后···')
    dic['城市'] = city
    url = []
    for page in range(1, 6):
        new_url = 'http://www.mafengwo.cn/search/s.php?q=' + city + '&p=' + str(page) + '&t=poi&kt=1'
        url.append(new_url)
    pool = Pool()
    pool.map(parser_one_page, url)


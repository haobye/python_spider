import requests
import os
import json
from lxml import etree


if os.path.exists('汽车之家-xpath.txt'):
    os.remove('汽车之家-xpath.txt')


url = 'https://www.autohome.com.cn/news/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
response = requests.get(url, headers=headers).content.decode('gbk')

select = etree.HTML(response)

items = select.xpath('//*[@id="auto-channel-lazyload-article"]/ul/li/a')
for item in items:
    dic = {}
    dic['详情链接'] = item.xpath('./@href')[0]
    dic['图片链接'] = item.xpath('./div[1]/img/@src')[0]
    dic['标题'] = item.xpath('./h3/text()')[0]
    dic['发布时间'] = item.xpath('./div[2]/span[1]/text()')[0]
    dic['阅读次数'] = item.xpath('./div[2]/span[2]/em[1]/text()')[0]
    dic['评论次数'] = item.xpath('./div[2]/span[2]/em[2]/text()')[0]
    dic['简介'] = item.xpath('./p/text()')[0]
    # print(dic)

    with open('汽车之家-xpath.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(dic, ensure_ascii=False) + '\n')


print('完成')


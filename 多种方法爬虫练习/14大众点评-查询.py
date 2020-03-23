import json
import os
import requests
from lxml import etree


with open('大众点评地区ID信息.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    # word = '北京'
    word = input('请输入要查询地区>>>').strip()
    for dic in data:
        dic = dic.strip('\n')
        dic = json.loads(dic)
        if word in dic['chname'] or word == dic['enname']:
            id = dic['id']
            city_name = dic['chname']
            city_url = dic['url']

print('正在查询，请稍等···')
if os.path.exists('大众点评-' + city_name + '-信息.txt'):
    os.remove('大众点评-' + city_name + '-信息.txt')

url = 'http://www.dianping.com/shopall/' + id + '/0'
# print(url)
headers = {
    'Host': 'www.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = requests.get(url, headers=headers)
data = etree.HTML(response.text)

with open('大众点评-' + city_name + '-信息.txt', 'a', encoding='utf-8') as f:
    f.write('以下信息来源于网址：{}'.format(url) + '\n\n')
    f.write('商区>>>>>>>>>>' + '\n')

items = data.xpath('//*[@id="J-shopall"]/div/div[2]/dl')
if items == []: print('此地区暂无商区')
for item in items:
    shop = item.xpath('.//text()')
    shop = ''.join(shop).replace('\n', '').replace('\t', '').replace(' ', '')
    # print(shop)
    with open('大众点评-' + city_name + '-信息.txt', 'a', encoding='utf-8') as f:
        f.write(shop + '\n')

with open('大众点评-' + city_name + '-信息.txt', 'a', encoding='utf-8') as f:
    f.write('\n' + '地标>>>>>>>>>>' + '\n')

select = data.xpath('//*[@id="J-shopall"]/div/div[3]/dl')
if select == []: print('此地区暂无地标')
for sel in select:
    box = sel.xpath('.//text()')
    box = ''.join(box).replace('\n', '').replace('\t', '').replace(' ', '')
    # print(box)
    with open('大众点评-' + city_name + '-信息.txt', 'a', encoding='utf-8') as f:
        f.write(box + '\n')

with open('大众点评-' + city_name + '-信息.txt', 'a', encoding='utf-8') as f:
    f.write('\n' + '地铁>>>>>>>>>>' + '\n')

items = data.xpath('//*[@id="J-shopall"]/div/div[4]/dl')
if items == []: print('此地区暂未开通地铁')
for item in items:
    path = item.xpath('.//text()')
    path = ''.join(path).replace('\n', '').replace('\t', '').replace(' ', '')
    # print(path)
    with open('大众点评-' + city_name + '-信息.txt', 'a', encoding='utf-8') as f:
        f.write(path + '\n')

print('您所查询所有信息已保存至：大众点评-' + city_name + '-信息.txt')

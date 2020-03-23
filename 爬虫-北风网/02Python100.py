# 使用BeautifulSoup
import requests
import json
import os
from bs4 import BeautifulSoup


if os.path.exists('python100例.txt'):
    os.remove('python100例.txt')


# 拼接一百个练习的链接
url = 'http://www.runoob.com/python/python-100-examples.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
html = requests.get(url, headers=headers).content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
data = soup.find(id='content').ul.find_all('a')
all_url = []
for i in data:
    new = i.attrs['href']
    new_url = 'http://www.runoob.com' + new
    all_url.append(new_url)
# print(all_url)


# 解析每个页面所需信息(sibling)
for i in range(10):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
    page_html = requests.get(all_url[i], headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(page_html, 'html.parser')
    dic = {}
    dic['题号'] = soup.find(id='content').h1.text
    dic['题目'] = soup.find(id='content').find_all('p')[1].text
    dic['程序分析'] = soup.find(id='content').find_all('p')[2].text
    try:
        dic['源代码'] = soup.find(class_='hl-main').text
    except:
        dic['源代码'] = soup.find('pre').text
    # print(dic)

# 储存信息，写入文件
    with open('python100例.txt', mode='a+', encoding='utf-8') as f:
        f.write(json.dumps(dic, ensure_ascii=False) + '\n')




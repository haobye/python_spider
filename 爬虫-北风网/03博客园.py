import requests
import os
import json
from lxml import etree


if os.path.exists('博客园.txt'):
    os.remove('博客园.txt')


for page in range(1, 11):
    url = 'https://www.cnblogs.com/#p' + str(page)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
    html = requests.get(url, headers=headers).content.decode('utf-8')
    select = etree.HTML(html)
    data = select.xpath('//*[@id="post_list"]/div/div[2]')
    all_url = []
    for items in data:
        new_url = items.xpath('./h3/a/@href')
        new_url = ''.join(new_url)
        all_url.append(new_url)


    for i in all_url:
        # dic = {}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
        html2 = requests.get(i, headers=headers).content.decode('utf-8')
        select2 = etree.HTML(html2)
        data = select2.xpath('//*[@id="cnblogs_post_body"]/p/text()')
        # dic['网址'] = i
        # dic['内容'] = data

        with open('博客园.txt', mode='a+', encoding='utf-8') as f:
            # f.write(json.dumps(dic, ensure_ascii=False) + '\n')
            f.write(i+'\n')
            f.write(str(data)+'\n')
            f.write('*'*90+'\n')

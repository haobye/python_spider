# 此为源代码

#-*- conding:utf-8 -*-
''''''
from lxml import etree
import requests
'''
    需求分析
        爬取博客园的贴子
    源码的分析
        https://www.cnblogs.com/
        tz = post_item_body
        title = cb_post_title_url
        content = cnblogs_post_body
    代码实现
        1.根据入口url请求源码
        2.提取数据（每篇帖子的url）
        3.根据帖子url进入到帖子详情，获取详细内容
        4.保存数据
'''

#1.根据入口url请求源码
url = 'https://www.cnblogs.com/'
nwo_url = url
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
num = 1
page = 1
while True:
    r = requests.get(nwo_url,headers).text
    # print(r)
    #解析
    index = etree.HTML(r)
    # print(index)

    #2.提取数据（每篇帖子的url）
    tz_url = index.xpath('//div[@class="post_item_body"]/h3/a/@href')
    next_url = index.xpath('//div[@class="pager"]/a[last()]')
    # print(next_url[0].xpath('@href'))
    # print(next_url[0].xpath('text()'))

    #3.根据帖子url进入到帖子详情，获取详细内容
    for i in tz_url:
        re = requests.get(i).text
        html = etree.HTML(re)
        #提取标题和内容
        tz_title = html.xpath('//a[@id="cb_post_title_url"]/text()') #list
        print(tz_title)
        tz_content = html.xpath('string(//*[@id="cnblogs_post_body"])')  #str
        print(tz_content)

        #保存内容
        with open('cn-blogs.csv','a+',encoding='utf-8') as file:
            file.write(tz_title[0]+'\n')
            file.write(tz_content+'\n')
            file.write(i+'\n')
            file.write('*'*50+'\n')
        print('{0}页第{1}篇帖子'.format(page,num))
        num += 1

    if next_url[0].xpath('text()')[0] == 'Next >':
        nwo_url = url[:-1]+next_url[0].xpath('@href')[0]
        print(nwo_url)
        page+=1
        num=1
        print(page)

    else:
        break

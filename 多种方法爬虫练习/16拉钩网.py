# 每个职位只爬取第一页的信息
# 放开注释信息，使用for循环即可爬取多页
import requests
import json
import os
from lxml import etree

if os.path.exists('拉钩网16.txt'):
    os.remove('拉钩网16.txt')


def get_home_page(headers):
    url = 'https://www.lagou.com/'
    response = requests.get(url, headers=headers)
    data = etree.HTML(response.text)
    name = data.xpath('//*[@id="sidebar"]/div/div/div[2]/dl/dd/a/text()')
    company = data.xpath('//*[@id="sidebar"]/div/div/div[2]/dl/dd/a/@href')
    lst = []
    for i in range(len(name)):
        dic = {
            'name': name[i],
            'url': company[i],
        }
        lst.append(dic)
    return lst


def get_lst_page(lst, headers):
    for dic in lst:
        company_url = dic['url']
        # company_url = company_url + str(page) + '/?filterOption=' + str(page)
        print(company_url)
        response = requests.get(company_url, headers=headers)
        data = etree.HTML(response.text)
        info_url = data.xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/@href')
        save_info(dic['name'], info_url)


def save_info(name, info_url):
    headers = {
        'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for sa_url in info_url:
        response = requests.get(sa_url, headers=headers)
        data = etree.HTML(response.text)
        laiyuan = data.xpath('/html/body/div[2]/div/div[1]/div/div[1]/text()')
        laiyuan = ''.join(laiyuan)
        zhiwei = data.xpath('/html/body/div[2]/div/div[1]/div/span/text()')
        zhiwei = ''.join(zhiwei)
        yaoqiu = data.xpath('/html/body/div[2]/div/div[1]/dd/p[1]//text()')
        yaoqiu = ''.join(yaoqiu).replace('\n', '').replace(' ', '')
        address = data.xpath('//*[@id="job_detail"]/dd[3]/div[1]//text()')
        address = ''.join(address).replace('\n', '').replace(' ', '')[:-4]
        fuli = data.xpath('//*[@id="job_detail"]/dd[1]/p/text()')
        fuli = ''.join(fuli)
        dic = {
            '网址': sa_url,
            '职位': zhiwei,
            '要求': yaoqiu,
            '地址': address,
            '福利': fuli,
            '招聘': laiyuan,
        }
        with open('拉钩网16.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')
    print('完成写入关于{}的详细信息···'.format(name))


def main():
    headers = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    lst = get_home_page(headers)
    get_lst_page(lst, headers)


if __name__ == '__main__':
    main()

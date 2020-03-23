import requests
import json
import os
from lxml import etree

if os.path.exists('校园招聘.txt'):
    os.remove('校园招聘.txt')


def get_big_clssify():
    url = 'https://xiaoyuan.zhaopin.com/full'
    headers = {
        'Host': 'xiaoyuan.zhaopin.com',
        'Referer': 'https://xiaoyuan.zhaopin.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    data = etree.HTML(html)
    position = data.xpath('//*[@id="subIndustry"]/li/a/@href')
    return position


def get_info_url(lst):
    headers = {
        'Host': 'xiaoyuan.zhaopin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for url in lst:
        for page in range(1, 3):
            change_url = url + '/0_0_0_0_-1_0_' + str(page) + '_0'
            response = requests.get(change_url, headers=headers)
            data = etree.HTML(response.text)
            # print(change_url)
            name = data.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/ul/li/span/text()')
            print('正在查询并写入关于-{}-的第-{}-页职位信息'.format(name, page))
            info_url = data.xpath('/html/body/div[2]/div[3]/div[1]/div/div[2]/ul/li/div[2]/p[1]/a/@href')
            save_info(url, info_url)


def save_info(url, info_url):
    headers = {
        'Host': 'xiaoyuan.zhaopin.com',
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for one in info_url:
        save_url = 'https:' + one
        response = requests.get(save_url, headers=headers)
        html = response.text
        data = etree.HTML(html)
        name = data.xpath('//*[@id="JobName"]/text()')
        name = ''.join(name).replace('\r', '').replace('\n', '').replace(' ', '')
        if name == '': name = '已下架'
        job_addr = data.xpath('//*[@id="currentJobCity"]/text()')
        job_addr = ''.join(job_addr).replace('\r', '').replace('\n', '').replace(' ', '')
        time = data.xpath('//*[@id="liJobPublishDate"]/text()')
        time = ''.join(time)
        stu = data.xpath('//*[@id="divMain"]/div/div/div[1]/div[1]/ul[2]/li[12]/text()')
        stu = ''.join(stu)
        if stu == '': stu = '不限'
        dic = {
            'url': save_url,
            'name': name,
            'job_address': job_addr,
            'work_time': time,
            'student': stu,
        }
        with open('校园招聘.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    lst = get_big_clssify()
    get_info_url(lst)


if __name__ == '__main__':
    main()


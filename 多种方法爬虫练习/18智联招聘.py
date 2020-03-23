# 本篇用于查询
import requests
import json
import re
import os
from lxml import etree

if os.path.exists('智联招聘.txt'):
    os.remove('智联招聘.txt')


def save_data_num():
    url = 'https://dict.zhaopin.cn/dict/dictOpenService/getDict?dictNames=region_relation,education,recruitment,education_specialty,industry_relation,careet_status,job_type_parent,job_type_relation'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    data = re.findall('{"id":(.*?),"parentIntKey":.*?"strKey":"(.*?)",.*?,"value":"(.*?)"', html)
    for tuples in data:
        lst = list(tuples)
        dic = {
            'id': lst[0],
            'num': lst[1],
            'name': lst[2],
        }
        print(dic)
        with open('智联招聘数字码.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def get_city_num():
    with open('智联招聘数字码.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        # city = '合肥'     # 输入城市（按字少的输入，不用加省、市）
        city = input('请输入城市关键字>>>')
        print('正在查询城市码，请稍后。。。')
        for dic in data:
            dic = json.loads(dic)
            if city in dic['name']:
                city_num = dic['num']
                print('切换页面至{}城市'.format(dic['name']))
                return city_num   # 返回城市数字码


def get_position_info():
    url = 'https://www.zhaopin.com/'
    headers = {
        'Host': 'www.zhaopin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = etree.HTML(response.text)
    position = data.xpath('//*[@id="root"]/div[2]/div[2]/div[1]/ol/li/div[2]/div/div[2]/a/text()')
    # i_word = 'python'   # 统一使用小写字母,职位的
    i_word = input('请输入职位关键字>>>').lower()
    for ok_word in position:
        ok_word = ok_word.lower()
        if i_word in ok_word:
            # print(ok_word)
            print('正在查询关于{}的信息'.format(ok_word))
            return ok_word    # 返回写入url的职位名称


def make_canshu(page, num, word):
    url = 'https://fe-api.zhaopin.com/c/i/sou?'
    headers = {
        'Host': 'fe-api.zhaopin.com',
        'Origin': 'https://sou.zhaopin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    params = {
        'start': page * 90,
        'pageSize': '90',
        'cityId': num,
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kw': word,
        'kt': '3',
    }
    # canshu_one = response.headers['x-zp-request-id']    # 确定城市和职位后服务器返回的
    # data = time.time()
    # canshu_two = int(data*1000)       # 当前时间的毫秒时间戳
    response = requests.get(url, headers=headers, params=params)
    print('     根据您输入的要求正在写入第{}页有关于{}的职位信息···'.format(page+1, word))
    data = json.loads(response.text).get('data')['results']
    for items in data:
        res2 = requests.get(items['positionURL'])
        data2 = etree.HTML(res2.text)
        address = data2.xpath('/html/body/div[1]/div[3]/div[5]/div[2]/div[2]/ul/li[5]/strong/text()')
        address = ''.join(address).replace('\n', '').replace('\r', '').replace(' ', '')
        dic = {
            'zhiw': items['jobName'],
            'stud': items['eduLevel']['name'],
            'url': items['positionURL'],
            'fuli': ''.join(items['welfare']),
            'money': items['salary'],
            'jingy': items['workingExp']['name'],
            'xinz': items['company']['type']['name'],
            'gongx': items['company']['name'],
            'address': address,
        }
        # print(dic)
        save_data_info(dic)


def save_data_info(dic):
    with open('智联招聘.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    # again = input('是否更新智联招聘数字码（是/否）：')
    # if again == '是':
    #     save_data_num()
    num = get_city_num()
    word = get_position_info()
    for page in range(2):
        make_canshu(page, num, word)


if __name__ == '__main__':
    main()

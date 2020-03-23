import requests
import json
import urllib.parse
from lxml import etree


def get_home_page():
    leix = input('请输入您要查询的疾病名称（例如：甲亢 乙肝 ）>>>')
    # leix = '糖尿病'
    leix_parse = urllib.parse.quote(leix)
    url = 'https://www.guahao.com/json/white/area/provinces'
    headers = {
        'referer': 'https://www.guahao.com/s/%E7%B3%96%E5%B0%BF%E7%97%85',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    province = input('请输入省或直辖市（请输入正确格式，例如：北京，全国，安徽）>>>')
    # province = '安徽'
    province_parse = urllib.parse.quote(province)
    for dic in data:
        if province == dic['text']:
            province_num = dic['value']
            if province != '上海' or province != '北京' or province != '广州' or province != '深圳' or province != '武汉' or province != '杭州' or province != '长沙' or province != '南京' or province != '重庆' or province != '青岛' or province != '西安':
                url = 'https://www.guahao.com/json/white/area/citys?provinceId=' + province_num
                response = requests.get(url, headers=headers)
                items = json.loads(response.text)
                city = input('请输入城市名（例如：不限,，淮北，合肥）>>>')
                # city = '合肥'
                city_parse = urllib.parse.quote(city)
                for item in items:
                    if city == item['text']:
                        city_num = item['value']
                        hos_url = 'https://www.guahao.com/s/' + leix_parse + '/hospital/' + province_num + '/' + province_parse + '/' + city_num + '/' + city_parse
                        return hos_url


def into_hospital(url):
    lst = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    try:
        for page in range(10):
            end_url = url + '/p' + str(page)
            response = requests.get(end_url, headers=headers)
            data = etree.HTML(response.text)
            items = data.xpath('//*[@id="g-cfg"]/div[1]/div[3]/ul/li')
            for item in items:
                into_url = item.xpath('./a/@href')[0]
                lst.append(into_url)
    except:
        return None
    return lst


def parse_info(lst):
    for url in lst:
        response = requests.get(url)
        data = etree.HTML(response.text)
        name = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/h1/strong/a/text()')[0]
        address = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/div[1]/span/text()')
        address = ''.join(address).replace('\n', '').replace(' ', '')
        dic = {
            'name': name,
            'address': address
        }
        with open('微医-查询.txt', 'a', encoding='utf-8') as f:
            print('正在写入{}相关信息'.format(name))
            f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    url = get_home_page()
    lst = into_hospital(url)
    parse_info(lst)


if __name__ == '__main__':
    main()



import requests
import json
from lxml import etree


def get_all_url(url):
    lst = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    data = etree.HTML(response.text)
    items = data.xpath('//*[@id="gh"]/div[3]/div[1]/div/div')
    for item in items:
        common_url = item.xpath('./div[1]/ul/li/span/a/@href')
        for common in common_url:
            common = common + '/hospital'
            lst.append(common)
        all_url = item.xpath('./div[2]/div/div/ul/li/p/a/@href')
        for all in all_url:
            all = all + '/hospital'
            lst.append(all)
    return lst


def get_hospital_url(lst):
    two_lst = []
    for url in lst[:4]:
        response = requests.get(url)
        data = etree.HTML(response.text)
        items = data.xpath('//*[@id="g-cfg"]/div[1]/div[3]/ul/li/a/@href')
        two_lst.append(items)
    return two_lst


def hospital_info(two):
    for lst in two:
        for url in lst[:4]:
            # print(url)
            response = requests.get(url)
            data = etree.HTML(response.text)
            name = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/h1/strong/a/text()')[0]
            guanz = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[1]/p[2]/span/text()')[0]
            address = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/div[1]/span/text()')
            address = ''.join(address).replace('\n', '').replace(' ', '')
            phone = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/div[2]/span/text()')
            phone = ''.join(phone).replace('\n', '').replace(' ', '')
            website = data.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/div[3]/span/text()')
            website = ''.join(website)[1:]
            dic = {
                'url': url,
                'name': name,
                'guanzhu': guanz,
                'address': address,
                'phone': phone,
                'website': website,
            }
            with open('微医07.txt', 'a', encoding='utf-8') as f:
                f.write(json.dumps(dic, ensure_ascii=False) + '\n')


def main():
    url = 'https://www.guahao.com/'
    lst = get_all_url(url)
    two = get_hospital_url(lst)
    hospital_info(two)


if __name__ == '__main__':
    main()

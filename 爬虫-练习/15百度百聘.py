import requests
import json
import os

# if os.path.exists('百度百聘.txt'):
#     os.remove('百度百聘.txt')


def get_cat(url):
    headers = {
        'Host': 'zhaopin.baidu.com',
        'Referer': 'https://zhaopin.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    session = requests.session()
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        return response
    return None


def parser_page(response):
    data = json.loads(response.text).get('data')
    items = data['disp_data']
    for item in items:
        name = item['@name']
        education = item['ori_education']
        address = item['district']
        money = item['ori_salary']
        source = item['source']
        yield {
            'name': name,
            'education': education,
            'address': address,
            'money': money,
            'source': source,
        }


def save_data(data):
    list_data = list(data)
    print(list_data)
    with open('百度百聘.txt', mode='a', encoding='utf-8') as f:
        for dd in list_data:
            f.write(json.dumps(dd, ensure_ascii=False) + '\n')


def main(city):
    for page in range(1, 6):
        url = 'http://zhaopin.baidu.com/api/qzasync?query=&city={}&is_adq=1&pcmod=1&token=%3D%3DwlSr9pUyNqbpVnWq5lSumnV62ZIiYasVpZTGnmUO5l&pn={}&rn=10'.format(city, page*10)
        response = get_cat(url)
        data = parser_page(response)
        save_data(data)


if __name__ == '__main__':
    city = input('请输入城市>>>')
    main(city)
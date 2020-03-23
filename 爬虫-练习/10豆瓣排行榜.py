import requests
import re
import os
from bs4 import BeautifulSoup


if os.path.exists('豆瓣.txt'):
    os.remove('豆瓣.txt')


def get_big_page(url):
    headers = {
        'Referer': 'https://movie.douban.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Cookie': 'll="118183"; bid=BI2yszMd7TM; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1548252088%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dzf6gum9_tD2bfCJYaVXfPJ0-BoAB8XOQaF-8sm0IAYIt0xINdwE7lTIubhdPOVfF%26wd%3D%26eqid%3D8f7c7a0f00000e21000000045c487332%22%5D; _pk_id.100001.4cf6=df66cceb534199d3.1548252088.1.1548252088.1548252088.; _pk_ses.100001.4cf6=*; __utma=30149280.231883232.1548252088.1548252088.1548252088.1; __utmb=30149280.0.10.1548252088; __utmc=30149280; __utmz=30149280.1548252088.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.690640473.1548252088.1548252088.1548252088.1; __utmc=223695111; __utmz=223695111.1548252088.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=223695111.1.10.1548252088; __yadk_uid=oW5ZP5PjoKvKC5phXfuCud3LWWWVbOcQ',
        'Host': 'movie.douban.com'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html


def parser_big_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="pl2")
    data = []
    for item in items:
        dic = {}
        name = item.a.text
        name = ''.join(name).replace(' ', '').replace('\n', '')
        movie_url = item.a.attrs['href']
        time_attrs = item.find('p').text
        score = item.find(class_="rating_nums").text
        person = item.find('span', class_="pl").text
        person = ''.join(person)
        person = re.findall(r'((\d+)人评价)', person)
        # print(list(person[0])[1])
        dic['name'] = name
        dic['movie_url'] = movie_url
        dic['time_attrs'] = time_attrs
        dic['score'] = score
        dic['person'] = list(person[0])[1]
        data.append(dic)
    return data


def save_big_page(data):
    with open('豆瓣排行榜.txt', 'a', encoding='utf-8') as f:
        for dic in data:
            f.write('电影名称：' + dic['name'] + '\n')
            f.write('电影链接：' + dic['movie_url'] + '\n')
            f.write('参与演员：' + dic['time_attrs'] + '\n')
            f.write('电影评分：' + dic['score'] + '\n')
            f.write('评分人数：' + dic['person'] + '\n')
            f.write('*' * 60 + '\n')


def main():
    url = 'https://movie.douban.com/chart'
    html = get_big_page(url)
    data = parser_big_page(html)
    save_big_page(data)


if __name__ == '__main__':
    main()



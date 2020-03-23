import requests
from bs4 import BeautifulSoup
import re
import urllib.parse


def get_target_url(url):
    url_lst = []
    headers = {
        'Host': 'www.stats.gov.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for page in soup.select('span.cont_tit font script'):
        page = str(page)
        data = re.findall(r"var urlstr = '(.*?)'", page, re.S)
        url = data[0]
        url_lst.append(url)
    return url_lst


def get_content(lst):
    for url in lst:
        headers = {
            'Referer': 'http://www.stats.gov.cn/was5/web/search?channelid=288041&andsen=%E5%90%88%E8%82%A5%E8%81%8C%E4%B8%9A%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        title = soup.title.string
        date = soup.select('font.xilan_titf')[0].get_text()
        date = ''.join(date).replace('\n', '')
        try:
            content = soup.select('div.TRS_PreAppend')[0].get_text()
            content = ''.join(content)
        except:
            return None
        with open('E:\python爬虫\国家统计局/' + title + '.txt', 'w', encoding='utf-8') as f:
            print('正在写入', title)
            f.write(title + '\n')
            f.write(date + '\n' + '\n')
            f.write(content)


def main():
    word = input('请输入需要查询关键词>>>')
    parse = urllib.parse.quote(word)
    url = 'http://www.stats.gov.cn/was5/web/search?channelid=288041&andsen=' + parse
    lst = get_target_url(url)
    get_content(lst)


if __name__ == '__main__':
    main()

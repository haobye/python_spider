# 未完成

import requests
from lxml import etree
from bs4 import BeautifulSoup
session = requests.session()


def get_subject_url():
    url = 'http://www.jyeoo.com/'
    headers = {
        'Host': 'www.jyeoo.com',
        'Referer': 'http://www.jyeoo.com/account/oauthloginform?s=eeda803ec23d4715980b747da7f0b687&t=10',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = session.get(url, headers=headers)
    data = etree.HTML(response.text)
    items = data.xpath('/html/body/div[6]/div/ul/li[2]/div[2]/ul')
    for item in items:
        subject = item.xpath('/html/body/div[6]/div/ul/li[2]/div[2]/ul/li/a[1]/@href')
        return subject


def joint_subject_url(lst):
    questions_url = []
    for end in lst:
        complete = 'http://www.jyeoo.com/' + end
        questions_url.append(complete)
    return questions_url


def get_chapter_params(lst):
    # for consice_url in lst:
    consice_url = lst[0]
    print(consice_url)
    headers = {
        'Host': 'www.jyeoo.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = session.get(consice_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # for li in soup.select('ul#JYE_BOOK_TREE_HOLDER li ul li'):
    #     params = li.attrs['bk']
    #     print(params)


def main():
    lst = get_subject_url()
    concise_url = joint_subject_url(lst)
    get_chapter_params(concise_url)


if __name__ == '__main__':
    main()


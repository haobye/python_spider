# 未完成

import requests
import re
from lxml import etree


def get_page_url(url):
    headers = {
        'referer': 'https://y.qq.com/portal/sw.js',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    new_url = re.findall(r'<div class="playlist__cover mod_cover">.*?href="(.*?)"', response.text, re.S)
    all_url = []
    for u in new_url:
        url = 'https:' + u
        all_url.append(url)
    return all_url


def get_all_music(all_url):
    for url in all_url[:4]:
        print(url)
        response = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
        })
        html = response.text
        select = etree.HTML(html)
        # print(select)
        # print(list(select))
        music = select.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/ul[2]/li/div/div[3]/span/a/@href')
        print(music)


def main():
    url = 'https://y.qq.com'
    all_url = get_page_url(url)
    get_all_music(all_url)


if __name__ == '__main__':
    main()







#
#
#
# # 未完成
#
# import requests
# import re
# from lxml import etree
# from bs4 import BeautifulSoup
#
#
# def get_num_key(url):
#     headers = {
#         'Referer': 'https://y.qq.com/portal/playlist.html',
#         'Host': 'y.qq.com',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     html = response.content.decode('utf-8')
#     key = re.findall(r'"dissid":"(.*?)"', html, re.S)
#     return key
#     # print(key)
#
#
# def get_cat_list(items):
#     all_url = []
#     for item in items:
#         cat_url = 'https://y.qq.com/n/yqq/playsquare/' + item + '.html#stat=y_new.playlist.pic_click'
#         all_url.append(cat_url)
#     return all_url
#     # print(all_url)
#
#
# def parser_music_key(all_url):
#     url = all_url[2]
#     # for url in all_url:
#     referer, no = url.split('#')
#     headers = {
#         'referer': referer,
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
#     }
#     html = requests.get(url, headers=headers).text
#     print(html)
#
#     # select = etree.HTML(html)
#     # music_url = select.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/ul[2]/li/div/div[3]/span/a/@href')
#     # soup = BeautifulSoup(html, 'html.parser')
#     # music_url = soup.find('span', class_="songlist__songname_txt")
#     # music_url = re.findall(r'<span class="songlist__songname_txt".*?href="(.*?)"', html, re.S)
#
#     # print(music_url)      # 无法拿到歌曲URL
#
#
# def main():
#     url = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.5763118180791627&g_tk=1806862358&jsonpCallback=a&loginUin=1009137312&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin=0&ein=29'
#     lis = get_num_key(url)
#     all_url = get_cat_list(lis)
#     parser_music_key(all_url)
#
#
# if __name__ == '__main__':
#     main()

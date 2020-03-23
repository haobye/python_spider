import requests
import re
from pyquery import PyQuery as pq


class Song(object):
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'Host': 'music.163.com',
            'Referer': 'https://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }

    def into_home(self):
        url = 'https://music.163.com/discover/playlist'
        response = self.session.get(url, headers=self.headers)
        return response

    def get_playlist_url(self, response):
        html = response.text
        rule = r'<a title=".*?" href="(.*?)"'
        data = re.findall(rule, html, re.S)
        items = []
        for item in data:
            item = ''.join(item)
            if item.startswith('/playlist?id='):
                url = 'https://music.163.com' + item
                items.append(url)
        return items

    def get_every_song_info(self, items):
        for url in items:
            # url = items[0]
            response_two = self.session.get(url, headers=self.headers)
            html = response_two.text
            doc = pq(html)
            data = doc('ul.f-hide')
            star = data.find('li').find('a').items()
            for single in star:
                id = single.attr('href')
                id = ''.join(id).replace('song', 'url')
                url = 'http://music.163.com/song/media/outer' + id + '.mp3'
                name = single.text()
                self.save_song(name, url)

    def save_song(self, name, url):
        response = self.session.get(url, headers=self.headers, allow_redirects=False)
        need_url = response.headers['Location']
        res = self.session.get(need_url)
        with open('E:\python爬虫\网易云/' + name + '.mp3', 'ab') as f:
            try:
                f.write(res.content)
                print(name, '--下载完成')
            except:
                print(name, '=====下载失败')
# 歌曲url应该有重复，显示下载63首，E盘实际写入41首，检查发现有重复歌曲下载

    def main(self):
        response = self.into_home()
        items = self.get_playlist_url(response)
        self.get_every_song_info(items)


if __name__ == '__main__':
    s = Song()
    s.main()

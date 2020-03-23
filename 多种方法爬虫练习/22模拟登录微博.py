# 未完成

import requests
from lxml import etree


s = requests.session()

url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn&uid=1890493665'
headers = {
    'Host': 'passport.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = s.get(url, headers=headers)
print(response.content.decode('gbk'))

login_url = 'https://passport.weibo.cn/sso/login1'
login_headers = {
    'Host': 'passport.weibo.cn',
    'Origin': 'https://passport.weibo.cn',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn&uid=1890493665',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
login_params = {
    'username': '18856185911',
    'password': 'hch20001116hch',
    'savestate': '1',
    'r': 'https://weibo.cn',
    'ec': '0',
    'pagerefer': '',
    'entry': 'mweibo',
    'wentry': '',
    'loginfrom': '',
    'client_id': '',
    'code': '',
    'qq': '',
    'mainpageflag': '1',
    'hff': '',
    'hfp': '',
}
response = s.get(login_url, headers=login_headers, params=login_params)
print(response.text)



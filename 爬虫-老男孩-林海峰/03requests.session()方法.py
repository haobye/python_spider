import requests
import re


session = requests.session()

url = 'https://github.com/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
}
res1 = session.get(url, headers=headers)
authenticity_token = re.findall(r'name="authenticity_token" value="(.*?)"', res1.text, re.S)[0]


url = 'https://github.com/session'
data = {
        'commit': '登入',
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'login': 'bobyhaohao',
        'password': 'hch20001116hch',
}
res2 = session.post(url, headers=headers, data=data)


# 在Email页面查看邮箱，以判断是否进入
url = 'https://github.com/settings/emails'
res3 = session.get(url)
print('2432387295@qq.com' in res3.text)

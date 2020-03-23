import requests
import re

# 在登陆网页获取下面data中所需信息authenticity_token，以及cookies（get_dict()直接转换为字典形式）
url = 'https://github.com/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
}
res1 = requests.get(url, headers=headers)

authenticity_token = re.findall(r'name="authenticity_token" value="(.*?)"', res1.text, re.S)[0]

cookies = res1.cookies.get_dict()

# 输入错误账号截取密码看是明文还是密文，在获取cookies
# 提交信息时带上获取的authenticity_token，cookies
url = 'https://github.com/session'
data = {
        'commit': '登入',
        'utf8': '✓',
        'authenticity_token': authenticity_token,
        'login': 'bobyhaohao',
        'password': 'hch20001116hch',
}
res2 = requests.post(url, headers=headers, data=data, cookies=cookies)

cookies2 = res2.cookies.get_dict()

# 在Email页面查看邮箱，以判断是否进入
url = 'https://github.com/settings/emails'
res3 = requests.get(url, cookies=cookies2)

# True为成功进入
print('2432387295@qq.com' in res3.text)

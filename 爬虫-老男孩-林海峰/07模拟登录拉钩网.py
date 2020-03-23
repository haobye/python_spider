# 步骤三的最后，获取信息不对
# 视频中源代码拿来运行也是错误

import requests
import re

session = requests.session()

# 步骤一
url = 'https://passport.lagou.com/login/login.html'
headers = {
    'Host': 'passport.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
}
res1 = session.get(url, headers=headers)

Token = re.findall(r"window.X_Anti_Forge_Token = '(.*?)'", res1.text, re.S)[0]
Code = re.findall(r"window.X_Anti_Forge_Code = '(.*?)'", res1.text, re.S)[0]
# print(Token)


# 步骤二
url = 'https://passport.lagou.com/login/login.json'
headers = {
    'Host': 'passport.lagou.com',
    'Referer': 'https://passport.lagou.com/login/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36',
    'X-Anit-Forge-Code': Code,
    'X-Anit-Forge-Token': Token,
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'isValidate': True,
    'username': '18856185911',
    'password': '055aa367f38ef62ded514d602fde7475',
    'request_form_verifyCode': '',
    'submit': '',
}
res2 = session.post(url, headers=headers, data=data)


# 步骤三
url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36',
    'Host': 'passport.lagou.com',
    'Referer': 'https://passport.lagou.com/login/login.html'
}
res3 = session.get(url, headers=headers, allow_redirects=False)     # False禁止跳转页面
# print(res3.text)      # 打印出跳转前的页面，为空
print(res3.headers['Location'])     # 卡死在这里，获取的内容（URL）与浏览器中不同


# 步骤四
url = res3.headers['Location']
headers = {
    'Host': 'www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
}
res4 = session.get(url, headers=headers, allow_redirects=True)


# 步骤五
res5 = session.get('http://www.lagou.com', headers={
                                        'Host': 'www.lagou.com',
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'})

print(res5.headers)

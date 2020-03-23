# 进行模拟登陆

import requests
import re
import json


s = requests.session()
url = 'https://passport.lagou.com/login/login.html'
headers = {
    'Host': 'passport.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
res1 = s.get(url, headers=headers)
html = res1.text
code = re.findall(r"window.X_Anti_Forge_Code = '(.*?)'", html)[0]
token = re.findall(r"window.X_Anti_Forge_Token = '(.*?)'", html)[0]
print(code)
print(token)


url = 'https://api.geetest.com/get.php'
headers = {
    'Host': 'api.geetest.com',
    'Origin': 'https://passport.lagou.com',
    'Referer': 'https://passport.lagou.com/login/login.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
res0 = s.post(url, headers=headers)
print(res0.headers)




# url = 'https://passport.lagou.com/login/login.json'
# headers = {
#     'Host': 'passport.lagou.com',
#     'Origin': 'https://passport.lagou.com',
#     'Referer': 'https://passport.lagou.com/login/login.html',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#     'X-Anit-Forge-Code': code,
#     'X-Anit-Forge-Token': token,
#     'X-Requested-With': 'XMLHttpRequest',
# }
# data = {
#     'isValidate': True,
#     'username': '18856185911',
#     'password': '055aa367f38ef62ded514d602fde7475',
#     'request_form_verifyCode': '',
#     'submit': '',
#     # 'challenge': 'af7ba312f26e6b0f0a10184cd08ac0aa',
# }
# res2 = s.post(url, headers=headers, data=data)
# print(res2.text)
# print(res2.headers)
#
#
# url = 'https://passport.lagou.com/grantServiceTicket/grant.html'
# headers = {
#     'Host': 'passport.lagou.com',
#     'Referer': 'https://passport.lagou.com/login/login.html',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# }
# res3 = s.get(url, headers=headers, allow_redirects=False)
# print(res3.text)
# print(res3.headers)


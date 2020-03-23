# from urllib.parse import urlencode
# import requests
# k = input('请输入需要查询的内容>>>').strip()
# res = urlencode({'wd':k}, encoding='utf-8')
# url = 'https://www.baidu.com/s?%s' % res
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
# response = requests.get(url, headers=headers)
# if response.status_code == 200:
#     with open('02.html', 'w', encoding='utf-8') as f:
#         f.write(response.text)
#         print('网址已下载至本地')



# 使用requests库
import requests
k = input('请输入需要查询的内容>>>').strip()
url = 'https://www.baidu.com/s?'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
params = {'wd':k}
response = requests.get(url, headers=headers, params=params)
with open('02.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
    print('完成')

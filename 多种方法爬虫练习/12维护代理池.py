# 怎样将代理池里的重复代理去除多余的
#       字典读取形式，去重

import requests
import json
import os


if os.path.exists('代理池-维护后.txt'):
    os.remove('代理池-维护后.txt')


lst = []
with open('代理池.txt', 'r') as f:
    data = f.readlines()
    print('代理池现有{}个代理···'.format(len(data)))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url = 'http://www.baidu.com/'
    for dic in data:
        proxies = dic.replace('\n', '')
        proxies = json.loads(proxies)
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=20)
            if response.status_code == 200:
                print('未失效：', proxies)
                with open('代理池-维护后.txt', 'a') as fp:
                    fp.write(json.dumps(proxies, ensure_ascii=False) + '\n')
        except:
            print('删除已失效代理', proxies)


with open('代理池-维护后.txt', 'r') as fr:
    line = fr.readlines()
    print('余下{}个可用代理'.format(len(line)))


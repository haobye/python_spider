# 先模拟登录，再抓取热榜问题及答案
# 未完成

import requests
import time


def get_time():
    now = int(time.time())
    local = time.localtime(now)
    fm = time.strftime('%Y.%m.%d', local)
    print(fm)


def get_hot_url():
    url = 'https://www.zhihu.com/hot'
    headers = {
        'referer': 'https://www.zhihu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response.text)


def main():
    get_time()
    get_hot_url()


if __name__ == '__main__':
    main()

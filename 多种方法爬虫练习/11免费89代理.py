import requests
import re
import json


def get_page(page):
    url = 'http://www.89ip.cn/index_' + str(page) + '.html'
    headers = {
        'Host': 'www.89ip.cn',
        'Referer': 'http://www.89ip.cn/ti.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    data = re.findall(r'<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>', html, re.S)
    lst = []
    for a in data:
        a = list(a)
        ip = ''.join(a[0]).replace('\n', '').replace('\t', '')
        prot = ''.join(a[1]).replace('\n', '').replace('\t', '')
        http = 'http://' + ip + ':' + prot
        proxies = {'http': http}
        lst.append(proxies)
    return lst


def try_proxies(lst):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url = 'http://www.baidu.com/'
    for proxies in lst:
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            state = response.status_code
            if state == 200:
                save_effective(proxies)
                print('加入代理池>>>', proxies)
        except:
            print('失效', proxies)


def save_effective(proxies):
    with open('代理池.txt', 'a') as f:
        f.write(json.dumps(proxies, ensure_ascii=False) + '\n')


def main():
    for page in range(5):
        lst = get_page(page)
        try_proxies(lst)


if __name__ == '__main__':
    main()

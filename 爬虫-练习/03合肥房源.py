import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import os
import json


if os.path.exists('合肥房源.txt'):
    os.remove('合肥房源.txt')


def get_one_page(page, url):
    data = {
        '__VIEWSTATE': '/ wEPDwULLTE5MDQ3MzMzNzMPZBYCAgMPZBYEAgsPFgIeC18hSXRlbUNvdW50Ag8WHmYPZBYCZg8VCQQ1ODQ0CTIwMTgxMjAwNAQ1ODQ0GOS4h + i + vuaWh + aXheaWsOWfjuWbm + acnxEyOCwzMSwzMiwzNiwzNywzOAg4OTM2NS4yMAM3MDMJMTksMTg4LjQ4BDAuMDBkAgEPZBYCZg8VCQQ1ODI2CTIwMTgxMTA1MAQ1ODI2CeaWh + azsOmZogMyMSMHNzk2Ny42NwI0NAkyMSwxNjUuMTIEMC4wMGQCAg9kFgJmDxUJBDU4MjUJMjAxODExMDQ5BDU4MjUJ5paH5rOw6ZmiBzEzIywxNCMIMTMyODAuMDMCNjAJMjEsMDEzLjQ0BDAuMDBkAgMPZBYCZg8VCQQ1ODI3CTIwMTgxMTA0OAQ1ODI3DOingeWxseiKseWbrR0zLTEwLDMtMTEsMy0xMiwzLTEzLDMtMTQsMy0xNQgyNTE0My42NgMxNTYJMTksMDA4LjE1BDAuMDBkAgQPZBYCZg8VCQQ1NzIzCTIwMTgxMDAzMwQ1NzIzEuiejeenkeWfjuWIm + mikOWbrQoxMSwzLDEyLDEzCDY0NDIwLjAxAzU2MwkxNSwxMzUuODEKMjg4LDcxMC4zM2QCBQ9kFgJmDxUJBDU3MTcJMjAxODExMDQ1BDU3MTcJ5Yek5pum5bqcGzE5IywyMCMsMjIjLDIxIywyMyMsMjQjLDI1Iwg4MzM4My4yNQM0MjAJMjIsMTI4LjQyCjY5NCw4NjAuNDJkAgYPZBYCZg8VCQQ1ODAyCTIwMTgxMTAzNgQ1ODAyDOS6keWzsOiKseWbrSRHMSxHMixHMyxHMTAsRzExLEcxMyxHMTUsRzE2LEcxNyxHMTkJMTA3NzgzLjk4AzkyNAkxNCwwNzAuODkKMjkxLDYyMy4zMmQCBw9kFgJmDxUJBDU2NTcJMjAxODExMDQyBDU2NTcM6IyC5oKm6Iqx5ZutBUcyLFk1CDE2MjQ4LjI0AzEzMgkxOCw3OTkuOTgKMzkzLDg5Ni43M2QCCA9kFgJmDxUJBDU3ODAJMjAxODExMDMxBDU3ODAb5Lit5Zu96ZOB5bu66Z2S56eA5Z + O55Kf5ZutCDMjLDQjLDUjCDQwNjA0LjM2AzQ0OAkxNCwxODguODgKMTgxLDI2OS40NmQCCQ9kFgJmDxUJBDU3ODgJMjAxODExMDMzBDU3ODgM5aSn5oiQ6Iqx6IuRCUExNSMsQTE2IwgxMTk1My42NwI4MAkyMywwNjYuMzAEMC4wMGQCCg9kFgJmDxUJBDU3ODkJMjAxODExMDM0BDU3ODkM5Y2X5LiD6Iqx5ZutF0EwMuWcsOWdlzEyLEEwM + WcsOWdlzI0Bzg1MjguNDQCNDgJMjIsMTM1LjQ1BDAuMDBkAgsPZBYCZg8VCQQ1Nzg2CTIwMTgxMTAzMgQ1Nzg2DOingeWxseiKseWbrQwxLTgsMS05LDEtMTAIMjMwNzUuMzMCNzEJMjcsMDAwLjIzBDAuMDBkAgwPZBYCZg8VCQQ1Nzc3CTIwMTgxMTAzNwQ1Nzc3CeawtOacqOWbrRMxIywyIywzIyw1Iyw2IyAgLDcjCDk2MTY0LjIzAzgyOQkxNCwwNzEuMzYKNTgwLDAwMS4zOWQCDQ9kFgJmDxUJBDU3NjgJMjAxODExMDE4BDU3NjgJ5a2m5oiQ6YeMAzIsNQgyNTI1MS4xNAMyNDYJMTQsMDcxLjA5CjI1Niw2MTcuMjhkAg4PZBYCZg8VCQQ1Nzc0CTIwMTgxMTAxNQQ1Nzc0EuS4lue6quiNo + W7t + Wwj + WMugU0Myw0MggyOTIyMi45OQMzMDgIOSw4NzYuODcEMC4wMGQCDQ8PFgQeC1JlY29yZGNvdW50AvcUHhBDdXJyZW50UGFnZUluZGV4AgJkZGRMcxbnGpEe5HGd264x3CQYFi0TWg ==',
        '__EVENTTARGET': 'AspNetPager1',
        '__EVENTARGUMENT': page,
        '__EVENTVALIDATION': '/ wEWBgL52K6MAgK38b7MBgLKwJ / YAQKq7uP1CgKt7uP1CgKM54rGBoe / rFP07QNZYhyafbcjwDYjYrj3',
        'AspNetPager1_input': 1
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': '220.178.124.94',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
    }
    try:
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求页面出错')
        return None


def parser_one_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('tr')[2:].__str__()
    data = data.replace(' ', '')
    # print(data)
    rule = r'<tr>\n<tdalign="center"nowrap="nowrap">\n<ahref=".*?"target="_blank">\r\n(.*?)</a>\n</td>\n<tdalign="center"nowrap="nowrap">\n<ahref=".*?"target="_blank">\r\n(.*?)\r\n</a>\n</td>\n<tdalign=".*?">\r\n(.*?)\r\n</td>\n<tdalign="center"nowrap="nowrap">\r\n(.*?)\xa0\r\n</td>\n<tdalign="center"nowrap="nowrap">\r\n(.*?)\r\n</td>\n<tdalign="center"nowrap="nowrap">\r\n(.*?)\xa0\r\n</td>\n<tdalign="center"nowrap="nowrap">\r\n(.*?)\xa0\r\n</td>\n</tr>'
    pattern = re.compile(rule, re.S)
    items = re.findall(pattern, data)
    return items


def write_one_page(content):
    with open('合肥房源.txt', mode='a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        # dumps可将dict转换成str


def main(page):
    url = 'http://220.178.124.94/fangjia/ws/DefaultList.aspx'
    html = get_one_page(page, url)
    items = parser_one_page(html)
    for item in items:
        write_one_page(item)


if __name__ == '__main__':
    for i in range(1, 3):
        main(i)





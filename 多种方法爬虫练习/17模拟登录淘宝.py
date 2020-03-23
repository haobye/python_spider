# 飞机
# import http.cookiejar as cookielib
# import requests
#
#
# taobaosession=requests.session()
# taobaosession.cookies = cookielib.LWPCookieJar(filename='taobaocookies.txt')
#
# headers={
#     'origin': 'https://login.taobao.com',
#     'referer': 'https://login.taobao.com/member/login.jhtml?spm=a2e15.8261149.754894437.1.3b5e29b4UC9Aqd&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%26clk1%3D9bc4c9c651796282f8a9a98f52c5f5ec%26upsid%3D9bc4c9c651796282f8a9a98f52c5f5ec',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
# }
#
#
# def taobaologin(user,pwd):
#     url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%26clk1%3D9bc4c9c651796282f8a9a98f52c5f5ec%26upsid%3D9bc4c9c651796282f8a9a98f52c5f5ec'
#     data = {
#         'TPL_username': user,
#         'TPL_password': pwd
#     }
#     response=taobaosession.post(url,headers=headers,data=data)
#     print(f"statusCode = {response.status_code}")
#     print(f"text = {response.text}")
#     taobaosession.cookies.save()
#
#
# def isLoginStatus():
#     logurl='https://www.taobao.com/markets/footmark/tbfoot?spm=a1z02.1.a2109.d1000391.20e0782dTqaAB7'
#     response=taobaosession.get(logurl,headers=headers,allow_redirects=False)
#     print(f'status_code={response.status_code}')
#     if response.status_code!=200:
#         return False
#     else:
#         return True
#
#
# if __name__ == '__main__':
#     taobaosession.cookies.load()
#     islogin=isLoginStatus()
#     print(f'is login={islogin}')
#     if islogin == False:
#         print(f"cookie失效，用户重新登录...")
#         taobaologin('18715200797','aaa')
#
#     res=taobaosession.post('https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8',headers=headers,allow_redirects = False)
#     print(f'res_status={res.status_code}')

import http.cookiejar as cookielib
import requests


taobaosession=requests.session()
taobaosession.cookies = cookielib.LWPCookieJar(filename='taobaocookies.txt')

headers={
    'origin': 'https://login.taobao.com',
    'referer': 'https://login.taobao.com/member/login.jhtml?spm=a2e15.8261149.754894437.1.3b5e29b4UC9Aqd&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%26clk1%3D9bc4c9c651796282f8a9a98f52c5f5ec%26upsid%3D9bc4c9c651796282f8a9a98f52c5f5ec',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}


def taobaologin(user,pwd):
    url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%26clk1%3D9bc4c9c651796282f8a9a98f52c5f5ec%26upsid%3D9bc4c9c651796282f8a9a98f52c5f5ec'
    data = {
        'TPL_username': user,
        'TPL_password': pwd
    }
    response=taobaosession.post(url,headers=headers,data=data)
    print(f"statusCode = {response.status_code}")
    print(f"text = {response.text}")
    taobaosession.cookies.save()


def isLoginStatus():
    logurl='https://www.taobao.com/markets/footmark/tbfoot?spm=a1z02.1.a2109.d1000391.20e0782dTqaAB7'
    response=taobaosession.get(logurl,headers=headers,allow_redirects=False)
    print(f'status_code={response.status_code}')
    if response.status_code!=200:
        return False
    else:
        return True


if __name__ == '__main__':

    taobaologin('18715200797','104119aa')



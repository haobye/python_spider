# 需要注意：
#   1、每一页下拉到最下面，网页还会再加载出一部分商品信息（找出更好的解决方法）
#               1、人为沉睡      2、使用EC看第六十个是否加载出来了
#   2、没有获取到图片链接，付款链接


import json
import os
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

if os.path.exists('京东查询.txt'):
    os.remove('京东查询.txt')

# 定义一个浏览器
chrome_options = Options()
# 设置chrome 浏览器无界面模式
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()

wait = WebDriverWait(browser, 10)


def search():
    try:
        words = input('请输入需要查询的关键字>>>')
        browser.get('https://www.jd.com/')
        key = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div.form > button > i')))
        key.send_keys(words)
        button.click()
        all_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        total = all_page.text
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li:nth-child(60)')))
        parser_content()
        return total
    except TimeoutError:
        return search()


def next_page(page):
    try:
        write = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input')))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a')))
        write.clear()
        write.send_keys(page)
        button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page)))
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li:nth-child(60)')))
        parser_content()
    except TimeoutError:
        next_page(page)


def parser_content():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gl-warp .gl-item')))
    html = browser.page_source
    doc = pq(html)
    items = doc.find('.gl-warp .gl-item').items()
    lst = []
    for item in items:
        dic = {
            'url': item.find('.p-img a').attr('href'),
            'price': item.find('.p-price').text()[2:],
            'title': item.find('.p-name').text().replace('\n', ''),
            'talk': item.find('.p-commit').text()[:-5],
            'store': item.find('.curr-shop').text(),
            'welfare': item.find('.p-icons').text().replace('\n', '，')
        }
        lst.append(dic)
    return lst


def save_data(page, lst):
    with open('京东查询.txt', 'a+', encoding='utf-8') as f:
        print('正在写入第{}页'.format(page))
        for data in lst:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')


def main():
    total = search()
    total = int(total)
    for page in range(1, total+1):
        next_page(page)
        lst = parser_content()
        save_data(page, lst)


if __name__ == '__main__':
    main()
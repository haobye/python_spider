# 使用selenium库，很简单很方便
# 用rpquery没有解析出页面，改用lxml就可以了
# 使用了无界面浏览器

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options
import os
from lxml import etree


if os.path.exists('起点.txt'):
    os.remove('起点.txt')

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)


def first():
    try:
        url = 'https://www.qidian.com/all'
        browser.get(url)
        page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#page-container > div > ul > li:nth-child(8) > a')))
        total = page.text
        return total
    except TimeoutError:
        return first()


def page_down(page):
    try:
        write = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#PAGINATION-INPUT')))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#PAGINATION-BUTTON')))
        write.clear()
        write.send_keys(page)
        button.click()
        parser()
    except TimeoutError:
        page_down(page)


def parser():
    html = browser.page_source
    data = etree.HTML(html)
    items = data.xpath('/html/body/div[2]/div[5]/div[2]/div[2]/div/ul/li')
    for item in items:
        name = item.xpath('./div[2]/h4/a/text()')
        name = ''.join(name)
        info = item.xpath('./div[2]/p[1]//text()')
        info = ''.join(info).replace('\n', '').replace(' ', '')
        summary = item.xpath('./div[2]/p[2]/text()')
        summary = ''.join(summary).replace('\n', '').replace(' ', '')
        url = item.xpath('./div[2]/h4/a/@href')[0]
        yield {
            'name': name,
            'url': url,
            'info': info,
            'summary': summary,
        }


def save_data(data):
    with open('起点.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def main():
    total = int(first())
    for i in range(1, total+1):
        page_down(i)
        content = parser()
        print('正在写入第{}页'.format(i))
        for data in list(content):
            save_data(data)


if __name__ == '__main__':
    main()
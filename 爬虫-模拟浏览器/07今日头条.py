# 点不到图集

from lxml import etree
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# option = Options()
# option.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=option)
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)


def get_home_page():
    try:
        browser.get('https://www.toutiao.com/')
        write = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#rightModule > div.search-wrapper > div > div > div.tt-input.tt-input-group.tt-input-group--append > input')))
        ok = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rightModule > div.search-wrapper > div > div > div.tt-input.tt-input-group.tt-input-group--append > div > button > span')))
        write.send_keys('街拍')
        ok.click()
        next_step()
    except TimeoutError:
        get_home_page()


def next_step():
    try:
        photo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div > div.y-box.container > div.y-left.index-middle > div.tabBar > ul > li.y-left.tab-item.active')))
        photo.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div.y-box.container > div.y-left.index-middle > div.feedBox.child-style > div > div')))
        parser()
    except TimeoutError:
        next_step()


def parser():
    html = browser.page_source
    data = etree.HTML(html)
    into = data.xpath('//div[contains(@id, "J_section")]/div/div/div[1]/div/div[1]/a/@href')
    print(into)


def main():
    get_home_page()


if __name__ == '__main__':
    main()

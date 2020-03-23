from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def get_home_page():
    browser = webdriver.Chrome()
    browser.get('https://www.geetest.com/type/')
    wait = WebDriverWait(browser, 10)
    target = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > section > div > ul > li:nth-child(2)')))
    target.click()
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#captcha > div.geetest_holder.geetest_wind.geetest_detect > div.geetest_btn > div.geetest_radar_btn > div.geetest_radar_tip > span.geetest_radar_tip_content')))
    button.click()
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.geetest_holder.geetest_mobile.geetest_ant.geetest_popup > div.geetest_popup_box > div.geetest_popup_wrap > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_slice.geetest_absolute')))
    time.sleep(3)
    browser.save_screenshot('photo2.png')


def get_end_photo():
    pass
    # top = img.location['y']
    # left = img.location['x']
    # right = img.location['x']+img.size['width']
    # bottom = img.location['y']+img.size['height']


def get_space():
    pass


def get_tracks():
    pass


def main():
    get_home_page()
    # get_end_photo()


if __name__ == '__main__':
    main()




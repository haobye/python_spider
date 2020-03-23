from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
# PIL模块最大支持python2.7
# pip install pillow就是封装了PIL

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 4)


def get_photo():
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
    browser.save_screenshot('snap.png')


try:
    browser.get('https://account.geetest.com/login')
    email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    email.send_keys('1234')
    password.send_keys('23456')
    validation = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_tip')))
    validation.click()
    get_photo()
finally:
    browser.close()








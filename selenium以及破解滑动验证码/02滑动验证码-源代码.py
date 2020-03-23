# 安装PIL模块
# pip3 install pillow

# 视频中的极验网站已改进，现在需要通过更改js数据来得到没有缺口的图片

# 代码失效

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time
from PIL import Image


def get_image(driver, n):
    canvas = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
    left = canvas.location['x']
    top = canvas.location['y']
    elementWidth = canvas.location['x'] + canvas.size['width']
    elementHeight = canvas.location['y'] + canvas.size['height']
    driver.save_screenshot(n + '.png')
    picture = Image.open(n + '.png')
    picture = picture.crop((left, top, elementWidth, elementHeight))
    picture.save('photo' + n + '.png')
    return picture


def get_space(picture1, picture2):
    start = 60
    threhold = 60

    for i in range(start, picture1.size[0]):
        for j in range(picture1.size[1]):
            rgb1 = picture1.load()[i, j]
            rgb2 = picture2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                return i
    return i - 10


def get_tracks(space):
    space += 20  # 先滑过一点，最后再反着滑动回来
    v = 0
    t = 0.2
    forward_tracks = []

    current = 0
    mid = space * 3 / 5
    while current < space:
        if current < mid:
            a = 2
        else:
            a = -3

        s = v * t + 0.5 * a * (t ** 2)
        v = v + a * t
        current += s
        forward_tracks.append(round(s))

    # 反着滑动到准确位置
    back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -3, -4]

    return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 4)
    driver.get('http://www.geetest.com/type/')
    # driver.get('https://account.geetest.com/login')
    # email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    # password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    # email.send_keys('1234')
    # password.send_keys('23456')

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/section/div/ul/li[2]/h2').click()
    time.sleep(1)
    # 1、出现滑块验证，获取有缺口的图片
    driver.find_element_by_xpath('//*[@id="captcha"]/div[2]/div[2]/div[1]/div[3]/span[1]').click()
    time.sleep(1)
    picture1 = get_image(driver, '1')
    # 2、执行js改变css样式，显示背景图
    driver.execute_script('document.querySelectorAll("canvas")[2].style=""')
    time.sleep(1)
    # 3、获取没有缺口的图片
    picture2 = get_image(driver, '2')
    # 4、对比两种图片的像素点，找出位移
    space = get_space(picture1, picture2)
    tracks = get_tracks(space)
    button = driver.find_element_by_class_name('geetest_slider_button')
    ActionChains(driver).click_and_hold(button).perform()
    for track in tracks['forward_tracks']:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
    time.sleep(0.5)
    for back_track in tracks['back_tracks']:
        ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()
    time.sleep(1)
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()










# def get_image():
#     # 拿到验证码图片在整个页面的元素
#     img=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
#     time.sleep(2)  # 保证验证码图片已经被加载成功
#     driver.save_screenshot('snap.png')
#
#     # 拿到图片的位置
#     top=img.location['y']
#     left=img.location['x']
#     right=img.location['x']+img.size['width']
#     bottom=img.location['y']+img.size['height']
#
#     from PIL import Image
#     full_snap=Image.open('snap.png')
#     crop_image=full_snap.crop((left,top,right,bottom))
#
#     # crop_image.show() #显示剪裁后的图片
#     # crop_image.size #宽weight和高height
#
#     return crop_image
#
#
# def get_distance(image1,image2):
#     p1=image1.load()
#     p2=image2.load()
#     x=60
#     for i in range(x,image1.size[0]):
#         for j in range(20,image1.size[1]-20):
#             print(i,j)
#             dot1=p1[i,j]
#             dot2=p2[i,j]
#             r=abs(dot1[0]-dot2[0])
#             g=abs(dot1[1]-dot2[1])
#             b=abs(dot1[2]-dot2[2])
#             if not (r < 60 and g < 60 and b < 60):
#                 return i-7
#
#
# def get_tracks(distance):
#     t = 0.2
#     v = 0
#     mid=distance*3/5
#     tracks=[]
#
#     current=0
#     while current < distance:
#         if current < mid:
#             a=2
#         else:
#             a=-3
#         v0 = v
#         s = v0 * t + 0.5 * a * (t ** 2)
#         current+=s
#         v=v0+a*t
#         # print(round(s))
#
#         tracks.append(round(s))
#     return tracks
#
#
# driver=webdriver.Chrome()
# wait=WebDriverWait(driver,10)
#
# try:
#     # 步骤一：访问登录页面，拿到点击按钮，点击出图（完整的图）
#     driver.get('https://account.geetest.com/login')
#     email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
#     password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
#     email.send_keys('1234')
#     password.send_keys('23456')
#
#     button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_radar_tip')))
#     button.click()
#
#     # 步骤二：拿到验证码图片（没有缺口）
#     image1=get_image()
#
#     # 步骤三：拿到滑动按钮，点击出图（有缺口的图）
#     button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
#     button.click()
#
#     # 步骤四：拿到验证码图片（有缺口）
#     image2=get_image()
#
#     # 步骤五：对比两种图的像素RGB,得到不一样的像素点，取位移
#     distance=get_distance(image1,image2)
#     print(image1.size)
#     print(image2.size)
#     print(distance)
#
#     # 步骤六：把distance分解成一段一段的小轨迹，模拟人的行为：先匀加速再匀减速
#     tracks=get_tracks(distance)
#
#     # 步骤七：按照轨迹列表先匀加速移动再匀减速运动
#     button=wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
#     ActionChains(driver).click_and_hold(button).perform()
#     for track in tracks:
#         ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
#     else:
#         ActionChains(driver).move_by_offset(xoffset=3,yoffset=0).perform()
#         ActionChains(driver).move_by_offset(xoffset=-3,yoffset=0).perform()
#
#     time.sleep(0.5)
#     ActionChains(driver).release().perform()
#
#     time.sleep(10)
#
# finally:
#     driver.close()


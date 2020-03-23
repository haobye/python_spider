# 主要解决网页中JavaScript渲染
# 需下载浏览器driver文件至python中scrip目录下

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# # 声明浏览器对象
# browser = webdriver.Chrome()
# try:
#     browser.get('https:www.baidu.com')    # 打开百度
#     input = browser.find_element_by_id('kw')    # 准备搜索关键词
#     input.send_keys('Python')              # 输入文本python
#     input.send_keys(Keys.ENTER)             # 模拟点击，和input.click()效果一样
#     wait = WebDriverWait(browser,10)        # 显式等待10秒
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#                                                           # # EC.presence_of_element_located是确认元素是否已经出现了
#                                                           # # EC.element_to_be_clickable（）是确认元素是否是可点击的
#     print(browser.current_url)        # 输出现在的url地址
#     print(browser.get_cookies())      # 输出当前cookie
#     print(browser.page_source)        # 输出此页的源代码
# finally:
#     browser.close()


# # # 查找单个节点的方法
'''
# # find_element_by_id
# # find_element_by_name
# # find_element_by_xpath
# # find_element_by_link_text
# # find_element_by_partial_link_text
# # find_element_by_tag_name
# # find_element_by_class_name
# # find_element_by_css_selector
'''
# # 单个节点查找（以淘宝网举例）
# browser = webdriver.Chrome()
# browser.get('http:www.taobao.com')
# one = browser.find_element_by_id('J_SearchTab')     # 查找id，css、xpath都是类似的
# print(one)
# browser.close()
#
# # 通用方法查找：
# browser = webdriver.Chrome()
# browser.get('http:www.taobao.com')
# one = browser.find_element(By.ID, 'J_SearchTab')
# print(one)
# browser.close()
# # find_element()里面需要两个参数，查找方式By和值，
# # 例如：find_element(By.ID,'J_SearchTab') 通过查找ID的同时，查找id为J_SearchTab。



# # 多个节点查找
# #获取多个节点的方法：
'''
find_elements_by_id
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
通用方法在这里同样适用。
'''
# browser = webdriver.Chrome()
# browser.get('http:www.taobao.com')
# lot_1 = browser.find_elements_by_css_selector('.service-bd')
# # [<selenium.webdriver.remote.webelement.WebElement (session="5758b568bcdc95c6635572a0cd84d311", element="0.4183302540140885-1")>]
# print(lot_1)
# browser.close()



# # 节点交互
# import time
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()  # 点击
# # # 自己写一遍
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# input = browser.find_element_by_id('kw')
# input.send_keys('one_fine')
# input.clear()
# time.sleep(1)
# input.send_keys('selenium库中交互动作链')
# input.send_keys(Keys.ENTER)
# ############## 下面的这个点击亦可使用
# # button = browser.find_element_by_id('su')
# # button.click()



# # 动作链
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')             # 定位切换到里面
# source = browser.find_element_by_css_selector('#draggable')         # 找到被拖拽的标签
# target = browser.find_element_by_css_selector('#droppable')         # 找到拖拽目的地的标签
# actions = ActionChains(browser)             # 对browser使用ActionChains的方法
# actions.drag_and_drop(source, target)       # 拖拽某个元素然后分开
# actions.perform()               # 执行链接中所有动作



# # # 执行JavaScript
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'http://www.zhihu.com/explore'
# browser.get(url)
# browser.execute_script('')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom 最下")')



# # # 获取属性
# browser = webdriver.Chrome()
# url = 'http://www.zhihu.com/explore'
# browser.get(url)
# a = browser.find_element_by_class_name('post-link')
# print(a)
# print(a.get_attribute('href'))  # 属性
# print(a.text)           # 文本
# print(a.id)             # ID
# print(a.location)       # 位置
# print(a.tag_name)       # 标签名
# print(a.size)           # 大小
# browser.close()



# # 关于Frame
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# # source = browser.find_element_by_css_selector('#draggable')
# # print(source)
# # try:
# #     logo = browser.find_element_by_class_name('logo')
# # except NoSuchElementException:
# #     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)



# # 隐式等待
# url = 'http://www.zhihu.com/explore'
# browser = webdriver.Chrome()
# browser.implicitly_wait(5)
# browser.get(url)
# content = browser.find_element_by_id('zh-recommend-list')
# print(content)
############
# # 显式等待（最上面的就是）
# # EC.presence_of_element_located（）是确认元素是否已经出现了
# # EC.element_to_be_clickable（）是确认元素是否是可点击的
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)
#
'''
title_is 标题是某内容
title_contains 标题包含某内容
presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
visibility_of_element_located 元素可见，传入定位元组
visibility_of 可见，传入元素对象
presence_of_all_elements_located 所有元素加载出
text_to_be_present_in_element 某个元素文本包含某文字
text_to_be_present_in_element_value 某个元素值包含某文字
frame_to_be_available_and_switch_to_it frame加载并切换
invisibility_of_element_located 元素不可见
element_to_be_clickable 元素可点击
staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
element_to_be_selected 元素可选择，传元素对象
element_located_to_be_selected 元素可选择，传入定位元组
element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
alert_is_present 是否出现Alert
'''


# # 浏览器的前进、后退
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()        # 依此请求上面的三个页面，在后退回淘宝
# time.sleep(1)
# browser.forward()     # 再前进到python
# browser.close()


# # 获取cookies
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


# # 选项卡管理
# # 通过执行js命令实现新开选项卡window.open()
# # 不同的选项卡是存在列表里browser.window_handles
# # 通过browser.window_handles[0]就可以操作第一个选项卡
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')
# # 自己来一次
# import time
# browser = webdriver.Chrome()
# browser.get('http://baidu.com')
# browser.execute_script('window.open()')
# browser.switch_to_window(browser.window_handles[1])
# browser.get('http://taobao.com')
# browser.switch_to_window(browser.window_handles[0])
# input = browser.find_element_by_id('kw')
# input.send_keys('我不、不、不、、、是最棒的')
# time.sleep(3)
# input.clear()
# time.sleep(3)
# input.send_keys('我是最棒的')
# input.send_keys(Keys.ENTER)



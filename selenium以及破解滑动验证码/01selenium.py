from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
#
# # 隐式等待，下面所有的元素都有等待效果
# browser.implicitly_wait(4)
# #
# # 显式等待，明确等待某些元素被加载
# wait = WebDriverWait(browser, 4)
#
# browser.get('https://www.baidu.com')



# 动作链，滑动验证
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')         # 定位切换到里面(swith_to_frame封装为swith_to.frame)
one = browser.find_element_by_id('draggable')
two = browser.find_element_by_id('droppable')
action = ActionChains(browser)          # 对browser使用ActionChains的方法
action.drag_and_drop(one, two)          # 拖拽某个元素然后分开
action.perform()                         # 执行链接中所有动作


from pyquery import PyQuery as pq

html = '''
<div class="movie-list-item unplayable unwatched">
    <div class="movie-content">
        <div class="movie-info">
            <div class="movie-name">
                <span class="movie-name-text">
                    <a id='1' href="https://movie.douban.com/subject/1296141/" target="_blank">
                    控方证人
                     </a>
                     <a class='one two' href="https://movie.douban.com/subject/1296141/">
                    DOM操作
                     </a>
                     <a id='2' id='5' href="https://movie.douban.com/subject/121/" target="_blank">
                    补充为第二个
                     </a>
                     <a id='3'  href="https://movie.douban.com/subject/16141/" target="_blank">
                    补充为第三个(现为第四个）
                     </a>
                     <p class='emmm'>dfghjk后续呢<span>咋地</span></p>
                     <p id='77'>实验田ertyui</p>
                 </span>
            </div>
        </div>
    </div>
</div>
'''

# # 初始化
#
# 1、打印所有a标签
# doc = pq(html)
# print(doc('a'))
#
# 2、输出网站头部信息
# doc = pq(url='http://www.baidu.com/')
# print(doc('head'))
#
# 3、也可以初始化本地文件
# doc = pq(filename='dochtml.html')   # 不存在此文件，只用于举例子
# print(doc('span'))


# #基本CSS选择器
#
# 1、打印class使用.点    打印id使用#    打印标签就什么都不加
#    可以叠加使用，不一定非要父与子，只要有层级关系就可
# doc = pq(html)
# print(doc('.movie-name a'))
#
# 2、子元素
# doc = pq(html)
# a_s = doc('.movie-name-text')
# a = a_s.find('a')
# print(a)
#
# 3、父元素
# doc = pq(html)
# span = doc('.movie-name-text')
# # far = span.parent()
# # print(far)
# 3.2、祖父元素
# # fars = span.parents()
# # # print(fars)
# 3.3、特定的一个父元素
# far_one = span.parents('.movie-info')
# print(far_one)
#
# 4、兄弟元素(只输入它的兄弟)
# doc = pq(html)
# a = doc('.movie-name-text #1')
# print(a.siblings())
# # 4.2、特定兄弟
# # doc = pq(html)
# # a = doc('.movie-name-text #1')
# # print(a.siblings('#2'))


# # 遍历
# doc = pq(html)
# dd = doc('a').items()
# for d in dd:
#     print(d)


# 1、获取属性
# doc = pq(html)
# a = doc('#1')
# print(a.attr('href'))   # 常用
# print(a.attr.href)
#
# 2、获取文本
# doc = pq(html)
# a = doc('#1')
# print(a.text())
#
# 3、获取HTML（里面的HTML内容）
# doc = pq(html)
# all_a = doc('.movie-name-text')
# print(all_a.html())


# # DOM操作，即修改
#
# 1、类class的增减
# doc = pq(html)
# a = doc('.one.two')
# print(a)
# a.remove_class('two')
# print(a)
# a.add_class('three')
# print(a)
#
# # 2、attr，css
# doc = pq(html)
# p = doc('#77')
# print(p)
# p.attr('name', 'xinyue')
# print(p)
# p.css('font', 'love-14px')
# print(p)
#
# # 3、remove
# doc = pq(html)
# p = doc('.emmm')
# print(p.text())
# p.find('span').remove()
# print(p.text())


# 伪类选择器
doc = pq(html)
# one_a = doc('a:first-child')
# print(one_a)
# two_a = doc('a:nth-child(2)')
# print(two_a)
# last_p = doc('p:last-child')
# print(last_p)
#
# even = doc('a:nth-child(2n)')    # 获取第偶数个 a的标签（2n+1可表示奇数）
# print(even)
# big = doc('a:gt(1)')        # a标签中大于第一个的
# print(big)
# none = doc('a:contains(操作)')    # 获取text中带有'操作'的
# print(none)









import requests
import re


url = 'https://www.autohome.com.cn/news/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'}
response = requests.get(url, headers=headers).content.decode('gbk')

for i in range(15):
    dic = {}
    # dic['详情页链接'] = re.findall(r'<li data-artidanchor.*?href="(.*?)"', response, re.S)
    dic['标题图片链接'] = re.findall(r'class="article-pic".*?src="(.*?)"', response, re.S)[i]
    dic['标题'] = re.findall(r'<h3>(.*?)</h3>', response, re.S)[i]
    dic['发布时间'] = re.findall(r'<span class="fn-left">(.*?)</span>', response, re.S)[i]
    # dic['阅读次数'] = re.findall(r'<i class="icon12 icon12-eye"></i>"(.*?)"</em>', response, re.S)[i]
    # dic['评论次数'] = re.findall(r'<i class="icon12 icon12-infor"></i>"(.*?)"</em>', response, re.S)
    dic['简介'] = re.findall(r'<i class="icon12 icon12-infor"></i>.*?<p>(.*?)</p>', response, re.S)[i]
    print(dic)

# 阅读次数,评论次数时隐时现，，详情页链接从未现身

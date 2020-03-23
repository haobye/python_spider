# 将手机号替换为123****4567
import re

nell = '12399994567'
pattern = re.compile('^(\d{3})(\d{4})(\d{4})$')
print(pattern.sub(r'\1****\3', nell))


# 匹配中文
strs = '你好，hello，世界'
pattern = re.compile('[\u4e00-\u9fa5]+')
print(pattern.findall(strs))





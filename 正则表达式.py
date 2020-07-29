#   re模块的介绍     在Python中需要通过正则表达式对字符串进行匹配的时候，可以使用一个 re 模块
import re

# 使用match方法进行匹配操作
result = re.match("itcast","itcast.cn")  # re.match() 根据正则表达式从头开始匹配字符串数据
# 获取匹配结果
info = result.group()   # 如果上一步匹配到数据的话，可以使用group方法来提取数据
print(info)

print("匹配单个字符   示例1：")
import re

ret = re.match(".","M")
print(ret.group())

ret = re.match("t.o","too")
print(ret.group())

ret = re.match("t.o","two")
print(ret.group())

# ...
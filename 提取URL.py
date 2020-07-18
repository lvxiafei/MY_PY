import re


def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url[0]


string = 'Google 的网页地址为：https://www.google.com/events/123'
print(Find(string))

# w2:
from urllib.parse import *

url = 'https://docs.google.com/spreadsheet/ccc?key=blah-blah-blah-blah#gid=1'
result = urlparse(url)
print(result.netloc)

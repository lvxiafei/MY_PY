import re


num = re.findall(r'\d+', 'hello 42 I\'m a 32 string 30')
print(num[0])
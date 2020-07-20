'''



'''
a = '1234'
b = '1234.1'
c = '1'
if a.isdigit():
    print('digit a:',a)
if a.isnumeric():
    print('numeric a:',a)

if b.isdigit():
    print('digit b:',b)
if b.isnumeric():
    print('numeric b:',b)
print(c.isnumeric())  # 只由数字组成

import sys
print(sys.path)
'''
给定一组数，调整顺序使其最大
2
10,2
o:210

4
1,10,100,101
o:1,101,10,100
比较规则：
    先比较首位，首位大的放前
    首位相同时比较第二位，没有第二位时用0比较，第二位大的放前
    直至末位

'''

import sys
# 读取第一行的n
n = int(sys.stdin.readline().strip())
# 读取每一行
line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
values = list(map(int, line.split(',')))

if not values:  print('')
if sum(values) == 0:print('0')
for i in range(len(values)):
    for j in range(len(values) - i - 1):
        if str(values[j]) + str(values[j+1]) > str(values[j+1])+ str(values[j]):
            values[j],values[j+1] = values[j+1],values[j]
ans =''
for i in values:
    ans = str(i)+ans
print(ans)











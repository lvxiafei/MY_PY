

with open('/Users/Merlin/Git/develop-interview/计算机网络.md', 'r') as f:
    # print(f.readlines())
    strage = []
    s = list(f.readlines())
    for i in range(len(s)):
        if s[i][0].isdigit():
            # print(s[i])
            strage.append(s[i][0:-1])
    print(strage)
    print(strage[-1])

import re

num = re.findall(r'\d+', strage[-1])
a = int(num[0])

b = 4
import random

# print("请输入题数 抽屉数:")
# a, b = map(int, input().split())
print(a,b)
ls = list(range(a))
ls2 = []
# 从x个数字中随机抽取10个数字
for i in range(b):
    rd = random.choice(ls)
    ls2.append(rd)
    # ls.remove(rd)
# 如果有重复，重新执行一次，直到没有重复为止
if len(set(ls2)) == len(ls2):
    # random_list()
    pass

# 检验结果
# print(ls)
ls2.sort()
print(ls2)

for i in ls2:
    print(strage[i])
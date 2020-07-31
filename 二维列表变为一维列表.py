

c = [[1,2,3], [4,5,6], [7,8,9]]

# 1.用列表推导式
a1 = [n for a in c for n in a ]
print(a1)

# 2.用嵌套循环展开
result=[]
for a in c:
    for n in a:
        result.append(n)
print(result)

print("用sum对列表的求和:")
# 3.用sum对列表的求和
ret = sum(c,[])
print(ret)
print(sum(c,[0]))
print(sum(c,[1]))
print(sum(c,[0,1]))

# sum 展开
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(sum(a,1)) # 此处加 [] 出错
print([]+a+b+c)
print([0]+a+b+c)
print([1]+a+b+c)
print([0,1]+a+b+c)

# 相关的模块

c = [[1,2,3], [4,5,6], [7,8,9]]
print("相关的模块：")
import operator
from functools import reduce

print(reduce(operator.add, c))



print("chain模块：")

from itertools import chain

c = [[1,2,3], [4,5,6], [7,8,9]]
# print(chain(*c))
ret3 = list(chain(*c))
# print(type(ret3))
print(ret3)
# [1,2, 3, 4, 5, 6, 7, 8, 9]



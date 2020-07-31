'''


'''
import random


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


print(random_int_list(0, 100, 10))  # 可能会两数重复

# 生成随机数
ret = random.randint(0, 10)
print(ret)

ret2 = random.random()  # [0,1)范围内的随机浮点数
print(ret2)


'''
从一个列表中随机抽取几个元素输出并在原列表删除，并保存该元素和列表（可保存入文件）
'''
print("-" * 100)
import random


ls = list(range(100))
ls10 = []
# 从x个数字中随机抽取10个数字
for i in range(10):
    rd = random.choice(ls)  # 可能会两数重复
    ls10.append(rd)
    ls.remove(rd)

# 检验结果
print(ls)
print(ls10)

# shuffle截取     保证不会重复
from random import shuffle

sf = list(range(100))
shuffle(sf)
print(sf[:10])

# shuffle 方法封装成函数
def shuffele_func(start, stop, length):
    sf = list(range(start,stop))
    shuffle(sf)
    return sorted(sf[:length])

ret3 = shuffele_func(0,100,10)
print(ret3)

print("shuffle 方法封装成函数  并实现第二次升成的数据不与第一次重复:")
# shuffle 方法封装成函数  并实现第二次升成的数据不与第一次重复
def shuffele_func2(start, stop, length, ignore_list):
    sf = list(range(start,stop))
    # for i in ignore_list:
    #     sf.remove(i)
    [sf.remove(i) for i in ignore_list]  # 列表生成式的写法
    print(sf)
    shuffle(sf)
    return sorted(sf[:length])
ignore_list = [4, 22, 27, 31, 32, 38, 49, 64, 78, 86]
ret4 = shuffele_func2(0,100,10,ignore_list)
print(ret4)

'''
扩展：
    闭包、装饰器实现 保存前几次调用的结果，实现去重
    数据库持久化存储，实现去重
'''
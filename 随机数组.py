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

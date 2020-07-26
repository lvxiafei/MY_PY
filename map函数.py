def add(x, y):
    return x + y
a = (2,3,4)
b = [10,5,3]

ret = list(map(add, a, b))  # 两个参数
print(ret)

# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 使用Step-wise线性搜索。

# def get_value(l, r, c):
#     return l[r][c]

def find(l, x):
    m = len(l) - 1  # 行
    n = len(l[0]) - 1   # 列
    r = 0  # 行
    c = n  # 列
    while c >= 0 and r <= m:
        # value = get_value(l, r, c)
        value = l[r][c]
        # print(value)
        if value == x:
            return True
        elif value > x: # 9>7
            c = c - 1 # 左移
        elif value < x:
            r = r + 1 # 下移
    return False

l = \
[
    [1,5,9],
    [2,6,10],
    [3,7,11]  # 从左下角开始，大右小下；从右上角开始，大下小左

]

print(find(l,7))
print(find(l,8))

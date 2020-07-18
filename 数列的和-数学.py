'''
输入
81 4
2 2
输出
94.73
3.41
'''
from math import sqrt
while True:
    try:
        n, m = map(int, input().split())
        t = 0
        for i in range(m):
            t += n
            n = sqrt(n)
        print('%.2f' % t)  # 格式化符号输出数据
    except:
        break
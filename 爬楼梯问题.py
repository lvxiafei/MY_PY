'''
一次只能上1个或2个
思路：
如果只有一级台阶，则一种解法
如果两级，则两种
f(n) = f(n-1)+f(n-2)

一次只能上1，2，3个
一级：1种
两级：2种
三级：4种
f(n) = f(n-1) + f(n-2) + f(n-3)
'''
import sys

n = int(sys.stdin.readline().strip())


def helper(n):
    if n == 1: return 1  # 多个出口条件
    if n == 2: return 2
    return helper(n - 1) + helper(n - 2)  # 推导式


print(helper(n))

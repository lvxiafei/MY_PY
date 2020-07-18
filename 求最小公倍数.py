'''
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。
输入5 7
输出 35


最小公倍数 = 两数之积除以最大公约数
'''

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)
while True:
    try:
        a,b=map(int,input().split())
        print(lcm(a,b))
    except:
        break

# 台阶问题/斐波那契
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
print(fib(3))

def fib2(n):
    if n <= 2:return n
    else:
        return fib2(n-1) + fib(n-2)

print(fib2(3))




# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

fib6 = lambda n: n if n < 2 else 2 * fib6(n - 1)

print(fib6(3))

def fib7(n):
    if n <= 2: return n
    else:
        # return fib7(n-1) + fib(n-2)+ ...+ fib(2)
        return 2 * fib7(n-1)


print(fib7(3))
'''
3

'''
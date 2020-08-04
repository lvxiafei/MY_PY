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
        # return fib(n-1) + fib(n-2)+ ...+ fib(2)+fib(1)+1
        return 2 * fib7(n-1)


print(fib7(3))

'''
3
原理是什么：
fib(n) = fib(n-1) + fib(n-2)+ ...+ fib(2)+fib(1)+1
fib(n-1) = fib(n-2)+ ...+ fib(2)+fib(1)+1
=》
fib(n) = 2 * fib(n-1)

    

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上 n-3 级（n>3）。求该青蛙跳上一个n级的台阶总共有多少种跳法。
fib(n) = fib(n-1) + fib(n-2)+ ...+ fib(3)
fib(n-1) = fib(n-2)+ ...+ fib(3)
=》
fib(n) = 2 * fib(n-1)
递归出口条件不同：n<=3:


一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上 n/2 级


'''
# 栈实现 模拟递归
print("栈实现普通跳台阶:")
def fib9(n):
    stack = [1,2]
    if n  <= 2 : return n
    temp = n - 2
    while(temp):
        stack.append(stack[-1]+stack[-2])
        temp -= 1
    return stack[-1]
print(fib9(3))

print("栈实现变态跳台阶:")
def fib10(n):
    stack = [1,2]
    if n  <= 2 : return n
    temp = n - 2
    while(temp):
        stack.append(sum(stack)+1)
        temp -= 1
    return stack[-1]
print(fib10(3))

print(fib10(6) == fib7(6))
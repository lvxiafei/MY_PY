# 递归：计算阶乘
'''
递归的基本思想：

step1：（n - 1）假设，需要假设较小的规模已经完成 factorial(n - 1)
step2：利用y已知和假设计算未知 factorial(n) = n * factorial(n - 1)
step3：确定结束条件 n == 0

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

'''
动态规划：

'''
def factorial2(n):
    array = [1]  # array[i]表示i的阶乘
    for i in range(2, n + 1):
        array.append(i * array[-1])  # 状态转移方程 dp[i] = i * dp[i - 1]
    return array[-1]

if __name__ == "__main__":
    print(factorial(3))
    print(factorial2(3))



'''
改写： 
    递归过程化： = 栈（模拟执行顺序）+字典（存储执行结果，哪一步：那个值）


'''

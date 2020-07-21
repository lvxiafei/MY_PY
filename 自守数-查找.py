'''
自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，
9376^2 = 87909376。请求出n以内的自守数的个数
输入描述: 2000
int型整数

输出描述: 8
n以内自守数的数量。
'''
while True:
    try:
        n = int(input())
        cnt = 0
        for i in range(n + 1):  # [0,n+1) == [0,n]
            l = len(str(i))
            if str(i ** 2)[-l:] == str(i):
                cnt += 1
        print(cnt)
    except:
        break

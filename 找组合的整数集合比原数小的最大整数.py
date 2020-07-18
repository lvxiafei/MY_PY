'''
输入一个整数n,把这个数的每一位的数拆开（个十百千位的数），组合为另一个数，另外组合的数算作集合m，
找出比n小，m中最大的整数输出

输入描述：十进制整数n，长度小于100位

输出描述：如果不存在，输出 Not found

153 -> 135

1536 - 1365
1534 - 1453

思路：
前面n-2位不变，后面2位是否顺序排列，若不是，逆序拼接输出
前面n-3位不变，后面3位是否顺序排序，若不是，小于倒数第三位的最大元素作为该位，剩下元素降序拼接
...


'''

if __name__ == "__main__":

    # str = input()
    str = "153" #135
    # str = "1536" #1365 不通过
    # str = "15344423"
    n = []
    for i in str:
        n.append(int(i))
    if n == sorted(n): print("Not found")
    # print(max(n))
    # print(len(str))
    for j in range(2, len(str)):
        if n[-j:] != sorted(n[-j:]):
            # print(n[-j:]) # 536
            t = n[-j:]
            tem = []
            for i in n[-j:]:
                if i < n[-j]:
                    tem.append(i)
            # print(tem[-1]) #3
            t.remove(tem[-1])
            t = sorted(t)
            ret = tem[-1:] + t[::-1]
            # print(ret) # 365

            temp = n[:-j] + ret
            # print(temp)
            l = len(temp)
            ans = 0
            # print(type(l))
            for k,t in enumerate(temp):
                # print(k,t)
                ans += t * 10**(l-1-k)
                # print(ans)
            print(ans)
            break

    # print(sorted(n))
    # print(type(n))
    # print(n)

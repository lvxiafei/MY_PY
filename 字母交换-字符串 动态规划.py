'''
字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。
询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？
输入 abcbaa 2
输出 2
'''

s, m = input().split()
m = int(m)
s = list(s)

arr = {}
for i in range(0, len(s)):
    if s[i] not in arr:
        arr[s[i]] = []
    arr[s[i]].append(i)

Max = 0
for i in arr:
    if len(arr[i]) > Max:
        for j in range(Max, len(arr[i])):
            Sum = 0
            for k in range(0, j + 1):
                Sum += abs(arr[i][(j // 2)] - arr[i][k]) - abs((0 + j // 2) - k)
            if Sum <= m:
                Max = max(Max, j + 1)
print(Max)
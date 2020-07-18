'''
5
5 4 3 2 1
5
1 2 3 4 5
o:
-1 5 4 3 2

'''

import sys


def helper(n, values):
    ans = [-1]
    for i in range(1, n):
        for j in range(i)[::-1]:
            if values[i] < values[j]:
                ans.append(values[j])
                break
            else:
                ans.append(-1)
                break

    # print(ans)
    ret = map(str,ans)
    print(' '.join(ret))
# 多组输入  加计数变量，偶数调用递归函数
# 读取第一行的n
n_all = []
values_all = []

while True:
    tmp = sys.stdin.readline().strip()
    # if len(tmp) == 0: ## 两个回车输出
    if not tmp:
        # print("dd")
        for i in range(len(n_all)):
            helper(n_all[i],values_all[i])
    else:
        n = int(tmp)
    # n = int(sys.stdin.readline().strip())
        n_all.append(n)
    # print(n_all)
    # 读取每一行
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split())) # 列表形式
    values_all.append(values)
    # print(values_all)


# help(n_all[0],values_all[0])
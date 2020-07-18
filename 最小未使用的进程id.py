'''
假定操作系统采用32位正整数作为进程id，当创建新进程时，需要找到"最小未使用的进程id"，试实现这个算法
第一行输入n,范围不超过2^20
接下来的n行代表已存在的进程id，正整数< 2^31，不保证排序
5
1
2
3
4
6
=> 5
5
2
5
7
96060
1000
=>1

'''

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = []
    ans = 1
    for i in range(n):
        # 读取每一行
        line.append(int(sys.stdin.readline().strip()))
    # print(line)
    for l in line:
        if l == ans:
            ans += 1
        else:
            print(ans)
            break













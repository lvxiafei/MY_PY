'''
3
1 2 3
3 2 1
1 3 2
=> 18

'''

import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
'''
输入一个字符串，首尾相接组成一个圆环，能否从某点切断产生一个回文
通过输出 Yes 否则 No
S = aab
=> Yes
aab从'a','a'间切开，回文aba

aab:  aab aba baa
分析：
step1: 数组

'''
import sys

if __name__ == "__main__":
    values = sys.stdin.readline().strip()
    ret = "No"
    for i in range(len(values)):
        # print(values[i:]+values[:i])
        value = values[i:] + values[:i]
        if value == value[::-1]:
            # print(ret)
            ret = "Yes"
            break
    print(ret)



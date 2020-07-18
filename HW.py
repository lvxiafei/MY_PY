'''
字符串中的数字升序排列

思路：
    判断字符是否为数字： i.isdigit() 列表存储
    升序排序
    列表转化为字符串输出
口诀：找到数字，列表存储，升序排列，字符串输出

'''
# str = input()
str='3d50J,Aa3'
s=[]
for i in str:
    if i.isdigit():
        s.append(i)
# s1=sorted(s)
s.sort()
# print(s)
# str(s)
print(s)
s1 = ''.join(s)
print(s1)

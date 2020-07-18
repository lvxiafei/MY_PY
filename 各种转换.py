

# 字符串转列表
# str = input()
str='3d50J,Aa3'
s=[]
for i in str:
        s.append(i)
print(type(s))
print(s)

#字符串转列表-一般情况
str1 = "hi hello world"
print(str1.split(" "))
print(list(str1))


# # 列表转字符串
# s1 = ''.join(s)
# print(type(s1))
# print(s1)
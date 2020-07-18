# 536 - 365

'''

小于某数的最大数

删除该元素

'''
n = [5, 3, 6]
tem =[]
for i in n:
    if i < n[0]:
        tem.append(i)
print(tem[-1])

n.remove(tem[-1])
print(n)

ret = tem[-1:] + n[::-1]
print(ret)

# 小于5 的最大数 4
# 遍历找到所有  排序  [-1]

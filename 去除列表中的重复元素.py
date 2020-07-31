
# 用集合
# l = [1,2,3,4,5,5]
l = ['b','c','d','b','c','a','a']
print(list(set(l)))

# 用字典
l1 = ['b','c','d','b','c','a','a']
l2 = {}.fromkeys(l1).keys()
print(l2)

# 用字典并保持顺序
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)

# 列表推导式
l1 = ['b','c','d','b','c','a','a']
l2 = []
[l2.append(i) for i in l1 if not i in l2]
print(l2)

# sorted排序并且用列表推导式.
l = ['b','c','d','b','c','a','a']
single = []
[single.append(i) for i in sorted(l) if i not in single]
print(single)
'''

sum()函数语法是这样的
sum(iterable[, start]) # 注，start在起始位置相加

iterable – 可迭代对象，如：列表(list)、元组(tuple)、集合(set)、字典(dictionary)。

start – 指定相加的参数，如果没有设置这个值，默认为0。
也就是说sum()最后求得的值 = 可迭代对象里面的数加起来的总和(字典:key值相加) +
start的值(如果没写start的值，则默认为0)

'''
sum1 = sum([1,2],5)
print(sum1)

# 3.用sum对列表的求和
c = [[1,2,3], [4,5,6], [7,8,9]]

ret = sum(c,[])
print(ret)
print(sum(c,[0]))
print(sum(c,[1]))
print(sum(c,[0,1]))

# sum 展开
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(sum(a,1)) # 此处加 [] 出错
print([]+a+b+c)
print([0]+a+b+c)
print([1]+a+b+c)
print([0,1]+a+b+c)

# 相加不一定是数值相加，列表亦可相加，默认start为int型0
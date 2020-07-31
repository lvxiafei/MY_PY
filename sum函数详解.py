'''

sum()函数语法是这样的
sum(iterable[, start])

iterable – 可迭代对象，如：列表(list)、元组(tuple)、集合(set)、字典(dictionary)。

start – 指定相加的参数，如果没有设置这个值，默认为0。
也就是说sum()最后求得的值 = 可迭代对象里面的数加起来的总和(字典:key值相加) +
start的值(如果没写start的值，则默认为0)

'''
sum = sum([1,2],5)
print(sum)
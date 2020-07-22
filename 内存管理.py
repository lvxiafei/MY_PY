'''
Python中一切皆对象，python的存储问题是对象的存储问题，并且对于每个对象，python会分配一块内存空间去存储它
Python的内存管理机制：引用计数、垃圾回收、内存池机制
引用计数机制：在Python中，每个对象都有指向该对象的引用总数---引用计数，查看对象的引用计数：sys.getrefcount()
垃圾回收：引用计数降为0时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾
内存池机制：
	大内存使用malloc进行分配
	小内存使用内存池进行分配 即Pymalloc机制，用于管理对小块内存的申请和释放

'''
#   变量：通过变量指针引用对象
var1 = object
var2 = var1
print(id(var1) == id(var2))    # 139697863383968    True

a = 123
b = a
print(id(a) == id(b))   # True
a = 456
print(id(a) == id(b))   # False

#   通过is进行引用所指判断，is是用来判断两个引用所指的对象是否相同。
#整数
a = 1
b = 1
print(a is b)  #  True

#短字符串
c = "good"
d = "good"
print(c is d)  # True

#长字符串
e = "very good"
f = "very good"
print(e is f)  # True

#列表   Python没有缓存列表，可以有多个相同的对象，可以使用赋值语句创建出新的对象
g = []
h = []
print(id(g), id(h))
print(g is h)   # False

# 引用计数
# 在Python中，每个对象都有指向该对象的引用总数---引用计数
# 查看对象的引用计数：sys.getrefcount()
print("引用计数")
import sys

a = [1, 2, 3, 4]
print(sys.getrefcount(a))   # 2

b = a
print(sys.getrefcount(a))   # 3
print(sys.getrefcount(a))   # 3
print(sys.getrefcount(b))   # 3

# 注意：  当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用
#        因此，getrefcount()所得到的结果，会比期望的多1，只创建一次

# 引用计数增加
print("引用计数增加")
#   对象被创建
print(sys.getrefcount(1234)) # 3
n = 1234
print(sys.getrefcount(1234)) # + 1 => 4
#   另外的别人被创建
m = n
print(sys.getrefcount(1234))  # + 1 => 5
#   作为容器对象的一个元素
a=[1,12,1234]
print(sys.getrefcount(1234))  # + 1 => 6
# 作为参数传递给函数：foo(x)

# 引用计数减少
print("引用计数减少")
#   对象的别名被显式的销毁
#
del m
print(sys.getrefcount(1234))
#   对象的一个别名被赋值给其他对象
n = 456
print(sys.getrefcount(1234))
#   对象从一个窗口对象中移除，或，窗口对象本身被销毁
a.remove(1234)
# print(a)
print(sys.getrefcount(1234))

# import os
# print(os.path)
'''
垃圾回收：
​当Python中的对象越来越多，占据越来越大的内存，启动垃圾回收(garbage collection)，将没用的对象清除。
原理：
当Python的某个对象的引用计数降为0时，说明没有任何引用指向该对象，该对象就成为要被回收的垃圾。
比如某个新建对象，被分配给某个引用，对象的引用计数变为1。如果引用被删除，对象的引用计数为0，
那么该对象就可以被垃圾回收。
del 后，已经没有任何引用指向之前建立的[321,123]，该表引用计数变为0，用户不可能通过任何方式接触或者
动用这个对象，当垃圾回收启动时，Python扫描到这个引用计数为0的对象，就将它所占据的内存清空

(1)、垃圾回收时，Python不能进行其它的任务，频繁的垃圾回收将大大降低Python的工作效率；
(2)、Python只会在特定条件下，自动启动垃圾回收（垃圾对象少就没必要回收）
(3)、当Python运行时，会记录其中分配对象(object allocation)和取消分配对象
    (object deallocation)的次数。当两者的差值高于某个阈值时，垃圾回收才会启动。
'''
print("垃圾回收")

laji = [321,123]
print(sys.getrefcount(laji))
del laji
# print(sys.getrefcount(laji))

import gc
print(gc.get_threshold())   # gc模块中查看阈值的方法
'''
Out:(700, 10, 10)
阈值分析：
    700即是垃圾回收启动的阈值；
    每10次0代垃圾回收，会配合1次1代的垃圾回收；而每10次1代的垃圾回收，才会有1次的2代垃圾回收；
    当然也是可以手动启动垃圾回收：

何为分代回收:
　　Python将所有的对象分为0，1，2三代；
　　所有的新建对象都是0代对象；
　　当某一代对象经历过垃圾回收，依然存活，就被归入下一代对象
'''

print("内存池机制")
'''
Python中有分为大内存和小内存：（256K为界限分大小内存）
​ 1、大内存使用malloc进行分配
​ 2、小内存使用内存池进行分配    
    引用了一个内存池机制，即Pymalloc机制，用于管理对小块内存的申请和释放
'''
# lambda表达式，为了解决简单函数的情况，如：
def func0(a1,a2):
    return a1 + a2

func = lambda a1,a2:a1+a2
# 上面这两个是一样的
print(func0(1,2))
print(func(1,2))

func1 = lambda :100
# 表示函数没参数，只返回一个100
print(func1())

func2 = lambda x1:x1 + 100# 表示函数传递一个参数,返回x1+100
print(func2(100))

func3 = lambda *args,**kwargs:len(args)+len(kwargs)# 可以传递万能参数print(func3(1,2,3,wdc=123))
print(func3(1,2,3, wdc=123))
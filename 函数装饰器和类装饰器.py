#  https://www.cnblogs.com/hiyang/p/12634734.html

# 简单装饰器
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
    print('hello world')

greet = my_decorator(greet)
greet()

# 输出
# wrapper of decorator
# hello world


# 更优雅的表示
print("更优雅的表示")
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

@my_decorator   #  等于 greet = my_decorator(greet)
def greet():  # greet作为my_decorator的参数
    print('hello world')

greet()

# 输出
# wrapper of decorator
# hello world

# 带参数的装饰器

print("带参数的装饰器")
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(message):
    print(message)

greet('hello world')

# 输出
# wrapper of decorator
# hello world

print("自定义参数的装饰器")
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator {}'.format(i))
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)

greet('hello world')

# 输出：
# wrapper of decorator 0
# hello world
# wrapper of decorator 1
# hello world
# wrapper of decorator 2
# hello world
# wrapper of decorator 3
# hello world

print("原函数还是原函数吗？")

print(greet.__name__)
## 输出
'wrapper'

help(greet)
# 输出
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)
'''
greet() 函数被装饰以后，它的元信息变了。元信息告诉我们“它不再是以前的那个 greet() 函数，
而是被 wrapper() 函数取代了”。
为了解决这个问题，通常使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息
（也就是将原函数的元信息，拷贝到对应的装饰器函数里）。
'''
print("使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息")
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)
greet("hello")

print(greet.__name__)
help(greet)
# 输出    'greet'


#  类装饰器
print("类装饰器")
'''
实际上，类也可以作为装饰器。类装饰器主要依赖于函数__call__()，每当你调用一个类的示例时，
函数__call__()就会被执行一次

我们定义了类 Count，初始化时传入原函数 func()，而__call__()函数表示让变量 num_calls 
自增 1，然后打印，并且调用原函数。因此，在我们第一次调用函数 example()时，num_calls 的
值是 1，而在第二次调用时，它的值变成了 2
'''

class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello world")

example()
example()

# # 输出
# num of calls is: 1
# hello world
#
# example()
#
# # 输出
# num of calls is: 2
# hello world
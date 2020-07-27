# 1. 使用模块实现：Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
# 当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函
# 数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做

from 单例的多种实现方法_模块文件 import Singleton

s1 = Singleton('IT圈')
print(s1)
print(s1.name)
s2 = Singleton('程序IT圈')
print(s2)
print(s2.name)
print(s1 == s2) # True

'''
2. 用__new__特殊方法实现class Singleton:
'''
print("2. 用__new__特殊方法实现class Singleton:")
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    def __init__(self, name):
        self.name = name
s1 = Singleton('IT圈')
s2= Singleton('程序IT圈')
print(s1 == s2) # True

print("3. 使用装饰器实现")
def singleton(cls):
    _instance = {}
    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return inner
@singleton
class Singleton:
    def __init__(self, name):
        self.name = name
s1 = Singleton('IT圈')
s2= Singleton('程序IT圈')
print(s1 == s2) # True

print("4. 类装饰器实现")
class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args)
        return self._instance[self._cls]
@Singleton
class Singleton:
    def __init__(self, name):
        self.name = name
s1 = Singleton('IT圈')
s2= Singleton('程序IT圈')
print(s1 == s2) # True


print("5. 使用元类实现方式")

class Singleton1(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton1, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton1, self).__call__(*args, **kwargs)
        return self.__instance

class Singleton(metaclass=Singleton1):
    def __init__(self, name):
        self.name = name
s1 = Singleton('IT圈')
s2= Singleton('程序IT圈')
print(s1 == s2) # True

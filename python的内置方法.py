# https://blog.csdn.net/WSRY_GJP/article/details/100629916?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~baidu_landing_v2~default-1-100629916.nonecase

class Foo(object):
    pass
obj = Foo()
ret = isinstance(obj, Foo)  # 检查obj是否是类 cls 的对象
print(ret)

class Foo(object):
    pass
class Bar(Foo):
    pass
ret = issubclass(Bar, Foo)  # 检查sub类是否是 super 类的派生类
print(ret)

print("item系列： ")

class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __getitem__(self, item):
        print('触发__getitem__')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print('触发__setitem__')
        self.__dict__['key']=value

    def __delitem__(self, key):
        print('触发__delitem__')
        del self.__dict__[key]

obj=Foo('大鹏',23)

# ##注意以字典的形式调用才会触发，obj.name并不会触发
print(obj.name)
obj['name']
# # 大鹏
# # 触发__getitem__

obj['sex']='male'
# # 触发__setitem__


del obj['name']
# 触发__delitem__


print("_str_ 改变对象的字符串显示：")
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        print('触发__str__')
        return '<name>:%s\n<age>:%s' %(self.name,self.age)


stu=Foo('dapeng',18)
print(str(stu))
print(stu)

# 触发__str__
# <name>:dapeng
# <age>:18
# 触发__str__
# <name>:dapeng
# <age>:18

print("__del__()：")
'''
析构方法，当对象在内存中被释放时，自动触发执行
'''
class Foo:

    def __del__(self):
        print('执行我啦')

f1=Foo()
del f1
print('------->')

#输出结果
# 执行我啦
# ------->


'''
enter、exit
这两个方法的重写可以让我们对一个对象使用with方法来处理工作前的准备，以及工作之后的清扫行为。
'''


class MySQL:
    def connect(self):
        print('启动数据库连接，申请系统资源')

    def execute(self):
        print('执行sql命令，操作数据')

    def finish(self):
        print('数据库连接关闭，清理系统资源')

    def __enter__(self):  # with的时候触发，并赋给as变量
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # 离开with语句块时触发
        self.finish()


with MySQL() as mysql:
    mysql.execute()

# 结果:
# 启动数据库连接，申请系统资源
# 执行sql命令，操作数据
# 数据库连接关闭，清理系统资源
class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print('hello', name)
    def foo2(self, name):
        print('hello', name)
    @classmethod
    def foo3(cls, name):
        print('hello', name)

a = A()
a.foo1('mamq') # 输出: hello mamq
A.foo1('mamq')# 输出: hello mamq
a.foo2('mamq')
# A.foo2('mamq') #报错: unbound method foo2()
a.foo3('mamq')
A.foo3('mamq')
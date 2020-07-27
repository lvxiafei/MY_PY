class A:

    country = "中国"
    area = "深圳"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print(666)

a = A("Jane", 18)
# 对象的属性
print(a.name)                       # Jane

# 注意这个变量名也要用字符串形式！
print(hasattr(a, "name"))           # True

# 不是这样用，而是字符串形式的属性名
print(hasattr(a, "Jane"))           # False

# 一般 hasattr 与 getattr 结合起来使用
if hasattr(a, "name"):
    print(getattr(a, "name"))       # Jane

# 可以设置一个默认值，目的是防止程序报错
# 如果没有该属性，就返回默认值
print(getattr(a, "sex", None))      # None

print(a.country)                    # 中国
print(getattr(a, "country"))        # 中国

ret = getattr(a, "func")
# 注意这里　ret() 相当于 func()
print(ret())                        # 666

# 给对象添加一个属性
setattr(a, "sex", "男")
print(a.sex)                        # 男

# 删除对象的某个属性
# delattr(a, "name")
# print(a.name)
aaa = print("eexxeecc")
code= "aaa"
exec(code)
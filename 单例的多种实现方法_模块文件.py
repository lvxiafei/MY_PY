#单例的多种实现方法_模块文件.py
__all__ = ['Singleton']
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    print(Singleton('IT圈'))
    print(Singleton('IT圈').name)

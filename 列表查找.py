'''
输入:列表或者待查找元素
输出:元素下标或者未查到的元素
顺序查找
从元素的第一个开始,按顺序进行查找,直到找到为止

二分查找
从有序列表的候选区data[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半。

理论上顺序查找的时间复杂度为O(n),二分查找的为O(logn)
循环减半的过程,O(logn)

'''
import time


# 定义一个计算运行时间的装饰器
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('%s:%s' % (func.__name__, t2 - t1))
        return res

    return wrapper


# 顺序查找
@cal_time
def linear_search(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i


# 二分查找
@cal_time
def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            return mid
        elif data_set[mid] < value:
            low = mid + 1
        else:
            high = mid - 1


ret = linear_search(list(range(100000)), 99999)

ret2 = bin_search(list(range(100000)), 99999)
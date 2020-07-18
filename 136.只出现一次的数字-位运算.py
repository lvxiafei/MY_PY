'''
某个元素只出现一次，其余元素均出现两次，找到那个只出现一次的元素
[4,1,2,1,2]
o:4

分析：
统计出现次数 Counter()函数
    data = Counter(nums)
    for d in data:
    if data[d] == 1 :
        return d
数据存储形式，01编码 -> 位运算：相同为0，不同为1，满足交换律  0 ^ 非0 == 非0

数学方式： 去重求和*2 - 未去重求和


'''

def singleNumber(nums):
    return sum(set(nums))*2 - sum(nums)

def singleNumber2(nums):
    a = 0
    for i in nums:
        a = a ^ i
    return a
def singleNumber3(nums):
    from collections import Counter
    data = Counter(nums)
    for d in data:
        if data[d] == 1:
            return d

print(singleNumber3([4,1,2,1,2]))
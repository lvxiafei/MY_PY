'''
给定一个包含n+1个整数的数组nums，其数字都在1到n之间（包括1，n），可知至少存在一个重复数，找到
[1,3,4,2,2]
o:2

思路:
    重复数 = 数组求和 - 数组去重求和

'''
def findDuplicate(nums):

    ans = sum(nums)-sum(set(nums))

    return ans
    # pass

'''
思路2：
    记录出现次数
    如果重复，返回


'''
def findDuplicate2(nums):
    from collections import Counter
    dic = Counter(nums)
    print(dic)
    # for k in dic:
    #     if dic[k] != 1:
    #         return k
    # print(dic.items())
    for k, v in dic.items():
        if v > 1:
            return k


'''
思路3： 二分查找 
数组长度为n+1,则数组中元素属于[1,n],且只有一个重复元素。设一个数组k属于[1,n],统计数组中小于等
于k的数字个数count
若 count <= k,则重复数字一定在[k+1,]范围内
否则一定在[,k]范围内



'''
def findDuplicate3(nums):
    l = 1
    r = len(nums) -1
    while(l < r): # 执行log(n)次遍历n
        mid = (l + r)//2
        count = 0
        for num in nums:
            if (num <= mid):
                count += 1
        if (count <= mid):
            l = mid +1
        else:
            r = mid
    # print(l,r) # 找到后l == r
    return l


    # pass

print(findDuplicate3([1,3,4,2,2]))
'''
在一个长度为n的数组nums里的所有数字都在 0-n-1范围内。数组中某些数字是重复的，但不知道有几个数组重复了
，也不知道重复了几次，找出任意一个重复的数字

[2,3,1,0,2,5,3]
o:2 或 3


'''


def findRepateNUmber(nums):
    for i in nums:
        if i in nums[i:]:
            return i
    #     return i if i in nums[i:] else None


def findRepateNUmber2(nums):
    d = dict([(k, 0) for k in nums])  # 初始化(key,value)对
    # print(d)
    for i in range(len(nums)):
        if d[nums[i]] > 0:
            return nums[i]
        else:
            d[nums[i]] += 1
def findRepateNUmber3(nums):
    d ={}
    for i in nums:
        d[i] = nums.count(i)
        return i if d[i] > 1 else None

def findRepateNUmber4(nums):
    for i in nums:
        if nums.count(i) > 1:
            return i
        # print(nums.count(i))

print(findRepateNUmber4([2, 3, 1, 0, 2, 5, 3]))

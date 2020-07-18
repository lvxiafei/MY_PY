'''
给定一个数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回数组下标

nums = [2, 7, 11, 15], target = 9
返回 [0, 1]

9-7 in 2
9-11 in 2,7
9-15 in 2,7,11

基本思想：
step1：转化 target - num in nums(except num)
step2：遍历 nums的顺序元素num;
           nums(except) 为num之前的数组 d.append(num)
step3：返回 数组下标 [num下标, target - num下标]
'''
def twoSum(self, nums, target):
    d = []
    for num in nums:
        if target - num in d:
            return [nums.index(target - num), nums.index(num)]
        d.append(num)

def twoSum2(self, nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:  # 遍历键
            return [d[target - num], i]
        d[num] = i

if __name__ == '__main__':
    print(twoSum(0, [2, 7, 11, 15], 9))
    print(twoSum2(0, [2, 7, 11, 15], 9))

'''
给定一个整数数组nums，找到一个具有最大和的连续子数组（至少包含一个元素），返回最大和
[-2,1,-3,4,-1,2,1,-5,4]
o:6
[4,-1,2,1] - 》6



思路：
生成不同子序
存储当前子序 和
比较 更新


'''

def maxSubArray(nums):

    # pass
    max = float("-inf")
    for left in range(len(nums)):
        # print(nums[left:])
        # print(len(nums[left:]))
        for right in range(left, len(nums)):
            # print(left, right)
            if sum(nums[left:right]) > max:
                max = sum(nums[left:right])
    return max


'''
分治：
最大子序和要么在左半边，要么在右半边，要么在中间，中间部分直接计算出俩

'''

def maxSubArray2(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        max_left = maxSubArray2(nums[0:len(nums)//2])
        max_right = maxSubArray2(nums[len(nums)//2:len(nums)])
    # 计算中间
    max_mid_left = nums[len(nums)//2 - 1]
    for i in range(len(nums)//2-1, -1, -1):
        max_mid_left = max(sum(nums[i:len(nums)//2 - 1]), max_mid_left)

    max_mid = max_mid_left
    for j in range(len(nums)//2, len(nums)):
        max_mid = max((sum(nums[len(nums)//2:j]) + max_mid_left), max_mid)



    return max(max_left,max_right,max_mid)

print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))

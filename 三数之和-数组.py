'''
给定一个包含n个整数的的数组nums，判断nums中是否存在三个元素a,b,c,使得a+b+c=0?
找出所有满足条件且不重复的三元组

nums = [-1,0,1,2,-1,-4]
o:
[
[-1,0,1],
[-1,-1,2]
]

思路：
0-a-b==c 当a,b确定后判断  c是否存在于剩下元素

'''

def threeSum(nums):
    res = []
    for a in nums:
        nums2 = nums
        nums2.remove(a)
        for b in nums2:
            nums3 = nums2
            nums3.remove(b)
            if 0 - a - b in nums3:  # 自动去重
                res.append([a, b, 0-a-b])
    return res

# 指针
def threeSum2(nums):
    n = len(nums)
    if (not nums or n < 3): return []  # 异常条件
    nums.sort()  # 排序，方便去重
    res = []
    for i in range(n-2): #
        if(nums[i]>0): return res  # 最小的不能大于0
        if(i>0 and nums[i] == nums[i - 1]): continue  # 第一个元素去重
        L = i + 1
        R = n - 1
        while(L < R):
            if(nums[i] + nums[L] + nums[R] == 0):
                res.append([nums[i], nums[L], nums[R]])

                while (L < R and nums[L] == nums[L+1]):L = L + 1  #第二个元素去重
                while (L < R and nums[R] == nums[R-1]):R = R - 1  #第三个元素去重
                # 指针移动,找满足条件
                L = L + 1
                R = R - 1
            # 指针移动，调整
            elif(nums[i] + nums[L] + nums[R] > 0): R = R - 1
            else: L = L + 1
    return res

print(threeSum2([-1, 0, 1, 2, -1, -4]))

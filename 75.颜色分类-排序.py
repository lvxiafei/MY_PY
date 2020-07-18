'''
给定一个包含红色、白色和蓝色，一共n个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红
白蓝顺序排列
使用0、1、2分别代表红白蓝
[2,0,2,1,1,0]
o:[0,0,1,1,2,2]

思路1：排序函数

思路2：
三指针 交换数据  指针可以在不需要额外空间的情况下进行操作
当w<=b:
    if nums[w] == 0: 交换 nums[w] ,nums[r] r+=1 w+=1
    elif nums[2] == 1: w += 1
    else:交换mums[w],nums[b] b -= 1

'''


def sortColors(nums):
    # return sorted(nums)
    r, w, b = 0, 0, len(nums) - 1
    while w < b:
        if nums[w] == 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
            r += 1
        elif nums[w] == 1:
            w += 1
        else:
            nums[w], nums[b] = nums[b], nums[w]
            b -= 1
    return nums


print(sortColors([2, 0, 2, 1, 1, 0]))

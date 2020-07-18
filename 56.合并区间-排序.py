'''

 给出一个区间的集合，请合并所有重叠的区间
 [[1,3],[2,6],[8,10],[15,18]]
 O:[[1,6],[8,10],[15,18]]
思路：
左边界排序sort()
遍历 合并
伪代码：
    遍历：
        if 右边界 < 下一个左边界：append
        else:
            右边界 = max(右边界，下一个右边界)
'''

def merge(intervals):
    intervals.sort() # 二维列表排序，默认左边界
    # return intervals
    ans = []
    for i in intervals:
        # print(i[0])
        # break
        if not ans or ans[-1][1] < i[0]:
            ans.append(i)
        else:
            ans[-1][1] = max(ans[-1][1], i[1])
            # ans[-1][1] = i[1] # 若右边界比左边界大
    return ans



print(merge([[1,3],[2,1],[8,10],[15,18]]))
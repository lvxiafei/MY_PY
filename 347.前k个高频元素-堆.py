'''
返回出现频率前k高的的元素
in: nums = [1,1,1,2,2,3] k = 2
out: [1,2]

'''

def topKFrequent(nums,k):
    # pass
    import heapq
    from collections import Counter
    count = Counter(nums) # 次数统计
    # print(count)
    # print(count.keys())
    # print(count.get)
    return heapq.nlargest(k, count.keys(),key=count.get)




if __name__=="__main__":
    print(topKFrequent([1,1,1,2,2,3], 2))
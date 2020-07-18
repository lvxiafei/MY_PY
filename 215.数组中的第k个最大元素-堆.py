'''
in: [3,2,1,5,6,4]  k=2
out: 5

in:[3,2,3,1,2,4,5,5,6] k=4
out: 4
'''

# def findKthLargest(nums,k):
#     return sorted(nums)[-k]

# def findKthLargest(nums,k):
#     from heapq import nlargest
#     # print(nlargest(k,nums))
#     return nlargest(k,nums)[-1]

def findKthLargest(nums,k):
    import heapq
    # 使用优先队列存储前k个元素
    heap =[float("-inf") for _ in range(k)]
    # print(heap)
    for i in nums:
        if i > heap[0]:
            heapq.heappop(heap)  # heapq 小顶堆,其余所有<heap[0]<heap[1]
            heapq.heappush(heap, i)
    # print(heap)
    return heap[0]

if __name__=="__main__":
    print(findKthLargest([3,2,1,5,6,4],2))
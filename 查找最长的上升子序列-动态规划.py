def longest_inc_subseq(seq):
    if seq is None:
        raise TypeError('seq cannot be None')
    if not seq:
        return []
    temp = [1] * len(seq)  # 记录下对应的长度变化
    prev = [None] * len(seq)
    for r in range(1, len(seq)):  # 双指针
        for l in range(r):
            if seq[l] < seq[r]:
                if temp[r] < temp[l] + 1:
                    temp[r] = temp[l] + 1
                    prev[r] = l
    max_val = 0
    max_index = -1
    results = []
    for index, value in enumerate(temp):  # 找到最长的长度和对应的下标
        if value > max_val:
            max_val = value
            max_index = index
    curr_index = max_index
    while curr_index is not None:
        results.append(seq[curr_index])  # 找到对应的逆序序列
        curr_index = prev[curr_index]  # 找到相应的下一个下标
    return results[::-1]

shili = longest_inc_subseq([3, 4, -1, 0, 6, 2, 3])
print(shili)
# [-1, 0, 2, 3]
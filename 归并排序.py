'''
归并排序
时间复杂度：O(nlogn)，空间复杂度O(n)，稳定性：稳定

归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组
将数据分解到最小之后，然后合并两个有序数组，基本思想是比较两个数组的最前面的数，谁小就先取谁，
取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分赋值过来即可

'''

def merge_sort(data):
    if len(data) == 1:
        return data

    mid = int(len(data) / 2)
    left = data[:mid]
    right = data[mid:]

    left_merge = merge_sort(left)
    right_merge = merge_sort(right)
    return merge(left_merge, right_merge)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))

        else:
            result.append(right.pop(0))

    result = result +left + right
    # result += left
    # result += right
    return result


data = [1, 5, 2, 3, 9, 6]
print(merge_sort(data))
# 打印内容: [1, 2, 3, 5, 6, 9]
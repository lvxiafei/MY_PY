'''
快速排序
时间复杂度：最好O(nlogn)，最坏O(n2)，稳定性，不稳定

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

'''


# 快速排序
# 有自身递归
def quick_sort(array):
    if len(array) < 2:
        return array  # 基线条件 为空或包含一个元素
    else:
        pivot = array[0]  # 基准值
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(list))
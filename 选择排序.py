'''
选择排序：
时间复杂度：最好=最差O(n^2)， 空间复杂度O(1)， 稳定性：不稳定

'''
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:36:54 2018
@author: zhipeng
function:选择排序
input：list
"""
# 通过n-i次关键字之间的比较，从n-i+1个记录中选出关键字最小的记录，并和第i个记录进行交换

def select_sort(data):
    for i in range(0, len(data) - 1): # 遍历n-1次
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]: # n-(i+1)+1 = n-i次比较 选择 选择最小的
                min_index = j

        # tmp = data[min_index]
        # data[min_index] = data[i]
        # data[i] = tmp
        data[min_index], data[i] = data[i], data[min_index]

    print(data)


data = [1, 5, 2, 3, 9, 6]
select_sort(data)
# 输出结果：[1, 2, 3, 5, 6, 9]
# 同理，要是想倒序输出，改变一下if条件，就可以了。
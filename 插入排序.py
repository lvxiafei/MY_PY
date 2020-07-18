'''
插入排序
复杂度：最好O(n)，最差O(n^2)，空间复杂度O(1) ，稳定性：不稳定

'''
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:36:54 2018
@author: zhipeng
function:插入排序
input：list
"""
#基本操作是将一个记录从后向前插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表

def insert_sort(data):
    for i in range(1, len(data)):
        pre_index = i - 1
        current = data[i]
        while pre_index >= 0 and data[pre_index] > data[i]:#从后向前比较，当当前元素小时
            data[pre_index + 1] = data[pre_index]
            pre_index -= 1
        data[pre_index + 1] = current

    print(data)


data = [1, 5, 2, 3, 9, 6]
insert_sort(data)
# 打印内容：[1, 2, 3, 5, 6, 9]
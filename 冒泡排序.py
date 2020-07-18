# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 08:36:54 2018
@author:
function:冒泡排序
input：list
"""
# 交换排序的一种，其核心思想是：两两比较相邻记录的关键字，如果反序则交换，直到没有反序记录为止


def Bubblle_sort(data):
    for i in range(0, len(data)): # 每次定一位，冒一泡，倒数升序i位最大 泡泡
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j + 1]: # swap
                # tmp = data[j + 1]
                # data[j + 1] = data[j]
                # data[j] = tmp
                data[j + 1], data[j] = data[j], data[j + 1] # 交换
    print(data)


data = [1, 5, 11, 3, 9, 6]
Bubblle_sort(data)
'''
时间复杂度：最好状态O(n)，最差O(n^2)，空间复杂度O(1)，属于稳定排序
稳定排序：是指当有一个相等的数字进来时，它会确定性的放在其相等数字的后面
打印内容：[1, 2, 3, 5, 6, 9]
更进一步，上面是顺序排列，如果需要倒序排列的话，data[j] < data[j + 1]，输出是[9, 6, 5, 3, 2, 1]
'''

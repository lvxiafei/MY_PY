'''
题目描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，
结果保留一位小数。

输入描述:
首先输入一个正整数n，
然后输入n个整数。
5
1
2
3
4
5
输出描述:
输出负数的个数，和所有正整数的平均值。
0 3
'''


while True:
    try:
        n = int(input())
        result_list = []
        result_list = list(map(int, input().split()))
        # print(len(result_list))
        # for i in range(n):  # 不能用这种
        #     result_list.append(int(input().split()))
        print(len(result_list))
        cnt = 0
        pos_list = []
        for i in result_list:
            if i < 0:
                cnt += 1
            elif i > 0:
                pos_list.append(i)
        print(cnt, round(sum(pos_list)/len(pos_list), 1))
    except:
        break
'''  可反复调用 =》while True:    except:
输入描述: 输入一串字符。  aadddccddc
输出描述:               dca
对字符中的各个英文字符（大小写分开统计），数字，空格进行统计，并按照统计个数由多到少输出,如果统计的个
数相同，则按照ASII码由小到大排序输出 。如果有其他字符，则对这些字符不用进行统计。

'''
# # s = input()
# s = 'aadddccddc'
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# ans = sorted(d, reverse=True)
# print(''.join(ans))

'''
思路：
    先根据ascii码排序
    在根据词频排序

'''
while True:
    try:
        a = input()
        # a = 'bbaa ,*@! &&'
        d = {}
        res = ''
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d_1 = sorted(d.items(),key = lambda item:item[0])  # 按照ASII码由小到大排序输出
        # print(d)
        # print(d_1)

        d_1.sort(key = lambda i:i[1],reverse = True)  # 词频降序
        # print(d_1)
        for i in d_1:
            res += i[0]
        print(res)
    except:
        break


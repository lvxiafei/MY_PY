'''
5 3
1 2 3 4 5

思路：
字典存储商品种类和数量
count = 0
从大到小组合，count + 1,已用种类数量-1
数量为0，删除
当长度小于3，输出

'''

n, k = map(int, input().split())
list = list(map(int, input().split()))
list.sort()
# print(n, k, list)
count = 0
# list[-1] = list[-1]-1
while True:
    for i in range(1,k+1):
        if list[-i] > 0:
            list[-i] = list[-i]-1
    # print('start',list)
    count += 1
    # print(count)

    for i in list:
        if i == 0:
            list.remove(i)


    # print(list)
    if len(list)<3:
        print(count)
        break

# print(list)

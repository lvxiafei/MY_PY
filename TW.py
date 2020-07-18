'''
无人机定位
input:
4 6
R-GFG
FRGFR
FFRRF
RFF-G
RRG-F
RGFRG
GGFRF
G-RGR
'''
print("请输入：")
m, n = map(int, input().split())  # 录入行列 4 6
str = []
j = 0
table = [[] for i in range(m)]
for i in range(0, 8): # 录入无人机拍照数据
    str.append(input())
print("录入坐标是：", str)#输出录入数据
print("--------------------------")
for i in range(m):
    table[j].append(str[i][4])      # 0,0 G
    table[j].append(str[i][0])      # 0,1 R
    table[j].append(str[i][2])      # 0,2 G
    table[j].append(str[7-i][4])    # 0,3 R
    table[j].append(str[7-i][0])    # 0,4 G
    table[j].append(str[7-i][2])    # 0,5 R
    j += 1
print("地形是：")
for i in range(m):
    print(table[i])
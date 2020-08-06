'''
最小需要一心几用，才能上完买的所有课-> 最后是一个列表，比大小->列表中的每个元素是
课程数，起止时间
算法题不给全测试用例，考的就是测试能力，考虑全各种情况
4
1 4
1 2
2 3
3 4

o:2

4
1 6
1 2
2 4
3 5
o:3
未考虑一心截至不用的时间点
4
1 2
1 3
2 3
3 5
o:2
[1,5]
[1,3]

4
3 5
3 6
1 4
1 3
o:3
[1,5]
[1,4]
[3,6]
思路：
    多个区间压缩，找最大重叠区间数
    非重叠区间合并，找到最后生成的区间数


'''
n = int(input())

d = []  # n行2列
for i in range(n):
    a, b = map(int, input().split())
    d.append([a, b])
d.sort()  # 根据第一个元素排序
d = sorted(d, key = lambda x: x[1])  # 根据第二个元素排序
# print(d)    # [[1, 3], [1, 4], [3, 5], [3, 6]]
l = d[0][0]
r = max(d, key = lambda x:x[1])
r = r[1]
# print(l,r)
m = [0]*(r-l+1)
# print(m)
'''

最大区间 [1,6]
遍历每个时间节点，找到重复数最大的次数
1 2
2 2
3 3
4 2
5 1
'''
for i in range(l, r):
    for j in d:
        if i in list(range(j[0], j[1])):
            m[i] += 1
    # print(m[i],end=' ')
# print(m)
print(max(m))





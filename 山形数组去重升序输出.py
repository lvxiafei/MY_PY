'''
1,3,5,8,9,7,7,3,1
输出：去重升序
'''

# import sys
# line = sys.stdin.readline().strip()
# values = list(map(int, line.split(',')))

#  sys.stdin.readline().strip() == input()
values = list(map(int, input().split(',')))

mm = sorted(values)
mmm = list(set(mm))

c = map(str, mmm)  # 列表中的元素并不是str类型，需要把b中的元素map成str类型

print(", ".join(c))  # 这里为什么用c而不是b我也没有搞清楚？？

b = [1, 2, 3, 4, 5]
c = map(str, b)  # 列表中的元素并不是str类型，需要把b中的元素map成str类型

print(" ".join(c))  # 这里为什么用c而不是b我也没有搞清楚？？

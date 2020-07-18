'''
生成随机列表
'''

import random


def random_list(start, stop, length):
    if length >= 0:
        length = int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


if __name__ == '__main__':
    print(random_list(0, 100, 10))

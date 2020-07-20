'''


'''
import random
def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
    random_list.append(random.randint(start, stop))
  return random_list

print(random_int_list(0,100,10))

# 生成随机数
ret = random.randint(0, 10)
print(ret)

ret2 = random.random() # [0,1)范围内的随机浮点数
print(ret2)
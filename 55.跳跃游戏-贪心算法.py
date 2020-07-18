'''

i: [2,3,1,1,4]
o: true

思路：尽可能到达最远距离（贪心）

不断更新最远距离
和最远位置进行比较

口诀：
    更新距离
        确定能到
        需要更新：当前位置+跳数>最远
    比较返回

'''

def canJump(nums):
    max_i = 0 # 初始化当前能到达最远的距离
    for i, jump in enumerate(nums): # i为当前位置，jump为当前位置的跳数
        if max_i >= i and i + jump > max_i:
            max_i = i + jump # 更新最远距离
    return max_i >= i

print(canJump([2,3,1,1,4]))
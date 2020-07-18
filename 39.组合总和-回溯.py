'''
给定一个无重复元素的数组dandidates和一个目标数target，找出candidates中所有可能和为target的组合
candidates中的数字可以无限制重复被读取

candidates = [2,3,6,7] target = 7
O:
[
[7],
[2,2,3]
]

'''

def combinationSum(candidates, target):
    output = []

    def backtrack(combination, target_changed):
        if target_changed == 0:
            if sorted(combination) not in output:
                return output.append(combination)
        elif target_changed > 0:
            for num in candidates:
                backtrack(combination+[num], target_changed - num)

    backtrack([], target)
    return output

'''
backtrack(combination, num_changed) 

'''

print(combinationSum([2,3,6,7], 7))
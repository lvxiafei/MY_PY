'''
给定一个包含2-9的字符串，返回所有可能表示的字母组合
d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

"23"
o:["ad","ae","af","bd","be","bf","cd","ce","cf"]

思路：
几个数字就几层循环，遍历输出（不可行） 循环层数不确定
分治：
    len == 1
    len != 1
        digits[0] + digits[1:]

'''

def letterCombinations(digits):
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = []
    if len(digits) == 1:
        return [k for k in d[digits]]
    else:
        a = letterCombinations(digits[0])
        b = letterCombinations(digits[1:])
        for i in range(len(a)):
            for j in range(len(b)):
                tmp = a[i] + b[j]
                ans.append(tmp)
    return ans


'''
回溯：通过穷举所有可能情况来找到所以解的算法。如果一个侯选解被发现并不是可行解，回溯算法会舍弃它，
并在前面的一些步骤做出一些修改，并重新尝试找到可行解

digits是数字字符串
s(digits)是digits所能代表的字母字符串
把s(digits)分解可表示为：
s(digits[0...n-1]) = letter(digits[0]) + letter(digits[1...n-1])
                   = letter(digits[0]) + letter(digits[1]) + letter(digits[2...n-1])
                   = ...
也是递归的一种
                   
'''

def letterCombinations2(digits):
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    output = []
    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            return output.append(combination)
        else:
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    if digits:
        backtrack('', digits)
    return output





print(letterCombinations2("23"))
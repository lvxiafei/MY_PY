'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串
具有不同开始位置或结束位置的子串，即使是相同的字符组成，也会被认为是不同的子串
"abc"
o:3
"a","b","c"

输入："aaa"
o:6
"a","a","a","aa","aa","aaa"

思路：
不同开始，结束位置的子串，正序==倒序

'''

def countSubstrings(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] == s[i:j][::-1]:
                ans += 1
    return ans

'''
动态规划：


'''


def countSubstrings2(s: str) -> int:
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        count = 1
        for j in range(i - 1, -1, -1):
            if s[j:i + 1] == s[j:i + 1][::-1]:
                count += 1
        dp[i] = dp[i - 1] + count
    return dp[-1]

print(countSubstrings2("aaa"))
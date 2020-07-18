'''
不含有重复字符的最长子串的长度
i: "abcabcbb"
o:3
"abc"

思路：

数据结构与算法选择：（相应时间复杂度与空间复杂的：   ）

不含有重复字符的子串
    双指针
找到最长

'''

def lengthOfLongestSubstring(s):
    res = ""
    for f in range(len(s)):
        for r in range(f, len(s)):
            sub = s[f:r]  # 子串
            # print(sub)
            if len(sub) == len(set(sub)):
                # print(sub)
                if len(sub)>len(res):
                    res = sub
    return res

'''
字典记录字符和下标，下次遇到计算长度


'''
def lengthOfLongestSubstring2(s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
        if c in d:
            start = max(start, d[c])
        d[c] = i
        ans = max(ans, i - start)
    return ans



print(lengthOfLongestSubstring2("abcabcbb"))
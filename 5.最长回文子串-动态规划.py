'''
给定一个字符串s,找到s中最长的回文串
"babad"
o:"bab"

cbbd -》 "bb"

思路：
双指针
找回文子串

比较输出




'''

def longestPalindrome(s):

    # pass
    ans = ""
    for left in range(len(s)):
        for right in range(left, len(s)):
            # print(left,right)
            if s[left:right] == s[left:right][::-1]:
                # print(s[left:right])
                if len(s[left:right]) > len(ans):
                    ans = s[left:right]
    return ans

print(longestPalindrome("babad"))
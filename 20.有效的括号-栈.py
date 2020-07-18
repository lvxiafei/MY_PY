"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true


思路：
左括号入栈，遇到匹配的右括号出栈

"""
def isValid(s:str):
    dic = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in s:
        if stack and i in dic:
            if stack[-1] == dic[i]: stack.pop()
            else:
                return False
        else:
            stack.append(i) # 左括号
    return not stack


if __name__ == '__main__':
    print(isValid("()"))










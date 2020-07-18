'''
s = "3[a]2[bc]"
out: aaabcbc

s = "3[a2[c]]"
out: accaccacc
'''

def decodeString(s:str):
    stack = [] # 执行顺序
    res = "" #结果
    multi = 0 # 重复次数
    for c in s:
        if c =='[': #入栈
            stack.append([res, multi]) #列表对
            res = ""
            multi = 0
        elif c ==']':
            last_res, last_multi = stack.pop()
            res = last_res + last_multi * res
        elif '0' <= c <= '9':
            multi = multi * 10 + int(c)
        else:
            res += c
            # print(res)
    return res



if __name__=="__main__":
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a]"))
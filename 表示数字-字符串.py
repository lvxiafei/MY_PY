'''
输入  Jkdi234klowe90a3
输出  Jkdi*234*klowe*90*a*3*

思路：


'''
while True:
    try:
        s = input()
        # s = 'Jkdi234klowe90a3'
        d = []
        res = ''
        for i in s:
            if i.isnumeric():
                d.append('*' + i + '*')
            else:
                d.append(i)
        res = ''.join(d)
        res = res.replace('**', '') # 替换
        print (res)
    except:
        break
'''
2
abc
123456789

o:
abc00000
12345678
90000000
'''
while True:
    try:
        a= int(input())
        for i in range(a):
            s=input()
            while len(s)>8:
                print(s[:8])
                s=s[8:]
            # print(s.ljust(8,"0"))
            print(s+(8-len(s))*'0')
    except:
        break
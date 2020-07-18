while True:
    try:
        li = list(map(int, input().split()))
        print(li)
        count1 = 0
        count2 = 0
        su = 0
        for i in li:
            if i < 0:
                count1 += 1
            else:
                count2 += 1
                su += i
        print (count1)
        print ('%.1f' %(float(su)/count2))
    except:
        break
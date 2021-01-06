t = int(input())
if (t%3==1):
    print((t//3 -1)*7 + 4)
else:
    if (t%3 ==2):
        print((t//3)*7 +1 )
    else:
        print(t // 3 * 7)
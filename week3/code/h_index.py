n=int(input())
k=[float(x)for x in input().split()]
k.sort(reverse=True)
maxx=n
for i, x in enumerate(k):
    if x<i+1: 
        maxx=i
        break
print(maxx)
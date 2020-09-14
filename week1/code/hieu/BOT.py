n=int(input())
t=input().split()
t=[int(x)for x in t]
t.insert(0,int(0))
for i in range(1,n+1):
    t[i]=t[i]+t[i-1]

maxx = -1e18
q = 0
r1 = 0 
r2 = 0
for i in range(1,n+1):
    if t[q] > t[i]:
        q = i
    if maxx < t[i] - t[q]:
        maxx = t[i] - t[q]
        r1 = q
        r2 = i
print(r1+1,r2,maxx)
n = int(input())
a = input().split()
a = [int(x) for x in a]
a = [0] + a
for i in range(1,n+1):
    a[i] = a[i-1] + a[i]
m = -1e18
q = 0
r1 = 0 
r2 = 0
for i in range(1,n+1):
    if a[q] > a[i]:
        q = i
    if m < a[i] - a[q]:
        m = a[i] - a[q]
        r1 = q
        r2 = i
print(r1+1,r2,m)

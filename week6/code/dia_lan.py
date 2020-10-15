t = input().strip().split()
n,m =  [int(x) for x in t]
a = input().strip().split()
a = [int(x) for x in a]
it = [0] * n * 4 + [0]
def update(k,l,r,u,v):
    #print(k,u,l,r)
    if (u > r or u < l): 
        return
    if (l==r):
        it[k] = v
        return
    mid = (l + r)//2
    update(k*2,l,mid,u,v)
    update(k*2+1,mid+1,r,u,v)
    it[k] = it[k*2] & it[k*2+1]
def get(k,l,r,u,v):
    if (v<l or u>r): 
        return 2**12-1
    if (l>=u and r<=v):
        return it[k]
    mid = (l+r)//2
    return get(k*2,l,mid,u,v) & get(k*2+1,mid+1,r,u,v)
for i in range(n):
    update(1,1,n,i+1,a[i])
for i in range(n):
    #print(get(1,1,n,i+1,i+m),i+1,i+m)
    if (get(1,1,n,i+1,i+m)==0):
        print('YES')
        exit()
#print(4&3)
print('NO')
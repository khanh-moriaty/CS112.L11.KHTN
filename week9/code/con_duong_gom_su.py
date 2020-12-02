base = 50001;
MOD = 1000000003;
maxn = 100011;
POW = [0] * maxn
hashT = [0] * maxn
hashh = 0
mu = [0] * (base  + 5)
a = [0] * base * 2
n = 0
x = 0
res1 = [0] * 1005
res2 = [0] * 1005
res3 = [0] * 1005
dem = 0

def  getHashT(i,j):
    return (a[j] - a[i - 1]  + MOD * MOD) % MOD
n = int(input())
mu[0]=1
for i in range(1,50002):
    mu[i] = (mu[i-1]*base)%MOD
tmp = input().split()
a = [int(x) for x in tmp]
a = a + [0]
for i in range(n,0,-1):
    a[i] = a[i-1]
a[0] = 0
#for i in range(n+1):
#    print(a[i])
for i in range(1,n+1):
    a[i] = (a[i-1] + (mu[a[i]]))%MOD
for i in range(1,n+1):
    if (n%i == 0):
        x=-1;y=-1;z=-1;
        j= 0
        while(j<n):
            if (x==-1):
                x = getHashT(j+1,j+i)
                z = 1
            else:
                if (x == getHashT(j+1,j+i)):
                    z = z + 1
                else:
                    if (y == -1):
                        y = getHashT(j+1,j+i)
                    else:    
                        if (y != getHashT(j+1,j+i)):
                            z = -1
                            break
            j = j + i

        if (z==-1 or z==n/i):
            continue
        dem = dem + 1
        res1[dem] = i
        res2[dem] = n/i-z
        res3[dem] = z
if (dem ==0):
    print(-1)
else: 
    print(dem)
    for i in range(1,dem+1):
        print(int(res1[i]),int(res3[i]),int(res2[i]))
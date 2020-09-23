mport sys
sys.setrecursionlimit(10**6)

def matmul(a,b):
    c = [[0,0],[0,0]]
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % (10**9+7)
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % (10**9+7)
    return c

def mu(x, k):
    if k == 0:
        return [[1, 0], [0, 1]]
    t = mu(x, k//2)
    t = matmul(t, t)
    if k % 2 == 0:
        return t
    return matmul(t,x)

n, k = [int(x) for x in input().split()]

if k == 2:
    print(5*n)
elif k == 1:
    print(2*n)
else: 
    arr = [[0, 1], [-1, 3]]
    a = mu(arr, k-2)

    b = [[2, 0], [5, 0]]
    a = matmul(a, b)
    print(a[1][0] * n % (10**9+7))


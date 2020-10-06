from math import ceil
a, k, b, m, n = [int(x) for x in input().split()[:5]]
a, k, b, m = (a, k, b, m) if k <= m else (b, m, a, k)
l = ceil(n / (a+b))
r = ceil(n / (a+b) * k / (k-1))
r = 10**18
while l <= r:
    x = (l+r) // 2
    if x * (a+b) - a * (x//k) - b * (x//m) >= n:
        res = x
        r = x - 1
    else:
        l = x + 1

print(res)
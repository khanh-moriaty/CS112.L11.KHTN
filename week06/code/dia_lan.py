t = input().strip().split()
n,m =  [int(x) for x in t]
a = input().strip().split()

def bit_xor(a, b):
    return [a_i is not b_i for a_i, b_i in zip(a,b)]
    
def bit_or(a, b):
    return [a_i or b_i for a_i, b_i in zip(a,b)]

max_bit = 2**12
bit_mask = [True] * 12

def str2bit(x):
    a = [False] * 12
    x = int(x)
    d = 11
    while x > 0:
        if x % 2:
            a[d] = True
        x = x // 2
        d -= 1
        
    return bit_xor(a, bit_mask)
        
def inc():
    a = [False] * 12
    while True:
        yield a
        for i, a_i in enumerate(a[::-1]):
            if a_i:
                a[-i-1] = False
            else:
                a[-i-1] = True
                break
inc = inc()

def bit2int(a):
    x = 0
    pow = 1
    for a_i in a[::-1]:
        if a_i:
            x += pow
        pow *= 2
    return x

a = map(str2bit, a)
res = [0] + [1000000] * (max_bit-1)
for a_j in a:
    for i, res_i in zip(inc, res):
        c = bit_or(i, a_j)
        d = bit2int(c)
        res[d] = min(res[d], res_i+1)
if res[max_bit - 1] > m :
    print('NO')
else:
    print('YES')
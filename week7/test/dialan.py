import os
os.system(r"gen.exe")
for i in range(100):
    t = "test.in" + str(i+1)
    f = open(t, "r")
    t = str(f.readline()).split()
    n,m =  [int(x) for x in t]
    a = str(f.readline()).split()
    f.close()
    a = [int(x) for x in a]
    max_bit = 2**12
    t = "test.o" + str(i+1)
    f = open(t,"w")
    for i, a_i in enumerate(a):
        a[i] = a_i ^ (max_bit-1)
    res = [0] + [1000000] * (max_bit-1)
    for a_j in a:
        for i, res_i in enumerate(res):
            c = i | a_j
            res[c] = min(res[c], res_i+1)
    if res[max_bit - 1] > m :
        f.write('NO')
    else:
        f.write('YES')
    f.close()


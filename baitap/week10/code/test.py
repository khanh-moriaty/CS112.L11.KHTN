import phan_thuong

import random as rd
rd.seed(42)
def gen():
    n = 10
    k = 2
    
    a = []
    for i in range(n):
        a.append(rd.randint(1, 100))
        
    return a, n, k

def main(a, n, k):
    
    a = list(a)
    
    res = 1e10
    
    for i in range(n-k+1):
        t = -1e10
        if i-k >= 0:
            for j in range(i-k+1):
                t = max(t, sum(a[j:j+k]))
        for j in range(i+k, len(a)-k+1):
            t = max(t, sum(a[j:j+k]))
            
        # x = max(0, i-k+1)
        # for j in range(x, i):
        #     print(a[j:min(j+k,i)])
        #     print(a[i+k:i+k+(i-j)])
        #     t = max(t, sum(a[j:min(j+k,i)]) + sum(a[i+k:i+k+(i-j)]))
            
        x = sum(a[i:i+k])
        
        # print(i, i+k-1, t, x)
        if t > x: continue
        
        if x < res:
            res = x
    
    return res
                
            

if __name__ == '__main__':
    
    # n, k = map(int, input().strip().split())
    # a = map(int, input().strip().split())
    # res = main(a, n, k)
    # print(res)
    
    for i in range(100000):
        a, n, k = gen()
        print(n, k)
        print(' '.join([str(x) for x in a]))
        print()
        res1 = main(a, n, k)
        res2 = phan_thuong.main(a, n, k)
        if res1 != res2: 
            print(res1, res2)
            break
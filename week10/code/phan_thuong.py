from itertools import accumulate

def main(a, n, k):

    a = list(accumulate(a))

    a[:0] = [0]
    a = [x-y for x, y in zip(a[k:], a)]

    b = {}
    for i, x in enumerate(a):
        if x not in b: b[x] = (i, i)
        else: b[x] = (b[x][0], i)

    mx = max(b.keys())
    if b[mx][1] - b[mx][0] >= k:
        return min(a)
        
    c = [(x, y) for (x, y) in b.items()]
    c.sort(key=lambda x: x[0], reverse=True)

    print(a)
    print(c)

    del b

    s, t = 1e10, -1e10
    for x in c:
        # print(s, t)
        s_t = min(s, x[1][0])
        t_t = max(t, x[1][1])
        
        if t_t - s_t >= k:
            x = t-s+1
            t = min(len(a), s+k)
            s = max(0, s+x-k)
            # print(s, t)
            return min(a[s:t])
            
        s = s_t
        t = t_t
        
if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    a = map(int, input().strip().split())
    print(main(a, n, k))

'''
10 2
1 2 4 5 2 4 2 2 1 6 

'''
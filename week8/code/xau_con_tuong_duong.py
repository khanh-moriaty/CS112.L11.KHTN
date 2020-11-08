from sys import stdin, stdout

s = stdin.readline().strip()
n = len(s)

max_len = n+1
base = [1] * 26
for i, b in enumerate(base):
    if i is 25: break
    base[i+1] = b * max_len

t = [0] * (n+1)
t[0] = base[ord(s[0]) - 97]
s = s[1:]
for i, (c, x) in enumerate(zip(s, t)):
    t[i+1] = x + base[ord(c) - 97]
    
k = int(stdin.readline().strip())

res = []
for i in range(k):
    a, b, c, d = [int(x) for x in stdin.readline().strip().split()]
    res.append('YES\n' if t[b-1] - t[a-2] == t[d-1] - t[c-2] else 'NO\n')
stdout.writelines(res)

'''

abcbacaac
2
1 3 4 6
1 3 5 7

'''


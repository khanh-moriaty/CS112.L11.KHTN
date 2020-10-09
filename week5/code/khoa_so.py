from sys import stdin, stdout
from collections import Counter

n = stdin.readline().strip()
count = Counter(n)
tong = sum(map(int, n)) % 3

du = [[]] * 3
du[1] = ['1', '4', '7']
du[2] = ['2', '5', '8']
du = [[x for x in d if x in count] for d in du]

if tong:
    d = sum(count[x] for x in du[tong])
    c = 1
    if not d:
        c = 2
        tong = 3 - tong
    for x in du[tong]:
        t = min(c, count[x])
        c -= t
        count[x] -= t

for x in sorted(count.keys(), reverse=True):
    stdout.write(x * count[x])
print()
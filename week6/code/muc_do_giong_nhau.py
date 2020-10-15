s, t = input(), input()
a = {x+y for x,y in zip(t[:-1], t[1:])}
print(sum([x+y in a for x,y in zip(s[:-1], s[1:])]))
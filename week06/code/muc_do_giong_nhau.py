s, t = input(), input()
a = {x+y for x,y in zip(t, t[1:])}
print(sum([x+y in a for x,y in zip(s, s[1:])]))
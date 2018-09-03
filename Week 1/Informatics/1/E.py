v = int(input())
t = int(input())
s = abs(v) * t
s1 = s % 109
if s1 == 0:
    print(0)
elif v < 0:
    print(109 - s1)
else:
    print(s1)
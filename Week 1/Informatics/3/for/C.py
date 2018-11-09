import math
a = int(input())
b = int(input())
for x in range(a, b+1):
    c = math.sqrt(x)
    if c - math.floor(c) == 0:
        print(x)
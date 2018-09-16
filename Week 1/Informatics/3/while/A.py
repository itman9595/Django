import math
N = int(input())
x = 1
while(x != N+1):
    s = math.sqrt(x)
    if(s - math.floor(s) == 0):
        print(x)
    x += 1
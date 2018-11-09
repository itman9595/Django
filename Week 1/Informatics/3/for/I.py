import math
x = int(input())
count = 0
for n in range(1, math.floor(math.sqrt(x))-1):
    if x % n == 0:
        count += 1
        print(n)
count = int(math.pow(count, 2))
if(math.sqrt(x) % 2 == 0):
    count += 1
print(count)
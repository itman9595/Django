N = int(input())
print(1)
k = 2
while(k != N+1):
    n = k
    while(n != 1):
        if n % 2 == 0:
            n /= 2
        else:
            break
    if n == 1:
        print(k)
    k += 1
    
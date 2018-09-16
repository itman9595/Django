x = int(input())
for n in range(2, x+1):
    if x % n == 0:
        print(n)
        break
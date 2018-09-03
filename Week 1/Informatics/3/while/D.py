N = int(input())
while(N != 1):
    if N % 2 == 0:
        N /= 2
    else:
        break
if N == 1:
    print('YES')
else:
    print('NO')
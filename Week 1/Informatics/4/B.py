N = int(input())
array = []
for x in range(0, N):
    y = int(input())
    array.append(y)
for x in range(0, N):
    if array[x] % 2 == 0:
        print(array[x])
N = int(input())
array = []
for x in range(0, N):
    y = int(input())
    array.append(y)
count = 0
for x in range(N-1, -1, -1):
    if array[x] >= array[x-1] and x != 0:
        count += 1
print(count)
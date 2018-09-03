N = int(input())
array = [int(x) for x in range(0, N)]
for x in range(0, len(array)):
    y = int(input())
    array.append(y)
k = 0
while(k < len(array)):
    print(array[k])
    k += 2
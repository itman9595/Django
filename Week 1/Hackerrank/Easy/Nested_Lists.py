if __name__ == '__main__':
    arr = []
    i = 0
    k = 0
    s = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        if i == 0:
            k = score
        if k > score:
            s = k
            k = score
        i += 1
    new_arr = []
    for x in range(0, len(arr)):
        if arr[x][1] == s:
            new_arr.append(arr[x][0])
    new_arr.sort()
    for x in range(0, len(new_arr)):
        print(new_arr[x])
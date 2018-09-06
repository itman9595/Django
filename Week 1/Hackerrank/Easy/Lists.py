if __name__ == '__main__':
    N = int(input())
    list1 = []
    list2 = []
    for _ in range(N):
        command, *line = input().split()
        numbers = list(map(int, line))
        if command == "insert":
            list1.insert(numbers[0], numbers[1])
        elif command == "print":
            temp = []
            for x in range(0, len(list1)):
                temp.append(list1[x])
            list2.append(temp)
        elif command == "remove":
            list1.remove(numbers[0])
        elif command == "append":
            list1.append(numbers[0])
        elif command == "sort":
            list1.sort()
        elif command == "pop":
            list1.pop()
        elif command == "reverse":
            list1.reverse()

    for x in range(0, len(list2)):
        print(list2[x])
    
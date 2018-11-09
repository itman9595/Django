line = input().split()
numbers = list(map(int, line))
symbol = ".|."
factor = 1
list1 = []
for x in range(0, numbers[0]):
    if x == int(numbers[0] / 2):
        print('WELCOME'.center(numbers[1], '-'))
        list1.reverse()
    elif x < int(numbers[0] / 2):
        symbol = symbol * factor
        factor += 2
        text = symbol.center(numbers[1], '-')
        list1.append(text)
        print(text)
        symbol = ".|."
    else:
        for y in list1:
            print(y)
        break
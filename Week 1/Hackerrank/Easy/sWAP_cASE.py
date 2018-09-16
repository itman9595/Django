def swap_case(s):
    s1 = ""
    for x in s:
        if x.islower():
            s1 += x.upper()
        else:
            s1 += x.lower()
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
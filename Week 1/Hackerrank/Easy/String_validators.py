if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    for x in range(0, len(s)):
        if s[x].isalnum():
            isalnum = True
        if s[x].isalpha():
            isalpha = True
        if s[x].isdigit():
            isdigit = True
        if s[x].islower():
            islower = True
        if s[x].isupper():
            isupper = True

    print (isalnum)
    print (isalpha)
    print (isdigit)
    print (islower)
    print (isupper)
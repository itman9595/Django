def wrap(string, max_width):
    string = textwrap.wrap(string, max_width)
    str1 = ""
    for s in string:
        str1 += s + "\n"
    return str1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
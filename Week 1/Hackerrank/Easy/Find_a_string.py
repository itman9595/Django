def count_substring(string, sub_string):
    count = 0
    for x in range(0, len(string)):
        if len(sub_string) <= len(string)-x:
            str1 = ""
            str1 = string[(len(string) - (len(string)-x)):x+(len(sub_string))]
            if str1 == sub_string:
                count += 1
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
a = int(input())
text = "The next number for the number {} is {}."
print(text.format(a, a+1))
text = "The previous number for the number {} is {}."
print(text.format(a, a-1))
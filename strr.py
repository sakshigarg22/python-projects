def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = "python is"
print(reverse(s))

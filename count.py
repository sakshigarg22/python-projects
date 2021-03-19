str = input()
c = 0
e = 0
for i in str:
    if 97 <= ord(i) <= 122:
        c = c+1
    elif 65 <= ord(i) <= 90:
        e = e+1
print(c,e)

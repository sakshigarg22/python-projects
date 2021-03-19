a = input().upper()
f = 0
for i in range(65,91):
    if (chr(i)not in a):
        f = 1
        break
if (f == 0):
    print('panagram')
else:
    print('not panagram')
print(a)

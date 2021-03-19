a = eval(input())
for i in range(len(a)):
    if a[i] == i:
        print(i)
        break
else:
    print('False')

list = [1,2,2,3,4,5,3,4,3]
uniquelist = []
for i in list:
    if i in list and i not in uniquelist:
        uniquelist.append(i)
print(uniquelist)

n = int(input("enter the limits of number"))
l = []
for i in range(n):
    i.append()
for i in range(n):
    if l.count(l[i])>1:
        c = 0
    for j in range(i,n):
        if l[j]==l[i]:
            l[j]=l[j]+c
            c+=1
print(l)

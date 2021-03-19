n = int(input())
a = [int(i)for i in input().split()]
b = 0
l = []
for i in a:
    if a.count(i)>b:
        b = a.count(i)
c = sorted(a,reverse=True)
for i in range(b):
    l.append(c[i])
print(l,len(l))
                

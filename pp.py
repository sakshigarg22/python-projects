items = list(map(str,input().split(',')))
c = [items[0]]
for i in range(len(items)):
    for j in range(0,len(items)):
        if c[i][-1]==items[j][0]:
            c.append(items[j])
            items.remove(items[j])
            items.insert(j,"0")
            break
print(c)



s = input().split()
c = []
[c.append(i)for i in s if i not in c]
c.sort()
print(*c)

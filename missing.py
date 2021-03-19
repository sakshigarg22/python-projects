a = list(range(1,51))
c = [1,22,45,49,34]
b = []
for i in range(len(a)):
    if i not in c:
        b.append(i)
print(b)
        

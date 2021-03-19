n1 = []
for i in range(2000,3000):
    if i%7==0 and i%5!=0:
        n1.append(str(i))
print(','.join(n1))

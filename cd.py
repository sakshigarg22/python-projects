c=50
h=30
lst = []
s=input()
ls = s.split(",")
for i in ls:
    q=(2*c*int(i)//h)**.5 
    lst.append(str(q))
print(','.join(lst))

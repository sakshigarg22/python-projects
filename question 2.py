a = []
b,c = [],[]
f = open('C:/Users/PC/Documents/doc/s.txt','r') 
for i in f.readlines():
    d = i.split()
    b.append(d[0]),c.append(d[1])
for i in b:
    if i in c:
        print(i+"is fraud voter")
    else:
        c.append(i)
d = {}
for i in a:
    d[i] = d.get(i,0) + 1
{b: v for b,v in sorted(d.items(),key = lambda item:item[0])}
p = 1
for i,j in d.items():
    if c<4:
        print(c,"candidate is :",i)
        c += 1
    else:
        break
            

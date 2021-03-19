b = list(eval(input()))
b.append("00")
k = int(input())
r,s = [set()],0
re = []
result = []
for i in range(1,len(b)):
    if b[i-1][0]==b[i][0]:
        r[s].add(b[i-1][0])
        r[s].add(b[i-1][1])
    else:
        r[s].add(b[i-1][1])
        re.append(b[i-1][0])
        s+=1
        r.append(set())
for i in range(len(r)):
    for j in range(i+1,len(r)-1):
        d=str(len(r[i].intersection(r[j])))+str(abs(len(r[i])-len(r[j])))
        result.append((d,re[i],re[j]))
p = lambda result:int(result[0][0][0])
result.sort(key=p,reverse=True)
b = result
for i in range(len(b)):
    for j in range(i,len(b)):
        if b[i][0][0]==b[j][0][0] and int(b[i][0][1])>int(b[j][0][1]):
                                          b[i],b[j] = b[j],b[i]
        elif b[i][0][0]!=b[j][0][0]:
            break
for i in range(k):
    print(tuple(b[i][1:]))
                                          
         

def flatten(i,j):
    r ={}
    for k,l in j.items():
        if type(l)!=dict:
            r[i+k]=l
    while(type(l)==dict):
        for m,n in l.items():
            r[i+k+m]=n
        break
    return(r)
d=eval(input())
r = dict()
for i,j in d.items():
    if type(j) is dict:
        r.update(flatten(i,j))
    else:
        r[i]=j
print(r)


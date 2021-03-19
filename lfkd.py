n=list(map(int,input().split()))
b=[]
for i in n:
        if i not in b:
                b.append(i)
print(b,sep="*")                                       

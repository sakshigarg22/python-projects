n = input(int())
m = 0
for i in range(n):
    l = list(map(int,input().split()))
    for i in l:
        if i.count(1)>1:
            m = m+1
        else:
            m
    print(m)
            

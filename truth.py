x,n =0,input(int())
while(n>0):
    a = list(map(int,input().split())).count(1)
    n = n-1
    if a>=2:
        x = x+1
print(x)
    
            

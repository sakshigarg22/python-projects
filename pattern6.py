h = int(input())
p = 1
e = 0
for i in range(1,h+1):
    print(" "*(2*h-i*2),end = " ")
    if i!=1:
        print(("*"*i)+(" "*(p))+("*"*i))
        e+=2
        p+=e
    else:
        print("*"*i)

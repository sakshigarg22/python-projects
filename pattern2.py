num = 4
for i in range(num+1):
    for j in range(num+1):
        if i==0 or i==3 or j==0 or j==3:
            print("*",end = " ")
        else :   
            print(end = " ")
    print()

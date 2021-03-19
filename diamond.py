for i in range(0,5):
    for k in range(0,5):
        if i+k==2 or k-i==2 or i-k==2 or i+k==6:
            print("*",end="")
        else:
            print(end=" ")
    print()        

def greatest(x,y):
    if x>y:
        small = y
    else:
        small = x
    for i in range(1,small+1):
        if (x%i == 0) and (y%i == 0):
            gcd = i
    return gcd
a = int(input("the first number :"))
b = int(input("the second number :"))
print(greatest(a,b))

def lower(x,y):
    if x>y:
        greatest = x
        min = y
    else:
        greatest = y
        min = x

    for i in range(1,greatest+1):
        if (x%i == 0) and (y%i == 0):
            
        
        return lcm
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print(lower(a,b))

def findLCM(a, b): 
  
    lar = max(a, b) 
    small = min(a, b) 
    i = lar 
    while(1) : 
        if (i % small == 0): 
            return i 
        i += lar 
      
# Driver Code 
a = 5
b = 7
print("LCM of " , a , " and ", s 
                  b , " is " ,  
      findLCM(a, b), sep = "") 

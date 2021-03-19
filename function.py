def subtract(a,b):
    if type(a) is [dict,set]:
        a.update(b)
        return (a-b)
    else:
        c = a-b
        return c
        
v = eval(input("enter the first number"))
u = eval(input("enter the second number"))
c = subtract(v,u)
print(c)


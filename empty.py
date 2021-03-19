v = 0
c = 0
v1 = 0
n = 0
w = 0
a = input()
for i in a:
    if i in ['a','e','i','o','u']:
        print(i)
        v = v+1
    elif i in ['A','E','I','O','U']:
        print(i)
        v1 = v1+1
    elif i.isalpha():
        print(i)
        c = c+1
    elif i.isnumeric():
        print(i)
        n = n+1
print(v,v1,c,w)
        

def fact(n):
    p = 1
    if n == 0:
        return p
    else:
        p = n*fact(n-1)
num = int(input())
out = fact(0)
print(out)

def fact(n):
    
    if n == 0:
        return 1
    else:
        p = n*fact(n-1)
        return p
num = int(input())
out = fact(0)
print(out)

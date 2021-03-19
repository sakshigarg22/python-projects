from math import factorial
t=map(int,input().split())
lst = []
for i in t:
    lst.append(str(factorial(i)))
print(','.join(lst))


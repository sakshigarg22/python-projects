import functools
def mul(x1,x2):
    return x1*x2  # set first 1*3 as a default
k = [1,3,4,6]
out = functools.reduce(mul,k)
print(out)  # 12*6

from functools import reduce
k = [1,3,4,6]
out = reduce(lambda x1,x2:x1*x2,k)
print(out)

def my_fun(x):  # x=v
    x += [2,5]
    print(x)
# immutable
v = 20
my_fun(v)
print(v)

def my_fun(x):
    x.clear()


    
#explaination
x1 = 1  # k[0]
x2 = 3  # k[1]
out = 3
#2
x1 = out  # 3
x2 = 4
out = 12
#3
x1 = out  #12
x2 = 6
out = 72

lst = [2,5,8,0,2,4,1]
lst.sort()
print(lst)


def sorted_or_not(k):
    # x = k.copy()
    # x.sort()
    # return x == k
    return k == sorted(k)

lst = [2,5,6,8,0,4,5,7]
out = sorted_or_not(lst)
print(out)

p = [1,2,3,4]
m = 0

    












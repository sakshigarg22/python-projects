# lambda function
def add(a,b):
    return "special category" if a+b >20 else "normal number"
l = add(1000,8)
print(l)

add = lambda a,b : 'special category' if a+b > 20 else 'normal number'
l = add(100,2)
print(l)

add = lambda a,b,c : 'special category' if a>20 else 'normal number'
l = add(10,8,6)
print(l)

cat = lambda *a: 'special number' if a > 20 else 'normal number'
l = cat(29,8,6)
print(l)
  
ls = [29,8,6]
out = list()
for i in range(len(ls)):
    if i > 20:
        cat(out.append("special number"))
    else:
        cat(out.append('normal number'))
print(ls)
print(out)






ls = [2,45,23,4,12]
out = map(lambda a: 'special number'if a > 20 else 'normal number',ls)
print(out)

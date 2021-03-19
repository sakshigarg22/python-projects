k = [85,8,5,45]
out =list(map(lambda x:x+2, k))
print(out)

k1 = [7,4,32,90,45]
out2 = list(filter(lambda x:x%2 ,k1))
print(out2)

k2 = [7,43,2,32,90,45]
odd = []
for i in range(len(k)):
    if i%2 :
        odd.append(i)
print(odd)

# example 2 sorting with surname alphabetically
k = ['ruchi gupta','rahul sharma','abhinav pandey','rishabh garg','saransh pathak'] 
k.sort(key = lambda x:x.split()[-1])
print(k)

#max()
k.sort(key = lambda x:sum(map(ord ,x)))
print(k)

s = ['hello','hi','ravi','class','abc xyz gd']
out1 =min(s,key = len)
out2 =max(s,key = len)
print(out1)
print(out2)

l = ['hello','Hzzz','abhinav','RAjan']
out = min(l, key = lambda t: sum(list(map(ord, t))))
print(out)

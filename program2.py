from functools import p
p
res = sorted(p, key = lst(lambda i, j: -1 
                if str(j) + str(i) < str(i) + str(j) else 1)) 
print ("The largest possible number : " + ''.join(map(str,res))) 

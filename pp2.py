from itertools import permutations
e = list(map(str,input().split()))
m = int(max(("".join(i) for i in permutations(str(i) for i in e))))
print("the largest possible number: " + str(m))        

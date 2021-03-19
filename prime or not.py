def prime_or_not(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    else:
        return True

lst = [2,4,6,7,24,67]
res = []
for n in lst:
    if prime_or_not(n):
        res.append(n)
print(res)

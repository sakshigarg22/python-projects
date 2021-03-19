def my_fun(*argv):
    print(argv)
my_fun(*range(255))

import random
lst = ['chanchal','bhavya','dheeraj','alok','lakshay']
out1 = random.choices(lst)
print(out1)

import random
ut = random.getrandbits(8)
                    
print(ut)

import random
lst = ['chanchal','bhavya','dheeraj','alok','lakshay']
out2 = random.sample(lst,k = 5)
print(out2)

print(random.triangular(1,20,15))

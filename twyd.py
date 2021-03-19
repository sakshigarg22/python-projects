import random
out = int(random.random()*10**6)
print(out)


import random
put = random.randrange(100000,999999)
print(put)

import random
for i in range(6):
    o = random.randint(0,9)
    print(o,end = "")

# choice()
h = [1,3,6,7,9,4,5,6,'hello']
pp = random.choice(h)
print(pp)

import random as r
sys_num = r.randint(0,100)
count = 0
while 1:
    count += 1
    num = int(input('enter the positive integer'))
    if num < sys_num:
        print('user guessed number is lower')
    elif num > sys_num:
        print('user guessed high value')
    else:
        print('right number with score count',count)
        break

lst = list(range(1,56))

while lst:
    input('enter the next person')
    print(r.choice(lst))

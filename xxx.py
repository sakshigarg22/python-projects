def showinfo(name,course = 'btech'):
    print(name ,course )
showinfo('sakshi','bca')
showinfo('sakshi')




import random
lst = [1,2,4,5]
print('original list : ' + str(lst))
for i in range(len(lst)-1,0,-1):
    j = random.randint(0,i+1)
    lst[i], lst[j] = lst[j], lst[i]
print('shuffle list: ' + str(lst))

def my_fun(ls):
    k = ls.copy()
    ls.clear()
    while k:
        x = random.choice(k)
        ls.append(x)
        k.remove(x)

lst = ['chanchal','bhavya','alok','ram']
print(lst)
my_fun(lst)
print(lst)


# seed()
random.seed(100)
h = random.random()
k = random.random()
print(h)
print(k)

def f(number):
    return number
print(f(5))

def func(message,num = 1):
    print(message*num)
func('welcome')
func('viewers',3)



def func(x = 1,y = 2):
    x = x+y
    y += 1
    print(x,y)
func(y = 2,x = 1)


num = 1
def func():
    global num
    num = num+3
    print(num)
func()
print(num)

def test(x = 1,y = 2):
    x = x+y
    y += 1
    print(x,y)
test(y = 2,x = 1)

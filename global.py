def my_fun():
    global a
    a = 10
    print(a)
a = 20
my_fun()
print(a)
 
def my_fun(argv):  # argv = k
    argv.append(2)
k = [7,8]
my_fun(k)
print(k)

def my_fun():
    def inner():
        k = 78
    def inner_non():
        nonlocal k
        k = 60
    def inner_global():
        global k
        k = 90
    k = 0
    inner()
    print(k)
    inner_non()
    print(k)
    inner_global()
    print(k)

k = 1
my_fun()
print(k)

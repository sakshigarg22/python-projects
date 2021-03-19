import time
f = open('abc.dat','w')


a = int(input('enter the first number '))
b = int(input('enter the second number '))

print('''

choices
1.add
2.subtact
3.div
4.multipy

''')

c = input('enter the choice')
if c == '1':
    res = a+b
    op = 'add'
elif c == '2':
    res = abs(a-b)
    op = 'subtract'
tt = time.asctime()
tmp = f'{a}\t{b}\t{res}\{op}\t{tt}'

f.write(tmp)
print(tmp)
f.close()




    









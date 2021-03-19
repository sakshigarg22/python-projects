##rule 1
##try:
##    pass
##except:
##    pass

try:
    int('ddsd')
except:
    print('error handled')


while 1:
    try:
        i = int(input())
        print(i)
        break
    except ValueError :
        print('not valid integer...try again')
    except EOF:
        print('please enter something')


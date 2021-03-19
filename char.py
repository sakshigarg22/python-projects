for _ in range(int(input())):
    
    e = input()
    a = ''
    for i in range(len(e)):
        if e[i].isdigit() :
            a+=e[i]
            if i+1<len(e) and not e[i+1].isdigit():
                a+=' '
    print(a if a else "no integers")

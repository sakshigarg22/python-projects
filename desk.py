for i in range(int(input())):
    a = list(map(str,input().split(".")))
    print(".".join(a[::-1]))

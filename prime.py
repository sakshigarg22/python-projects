        for _ in range(int(input())):
    s = input()
    c = 0
    for i in s:
        num = int(i)
        if num > 1:
            for i in range(2,num):
                if (num%i)==0:
                    break

                else:
                    c+=num
    print(c)

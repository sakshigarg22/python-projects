t = int(input())
i = 1
a,b,c = list(map(int,input().split()))
while(i<=t):
    i += 1
    if a+b+c==180:
        print("YES")
else:
    print("NO")

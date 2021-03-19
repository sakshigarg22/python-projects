n = int(input())
l = list(map(int,input().split()))
a = 0
for i in l:
    a = a^i
print(a)

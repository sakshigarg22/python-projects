str = input()
sub = input()
c = 0
for i in range(0,len(str)-len(sub)+1):
    if sub == str[0:3]:
        c = c+1
print(c)
        

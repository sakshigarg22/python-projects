def min_visible_bottles(d,n ):
    m = dict()
    ans = 0
    for i in range(n):
        m[d[i]] = m.get(d[i],0)+1
        ans = max(ans,m[d[i]])
    print('Minimum number of visible bottles are: ',ans)
n = int(input())
d = list(map(int,input().split(',')))
min_visible_bottles(d,n)



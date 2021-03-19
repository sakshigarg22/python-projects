m = dict()
arr = [1,2,3,3,4,5,4,6,4]
n = 9
ans = 0



for i in range(9):
	m[arr[i]] = m.get(arr[i],0)+1
	ans = max(ans,m[arr[i]])
	print(ans)
print(m)


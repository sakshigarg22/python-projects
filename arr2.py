def rearrange(arr,n):
    temp =n*[None]
    small,large = 0,n-1
    f = True
    for i in range(n):
        if f is True:
            temp[i] = arr[large]
            large -= 1

        else:
            temp[i] = arr[small]
            small += 1
        f = bool(1-f)
    for i in range(n):
        arr[i] = temp[i]
    return arr
arr = [1,2,3,4,5,6]
n = len(arr)
print("original array")
print(arr)
print("modified array")
print(rearrange(arr , n))

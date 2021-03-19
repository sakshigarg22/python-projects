def array_sum(arr,n):
    return sum(arr)

arr = list(map(int,input().split(' ')))
n = len(arr)
sum_of_array = array_sum(arr,n)
print(sum_of_array)

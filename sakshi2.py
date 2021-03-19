
lst = eval(input())
# string list
lst_new = list(map(str, lst))

# lst_new.sort(reverse=True)
# print(lst_new)
lst_new.sort(key=len)
print(lst_new)

lst_new.sort(reverse=True, key=lambda x:x[0])
print(lst_new)

out = ''.join(lst_new)
print(out)

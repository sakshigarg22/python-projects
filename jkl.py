s,d = input(),[]
[d.append(i) for i in s if i not in d]
print("".join(d))

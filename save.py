def outer(a,b):
    def inner():
        nonlocal a
        nonlocal b
        return(ord(a),ord(b))
    a1,b1 = inner()
    return(a1+b1)
print(outer('c','d'))

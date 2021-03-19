# open(filename,mode(permission))

# wwb: write only
#w+/wb+: write/read()

# r/rb: read only
# r+/rb+: read/write both


# a/ab; append write only
# a+/ab+: append both write and read



f = open('sample_file.txt', 'rb')
print('cursor location',f.tell())

data1 = f.read(5)  # read() is the file method to read the entire data from the current location

print('cursor location', f.tell())  # 5
data2 = f.read(5)
print('cursor location', f.tell())  # 10

data3 = f.read()

print('data1:----',data1)
print('data2:----',data2)
print('data2:----',data3)


f.close()

f = open('sample_file.txt', 'rb')
print('cursor location',f.tell())

data1 = f.read()  

print('cursor location', f.tell())  
data2 = f.read()
print('cursor location', f.tell())  

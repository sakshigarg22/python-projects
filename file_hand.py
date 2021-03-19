'''
standard input   input()
standard output   print()


file handling : reading and write operation with any file  
'''

f = open('xy.txt','w')
f.write('enter first number \n')
f.write('enter second number \n')
        
f.close()


# open(filename,mode(permission))

f = open('sample_file.txt', 'r')
data = f.read()    # read() is the file method to read the entire data of the file
print(data)
f.close()

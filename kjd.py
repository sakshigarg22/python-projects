##f = open('sample_file.txt', 'rb')
##data1 = f.read(10)
##print(data1)
##
##f.seek(2,0)
##
##data2 = f.read()
##print(data2)
##f.close()
# list of lines : list of lines

## next()
## iteration()


# readline()
##f = open('sample_file.txt', 'rb')
##ha = f.read(2)
##data1 = f.readlines() # read single line
##data2 = f.readline()
##print(data1)
##print(data2)
##
##f.close()
##
##read()
##readline()
##readlines()

# create file with student information

##f = open('info.dat','w')
##lst = ['riya sharme \n' ,'section o \n','roll number 20 \n', 'address GLA']
##if not f.closed:
##    print('file sucessfully closed', f.name)  # to print the name of file
##    f.writelines(lst)
##    f.close()
##    if f.closed:
##        print('file successfully saved',f.name)
##else:
##    print('file not opened')



    

##f = open('info.dat','rb')
##print(f)
##for line in f:
##     h = next(f)
##     print(line)
##
##f.close()


# r+/w+

with open('info.dat','r') as f:
     print(len(f.read().split()))



# r+/w+
#appendd mode
# edit mode r+/w+
## f = open('info.dat','a')
print(f.tell)





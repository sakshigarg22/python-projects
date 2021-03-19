HH = input()
MM = input()
for HH in range(0,23):
        if 0 < HH < 4 and 0<MM<59:
            print('Good Morning')
            
        elif 0 <= HH-12 <= 15 and 0<MM<59:
            print('Good Afternoon')
        
        elif 16 <= HH <= 20 and 0<MM<59:
            print('Good Evening')
        
        else :
            print('Good Night')
    

n = 5
for i in range(n):
    for j in range(i, n):           #so basically what we are doing is printing blank spaces in this loop
        print(' ', end='')          #and at the end of the blank spaces we are printing a "*"
    
    for j in range(i+1):
        print('*', end='')

    print()
num = 7
for line in range(1,num+1):
    for col in range(1,num+1):
        if line==1 or line==num or line == col or col+line == num+1 :
            print('*',end=' ')
        else:
            print(' ',end ='   ')
    print()

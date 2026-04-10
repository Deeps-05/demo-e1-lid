num=5
spaces=num//2+1
stars=1
for line in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for ast in range(1,stars+1):
        print('*',end=' ')
    print()
    if line<num//2+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
    

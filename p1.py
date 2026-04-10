num = 5
for line in range(num,0,-1):
    for space in range(1,line):
        print(' ',end = ' ')
    for col in range(num,line-1,-1):
        print(col,end=' ')
    print()

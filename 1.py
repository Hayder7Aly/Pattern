# for i in range(1,int(input('Please Enter The Number Of Rows : '))+1): print('*'*i)

user=int(input('PLEASE ENTER THE NUMBER OF ROWS : '))
for i in range(1,user+1):
    for j in range(1,user+1):
        if j<=i:
            print('*',end='')
        else:
            print(' ',end='')
    print()

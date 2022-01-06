user=int(input('PLEASE ENTER THE NUMBER OF ROWS : '))
for i in range(1,user+1):
    for j in range(user,0,-1):
        if i<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()


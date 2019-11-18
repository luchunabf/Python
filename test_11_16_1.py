a = 5
b = input('enter key:')
while int(b) != 5:
    if int(b) > 5:
        print('Too more!')
        b = input('enter key again:')
    else:
        print('Too Less!')
        b = input('enter key again:')
print('congratulations! key =')
print (a)
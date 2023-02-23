answ = 'yes'
while answ == 'yes':

    x = float(input('Type x: '))
    action = input('Type action: ')
    y = float(input('Type y: '))

    if action == '+':
        print(x + y)
    elif action == '-':
        print(x - y)
    elif action == '*':
        print(x * y)
    elif action == '/':
        if y == 0:
            print('Zero division!')
        else:
            print(x / y)
    else:
        print('Bad action')
    answ = input('Type "yes" to continue: ').lower()
    a = 1

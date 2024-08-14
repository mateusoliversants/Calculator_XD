while True:
    number1 = input('Enter a number: ')
    number2 = input('Enter another number: ')


    valid_numbers = None
    valid_operators = '+-*/'
    num1_float = 0
    num2_float = 0


    try:
        num1_float = float(number1)
        num2_float = float(number2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both numbers are not valid')
        continue


    operator = input('Enter an operator(+ - * /): ')
    if operator not in valid_operators:
        print('Invalid operator')
        continue
    if len(operator) > 1:
        print('Enter only one operator')
        continue


    print('===' * 3)
    print('Your account has been processed. Check out the result below:')
    if operator == '+':
        print(f'{number1} + {number2} =', num1_float + num2_float)
    elif operator == '-':
        print(f'{number1} - {number2} =', num1_float - num2_float)
    elif operator == '*':
        print(f'{number1} * {number2} =', num1_float * num2_float)
    elif operator == '/':
        print(f'{number1} / {number2} =', num1_float / num2_float)
    else:
        print('This should never happen wtfff')


    exit = input('Exit? [y]es: ').lower().startswith('y')
    if exit is True:
        break

print('Finished!')

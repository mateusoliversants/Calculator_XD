""" Calculadora com while """
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')


    numeros_validos = None
    operadores_validos = '+-*/'
    num1_float = 0
    num2_float = 0


    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos')
        continue


    operador = input('Digite um operador(+ - * /): ')
    if operador not in operadores_validos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue


    print('===' * 3)
    print('Sua conta foi realizada. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{numero1} + {numero2} =', num1_float + num2_float)
    elif operador == '-':
        print(f'{numero1} - {numero2} =', num1_float - num2_float)
    elif operador == '*':
        print(f'{numero1} * {numero2} =', num1_float * num2_float)
    elif operador == '/':
        print(f'{numero1} / {numero2} =', num1_float / num2_float)
    else:
        print('Isso nunca deveria acontecer wtfff')


    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break

print('Acabou XD')

numero = 0
tabuada = 1

print('--- Bem vindo a calculadora Python ---')

while True:
    operacao = int(input("""Ecolha uma opção do menu:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n9 - Sair da Calculadora"""))
    if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4 and operacao != 9:
        print('Digite uma opção valida')
        continue
    numero = 1
    if operacao == 9:
        print('Muito obrrigado por usar a caculado Python\n --- Fim do Programa ---')
        break
    while operacao == 1 and numero<11 and tabuada<11:
        print(f'{tabuada} + {numero} = {tabuada+numero}')
        numero += 1
        if numero == 11:
            numero = 1
            tabuada += 1
            print('\n')
    while operacao == 2 and numero<11 and tabuada<11:
        print(f'{tabuada} - {numero} = {tabuada-numero}')
        numero += 1
        if numero == 11:
            numero = 1
            tabuada += 1
        print('\n')
    while operacao == 3 and numero<11 and tabuada<11:
        print(f'{tabuada} * {numero} = {tabuada*numero}')
        numero += 1
        if numero == 11:
            numero = 1
            tabuada += 1
        print('\n')
    while operacao == 4 and numero<11 and tabuada<11:
        print(f'{tabuada} / {numero} = {tabuada/numero:.2f}')
        numero += 1
        if numero == 11:
            numero = 1
            tabuada += 1
        print('\n')

numero1 = int(input('Digite o primeiro número'))
numero2 = int(input('Digite o segundo número'))
operacao = 0
escolhaOperacao = int(input("""Escolha a operação desejada conforme opções abaixo\n 1 - soma\n 2 - subtração\n 3 - divisão\n 4 - multiplicação"""))
soma = numero1+numero2
subtracao = numero1-numero2
divisao = round(numero1/numero2)
multiplicacao = numero1*numero2


if (escolhaOperacao==1):
    print(f'O resultado da operação é {soma}')
if (escolhaOperacao==2):
    print(f'O resultado da operação é {subtracao}')
if (escolhaOperacao==3):
    print(f'O resultado da operação é {divisao}')
if (escolhaOperacao==4):
    print(f'O resultado da operação é {multiplicacao}')
if (escolhaOperacao>4):
    print('Você não escolheu um número válido para a operação. Reinicie o programa')

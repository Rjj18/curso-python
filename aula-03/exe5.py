lista = ['(',')']
fechado = 0
tamanho = len(lista)

while lista[-1] == ')' and len(lista)>0:
        lista.pop(-1)
        fechado = fechado + 1
        print('parenteses removido')
        if lista[-1] == '(' and fechado >= 1 and len(lista)>0:
            lista.pop(-1)
            fechado = fechado - 1
            print('parenteses removido')
        elif lista[-1] == '(' and fechado == 0 and len(lista)>0:
            lista.append (')')
            print('parenteses adicionado')
        elif len(lista) == 0 and fechado > 0:
            print('Erro')
            break
        else:
            print('tchau')

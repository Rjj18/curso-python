lista = [')', '(','(','(']
tamanho = len(lista)
fechado = 0


while True:
    if tamanho > 0 and lista[-1] == ')':
        lista.pop(-1)
        tamanho = len(lista)
        fechado+=1
        print('( removido')
        print(lista)
    elif tamanho > 0 and lista[-1] =='(' and fechado >=1:
        lista.pop(-1)
        tamanho = len(lista)
        fechado-=1
        print(') removido')
    elif tamanho > 0 and lista[-1] == '(' and fechado == 0:
        lista.append(')')
        tamanho = len(lista)
        print(') adicionado')
        print(lista)
    elif tamanho == 0 and fechado > 0:
        lista.append('(')
        print('( adicionado')
        tamanho = len(lista)
        print(lista)
    else:
        print('A lista está vazia')
        break

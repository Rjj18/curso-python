ultimoA = 10
filaA = list(range(1,ultimoA+1))
ultimoB = 10
filaB = list(range(1,ultimoB+1))

while True:
    print(f"\nExistem %d clientes na fila 1" %len(filaA))
    print("Fila atual:",filaA)
    print(f"\nExistem %d clientes na fila 2" %len(filaB))
    print("Fila atual:",filaB)
    print(" Digite A para atendimento da fila 1;\nDigite B para atendimento da fila 2;Digite F para atendimento na fila 1;\nDigite G para atendimento na fila 2;\nDigite S para sair")
    operacao = input(" Escolha a operação (A, B, F, G ou S:)")
    if operacao == "A":
        if (len(filaA))>0:
            atendido = filaA.pop(0)
            print("Clente %d da fila A atendido" % atendido)
        else:
            print("fila vazia")
    elif operacao == "B":
        if (len(filaB))>0:
            atendido = filaB.pop(0)
            print("Clente %d da fila B atendido" % atendido)
        else:
            print("fila vazia")
    elif operacao == "F":
        ultimoA+=1
        filaA.append(ultimoA)
    elif operacao == "G":
        ultimoB+=1
        filaB.append(ultimoB)
    elif operacao == "S":
        print("programa encerrado")
        break
    else:
        print("Operação invalida")

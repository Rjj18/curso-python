lista1 = [1,2,3,5]
lista2 = [4,5,6,3]

for i in lista1:
    print(i)

for i in lista2:
    print(i)

lista3 = set(lista1+lista2)

print("Abaixo segue a junção das duas listas")

for i in lista3:
    print(i)

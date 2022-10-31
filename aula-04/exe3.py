A = set([28,10,22,7,4,9,37])
B = set([22,87,84,2,35,37,9])
C = A-B
D = B-A

##A)os valores comuns às duas listas
print("Resposta A")
print(A|B)
##B)os valores que só existem na primeira lista
print("Resposta B")
print(A-B)
##C) os valores que existem apenas na segunda
print("Resposta C")
print(B-A)
##D)uma lista com os valores não repetidos nas duas listas
print("Resposta D")
print(C|D)
##E) a primeira lista sem os elementos repetidos na segunda lista
print("Resposta E")
print(A-B)

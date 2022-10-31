## Exercicio 02

la = "AAACTBF"
lb = "CTB" 
resultado =""
tamanho = 0 

for letra in la:
  if letra in lb and letra not in resultado:
    resultado += letra
    tamanho = len(resultado)

if tamanho > 0:
  print(resultado)
else:
  print("erro")

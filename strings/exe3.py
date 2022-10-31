##exercicio 03

la = "CTA"
lb = "ABC" 
resultado =""

for letra in la:
  if letra not in lb and letra not in resultado:
    resultado += letra

for letra in lb:
    if letra not in la and letra not in resultado:
      resultado += letra

print(resultado)

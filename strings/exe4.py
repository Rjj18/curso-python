## exercicio 4

l = "TTAAC"
posicao_t = 0 ## Variavel que determina a posicao de contagem da letra
contagem_t = 0 ## Variavel que determina quantas vezes a letra apareceu
posicao_a = 0 ##
contagem_a = 0 ##
posicao_c = 0 ##
contagem_c = 0 ##


while posicao_t > -1:
  posicao_t = l.find("T", posicao_t)
  if posicao_t >= 0:
    posicao_t +=1
    contagem_t +=1

while posicao_a > -1:
  posicao_a = l.find("A", posicao_a)
  if posicao_a >= 0:
    posicao_a +=1
    contagem_a +=1

while posicao_c > -1:
  posicao_c = l.find("C", posicao_c)
  if posicao_c >= 0:
    posicao_c +=1
    contagem_c +=1

print(f"Na string {l}\nT aparece {contagem_t} vezes\nA aparece {contagem_a} vezes e\nC aparece {contagem_c} vez")

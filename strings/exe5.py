##exercicio 05

palavra = input("Digite a palavra secreta: ").lower().strip()
for s in range(100):
  print()
digitadas = []
acertos = []
erros = 0
while True:
  senha=""
  for letra in palavra:
    senha += letra if letra in acertos else "."
  print(f"{senha} <- palavra secreta")
  if senha == palavra:
    print("Você acertou")
    break
  tentativa = input("\nDigite uma letra: ").lower().strip()
  if tentativa in digitadas:
    print("Você já tentou essa letra!")
    continue
  else:
    digitadas += tentativa
    if tentativa in palavra:
      acertos += tentativa
    else:
      erros += 1
      print("Você errou")
  print("X===:=\nX    :    ")
  print("X    O " if erros >=1 else "X")
  linha2 =""
  if erros == 2:
    linha2 = "   |   "
  elif erros == 3:
    linha2 = "  \|   "
  elif erros >= 4:
    linha2 = "  \|/   "
  print(f"X{linha2}")
  if erros >= 5:
    linha3 = "   |   "
##print(f"X{linha3}")
  linha4 = ""
  if erros == 6:
    linha4 += "  _/   "
  elif erros >= 7:
    linha4 = "  _/ \_ "
  print("X\n==============")
  if erros == 7:
    print(f"Enforcado\n A palavra secreta era {palavra}")
    break

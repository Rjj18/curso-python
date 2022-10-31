estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50]}
total = 0

while True:
    produto = input('Digite o nome do produto ou fim para terminar')
    if produto == "fim":
        print(f"O total a pagar é de R$ {total:5.2f}")
        print("Muito obrigado")
        break
    while produto in estoque:
        quantidade = int(input("digite a quantidade"))
        preco = estoque[produto][1]
        venda = preco * quantidade
        print(f" O custo do {produto} é de R$ {preco:6.2f}")
        estoque[produto][0] -= quantidade
        total += venda
        break
    else:
        print("Produto não existe")
        continue
        

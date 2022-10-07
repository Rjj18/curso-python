prod1 = 0.50
prod2 = 1
prod3 = 4
prod5 = 7
prod9 = 8
totalCompras = 0
boasVindas = 'Bem vindo ao Supermercado Python'

print(f"""{boasVindas:-^.100}\n   Boas Compras!""")
while True:
    produto = int(input('digite o codigo do produto'))
    if produto != 1 and produto != 2 and produto != 3 and produto != 5 and produto != 9 and produto != 0:
        print('Digite um código de produto válido')
        continue     
    elif produto == 1:
        qdeprod = int(input('digite a quantidade de produtos'))
        totalCompras = (qdeprod*prod1)+totalCompras
    elif produto == 2:
        qdeprod = int(input('digite a quantidade de produtos'))
        totalCompras = (qdeprod*prod2)+totalCompras
    elif produto == 3:
        qdeprod = int(input('digite a quantidade de produtos'))
        totalCompras = (qdeprod*prod3)+totalCompras
    elif produto == 5:
        qdeprod = int(input('digite a quantidade de produtos'))
        totalCompras = (qdeprod*prod5)+totalCompras
    elif produto == 9:
        qdeprod = int(input('digite a quantidade de produtos'))
        totalCompras = (qdeprod*prod9)+totalCompras
    elif produto == 0:
        print(f"""O valor total da sua compra é de R${totalCompras:.2f}\nMuito pelas compras!\n   Volte Sempre!\n--- Fim do Programa ---""")
        break
    
    
    

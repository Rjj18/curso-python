residencial500 = 0.40
residencialAcima500 = 0.65
comercial500 = 0.55
comercialAcima500 = 0.60 
industrial500 = 0.55
industrialAcima500 = 0.60
tipoInstalacao = input("""Informe o tipo da instalação conforme opções abaixo\n r para residencial\n c para comercial\n i para industrial""")
consumoMensal = float(input('Digite seu consumo mensal em KWh'))

if (tipoInstalacao == "i" and consumoMensal<=1000):
    print(f'O valor da sua fatura é de R$ {consumoMensal*industrial500:.2f}')
elif (tipoInstalacao == "i" and consumoMensal>1000):
    print(f'Seu consumo mensal foi de R$ {consumoMensal*industrial500:.2f}')
elif (tipoInstalacao == "c" and consumoMensal<=1000):
    print(f'Seu consumo mensal foi de R$ {consumoMensal*industrial500:.2f}')
elif (tipoInstalacao == "c" and consumoMensal>1000):
    print(f'O valor da sua fatura é de R$ {consumoMensal*industrial500:.2f}')
elif (tipoInstalacao == "r" and consumoMensal<=500):
    print(f'O valor da sua fatura é de R$ {consumoMensal*industrial500:.2f}')
elif (tipoInstalacao == "r" and consumoMensal>500):
    print(f'O valor da sua fatura é de R$ {consumoMensal*industrial500:.2f}')
else:
    print('Você digitou dados inválidos. Favor reiniciar o programa')

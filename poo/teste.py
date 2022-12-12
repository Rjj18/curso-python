from cliente import Cliente
from banco import Banco
from contas import Conta

roger = Cliente("Roger", "123456")
aline = Cliente("Aline", "632141")
heitor = Cliente("Heitor", "987456")

conta1 = Conta(roger, 10)

conta1.resumo()
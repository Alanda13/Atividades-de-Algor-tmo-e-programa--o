#ENTRADA#
x = int(input("Digite um número inteiro de minutos: "))

#PROCESSAMENTO#
dias = x // 1440 #1 dia tem 1440 minutos
minutos_restantes = x % 1440

#SAÍDA#
print(f"{x} minutos tem {dias} dias e {minutos_restantes} minutos.")

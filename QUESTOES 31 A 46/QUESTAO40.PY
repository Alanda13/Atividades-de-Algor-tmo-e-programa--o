print("---Quantidade de dinheiro gasto por um fumante---")
#ENTRADA#
x = float(input("Digite a quantidade de anos que você fuma: "))
y = float(input("Digite a quantidade de cigarros fumados por dia: "))
z = float(input("Digite o preço de uma carteira: "))

#PROCESSAMENTO#
cigarros_ano = y * 365
carteiras_ano = cigarros_ano /20
gasto_ano = carteiras_ano * z
gasto_total = gasto_ano * x

#SAÍDA#
print(f"Você gastou {gasto_total:.2f} reais sendo fumante.")

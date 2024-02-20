#ENTRADA#
valor = float(input("Digite um valor em metros: "))

#PROCESSAMENTO#
valor_km = valor // 1000
valor_m = valor % 1000
#SAÍDA#
print(f"O valor {valor} metros corresponde a {valor_km} km e {valor_m} metros ")
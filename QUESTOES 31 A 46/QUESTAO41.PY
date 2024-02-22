#ENTRADA#
custo_fabrica = float(input("Digite o preço do custo de fábrica do carro: "))

#PROCESSAMENTO#
porc_dist = (28/100) * custo_fabrica
porc_impost = (45/100) * custo_fabrica
custo_consum = custo_fabrica + porc_dist + porc_impost

#SAÍDA#
print(f"O valor de custo ao consumidor vai ser no total {custo_consum:.2f} reais")
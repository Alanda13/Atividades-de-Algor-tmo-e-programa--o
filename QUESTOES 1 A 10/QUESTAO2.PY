#Entrada#
horas = float(input("Digite um valor em horas: "))
minutos = float(input("Digite um valor em minutos: "))

#Processamento#
horas_em_min = horas * 60
valor_em_min = horas_em_min + minutos

#Saída#
print(f"O valor digitado equivale a {valor_em_min} minutos. ")
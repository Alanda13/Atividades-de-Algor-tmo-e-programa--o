#ENTRADA#
dias = int(input("Digite a quantidade de dias: "))

#PROCESSAMENTO#
semana = dias // 7
restante_dias = dias % 7

#SAÍDA#
print(f"{dias} dias corresponde a {semana} semanas e {restante_dias} dias")
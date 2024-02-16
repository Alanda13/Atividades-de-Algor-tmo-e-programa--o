#ENTRADA#
numero = int(input("Digite um número inteiro de horas: "))

#PROCESSAMENTO#
#Uma semana tem 168 horas#
semana = numero // 168
restante_horas = numero % 168
#Um dia tem 24 horas#
dias = restante_horas // 24
horas = restante_horas % 24

#SAÍDA#
print(f"{numero} horas tem {semana} semanas, {dias} dias e {horas} horas.")
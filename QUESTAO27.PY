#ENTRADA#
numero = int(input("Digite um número inteiro em segundos: "))

#PROCESSAMENTO#
horas = numero // 3600
segundos = numero % 3600
minutos = segundos // 60
segundos_total = segundos % 60

#SAÍDA#
print(f"{numero} segundos é equivalente a {horas} horas, {minutos} minutos e {segundos_total} segundos.")
#ENTRADA#
min = float(input("Digite um valor em minutos: "))

#PROCESSAMENTO#
horas = min // 60
minut = min % 60
#SAÍDA#
print(f"O seu valor em minutos corresponde a {horas} hora(s) e {minut} minuto(s)")
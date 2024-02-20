#ENTRADA#
velocidade_km = float(input("Digite uma velocidade em km/h:  "))
#PROCESSAMENTO#
velocidade_ms = velocidade_km / 3.6
#SAÍDA#
print(f"Sua velocidade {velocidade_km} km/h equivale a {velocidade_ms:.2f} em m/s")

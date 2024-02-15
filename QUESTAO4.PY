#ENTRADA#
dolar = float(input("Digite a cotação do dólar: "))
valor_dolar = float(input("Digite um valor em dólar: "))

#PROCESSAMENTO
valor_real = valor_dolar * dolar

#SAÍDA##
print(f"O valor {valor_dolar} em dolar equivale a {valor_real:.2f} em reais.")
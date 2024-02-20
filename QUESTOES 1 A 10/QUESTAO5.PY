#ENTRADA#
num = int(input("Digite um número inteiro de 3 dígitos: "))

#PROCESSAMENTO#
centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10
soma_elementos = centena + dezena + unidade
#SAÍDA#
print(f"A soma dos elementos é igual a: {soma_elementos}")

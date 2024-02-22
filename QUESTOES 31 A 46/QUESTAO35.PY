#ENTRADA#
numero = int(input("Digite um número inteiro de 4 dígitos: "))

#PROCESSAMENTO#
milhar = numero // 1000
centena = numero % 1000 // 100
dezena = numero % 100 // 10
unidade = numero % 10

soma = milhar + centena + dezena + unidade

#SAÍDA#
print(f"A soma dos elementos que compõem o número {numero} é igual a {milhar} + {centena} + {dezena} + {unidade} = {soma}")


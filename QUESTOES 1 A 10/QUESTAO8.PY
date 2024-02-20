#ENTRADA#
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

#PROCESSAMENTO#
soma = num1 + num2
subtracao = num1 - num2
divisao = soma / subtracao

#SAÍDA#
print(f"A soma dos dois números é igual a: {soma}")
print(f"A subtração dos dois números é igual a: {subtracao}")
print(f"A divisão da soma pela subtração dos dois números é igual a {divisao:.2f}")
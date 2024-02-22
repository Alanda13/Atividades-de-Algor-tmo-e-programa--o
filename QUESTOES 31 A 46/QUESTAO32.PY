#ENTRADA#
num = int(input("Digite um número inteiro de 3 digitos: "))

#PROCESSAMENTO#
inverso = int(str(num)[::-1])
diferenca = num - inverso

#SAÍDA#
print(f'A diferença entre {num} e seu inverso {inverso} é igual a : {diferenca}.')
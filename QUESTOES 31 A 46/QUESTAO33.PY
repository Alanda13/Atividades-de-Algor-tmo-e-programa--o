#ENTRADA#
num = int(input("Digite um numero inteiro de 3 digitos: "))

#PROCESSAMENTO#
inverso = int(str(num)[::-1]) 
soma = num + inverso

#SAÍDA#
print(f'A soma de {num} com o seu inverso {inverso} é igual a {soma}.')
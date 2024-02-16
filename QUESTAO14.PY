#ENTRADA#
nota1 = float(input("Digite a nota 1: "))
peso1 = float(input("Digite o peso da nota 1: "))
nota2 = float(input("Digite a nota 2: "))
peso2 = float(input("Digite o peso da nota 2: "))
nota3 = float(input("Digite a nota 3: "))
peso3 = float(input("Digite o peso da nota 3: "))

#PROCESSAMENTO#
media_ponderada = ((nota1*peso1) + (nota2*peso2) + (nota3*peso3)) / (peso1 + peso2 + peso3)

#SAÍDA#
print(f"A média ponderada das notas é igual a {media_ponderada:.2f}")

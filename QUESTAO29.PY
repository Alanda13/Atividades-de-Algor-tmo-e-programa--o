#ENTRADA#
numero = int(input("Digite um número inteiro de meses: "))

#PROCESSAMENTO#
ano = numero // 12  #1 ano tem 12 meses#
restante_meses = numero % 12

#SAÍDA#
print(f"{numero} meses tem {ano} anos e {restante_meses} meses.")

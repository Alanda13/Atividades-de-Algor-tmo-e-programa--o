#ENTRADA#
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

#PROCESSAMENTO#
idade_em_dias = (anos * 365) + (meses * 30) + dias

#SAÍDA#
print(f"A idade em dias é igual a: {idade_em_dias}.")
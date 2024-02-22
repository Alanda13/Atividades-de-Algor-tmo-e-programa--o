#ENTRADA#
idade = int(input("Digite a sua idade em dias: "))

#PROCESSAMENTO#
anos = idade // 365
meses = idade % 365 // 30
dias = (idade % 365) % 30

#SAÍDA#
print(f"A idade em dias {idade} é equivalente a {anos} anos, {meses} meses e {dias} dias.")
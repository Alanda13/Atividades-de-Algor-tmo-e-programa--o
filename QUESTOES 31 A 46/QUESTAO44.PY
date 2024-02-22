#ENTRADA#
latao = float(input("Digite a quantidade de latão em kg: "))

#PROCESSAMENTO#
cobre = (70 / 100) * latao
zinco = (30 / 100) * latao

#SAÍDA#
print(f"Para se obter {latao} kg de latão, é necessário {cobre} kg de cobre e {zinco} kg de zinco.")
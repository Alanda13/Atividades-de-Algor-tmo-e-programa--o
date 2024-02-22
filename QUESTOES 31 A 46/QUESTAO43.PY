#ENTRADA#
a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))
d = float(input("Digite um valor: "))
e = float(input("Digite um valor: "))
f = float(input("Digite um valor: "))

#PROCESSAMENTO#
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

#SAÍDA#
print(f"Os valores de x e y são igual a {x} e {y}.")
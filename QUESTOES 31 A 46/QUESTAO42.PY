import math
#ENTRADA#
x1 = float(input("Digite o x1 do ponto 1: "))
y1 = float(input("Digite o y1 do ponto 1: "))
x2 = float(input("Digite o x1 do ponto 2: "))
y2 = float(input("Digite o y1 do ponto 2: "))

#PROCESSAMENTO#
d = math.sqrt((x2 - x1)** 2 + (y2 - y1)**2 ) 

#SAÍDA#
print(f"A distância entre o ponto 1 ({x1} , {y1}) e o ponto 2 ({x2} , {y2}) é igual a: {d:.2f}")

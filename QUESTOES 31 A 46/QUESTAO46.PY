#ENTRADA#
mercadoria = float(input("Digite o valor da mercadoria: "))

#PROCESSAMENTO#
prestacao = mercadoria // 3
entrada = mercadoria - (prestacao * 2)

#SAÍDA#
print(f"O valor da entrada será de {entrada} reais e das duas prestações serão de {prestacao} reais cada.")

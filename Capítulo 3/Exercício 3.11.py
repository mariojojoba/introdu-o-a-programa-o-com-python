# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar. 

preço = float(input("Digite o valor da mercadoria: "))
desconto = int(input("Digite o porcentual de desconto: "))

n_preço = preço - (preço * desconto / 100)

print(f"O porcentual de desconto é {desconto}%")
print("O valor a ser pago é %5.2f" % n_preço)
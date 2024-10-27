# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.

salário = float(input("Digite seu salário atual: "))
aumento = int(input("Digite a porcentagem do aumento: "))

novo_salário = salário + (salário * aumento /100)

print(f"Você teve um aumento de {aumento}%")
print("Seu salário atual é R$%5.2f" % novo_salário)
# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salário = float(input("Insira o valor do seu salário: "))

if salário > 1250:
    salário = salário + (salário * 0.10)
else:
    salário = salário + (salário * 0.15)

print("Seu novo salário é R$%.2f" % salário)
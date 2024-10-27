# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Digite o valor da casa: "))
salário = float(input("Digite seu salário: "))
quantidade_anos = int(input("Digite quantos anos deseja pagar: "))

prestações = (valor_casa / (quantidade_anos * 12))

if prestações > salário * 0.30:
    print("Não aprovado.")
else:
    print("As prestações mensais ficam por %.2f durante %d meses." % (prestações, quantidade_anos*12) )



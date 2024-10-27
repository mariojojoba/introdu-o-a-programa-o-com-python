# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir.

kwh_consumidos = float(input("Digite a quantidade de kWh consumidas: "))
instalação = input("Digite seu tipo de instalação: (R) - Residência | (I) Indústrias | (C) Comércios").upper()

a = 0

if instalação == "R":
    if kwh_consumidos <= 500:
       a = kwh_consumidos * 0.40
    else:
       a = kwh_consumidos * 0.65
elif instalação == "I":
    if kwh_consumidos <= 1000:
       a = kwh_consumidos * 0.55
    else:
       a = kwh_consumidos * 0.60
elif instalação == "C":
    if kwh_consumidos <= 5000:
       a = kwh_consumidos * 0.55
    else:
       a = kwh_consumidos * 0.60
else:
    print("Instalação selecionada não é válida.")

if a > 0:
    print("Você deve um total de: R$%.2f" % a)
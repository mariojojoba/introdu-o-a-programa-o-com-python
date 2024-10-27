# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input("Escreva um valor em metros: "))
conversor = metros * 10**3

print("Seu valor convertido para milimetros é: %6.2f" % conversor)
# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

c_dias = dias * 24 * 3600
c_horas = horas * 3600
c_minutos = minutos * 60

conversão = c_dias + c_horas + c_minutos + segundos

print("Seu valor convertido em segundos é igual a %d" % conversão)
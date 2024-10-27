# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distância = float(input("Digite a distância desejada: "))
velocidade = int(input("Digite a velocidade média esperada: "))

tempo = distância / velocidade

print("O tempo de viagem é mais ou menos %5.2fH" % tempo)
# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distância = float(input("Digite a distância que deseja percorrer (em KM): "))

if distância <= 200: 
    a = distância * 0.50
    print("A viagem irá custar: $%.2f" % a)
else:
    a = distância * 0.45
    print("A viagem irá custar: R$%.2f" % a)
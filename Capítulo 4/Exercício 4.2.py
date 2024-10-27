# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h. 

velocidade = float(input("Qual a velocidade do usuário (KM): "))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f"Você está acima da velocidade, e foi multado em R${multa:.2f}")
else:
    print("Você está conforme a lei.")
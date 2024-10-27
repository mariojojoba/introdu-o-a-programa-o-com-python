# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km_percorridos = float(input("Digite o valor de kilometros percorridos (em KM): "))
dias = int(input("Digite o valor de dias alugados: "))

km_percorridos = km_percorridos * 0.15
dias = dias * 60

soma = km_percorridos + dias

print("O valor a ser pago é de R$%.2f" % soma)

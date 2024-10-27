# Modifique o programa da listagem 2.11, de forma que ele calcule um aumento de 15% para um salário de R$ 750.

salario = 750 # Salário.
aumento = 0.15 # Para não ter que fazer a fórmula "x * 15 / 100", simplificamos para um valor decimal.

print(salario + (salario * aumento)) # Primeiro é feita o cálculo da porcentagem, e depois é feita a soma dessa porcentagem com o valor
# do salário.

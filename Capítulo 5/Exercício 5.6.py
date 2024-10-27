# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

número = int(input("Digite o número que deseja ver a tabuada de multiplicação: "))

contador = 1

while contador <= 10:
    print("%d x %d = %d" % (número, contador, número * contador))
    contador += 1
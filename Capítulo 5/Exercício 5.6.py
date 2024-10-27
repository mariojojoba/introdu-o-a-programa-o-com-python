# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

número = int(input("Digite o número que deseja ver a tabuada de multiplicação: ")) #  Crio a variável que vai ser o número a ser multiplicado.

contador = 1 # Contador, que também vai ser usado como multiplicador da variável "número".

while contador <= 10: # Laço de repetição.
    print("%d x %d = %d" % (número, contador, número * contador)) # Uso os marcadores para melhorar a visualização do cálculo.
    contador += 1 # Uso o "Operador de Incrementação (+=)" que já adiciona "+1" a variável "contador".
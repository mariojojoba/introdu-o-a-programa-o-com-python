# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = int(input("Digite o último número da contagem: ")) # Variável que indica até que número o comando while irá exibir.
x = 1 # Contador.

while x <= fim: # Laço de repetição.
    if x % 2 != 0: # Se "x" for diferente de zero, exiba no terminal o valor de "x".
        print(x)
    x = x + 1 # Se não, ele só soma mais um na variável "x".

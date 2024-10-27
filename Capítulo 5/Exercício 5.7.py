# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

# Mesma coisa do exercício anterior, com a diferença que você escolhe o começo e o final da tabuada.

tabuada = int(input("Digite o número da tabuada que deseja visualizar: "))
contador = int(input("Digite de onde quer que a tabuada comece: "))
final = int(input("Digite onde você quer que a tabuada termine: "))

while contador <= final:
    print("%d x %d = %d" % (tabuada, contador, tabuada * contador))
    contador += 1
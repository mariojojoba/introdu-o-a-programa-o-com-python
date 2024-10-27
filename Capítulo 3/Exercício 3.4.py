# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. 
# Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

salário = float(input("Digite seu salário: ")) # Aqui usamos "float" antes do input para transformar uma entrada "string" em uma vari-
# ável "float", pense como se fosse uma conversão.
idade = int(input("Digite sua idade: ")) # E aqui usamos "int" tem quase a mesma função, só que ao invés de transformar em uma variável
# float, transformas em uma variável de valor inteiro.

makeTheL = salário > 1200 and idade > 18 # Cria-se uma variável lógica, que armazena um valor "True" ou "False", dependendo se o que 
# está dentro dela for atendida.

if makeTheL is True: # Se a variável for verdadeira o comando abaixo é exibido.
    print("Se vai pagar imposto paisão, se fez o L!")
else: # Se não exibe-se o comando abaixo.
    print("Você deu sorte, dessa vez você não precisa fazer o L...")
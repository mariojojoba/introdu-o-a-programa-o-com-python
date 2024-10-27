# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
operação = input("Qual operação você deseja realizar: (+): Soma; (-): Subtração; (*): Multiplicação; (/): Divisão.")

if operação == "+":
    print(a + b)

elif operação == "-":
    print(a - b)

elif operação == "*":
    print(a * b)

elif operação == "/" and b != 0:
    print (a / b)

else:
    print("Operação inválida.")
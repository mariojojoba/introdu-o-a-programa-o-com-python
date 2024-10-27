# Escreva um programa que leia três números e que imprima o maior e o menor.

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = int(input("Digite mais um número inteiro: "))

print("O maior número é: ")
if a >= b:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)

print("O menor número é: ")
if a <= b:
    print(a)
elif b <= c:
    print(b)
else:
    print(c)
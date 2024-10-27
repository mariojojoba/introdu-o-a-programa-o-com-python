# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7. 
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: 
# matéria1, matéria2 e matéria3.

matéria1 = float(input("Digite sua primeira nota: "))
matéria2 = float(input("Digite sua segunda nota: "))
matéria3 = float(input("Digite sua terceira nota: "))

situação = matéria1 and matéria2 and matéria3 > 7

if situação is True:
    print("Se foi aprovado lindão, agora é só correr pro abraço.")
else: 
    print("É paizão, não foi dessa vez, te vejo nas férias.")
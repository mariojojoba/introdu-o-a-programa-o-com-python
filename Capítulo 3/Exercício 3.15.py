# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. 
# Exiba o total em dias.

cigarros_dia = int(input("Digite quantos cigarros você fuma por dia: "))
anos_fumados = int(input("Digite quantos anos você fuma: "))

# Total de cigarros fumados
total_cigarros = cigarros_dia * 365 * anos_fumados

# Tempo perdido em minutos
tempo_perdido_minutos = total_cigarros * 10

# Convertendo minutos para dias
lost_time = tempo_perdido_minutos / 1440

print("Você perdeu um total de %d dias pelo fumo" % lost_time)
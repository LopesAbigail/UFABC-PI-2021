import math

horario_entrada = input()
horario_saida = input()

horario_entrada = horario_entrada.split(":")
horario_saida = horario_saida.split(":")

entrada_horas = int(horario_entrada[0])
entrada_minutos = int(horario_entrada[1])
saida_horas = int(horario_saida[0])
saida_minutos = int(horario_saida[1])

# if entrada_minutos > 0 and (saida_horas - entrada_horas) < 1:
#     entrada_horas += 1

# if saida_minutos > 0:
#     saida_horas += 1
#     saida_minutos = 0

entrada_total_horas = entrada_horas + entrada_minutos/60
saida_total_horas = saida_horas + saida_minutos/60

taxa_estadia = 0
estadia_horas = int(math.ceil(saida_total_horas - entrada_total_horas))
#estadia_horas = int(math.ceil(estadia_minutos/60))
hora = 0

if estadia_horas >= 15:
    while hora <= estadia_horas:
        hora += 1
        if hora >= 1:
            taxa_estadia += 5
        if hora >= 2:
            taxa_estadia += 3
        if hora >= 3:
            taxa_estadia += 3
        if hora >= 4:
            taxa_estadia += 3
        if hora >= 5:
            taxa_estadia += 2
print("R$ %.2f" % taxa_estadia)


# Algoritmo parquimetro

# Receber string com horario de entrada
# Receber string com horario de saida
# Separar string horario de entrada em hora e minuto
# Separar string horario de saida em hora e minuto

# Descobrir o total de minutos no horario de entrada (multiplicar horas por 60 e somar com minutos)
# Descobrir o total de minutos no horario de saida (multiplicar horas por 60 e somar com minutos)

# verificar o total de minutos de estadia (estadia_minutos = totalminutossaida - totalminutosentrada)

# se estadia_minutos < 15: taxa = 0
# se estadia_minutos = 60: taxa = 5
# se 120 <= estadia_minutos <= 240: taxa = 3*(estadia_minutos/60)
# se 240 > estadia_minutos >= 300: taxa = 2*(estadia_minutos/60)

# retornar a taxa no formato: R$ 00.00


horario_entrada = input()
horario_saida = input()

horario_entrada = horario_entrada.split(":")
horario_saida = horario_saida.split(":")

entrada_horas = int(horario_entrada[0])
entrada_minutos = int(horario_entrada[1])
saida_horas = int(horario_saida[0])
saida_minutos = int(horario_saida[1])

if entrada_minutos > 0:
    entrada_horas += 1

if saida_minutos > 0:
    saida_horas += 1
    saida_minutos = 0

entrada_total_horas = (entrada_horas*60) + entrada_minutos
saida_total_horas = (saida_horas*60) + saida_minutos

taxa_estadia = 0
estadia_horas = saida_total_horas - entrada_total_horas
estadia_horas = int(math.ceil(estadia_horas/60))
if estadia_horas >= 15:
    for hora in range(1, estadia_horas+1):
        if hora == 1:
            taxa_estadia += 5
        if hora == 2:
            taxa_estadia += 3
        if hora == 3:
            taxa_estadia += 3
        if hora == 4:
            taxa_estadia += 3
        if hora >= 5:
            taxa_estadia += 2
print("R$ %.2f" % taxa_estadia)

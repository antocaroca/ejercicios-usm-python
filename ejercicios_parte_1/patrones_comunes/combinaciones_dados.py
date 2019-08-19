#   Contar combinaciones de dados

k = int(input('Ingrese el puntaje: '))

combinaciones = 0

for i in range(1, 7):
    for j in range(1, 7):
        # print(f"i: {i} --- j: {j}")
        if i + j == k:
            combinaciones += 1
print(f"Hay {combinaciones} combinaciones para obtener {k}.")
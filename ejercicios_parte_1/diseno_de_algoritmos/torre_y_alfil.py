#   Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de una torre,
#  e indique cuál pieza captura a la otra:

fila_alfil = int(input('Fila Alfil: '))
columna_alfil = int(input('Columna Alfil: '))


# i = eje x de alfil
# y = eje y de alfil
i = fila_alfil   
y = i-1
while i <= 8: # suma hasta 8
    print(i, y)
    i += 1
    y += 1

i = i-1
y = 8

while i >= 1:    # resta hasta 1
    i -= 1
    y -= 1
    if y == 0:
        break
    print(i, y+1)

i = 1
while i <= fila_alfil: # suma hasta fila_alfil
    i += 1
    y += 1
    if i > fila_alfil:
        break
    print(i, y)

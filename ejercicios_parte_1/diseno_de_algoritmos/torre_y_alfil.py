#   Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de una torre,
#  e indique cuál pieza captura a la otra:

fila_alfil = int(input('Fila Alfil: '))
columna_alfil = int(input('Columna Alfil: '))

fila_torre = int(input('Fila torre: '))
columna_torre = int(input('Columna torre: '))

alfil = 0
torre = 0

# torre gana
if columna_torre == columna_alfil or fila_torre == fila_alfil:
  torre += 1

# alfil gana
if abs(fila_alfil - fila_torre) == abs(columna_alfil - columna_torre):
  alfil += 1

# contadores alfil y torre. El mayor a 0 gana
if alfil > 0:
    print('Alfil captura')
elif torre > 0:
    print('Torre captura')
else:
    print('ninguna captura')  

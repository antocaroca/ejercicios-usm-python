#   Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de una torre,
#  e indique cuál pieza captura a la otra:

fila_alfil = int(input('Fila Alfil: '))
columna_alfil = int(input('Columna Alfil: '))

fila_torre = int(input('Fila torre: '))
columna_torre = int(input('Columna torre: '))

x = fila_alfil
x2 = fila_alfil
x3 = fila_alfil
y = columna_alfil
y2= columna_alfil
y3= columna_alfil
y4= columna_alfil


for k in range(fila_alfil, 9):  # movimiento del alfil mientras asciende
    if k == fila_torre and y == columna_torre:
        print('Alfil captura')
    # print(k, y)
    y+=1
    if y == 9:
        break

while x > 1:    # resta hasta 1 alfil

    x -= 1
    y2-=1
    if y2 == 0:
        break
    # print(x, y2)
    if x == fila_torre and y2 == columna_torre:
        print('Alfil captura')
        break
      
    
while x3 > 1:    # resta hasta 1 otro eje alfil
    if x3 == fila_torre and y3 == columna_torre:
        print('Alfil captura')
    x3 -= 1
    y3 += 1
    if x3 == 0 or y3 == 9:
        break
    # print(x3, y3)
    
for l in range(fila_alfil, 9):  # movimiento del alfil mientras asciende otro eje
    y4-=1
    if y4 == 0:
        break
    if l == fila_torre and y4 == columna_torre:
        print('Alfil captura')
    # print(l, y4)
   

for j in range(1, fila_torre):  # movimiento de la torre mientras desciende
    if j == fila_alfil and columna_alfil == columna_torre:
        print('Torre captura')
        break
    # print('col:', j, columna_torre*1)
    # print()
    # print('fila:', fila_torre*1, j)
    # print()
    

for i in range(fila_torre, 9):  # movimiento de la torre mientras asciende
    if i == fila_alfil and columna_alfil == columna_torre:
        print('Torre captura')
        break
    # print('col', i, columna_torre*1)
    # print()
    # print('fila', fila_torre*1, i)
    # print()
  


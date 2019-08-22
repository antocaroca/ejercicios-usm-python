fila_alfil = int(input('Fila alfil: '))
columna_alfil = int(input('Columna torre: '))

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

while x > 1:    # resta hasta 1
    if x == fila_torre and y2 == columna_torre:
        print('Alfil captura')
        break
    x -= 1
    y2-=1
    if y2 == 0:
        break
    # print(x, y2)
    
    
while x3 > 1:    # resta hasta 1 otro eje
    if x3 == fila_torre and y3 == columna_torre:
        print('Alfil captura')
    x3 -= 1
    y3 += 1
    if x3 == 0 or y3 == 9:
        break
    # print(x3, y3)
    
for l in range(fila_alfil, 9):  # movimiento del alfil mientras asciende otro eje
    if l == fila_torre and y4 == columna_torre:
        print('Alfil captura')
    # print(l, y4)
    y4-=1
    if y4 == 0:
        break
    



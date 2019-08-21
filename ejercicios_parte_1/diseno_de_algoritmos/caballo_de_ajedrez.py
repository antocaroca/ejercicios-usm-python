#   Escriba un programa que reciba como entrada las coordenadas en que se encuentra un caballo, 
# y entregue como salida todas las casillas hacia las cuales el caballo puede desplazarse.
x = int(input('Ingrese coordenadas del caballo. \nFila: '))
y = int(input('Columna: '))

if x > 0 and x <= 8 and y > 0  and y <= 8:
    if x + 2 <= 8 and y + 1 <= 8:
        print(x+2 , y+1)
    if  x - 2 > 0 and y + 1 <= 8:
        print( x - 2, y + 1)
    if x - 2 > 0 and y - 1 > 0:
        print( x -2, y-1)
    if x + 2 <= 8 and y - 1 > 0:
        print(x + 2, y-1)
    if x +1 <= 8 and y + 2 <= 8:
        print(x+1, y+2)
    if x - 1 > 0 and y + 2 <= 8:
        print(x-1, y+2)
    if x-1 > 0 and y - 2 > 0:
        print(x-1, y-2)
    if x + 1 <= 8 and y -2 > 0:
        print(x + 1, y -2)
else:
    print("posición inválida")



#   Escriba un programa que pida al usuario que ingrese varios valores enteros, que pueden ser positivos o negativos.
#  Cuando se ingrese un cero, el programa debe terminar y mostrar un gráfico de cuántos valores positivos y negativos
#  fueron ingresados:

pos = 0
neg = 0

while True:
    n = int(input('Ingrese un número, termine con cero: '))
    if n == 0:
        break
    elif n > 0:
        pos +=1
    else:
        neg +=1
print(pos*('*'))
print(neg*('*'))
   
   


#   Desarrolle un programa que permita trabajar con las potencias fraccionales de dos.
#   0.5,0.25,0.125,0.0625,0.03125,0.015625,…
#   El programa debe mostrar tres columnas que contengan la siguiente información.
print('Potencia: \tFracción:\t      \t \tSuma: ')
contador = 0
suma = 0

for i in range(1,100000+1):
    # print(2**i)
    fraccion = ((1/(2**i)))
    if fraccion <= 0.000001:
        break
    suma +=((1/(2**i)))
    contador+=1
    print(' ', contador, '\t'+'\t',(1/(2**i)), ' \t',' ' +'\t',suma )

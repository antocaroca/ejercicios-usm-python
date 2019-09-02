i = 0
k = 0
cont = 0
precio = 0

# contador de monedas
cien = 0
cincuenta = 0
diez = 0

while i < 1:
    i += 1
    eleccion = input('Elija producto: ')
    if eleccion == 'A':
        precio = 270
        print(precio)
    elif eleccion == 'B':
        precio = 340
        print(precio)
    elif eleccion == 'C':
        precio = 390
        print(precio)

    while k < precio:
        monedas = int(input('Ingrese monedas: '))
        cont += monedas
        if cont >= precio:
            break
    if cont > precio:
        vuelto = (cont - precio)
        while vuelto/100 >= 1:
            cien += 1
            vuelto -= 100
        while vuelto/50 >= 1:
            cincuenta += 1
            vuelto -= 50
        while vuelto/10 >= 1:
            diez +=1
            vuelto -= 10

for vuelto in range(1, (cien+1)):
    print('100')
for vuelto in range(1, (cincuenta+1)):
    print('50')
for vuelto in range(1, (diez+1)):
    print('10')
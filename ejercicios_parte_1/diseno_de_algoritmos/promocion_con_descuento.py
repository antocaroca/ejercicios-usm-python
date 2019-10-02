
n = int(input('n: '))
cantidad_productos = int(input('Cantidad productos: '))
prod = 0
lista_productos = []
lista_tres = []
contador = 0
cont = 1
descuento = 0.40
suma = 0
resultado = []

while prod < cantidad_productos:
    prod += 1
    precio_producto = int(input(f'Precio producto {prod}: '))
    lista_productos.append(precio_producto)

for i in range(n):
    lista_tres.append(lista_productos[((contador)*n):(n*(cont))])
    contador+=1
    cont+=1

if cantidad_productos/n < n:
    n = int(cantidad_productos/n)
    #print(lista_tres[0:n])
elif cantidad_productos/n > n:
    n = n

precio_sin_descuento = []

for x in (lista_tres[0:n]):
    suma = (sum(x))
    precio_sin_descuento.append(suma)
    descuento /= 2
    suma = suma - int(descuento*suma)
    resultado.append(suma)
#print(sum(resultado))

total = []  
for outer in lista_tres:
    for inner in outer:
        total.append(inner)
print('total: ', sum(total))
#print('sin descto', sum(precio_sin_descuento))
print('descuento:', sum(precio_sin_descuento)- sum(resultado))
print(f'Por pagar: {(sum(total)- (sum(precio_sin_descuento)- sum(resultado)))}')

   
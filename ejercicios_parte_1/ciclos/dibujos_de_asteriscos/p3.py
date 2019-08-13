# #   Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:

lado = int(input('Ingrese lado: '))
espacio = (lado-1)
ancho_max= lado + ((lado-1)*2)
altura = lado + (lado-1)
    
for i in range(4, ancho_max+1, 2): 
    print(' '* espacio, ((i)*'*'), end=' ')
    espacio-=1
    print()

for j in range(lado*2, lado+1, -1): 
    print(' '* (espacio-2), ((j)*'*'), end=' ')
    espacio+=1
    print()

    
    
    
    
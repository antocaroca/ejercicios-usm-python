#    Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
# Lo logré! Me costó harto. hice un dibujo con los asteriscos y saqué cálculos en cuanto a los espacios que se repiten,
#  ancho min, ancho max (y la diferencia entre ambos) y altura. El segundo for lo saqué probando muchos cambios hasta que resultó.

lado = int(input('Ingrese lado: '))
espacio = (lado-1)
ancho_max= lado + ((lado-1)*2)
altura = lado + (lado-1)
    
for i in range(lado, ancho_max+1, 2): 
    print(' '* espacio, ((i)*'*'), end=' ')
    espacio-=1
    print()

for j in range(ancho_max-1, lado, -2): 
    print(' '* (espacio+2), ((j-1)*'*'), end=' ')
    espacio+=1
    print()

    
    
    
    
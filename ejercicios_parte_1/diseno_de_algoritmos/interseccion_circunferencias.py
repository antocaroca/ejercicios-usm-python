# Escriba un programa que determine si dos circunferencias se intersectan o no.
# se aplica la fórmula:  la distnacia entre los centros de las 2 circunferencias es menor que la suma de los radios y mayor que su diferencia. 
# Son secantes: tiene 2 puntos en común. Todos los demás casos no se intersectan
# para saber ña distancia entre los centros se aplica la fórmula:  se obtiene valores como si se tratara de un rectángulo,
# se obtiene base restando las x y la altura restando las y. Luego se obtiene la diagonal de ese rectángulo que es la distancia entre los centros
#con la siguiente fórmula: diaginal = raiz de la base **2 + altura **2
import math
 
x1 = float(input('x1: '))
y1 = float(input('y1: '))
r1 = float(input('r1: '))

x2 = float(input('x2: '))
y2 = float(input('y2: '))
r2 = float(input('r2: '))


distancia_centros = math.sqrt((abs(x1 - x2))**2) + ((abs(y1 - y2))**2)
suma_radios = r1 + r2
resta_radios = abs(r1 - r2)

if distancia_centros < suma_radios and distancia_centros > resta_radios:
    print('Se intersectan')
else:
    print('No se intersectan')
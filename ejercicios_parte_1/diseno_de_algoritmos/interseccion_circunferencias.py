# Escriba un programa que determine si dos circunferencias se intersectan o no.
 
x1 = float(input('x1: '))
y1 = float(input('y1: '))
r1 = float(input('r1: '))

x2 = float(input('x2: '))
y2 = float(input('y2: '))
r2 = float(input('r2: '))

distancia_centros = abs(x1 - x2) + abs(y1 - y2)
suma_radios = r1 + r2
resta_radios = abs(r1 - r2)

if distancia_centros < suma_radios and distancia_centros > resta_radios:
    print('Se intersectan')
else:
    print('No se intersectan')
# Escriba un programa que determine si dos circunferencias se intersectan o no.
x1 = float(input('x1: '))
y1 = float(input('y1: '))
r1 = float(input('r1: '))

x2 = float(input('x2: '))
y2 = float(input('y2: '))
r2 = float(input('r2: '))

suma_x = x1 + x2
suma_y= y1 + y2
suma_r= r1 + r2

resta_x = abs(x1 - x2)
resta_y= abs(y1 - y2)
resta_r= abs(r1 - r2)

resultado_x = suma_x + resta_x
resultado_y = suma_y + resta_y
resultado_r = suma_r + resta_r

res_x = abs(suma_x -  resta_x)
res_y = abs(suma_y -  resta_y)
res_r = abs(suma_r -  resta_r)

total_x = abs(resultado_x - res_x)
total_y = abs(resultado_y - res_y)
total_r = abs(resultado_r - res_r)

if total_r < total_y and total_r < total_x:
    print('Se intersectan')
else:
    print('No se intersectan')

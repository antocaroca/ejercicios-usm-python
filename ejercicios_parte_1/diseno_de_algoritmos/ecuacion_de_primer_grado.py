#   Escriba un programa que pida los coeficientes de una ecuación de primer grado: ax + b = 0,

a = int(input('Ingrese a: '))
b = int(input('Ingrese b: '))

if a == 0 and b !=0:
    print("sin solución")
elif  a == 0 and b == 0:
    print("no hay solución única")
else:
    x   = -b /a
    print(x)




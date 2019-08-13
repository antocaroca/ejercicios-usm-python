#   Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

n = int(input('Ingrese un número: '))

for i in range(n + 1):
    print(2**i)
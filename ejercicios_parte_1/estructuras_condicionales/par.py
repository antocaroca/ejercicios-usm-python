#   Escriba un programa que determine si el número entero ingresado por el usuario es par o no.
def par():
    n = int(input('Ingrese un número entero: '))
    if n % 2 == 0:
        print('Su número es par.')
    else:
        print('Su número es impar.')

par()
#   Escriba un programa que intente adivinar el número pensado por el usuario. 
# Cada vez que el computador haga un intento, el usuario debe ingresar <, > o =, 
# dependiendo si el intento es menor, mayor o correcto.
from random import randrange
n = randrange(101)
n_saved = n

intento = 1

while True:
    num = (print(f'Intento {intento}: {n}'))
    user = input('te toca: ')
    if user == '=':
        print(f'Adiviné en {intento} intentos!')
        break
    elif user == '>':
        n = randrange(n, 101)
    else:
        n = randrange(1, n)
    intento+=1

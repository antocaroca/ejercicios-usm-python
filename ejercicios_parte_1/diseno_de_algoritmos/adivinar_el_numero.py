#   Escriba un programa que «piense» un número entre 0 y 100, y entregue pistas al usuario para que lo adivine.
from random import randrange
n = randrange(101)
# print(n)
print('adivine el número: ')

intento = 1

while True:
    num = int(input(f'Intento {intento}: '))

    if num < n:
        print('Es mayor que', num)
    elif num > n:
        print('En menor que', num)
    else:
        print(f'Correcto! Adivinaste en {intento} intentos.')
        break
    intento += 1


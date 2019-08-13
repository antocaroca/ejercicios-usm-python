#   Escriba un programa que entregue todos los divisores del número entero ingresado:
n = int(input('Ingrese número: '))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
#   Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
def division():
    dividendo = int(input('Ingrese dividendo: '))
    divisor = int(input('Ingrese divisor: '))
    resto = dividendo % divisor
    cociente = int(dividendo/divisor)

    if dividendo % divisor == 0:
        print(f'La división es exacta. \nCociente: {cociente} \nResto: {resto}')
    else:
        print(f'La división NO es exacta. \nCociente: {cociente} \nResto: {resto}')

division()

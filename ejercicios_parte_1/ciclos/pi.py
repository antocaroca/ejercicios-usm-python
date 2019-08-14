#   Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
#   La entrada del programa debe ser un número entero n que indique cuántos términos de la suma se utilizará.

n = int(input('Ingrese un número: '))
contador1= 0
contador2 = 0

for value in range(1, n+n, 2):  
    # print(value)
    # print(range(1, n+n, 2).index(value))
    index = (range(1, n+n, 2).index(value))
    # print(index)
    if index%2 != 0:
        contador1 += (1/value*-1)
        # print(1/value*-1)
    else:
        contador2 += (1/value)
        # print(1/value)
    resultado = contador1 + contador2

num_pi = (4 * resultado)
print(num_pi)
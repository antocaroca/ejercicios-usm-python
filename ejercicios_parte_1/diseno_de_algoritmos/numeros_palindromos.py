#   Escriba un programa que indique si el número ingresado es o no palíndromo:
n = int(input('Ingrese un número: '))
n2 = n
r = 0
while n != 0:
    u = n % 10
    n = int(n/10)
    r = r * 10 + u
# print(r)
if r == n2:
    print(f"{n2} es palíndromo.")
else:
    print(f"{n2} no es palíndromo.")
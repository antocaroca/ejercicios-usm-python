#   Escriba un programa que entregue la suma de los primeros n números naturales, siendo n ingresado por el usuario.

n = int(input('Ingrese un número: '))
suma = 0

for i in range(1, n+1):
    suma += i
print("s1:", suma)

s2 = (n * (n + 1)) / 2

print("s2:", int(s2))

if suma == s2:
    print("Son iguales")
else:
    print("No son iguales")

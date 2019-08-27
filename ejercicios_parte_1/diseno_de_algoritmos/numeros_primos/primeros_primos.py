#   Escriba un programa que muestre los n primeros números primos, donde n es ingresado por el usuario:
n = int(input('Cuántos primos: '))

lista = []

for num in range(1, n**2):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            lista.append(num)

resultado = (lista[0:n])
for i in resultado:
    print(i)

        
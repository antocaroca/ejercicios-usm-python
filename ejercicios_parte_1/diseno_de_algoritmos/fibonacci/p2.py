#   Escriba un programa que reciba como entrada un número entero e indique si es o no un número de Fibonacci:

n = int(input('Ingrese n: '))

contador = 0
lista = [1,1]

while contador < n:
    anterior = lista[-2]
    siguiente = lista[-1]
    suma = anterior+siguiente
    if suma > n:
        break
    lista.append(suma)
    contador+=1

if (lista[-1]) == n:
    print(f'{n} es número de Fibonacci')
else:
    print(f'{n} no es número de Fibonacci')




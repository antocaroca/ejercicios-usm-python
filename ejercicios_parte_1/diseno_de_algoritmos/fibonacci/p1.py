#   Escriba un programa que reciba como entrada un número entero n, y entregue como salida el n-ésimo número de Fibonacci:
n = int(input('Ingrese n: '))

contador = 0
lista = [1,1]

while contador < n:
    
    anterior = lista[-2]
    siguiente = lista[-1]
    suma = anterior+siguiente
    lista.append(suma)
    contador+=1

print(f'F{contador}: {lista[n-1]}')


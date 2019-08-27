#   Escriba un programa que muestre los m primeros números de Fibonacci, donde m es un número ingresado por el usuario:
n = int(input('Ingrese n: '))

contador = 0
lista = [0,1]

while contador < n:
    
    anterior = lista[-2]
    siguiente = lista[-1]
    suma = anterior+siguiente
    lista.append(suma)
    contador+=1

total = (lista[0:n])
for i in total:
    print(i,"", end="")
print()

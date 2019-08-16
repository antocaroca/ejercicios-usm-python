#   Escriba un programa que muestre los números naturales menores o iguales que un número n determinado, 
# que no sean múltiplos ni de 3 ni de 7.

n = int(input('Ingrese un número: '))

for i in range(1, n):
    if i % 3 == 0 or i % 7 == 0:
        continue
    else:
        print(i)
    


#   Escriba un programa que reciba como entrada un número natural, e indique si es primo o compuesto:

n = int(input('Ingrese un número: '))

cont = 0 # contador de divisores

for i in range(1, n+1):
    for j in range(1, n+1):
        if j% i == 0 and j % n == 0: 
            # print(i)
            cont+=1

if cont == 2:
    print(n, 'es primo')
else:
    print(n, 'es compuesto')

            

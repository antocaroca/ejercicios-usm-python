#   Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
#   si el número es par, se lo divide por dos; si es impar, se le multiplica tres y se le suma uno;
#   la sucesión termina al llegar a uno.

n = int(input('Ingrese un número: '))

while n != 1:
    if n % 2 == 0:
        n  /= 2
    else:
        n = (n * 3) + 1
    print(n)

#   Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros positivos
#  menores que el ingresado por el usuario:

n2 = int(input('Ingrese un número: '))

while n2 != 1:
    if n2 % 2 == 0:
        n2  /= 2
        print(int(n2)*'*')
    else:
        n2 = (n2 * 3) + 1
        print(int(n2)*'*')
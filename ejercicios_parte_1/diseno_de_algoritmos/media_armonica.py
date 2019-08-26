#   Desarrolle un programa que calcule la media armónica de una secuencia de números.
#   El programa primero debe preguntar al usuario cuántos números ingresará. A continuación, 
# pedirá al usuario que ingrese cada uno de los n números reales. Finalmente, el programa mostrará el resultado.

numeros = int(input('Cuántos números: '))

contador = 0
x = 0

while contador < numeros:
    contador += 1
    n =  int(input(f'n{contador} = '))
    x =  x + (1/n)

print(f'H = {numeros/x}')

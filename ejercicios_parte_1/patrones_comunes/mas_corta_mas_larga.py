#   Desarrolle un programa que tenga la siguiente entrada:

#   primero, el usuario ingresa un número entero n, que indica cuántas palabras ingresará a continuación;
#   después el usuario ingresa n palabras.
#   La salida del programa debe mostrar la palabra más larga y la más corta que fueron ingresadas por el usuario.

n = int(input('Cantidad de palabras: '))
i = 0
mayor= []
while i < n:
    i += 1
    palabra = input(f'palabra {i}: ')
    mayor.append(palabra)
    print(palabra)

largo_palabras = []
for palabra in mayor:
    largo_palabras.append((len(palabra), palabra)) # se agrega el largo y la palabra de cada palabra en una lista.
    largo_palabras.sort() # se ordenan las listas según su largo de menor a mayor.
print("La palabra más larga es:", largo_palabras[-1][1])
print("La palabra más corta es es:", largo_palabras[0][1])
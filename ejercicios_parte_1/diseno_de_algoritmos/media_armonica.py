#   Desarrolle un programa que calcule la media armónica de una secuencia de números.
#   El programa primero debe preguntar al usuario cuántos números ingresará. A continuación, 
# pedirá al usuario que ingrese cada uno de los n números reales. Finalmente, el programa mostrará el resultado.

n = int(input('Cuántos números: '))
i = 0
count = 0
lista = []

while i < n:
    i += 1
    count+=1
    c = int(input(f'n{count}: '))
    lista.append(c)
# print(lista)
# print("n:",n)

contador = 0
for i in lista:
    contador += (1/i)
print("H =", n/contador)
    
    
    
    


